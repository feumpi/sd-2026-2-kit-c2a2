"""Testes da TAREFA 3: resiliencia na chamada ao LLM e degradacao elegante."""
import pytest
import requests
from fastapi.testclient import TestClient

from servicos.comum import llm
from servicos.comum.circuit_breaker import CircuitBreaker
from servicos.geracao import app as geracao
from servicos.geracao import resiliencia

TRECHOS = [
    {"texto": "O teorema CAP afirma que, diante de uma particao, e preciso escolher.",
     "origem": "teorema_cap.txt", "score": 0.61},
    {"texto": "Raft e um algoritmo de consenso.", "origem": "consenso_raft.txt", "score": 0.0},
]


class RespostaLLM:
    def __init__(self, status, corpo=None):
        self.status_code = status
        self._corpo = corpo or {"choices": [{"message": {"content": "resposta do LLM"}}]}

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}", response=self)

    def json(self):
        return self._corpo


@pytest.fixture(autouse=True)
def isolamento(monkeypatch):
    """Disjuntores novos, sem espera real no backoff e recuperacao simulada."""
    monkeypatch.setattr(geracao, "disjuntor_llm", CircuitBreaker(3, 20))
    monkeypatch.setattr(geracao, "disjuntor_recuperacao", CircuitBreaker(3, 20))
    esperas = []
    monkeypatch.setattr(resiliencia.time, "sleep", esperas.append)
    monkeypatch.setattr(geracao, "buscar_trechos", lambda pergunta: TRECHOS)
    return esperas


@pytest.fixture
def cliente():
    return TestClient(geracao.app)


@pytest.fixture
def llm_real(monkeypatch):
    """Ativa o caminho da API real do LLM com respostas HTTP programaveis."""
    monkeypatch.setattr(llm, "API_KEY", "chave-de-teste")
    respostas = []
    chamadas = []

    def post(url, headers, json, timeout):
        chamadas.append(timeout)
        item = respostas.pop(0)
        if isinstance(item, Exception):
            raise item
        return item

    monkeypatch.setattr(llm.requests, "post", post)
    return respostas, chamadas


def perguntar(cliente):
    return cliente.post("/perguntar", json={"pergunta": "o que diz o teorema CAP?"})


def test_modo_simulado_responde_com_os_trechos(cliente):
    r = perguntar(cliente)
    assert r.status_code == 200
    corpo = r.json()
    assert "MODO SIMULADO" in corpo["resposta"]
    assert "teorema CAP" in corpo["resposta"]
    assert corpo["fontes"] == ["teorema_cap.txt"]  # trecho com score 0 e descartado


def test_retentativa_recupera_falha_transitoria(cliente, llm_real, isolamento):
    respostas, chamadas = llm_real
    respostas += [requests.Timeout("lento"), RespostaLLM(502), RespostaLLM(200)]
    r = perguntar(cliente)
    assert r.status_code == 200
    assert r.json()["resposta"] == "resposta do LLM"
    assert len(chamadas) == 3
    assert chamadas[0] == llm.TIMEOUT  # toda chamada ao LLM tem tempo-limite
    # espera progressiva entre as tentativas: ~0,5 s e depois ~1 s (base 0,5 + jitter)
    assert len(isolamento) == 2
    assert 0.5 <= isolamento[0] <= 1.0 <= isolamento[1] <= 1.5
    assert geracao.disjuntor_llm.estado == "fechado"


def test_erro_4xx_nao_e_retentado(cliente, llm_real):
    respostas, chamadas = llm_real
    respostas += [RespostaLLM(401)]
    r = perguntar(cliente)
    assert r.status_code == 503
    assert len(chamadas) == 1


def test_disjuntor_abre_apos_falhas_e_devolve_503_elegante(cliente, llm_real):
    respostas, chamadas = llm_real
    respostas += [requests.ConnectionError("sem internet")] * 9
    for _ in range(3):
        assert perguntar(cliente).status_code == 503
    assert geracao.disjuntor_llm.estado == "aberto"
    assert len(chamadas) == 9  # 3 perguntas x 3 tentativas

    r = perguntar(cliente)
    assert r.status_code == 503
    assert len(chamadas) == 9  # circuito aberto: nem tenta chamar o LLM
    corpo = r.json()
    assert "disjuntor aberto" in corpo["erro"]
    assert corpo["fontes"] == ["teorema_cap.txt"]
    assert corpo["contexto"]
    assert int(r.headers["Retry-After"]) > 0
    assert cliente.get("/saude").json()["disjuntores"]["llm"] == "aberto"


def test_recuperacao_fora_do_ar_abre_o_disjuntor(cliente, monkeypatch):
    def fora(pergunta):
        raise requests.ConnectionError("recuperacao caiu")
    monkeypatch.setattr(geracao, "buscar_trechos", fora)
    for _ in range(3):
        r = perguntar(cliente)
        assert r.status_code == 503
        assert "recuperacao indisponivel" in r.json()["erro"]
    assert geracao.disjuntor_recuperacao.estado == "aberto"
    assert "disjuntor aberto" in perguntar(cliente).json()["erro"]


def test_sem_trechos_relevantes_nao_chama_llm(cliente, monkeypatch):
    monkeypatch.setattr(geracao, "buscar_trechos", lambda pergunta: [])
    monkeypatch.setattr(llm, "gerar", lambda *a: pytest.fail("nao deveria chamar o LLM"))
    r = perguntar(cliente)
    assert r.status_code == 200
    assert "Nao encontrei" in r.json()["resposta"]


def test_pergunta_vazia_e_rejeitada(cliente):
    assert cliente.post("/perguntar", json={"pergunta": ""}).status_code == 422


@pytest.mark.parametrize("erro, esperado", [
    (requests.Timeout(), True),
    (requests.ConnectionError(), True),
    (requests.HTTPError(response=RespostaLLM(503)), True),
    (requests.HTTPError(response=RespostaLLM(429)), True),
    (requests.HTTPError(response=RespostaLLM(400)), False),
    (KeyError("choices"), False),
])
def test_classificacao_de_falhas_transitorias(erro, esperado):
    assert resiliencia.eh_transitoria(erro) is esperado


def test_backoff_cresce_exponencialmente():
    assert 0.5 <= resiliencia.espera_backoff(1, 0.5) <= 1.0
    assert 1.0 <= resiliencia.espera_backoff(2, 0.5) <= 1.5
    assert 2.0 <= resiliencia.espera_backoff(3, 0.5) <= 2.5
