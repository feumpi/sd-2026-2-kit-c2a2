"""
Testes ponta a ponta (TAREFA 5) contra o sistema real no docker compose.

  docker compose up -d --build --wait
  python -m pytest -m e2e
"""
import subprocess
import time
from pathlib import Path

import pytest
import requests

from scripts.carregar_documentos import carregar

pytestmark = pytest.mark.e2e

RAIZ = Path(__file__).resolve().parent.parent
INGESTAO = "http://localhost:8001"
GERACAO = "http://localhost:8003"


def perguntar(pergunta):
    return requests.post(f"{GERACAO}/perguntar", json={"pergunta": pergunta}, timeout=60)


def compose(*args):
    subprocess.run(["docker", "compose", *args], cwd=RAIZ, check=True, capture_output=True)


def esperar(condicao, segundos=60):
    limite = time.monotonic() + segundos
    while time.monotonic() < limite:
        try:
            if condicao():
                return
        except requests.RequestException:
            pass
        time.sleep(1)
    pytest.fail("condicao nao atingida a tempo")


@pytest.fixture(scope="module", autouse=True)
def documentos_indexados():
    try:
        requests.get(f"{GERACAO}/saude", timeout=3)
    except requests.RequestException:
        pytest.skip("sistema fora do ar: rode docker compose up -d --build --wait")
    estado = carregar(INGESTAO, RAIZ / "documentos")
    assert estado["estado"] == "concluida"


def test_pergunta_entra_e_resposta_fundamentada_sai():
    r = perguntar("o que diz o teorema CAP?")
    assert r.status_code == 200
    corpo = r.json()
    assert "teorema_cap.txt" in corpo["fontes"]
    assert "particao de rede" in corpo["resposta"]


def test_pergunta_sobre_outro_documento():
    corpo = perguntar("como o Raft elege um lider?").json()
    assert "consenso_raft.txt" in corpo["fontes"]


def test_reindexar_mesmos_documentos_nao_duplica():
    antes = requests.get(f"{INGESTAO}/indice", timeout=5).json()["total"]
    estado = carregar(INGESTAO, RAIZ / "documentos")
    assert estado["novos"] == "0"
    assert requests.get(f"{INGESTAO}/indice", timeout=5).json()["total"] == antes


def test_derrubar_recuperacao_abre_o_disjuntor_e_depois_fecha():
    compose("stop", "recuperacao")
    try:
        for _ in range(3):
            r = perguntar("o que diz o teorema CAP?")
            assert r.status_code == 503
        saude = requests.get(f"{GERACAO}/saude", timeout=5).json()
        assert saude["disjuntores"]["recuperacao"] == "aberto"
        assert "disjuntor aberto" in perguntar("teorema CAP").json()["erro"]
    finally:
        compose("start", "recuperacao")
    # depois da espera do disjuntor, a chamada de teste passa e o circuito fecha
    esperar(lambda: perguntar("o que diz o teorema CAP?").status_code == 200)
    saude = requests.get(f"{GERACAO}/saude", timeout=5).json()
    assert saude["disjuntores"]["recuperacao"] == "fechado"
