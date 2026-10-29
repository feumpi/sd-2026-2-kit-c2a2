"""Configuracao comum dos testes: isola o diretorio de dados e o modo do LLM."""
import pytest


@pytest.fixture(autouse=True)
def ambiente_isolado(tmp_path, monkeypatch):
    """Cada teste usa um DIR_DADOS proprio e o LLM em modo simulado."""
    monkeypatch.setenv("DIR_DADOS", str(tmp_path / "dados"))
    from servicos.comum import llm
    monkeypatch.setattr(llm, "API_KEY", "")
    yield
