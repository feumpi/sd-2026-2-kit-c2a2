"""Sanidade do ambiente de testes."""
from servicos.comum.embeddings import Vetorizador, similaridade


def test_vetorizador_e_similaridade():
    v = Vetorizador()
    v.ajustar(["teorema cap", "raft consenso"])
    assert similaridade(v.vetorizar("teorema cap"), v.vetorizar("teorema cap")) > 0.99
