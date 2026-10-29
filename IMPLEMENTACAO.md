# IMPLEMENTACAO.md — Diário de desenvolvimento do C2.A2

Registro de como o projeto foi implementado, tarefa a tarefa: decisões, justificativas,
testes e desvios do plano em `CLAUDE.md`. Preencher ao concluir cada tarefa.

## Resumo

| # | Tarefa | Status | Commit(s) |
|---|--------|--------|-----------|
| 0 | Preparação (testes, dependências de dev) | concluída | `chore: prepara ambiente de testes` |
| 1 | Persistir o índice | pendente | |
| 2 | Busca por similaridade | pendente | |
| 3 | Circuit breaker, timeout e retry no LLM | pendente | |
| 4 | Mensageria (fila + worker) e Docker | pendente | |
| 5 | Fluxo ponta a ponta | pendente | |
| 6 | README com diagrama | pendente | |

<!--
Modelo para cada tarefa:

## Tarefa N — Título

**O que foi feito:**

**Decisões e justificativas:** (relacione com as aulas: fila/Aula 8, consistência/Aula 10,
resiliência e idempotência/Aula 11...)

**Arquivos:**

**Testes:** (quais casos, comando usado, resultado)

**Desvios do plano / pendências:**
-->

## Tarefa 0 — Preparação

**O que foi feito:** ambiente local com Python 3.12 via `uv` (`.venv`), dependências de teste
em `requirements-dev.txt` (pytest, httpx para o `TestClient` do FastAPI, fakeredis para testar
a fila sem Redis real) e `pytest.ini` com `pythonpath = .` e o marcador `e2e`, que fica
desligado por padrão.

**Decisões:** `tests/conftest.py` isola cada teste num `DIR_DADOS` temporário e força o LLM
em modo simulado. Assim nenhum teste unitário depende de rede, de Docker ou de chave de API.
`dados/` foi para o `.gitignore`, porque o índice persistido não deve ser versionado.

**Testes:** `python -m pytest`: teste de sanidade do vetorizador.
