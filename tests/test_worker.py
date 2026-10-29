"""Testes da TAREFA 4: mensageria (fila Redis + worker) na ingestao."""
import json

import fakeredis
import pytest
import redis
from fastapi.testclient import TestClient

from servicos.ingestao import app as ingestao
from servicos.ingestao import fila, indice, worker

DOC_CAP = {"texto": "O teorema CAP trata de consistencia e disponibilidade.", "origem": "cap"}
DOC_RAFT = {"texto": "Raft elege um lider por maioria.", "origem": "raft"}


@pytest.fixture
def r(monkeypatch):
    falso = fakeredis.FakeRedis(decode_responses=True)
    monkeypatch.setattr(ingestao, "redis_cliente", falso)
    return falso


@pytest.fixture
def cliente(r):
    return TestClient(ingestao.app)


def test_indexar_enfileira_e_devolve_202(cliente, r):
    resposta = cliente.post("/indexar", json=[DOC_CAP, DOC_RAFT])
    assert resposta.status_code == 202
    corpo = resposta.json()
    assert corpo["estado"] == "pendente"
    assert r.llen(fila.FILA) == 1
    # nada foi indexado ainda: quem indexa e o worker
    assert cliente.get("/indice").json()["total"] == 0
    assert cliente.get(corpo["acompanhar"]).json()["estado"] == "pendente"


def test_worker_processa_e_tarefa_fica_concluida(cliente, r):
    tarefa_id = cliente.post("/indexar", json=[DOC_CAP, DOC_RAFT]).json()["tarefa"]
    assert worker.processar_uma(r, timeout=0.1) is True
    estado = cliente.get(f"/tarefas/{tarefa_id}").json()
    assert estado["estado"] == "concluida"
    assert estado["novos"] == "2"
    assert cliente.get("/indice").json()["total"] == 2
    assert r.llen(fila.FILA) == 0
    assert r.llen(fila.PROCESSANDO) == 0


def test_fila_vazia_nao_bloqueia_para_sempre(r):
    assert worker.processar_uma(r, timeout=0.1) is False


def test_mensagem_repetida_nao_duplica_documentos(r):
    fila.enfileirar(r, [DOC_CAP])
    fila.enfileirar(r, [DOC_CAP])  # reentrega da mesma mensagem
    worker.processar_uma(r, timeout=0.1)
    worker.processar_uma(r, timeout=0.1)
    assert len(indice.carregar()) == 1


def test_falha_e_retentada_e_depois_vai_para_dlq(r, monkeypatch):
    def quebra(docs):
        raise OSError("disco cheio")
    monkeypatch.setattr(indice, "adicionar", quebra)
    tarefa_id = fila.enfileirar(r, [DOC_CAP])

    worker.processar_uma(r, timeout=0.1)
    assert r.llen(fila.FILA) == 1  # voltou para a fila
    assert fila.consultar_tarefa(r, tarefa_id)["tentativas"] == "1"

    for _ in range(fila.MAX_TENTATIVAS - 1):
        worker.processar_uma(r, timeout=0.1)
    assert r.llen(fila.FILA) == 0
    assert r.llen(fila.DLQ) == 1
    assert "disco cheio" in json.loads(r.lindex(fila.DLQ, 0))["erro"]
    assert fila.consultar_tarefa(r, tarefa_id)["estado"] == "falhou"


def test_falha_transitoria_e_superada_na_retentativa(r, monkeypatch):
    original = indice.adicionar
    chamadas = []

    def instavel(docs):
        chamadas.append(1)
        if len(chamadas) == 1:
            raise OSError("falha passageira")
        return original(docs)
    monkeypatch.setattr(indice, "adicionar", instavel)
    tarefa_id = fila.enfileirar(r, [DOC_CAP])
    worker.processar_uma(r, timeout=0.1)
    worker.processar_uma(r, timeout=0.1)
    assert fila.consultar_tarefa(r, tarefa_id)["estado"] == "concluida"
    assert r.llen(fila.DLQ) == 0


def test_mensagem_invalida_vai_direto_para_dlq(r):
    r.lpush(fila.FILA, "isto nao e json")
    worker.processar_uma(r, timeout=0.1)
    assert r.llen(fila.DLQ) == 1
    assert r.llen(fila.PROCESSANDO) == 0


def test_tarefa_interrompida_volta_para_a_fila(r):
    # simula worker que caiu depois de pegar a mensagem
    fila.enfileirar(r, [DOC_CAP])
    r.lmove(fila.FILA, fila.PROCESSANDO, "RIGHT", "LEFT")
    assert worker.recuperar_pendentes(r) == 1
    worker.processar_uma(r, timeout=0.1)
    assert len(indice.carregar()) == 1


def test_tarefa_inexistente_da_404(cliente):
    assert cliente.get("/tarefas/nao-existe").status_code == 404


def test_lista_vazia_e_rejeitada(cliente):
    assert cliente.post("/indexar", json=[]).status_code == 422


def test_redis_fora_do_ar_devolve_503(monkeypatch):
    class RedisFora:
        def __getattr__(self, nome):
            def falha(*a, **k):
                raise redis.ConnectionError("redis caiu")
            return falha
    monkeypatch.setattr(ingestao, "redis_cliente", RedisFora())
    cliente = TestClient(ingestao.app)
    assert cliente.post("/indexar", json=[DOC_CAP]).status_code == 503
    assert cliente.get("/saude").json()["fila"] == "redis indisponivel"
