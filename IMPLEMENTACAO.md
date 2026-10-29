# IMPLEMENTACAO.md — Diário de desenvolvimento do C2.A2

Registro de como o projeto foi implementado, tarefa a tarefa: decisões, justificativas,
testes e desvios do plano em `CLAUDE.md`. Preencher ao concluir cada tarefa.

## Resumo

| # | Tarefa | Status | Commit(s) |
|---|--------|--------|-----------|
| 0 | Preparação (testes, dependências de dev) | concluída | `chore: prepara ambiente de testes` |
| 1 | Persistir o índice | concluída | `feat(ingestao): persiste o índice em arquivo JSON` |
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

## Tarefa 1 — Persistir o índice

**O que foi feito:** o índice deixou de ficar numa lista em memória e passou a ser gravado em
`DIR_DADOS/indice.json`. A lógica ficou isolada em `servicos/ingestao/indice.py`
(`carregar`, `salvar`, `adicionar`, `revetorizar`); `app.py` só expõe as rotas.

**Decisões e justificativas:**
- **JSON em arquivo em vez de banco vetorial:** o corpus é pequeno e a busca é linear, então
  um arquivo basta e não acrescenta outro container. Os vetores ficam salvos junto dos textos.
- **Escrita atômica** (arquivo `.tmp`, `fsync` e `os.replace`): um leitor concorrente (a rota
  `GET /indice`) enxerga sempre o índice anterior completo ou o novo completo, nunca um
  arquivo pela metade. É a base do modelo de consistência do índice (Aula 10): consistência
  eventual, em que o documento novo aparece na busca assim que a escrita termina.
- **Idempotência** (Aula 11): o id do documento é `sha256(origem + texto)`, e reenviar o mesmo
  documento não o duplica. Isso será essencial quando o worker da fila (Tarefa 4) retentar
  mensagens.
- **Correção de um bug do kit:** o `/indexar` original fazia `INDICE.clear()` e só reinseria
  os documentos da chamada atual, perdendo os anteriores. Agora os documentos se acumulam.
- Como o vocabulário do TF-IDF muda a cada documento novo, todos os vetores são recalculados
  a cada inclusão. É aceitável para o tamanho do corpus.
- Arquivo corrompido é movido para `indice.corrompido` (para análise) em vez de ser
  sobrescrito em silêncio.

**Arquivos:** `servicos/ingestao/indice.py` (novo), `servicos/ingestao/app.py`, `tests/test_ingestao.py`.

**Testes:** reinício (estado vem só do arquivo), acúmulo entre chamadas, não duplicação,
vetores no mesmo espaço após novo documento, arquivo ausente, arquivo corrompido, ausência do
temporário após a escrita, rotas HTTP e validação de texto vazio (422). `python -m pytest`: 10 passaram.
