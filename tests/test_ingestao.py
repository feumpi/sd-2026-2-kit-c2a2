"""Testes da TAREFA 1: indice persistido do servico de ingestao."""
import json
import os

from fastapi.testclient import TestClient

from servicos.comum.embeddings import Vetorizador, similaridade
from servicos.ingestao import indice

DOC_CAP = {"texto": "O teorema CAP trata de consistencia e disponibilidade.", "origem": "cap"}
DOC_RAFT = {"texto": "Raft elege um lider por maioria.", "origem": "raft"}


def test_indice_sobrevive_a_reinicio():
    indice.adicionar([DOC_CAP, DOC_RAFT])
    # "reiniciar" = nao ha estado em memoria: tudo vem do arquivo
    itens = indice.carregar()
    assert [i["origem"] for i in itens] == ["cap", "raft"]
    assert all(len(i["vetor"]) > 0 for i in itens)
    assert indice.caminho_indice().exists()


def test_indexar_duas_vezes_acumula_documentos():
    indice.adicionar([DOC_CAP])
    resultado = indice.adicionar([DOC_RAFT])
    assert resultado == {"novos": 1, "total": 2}


def test_documento_repetido_nao_duplica():
    indice.adicionar([DOC_CAP])
    resultado = indice.adicionar([DOC_CAP, DOC_CAP])
    assert resultado == {"novos": 0, "total": 1}


def test_vetores_ficam_no_mesmo_espaco_apos_novo_documento():
    indice.adicionar([DOC_CAP])
    indice.adicionar([DOC_RAFT])
    itens = indice.carregar()
    assert len({len(i["vetor"]) for i in itens}) == 1
    # recuperacao reajusta com os mesmos textos e obtem o mesmo vocabulario
    v = Vetorizador()
    v.ajustar([i["texto"] for i in itens])
    assert similaridade(v.vetorizar(DOC_CAP["texto"]), itens[0]["vetor"]) > 0.99


def test_arquivo_ausente_e_indice_vazio():
    assert indice.carregar() == []


def test_arquivo_corrompido_e_isolado():
    caminho = indice.caminho_indice()
    caminho.parent.mkdir(parents=True)
    caminho.write_text("{nao e json")
    assert indice.carregar() == []
    assert caminho.with_suffix(".corrompido").exists()
    assert not caminho.exists()


def test_escrita_atomica_nao_deixa_temporario():
    indice.adicionar([DOC_CAP])
    arquivos = os.listdir(indice.caminho_indice().parent)
    assert arquivos == ["indice.json"]
    assert json.loads(indice.caminho_indice().read_text())["itens"][0]["origem"] == "cap"


def test_rotas_http():
    from servicos.ingestao.app import app
    cliente = TestClient(app)
    r = cliente.post("/indexar", json=[DOC_CAP, DOC_RAFT])
    assert r.status_code == 200
    assert r.json()["indexados"] == 2
    corpo = cliente.get("/indice").json()
    assert corpo["total"] == 2
    assert set(corpo["itens"][0]) == {"texto", "origem", "vetor"}
    assert cliente.get("/saude").json() == {"status": "ok", "documentos": 2}


def test_documento_sem_texto_e_rejeitado():
    from servicos.ingestao.app import app
    r = TestClient(app).post("/indexar", json=[{"texto": "", "origem": "x"}])
    assert r.status_code == 422
