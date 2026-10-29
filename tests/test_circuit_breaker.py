"""Testes do circuit breaker (Aula 11)."""
import threading

import pytest

from servicos.comum import circuit_breaker
from servicos.comum.circuit_breaker import CircuitBreaker, CircuitoAberto


class Relogio:
    def __init__(self):
        self.agora = 1000.0

    def __call__(self):
        return self.agora


@pytest.fixture
def relogio(monkeypatch):
    r = Relogio()
    monkeypatch.setattr(circuit_breaker.time, "time", r)
    return r


def falha():
    raise RuntimeError("dependencia fora do ar")


def falhar(disjuntor, vezes):
    for _ in range(vezes):
        with pytest.raises(RuntimeError):
            disjuntor.chamar(falha)


def test_abre_apos_limite_de_falhas(relogio):
    d = CircuitBreaker(limite_falhas=3, espera_segundos=20)
    falhar(d, 2)
    assert d.estado == "fechado"
    falhar(d, 1)
    assert d.estado == "aberto"


def test_aberto_recusa_sem_chamar_a_funcao(relogio):
    d = CircuitBreaker(limite_falhas=1, espera_segundos=20)
    falhar(d, 1)
    chamadas = []
    with pytest.raises(CircuitoAberto):
        d.chamar(lambda: chamadas.append(1))
    assert chamadas == []
    assert d.segundos_para_tentar() == 20


def test_meio_aberto_fecha_apos_sucesso(relogio):
    d = CircuitBreaker(limite_falhas=1, espera_segundos=20)
    falhar(d, 1)
    relogio.agora += 20
    assert d.chamar(lambda: "voltou") == "voltou"
    assert d.estado == "fechado"
    assert d.falhas == 0


def test_meio_aberto_reabre_apos_falha(relogio):
    d = CircuitBreaker(limite_falhas=3, espera_segundos=20)
    falhar(d, 3)
    relogio.agora += 21
    falhar(d, 1)  # uma unica falha no teste reabre
    assert d.estado == "aberto"
    with pytest.raises(CircuitoAberto):
        d.chamar(lambda: "nao deveria rodar")


def test_sucesso_zera_contagem_de_falhas(relogio):
    d = CircuitBreaker(limite_falhas=3, espera_segundos=20)
    falhar(d, 2)
    d.chamar(lambda: None)
    falhar(d, 2)
    assert d.estado == "fechado"


def test_meio_aberto_deixa_passar_uma_unica_chamada_de_teste(relogio):
    d = CircuitBreaker(limite_falhas=1, espera_segundos=20)
    falhar(d, 1)
    relogio.agora += 20
    liberar = threading.Event()
    em_teste = threading.Event()

    def chamada_lenta():
        em_teste.set()
        liberar.wait(2)
        return "ok"

    t = threading.Thread(target=d.chamar, args=(chamada_lenta,))
    t.start()
    em_teste.wait(2)
    with pytest.raises(CircuitoAberto):
        d.chamar(lambda: "concorrente")
    liberar.set()
    t.join()
    assert d.estado == "fechado"
