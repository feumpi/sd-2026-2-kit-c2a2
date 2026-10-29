"""Testes da TAREFA 2: busca por similaridade no servico de recuperacao."""
from pathlib import Path

import pytest
import requests
from fastapi.testclient import TestClient

from servicos.ingestao import indice
from servicos.recuperacao import app as recuperacao

DOCUMENTOS = Path(__file__).resolve().parent.parent / "documentos"


class RespostaFalsa:
    def __init__(self, corpo):
        self._corpo = corpo

    def raise_for_status(self):
        pass

    def json(self):
        return self._corpo


@pytest.fixture
def indice_real(monkeypatch):
    """Indexa os documentos de teste e faz o GET /indice devolver esse indice."""
    indice.adicionar([{"texto": p.read_text(encoding="utf-8"), "origem": p.name}
                      for p in sorted(DOCUMENTOS.glob("*.txt"))])
    itens = indice.carregar()
    monkeypatch.setattr(recuperacao.requests, "get",
                        lambda url, timeout: RespostaFalsa({"itens": itens}))
    return itens


@pytest.fixture
def cliente():
    return TestClient(recuperacao.app)


def test_pergunta_sobre_cap_traz_documento_do_cap_primeiro(indice_real, cliente):
    r = cliente.post("/buscar", json={"pergunta": "o que diz o teorema CAP?", "top_k": 3})
    assert r.status_code == 200
    resultados = r.json()["resultados"]
    assert resultados[0]["origem"] == "teorema_cap.txt"
    assert len(resultados) == 3


def test_pergunta_sobre_raft(indice_real, cliente):
    r = cliente.post("/buscar", json={"pergunta": "como funciona a eleicao de lider no Raft?"})
    assert r.json()["resultados"][0]["origem"] == "consenso_raft.txt"


def test_resultados_ordenados_por_score_e_limitados(indice_real, cliente):
    resultados = cliente.post("/buscar", json={"pergunta": "particao de rede",
                                               "top_k": 2}).json()["resultados"]
    assert len(resultados) == 2
    assert resultados[0]["score"] >= resultados[1]["score"]
    assert set(resultados[0]) == {"texto", "origem", "score"}


def test_indice_vazio_devolve_lista_vazia(monkeypatch, cliente):
    monkeypatch.setattr(recuperacao.requests, "get",
                        lambda url, timeout: RespostaFalsa({"itens": []}))
    r = cliente.post("/buscar", json={"pergunta": "qualquer coisa"})
    assert r.status_code == 200
    assert r.json()["resultados"] == []


def test_vetor_com_dimensao_diferente_e_recalculado(indice_real):
    itens = [dict(i, vetor=[1.0]) for i in indice_real]
    assert recuperacao.ranquear("teorema CAP", itens, 1)[0]["origem"] == "teorema_cap.txt"


def test_ingestao_fora_do_ar_devolve_503(monkeypatch, cliente):
    def falha(url, timeout):
        raise requests.ConnectionError("conexao recusada")
    monkeypatch.setattr(recuperacao.requests, "get", falha)
    r = cliente.post("/buscar", json={"pergunta": "teorema CAP"})
    assert r.status_code == 503
    assert "ingestao indisponivel" in r.json()["detail"]


def test_top_k_invalido_e_rejeitado(cliente):
    assert cliente.post("/buscar", json={"pergunta": "x", "top_k": 0}).status_code == 422
