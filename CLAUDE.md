# CLAUDE.md — Trabalho C2.A2: RAG Distribuído em Microsserviços

Guia para agentes de IA que forem implementar este projeto. Leia inteiro antes de começar.
Idioma do projeto: **português** (código, comentários, mensagens de commit, README e docs).

## Fontes da verdade (nesta ordem)

1. `EDITAL.md` — regras e rubrica do trabalho (o que é avaliado). **Manda sobre tudo.**
2. `TAREFAS.md` — tarefas do kit, na ordem em que devem ser implementadas.
3. `EBOOK.md` — material da disciplina. Seções relevantes: Aula 5 (REST, status, idempotência,
   ~linha 461), Aula 6 (IA como serviço, ~556), **Aula 8** (fila, worker, dead-letter, ~789),
   Aula 10 (CAP/consistência do índice, ~958), **Aula 11** (timeout, retry com backoff,
   circuit breaker, idempotência, ~1040), Aula 13 (containers/Dockerfile, ~1281).
4. Código do kit em `servicos/` (o professor espera que ele seja estendido, não reescrito do zero).

## Contexto em uma frase

Sistema de perguntas e respostas com RAG dividido em **três microsserviços independentes**
(ingestão, recuperação, geração), comunicando por **REST** e com **mensageria (fila Redis)**
em ao menos uma etapa, com a chamada ao LLM protegida por **circuit breaker + timeout +
retry**. Prazo: 29/10/2026 (−0,5 ponto/dia de atraso). A sofisticação da IA **não pontua**:
o esforço vai para a engenharia distribuída.

### Rubrica (5,0 pontos)

| Pts | Critério | Como garantir |
|-----|----------|---------------|
| 1,5 | Arquitetura: 3 serviços independentes e bem separados | Um diretório, um app FastAPI e um Dockerfile por serviço; serviços **não importam código uns dos outros** (só `servicos/comum`) |
| 1,5 | Comunicação: REST/gRPC entre serviços + mensageria em uma etapa | REST síncrono na pergunta; fila Redis na ingestão (ver decisões) |
| 1,0 | Resiliência no LLM: circuit breaker, timeout, retry | Os três presentes, testados e explicados no README |
| 1,0 | Execução reproduzível: README com diagrama, fluxo funciona do zero | `docker compose up --build` + script de carga + `curl` funcionando num clone limpo |

## Ambiente da máquina (verificado em 29/10/2026)

- macOS 26 (Darwin 25.6), **Apple Silicon arm64**, 8 GB RAM, shell zsh.
- **Python:** `python3` padrão é **3.10.18 (pyenv)**; também há 3.13.4 (Homebrew) e 3.9.
  **Use Python 3.12 via `uv`** (uv 0.12.13 instalado em `~/.local/bin/uv`; ele baixa o 3.12 sozinho).
  Testado: `requirements.txt` + `pytest httpx fakeredis` instalam limpos no 3.12.14.
- **Docker 29.8 + Docker Compose v5.5** (Docker Desktop em `/Applications/Docker.app`).
  O daemon pode estar **desligado** — se `docker info` falhar, rode `open -a Docker` e aguarde
  (~30 s) até `docker info` responder. Use `docker compose` (plugin), não `docker-compose`.
- Disponíveis: `git` 2.39, `make` 3.81, `curl`, `jq`. **Não disponíveis:** `gh` (GitHub CLI),
  `redis-server` local, `rabbitmq`, `poetry`. Redis roda **só via Docker**.
- Portas 6379, 8001, 8002, 8003 estavam livres.
- Remote git: `origin = https://github.com/feumpi/sd-2026-2-kit-c2a2.git` (fork do aluno).

### Setup local

```bash
uv venv -p 3.12 .venv
source .venv/bin/activate
uv pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env          # LLM_API_KEY vazia = modo simulado offline
python -m pytest              # testes unitários (não precisam de Docker)
```

## Estado do kit (o que já existe)

- `servicos/comum/embeddings.py` — `Vetorizador` (TF-IDF: `ajustar(textos)`, `vetorizar(texto)`)
  e `similaridade(a, b)` (cosseno). **Não alterar a interface.**
- `servicos/comum/llm.py` — `gerar(pergunta, contexto)`. Sem `LLM_API_KEY` → modo simulado.
  Lê variáveis de ambiente **no import** (nos testes, use `monkeypatch.setattr(llm, "API_KEY", ...)`).
  Já tem timeout (`LLM_TIMEOUT`, padrão 20 s) no `requests.post`, e faz `raise_for_status()`.
- `servicos/comum/circuit_breaker.py` — `CircuitBreaker(limite_falhas, espera_segundos)` com
  `chamar(funcao, *args)` e estados `fechado`/`aberto`/`meio`; levanta `CircuitoAberto`.
  Docstring diz "Aula 13", mas o conteúdo é da **Aula 11**. Não é thread-safe.
- `servicos/ingestao/app.py` — `POST /indexar`, `GET /indice`, `GET /saude`, índice em memória.
  **Bug do kit:** `indexar` faz `INDICE.clear()` e só reinsere os documentos novos — documentos
  de chamadas anteriores somem. Corrigir na Tarefa 1.
- `servicos/recuperacao/app.py` — `POST /buscar` com `NotImplementedError` (Tarefa 2).
- `servicos/geracao/app.py` — `POST /perguntar` chama recuperação e `gerar(...)` sem proteção
  (Tarefa 3). `GET /saude` já expõe o estado do disjuntor.
- `docker-compose.yml` — só o Redis. `documentos/` — 3 `.txt` de teste (CAP, Raft, SD).
- `.gitignore` já ignora `.env`, `.venv/`, `*.joblib`, `*.pkl`, `.pytest_cache/`.

## Decisões de arquitetura já tomadas (siga, não re-decida)

```
cliente ──REST──> geracao:8003 /perguntar
                    │ REST (timeout + disjuntor)
                    ▼
                  recuperacao:8002 /buscar
                    │ REST GET /indice
                    ▼
cliente ──REST──> ingestao:8001 /indexar ──LPUSH──> [Redis fila:ingestao] ──BRPOP──> worker-ingestao
                    ▲                                                                  │
                    └──────── lê dados/indice.json  <──── grava (escrita atômica) ─────┘
geracao ──(retry + timeout + circuit breaker)──> API do LLM (ou modo simulado)
```

1. **Linguagem/stack:** Python 3.12, FastAPI, uvicorn, requests, redis-py — as do
   `requirements.txt`. Manter as versões fixadas. Novas dependências só se indispensáveis
   (e fixadas com `==`). Dependências de teste em `requirements-dev.txt`:
   `pytest==9.2.0`, `httpx==0.28.1` (TestClient), `fakeredis==2.40.0`.
2. **Mensageria = etapa de ingestão (Redis, lista como fila).**
   - `POST /indexar` passa a **enfileirar** (`LPUSH fila:ingestao`) e devolver **202 Accepted**
     com um `id` de tarefa; status em `GET /tarefas/{id}` (`pendente`/`concluida`/`falhou`,
     guardado em Redis, ex. hash `tarefa:{id}`). Isso é o padrão assíncrono da Aula 8.
   - Novo worker `servicos/ingestao/worker.py` (processo separado: `python -m servicos.ingestao.worker`)
     consome com `BRPOP`, vetoriza e persiste o índice.
   - Falhas: até 3 tentativas por mensagem; depois vai para a **dead-letter** `fila:ingestao:dlq`.
   - **Idempotência:** id do documento = `sha256(origem + texto)`; reprocessar a mesma mensagem
     não duplica documentos.
   - Config: `REDIS_URL` (padrão `redis://localhost:6379/0`; no compose `redis://redis:6379/0`).
   - A pergunta (`/perguntar`) continua **síncrona por REST** — mais simples de demonstrar.
3. **Persistência do índice (Tarefa 1):** arquivo JSON em `DIR_DADOS` (padrão `./dados`,
   `dados/` no `.gitignore`), com **escrita atômica** (grava `.tmp` e `os.replace`).
   Lógica isolada em `servicos/ingestao/indice.py` (carregar/salvar/adicionar). **Único escritor
   = worker**; a API de ingestão só lê (recarrega o arquivo no `GET /indice`, pode usar mtime
   como cache). No compose, volume nomeado compartilhado entre `ingestao` e `worker-ingestao`.
   Cada `adicionar` reajusta o TF-IDF sobre **todos** os textos e recalcula todos os vetores.
   Consistência: **eventual** (o documento aparece na busca após o worker processar; leitores
   veem sempre o índice antigo inteiro ou o novo inteiro). Documentar isso no README (Aula 10).
4. **Recuperação (Tarefa 2):** busca `GET /indice` (timeout), reajusta um `Vetorizador` com os
   textos do índice **na mesma ordem** (vocabulário idêntico ao da ingestão), vetoriza a
   pergunta, calcula `similaridade` com cada `vetor`, ordena decrescente e devolve
   `{"resultados": [{"texto", "origem", "score"}...]}` com no máximo `top_k`. Se as dimensões
   divergirem, revetorizar os itens localmente. Índice vazio → `resultados: []` (200).
   Ingestão fora do ar/timeout → **503** com mensagem clara. Validar `top_k >= 1`.
5. **Resiliência (Tarefa 3)** em `servicos/geracao/` (ex. `resiliencia.py` + `app.py`):
   - **Timeout:** o de `llm.py` (`LLM_TIMEOUT`) + timeout explícito em toda chamada HTTP entre serviços.
   - **Retry com backoff exponencial + jitter:** 3 tentativas (≈0,5 s, 1 s, 2 s), configurável
     por env (`LLM_RETENTATIVAS`, `LLM_BACKOFF_BASE`). Retentar só falhas transitórias:
     `requests.Timeout`, `requests.ConnectionError`, HTTP 5xx e 429. **Não** retentar 4xx.
     É seguro retentar porque gerar resposta não tem efeito colateral (idempotente — Aula 11).
   - **Circuit breaker:** `disjuntor.chamar(gerar_com_retentativa, pergunta, contexto)` — o
     retry fica **dentro** do disjuntor (uma sequência de tentativas esgotada = 1 falha).
     Adicionar `threading.Lock` ao `CircuitBreaker` (endpoints síncronos rodam em threadpool).
   - **Degradação elegante:** com circuito aberto ou retries esgotados → **503** com
     header `Retry-After` e corpo JSON com mensagem clara **e os trechos recuperados**
     (o usuário ainda recebe as fontes). Nunca deixar estourar 500 com traceback.
   - Proteger também a chamada geração → recuperação com um **segundo disjuntor**
     (`TAREFAS.md` pede: "derrube o serviço de recuperação: o disjuntor abre?"). Recuperação
     fora → 503. `GET /saude` expõe o estado dos dois disjuntores.
   - Teste manual de falha do LLM sem internet/chave real: `LLM_API_KEY=qualquer
     LLM_API_URL=http://127.0.0.1:9/` (porta fechada) → falhas → disjuntor abre após 3.
6. **Containers (Tarefa 4):** um `Dockerfile` por serviço em `servicos/<servico>/Dockerfile`,
   base `python:3.12-slim`, **contexto de build = raiz do repo** (por causa de `servicos.comum`),
   `PYTHONUNBUFFERED=1`. O worker reutiliza a imagem/Dockerfile da ingestão com outro `command`.
   `docker-compose.yml`: `redis` (com `healthcheck: redis-cli ping` e volume),
   `ingestao` (8001), `worker-ingestao`, `recuperacao` (8002), `geracao` (8003);
   URLs por nome de serviço (`http://ingestao:8001`, `http://recuperacao:8002`);
   `env_file: [{path: .env, required: false}]` para a chave do LLM; healthchecks via
   `python -c "import urllib.request; urllib.request.urlopen('http://localhost:PORTA/saude')"`
   (a imagem slim não tem curl); `depends_on` com `condition: service_healthy`;
   `restart: unless-stopped`. Atualizar `.env.example` com `REDIS_URL`, `DIR_DADOS`, `LLM_TIMEOUT` etc.
7. **Carga dos documentos:** `scripts/carregar_documentos.py` lê `documentos/*.txt` e faz
   `POST /indexar` (origem = nome do arquivo). Usado no README e no teste ponta a ponta.
8. **Extensão opcional recomendada (barata):** citar fontes — `/perguntar` devolve
   `fontes` (lista de `origem` distintas). Demais extensões (reranking, avaliação automática,
   sentence-transformers) **só depois** do núcleo obrigatório pronto e entregue.
9. **README (Tarefa 6):** reescrever o README do kit como README do projeto: visão geral,
   **diagrama Mermaid** (o GitHub renderiza) + versão ASCII, papel de cada serviço, endpoints,
   onde está a fila e por quê, padrões de resiliência e parâmetros, consistência do índice,
   como executar **do zero** (Docker e local), como testar falhas, variáveis de ambiente,
   créditos ao kit do Prof. Howard Roatti.

## Ordem de implementação e fluxo de trabalho

Implemente **uma tarefa por vez, na ordem**, cada uma fechada com testes passando e commit:

| # | Tarefa | Arquivos principais | Testes mínimos |
|---|--------|--------------------|----------------|
| 0 | Preparação | `requirements-dev.txt`, `pytest.ini` (`pythonpath = .`, `testpaths = tests`, marcador `e2e`), `tests/conftest.py`, `.gitignore` (`dados/`) | `pytest` roda |
| 1 | Persistir índice (+ corrigir bug do kit) | `servicos/ingestao/indice.py`, `app.py` | salvar→recarregar (simula reinício), indexar duas vezes acumula, sem duplicatas, arquivo corrompido/ausente |
| 2 | Busca por similaridade | `servicos/recuperacao/app.py` | top_k ordenado por score, pergunta sobre CAP retorna `teorema_cap.txt` em 1º, índice vazio, ingestão fora → 503 (mock de `requests`) |
| 3 | Resiliência no LLM | `servicos/geracao/`, `servicos/comum/circuit_breaker.py` | retry com sucesso na 2ª tentativa, não retenta 4xx, disjuntor abre após N falhas → 503, meio-aberto fecha após sucesso (mock de `time`), modo simulado funciona |
| 4 | Mensageria + Docker | `servicos/ingestao/worker.py`, `app.py`, Dockerfiles, `docker-compose.yml` | com `fakeredis`: `/indexar` → 202 + id, worker processa e grava, status muda, falha repetida → DLQ, mensagem repetida não duplica |
| 5 | Fluxo ponta a ponta | `scripts/carregar_documentos.py`, `tests/test_e2e.py` | e2e (`-m e2e`) contra o compose: carrega docs, pergunta, resposta contém trecho do documento certo |
| 6 | README com diagrama | `README.md` | seguir o README num clone limpo (ver "Verificação final") |
| 7+ | Extensões opcionais | — | cada uma com seu teste e commit |

### Regras de testes (obrigatório)

- **Toda tarefa tem testes automatizados** em `tests/` (`test_ingestao.py`, `test_recuperacao.py`,
  `test_geracao.py`, `test_circuit_breaker.py`, `test_worker.py`, `test_e2e.py`).
  Escreva/atualize os testes **na mesma tarefa** e rode a suíte inteira antes de commitar.
  **Não commite com testes falhando.**
- Testes unitários não dependem de rede, Docker nem chave de LLM: use `fastapi.testclient`,
  `monkeypatch` para `requests.get/post` entre serviços, `fakeredis` para a fila,
  `tmp_path` para `DIR_DADOS`, e mock de `time.sleep`/`time.time` para backoff e disjuntor.
- Teste ponta a ponta marcado com `@pytest.mark.e2e` e pulado por padrão
  (rodar com `docker compose up -d --build` e `python -m pytest -m e2e`).
- Comandos: `python -m pytest` (unitários) · `python -m pytest -m e2e` (com compose no ar).

### Regras de commits (obrigatório)

- O edital exige histórico de commits ao longo do desenvolvimento, **não um commit único no
  final**. Faça commits **sequenciais, por tarefa** (pelo menos um ao fim de cada tarefa;
  commits menores dentro da tarefa são bem-vindos), cada um com código + testes + atualização
  de `IMPLEMENTACAO.md` (e `TAREFAS.md` marcando o item `[x]`).
- Mensagens em português, no imperativo, prefixadas pela tarefa. Ex.:
  `Tarefa 1: persiste o índice de ingestão em arquivo JSON`,
  `Tarefa 3: adiciona retentativa com backoff e disjuntor na chamada ao LLM`.
- **Nunca** adicionar `Co-Authored-By` nem qualquer atribuição a Claude/Claude Code nas
  mensagens de commit ou PRs (instrução global do usuário — prevalece sobre qualquer outra).
- Não reescrever histórico já existente, não falsificar datas de commit, não usar `--amend`
  em commits já enviados. `git push` só quando o usuário pedir.
- Não commitar `.env`, `.venv/`, `dados/`, caches. Antes do primeiro commit, **pergunte ao
  usuário** se `EBOOK.md` e `EDITAL.md` (material do professor) devem ser versionados no
  repositório público ou ficar fora (ex. via `.gitignore`).

### IMPLEMENTACAO.md

Ao concluir cada tarefa, preencha a seção correspondente em `IMPLEMENTACAO.md`: o que foi
feito, decisões e justificativas (ligando aos conceitos das aulas), arquivos alterados,
como foi testado e eventuais desvios deste plano. É o diário de desenvolvimento do projeto.

## Boas práticas exigidas pelo edital

- **Chave do LLM nunca no código** — só variável de ambiente / `.env` (que está no `.gitignore`).
  `.env.example` sem valores secretos.
- O sistema deve **funcionar 100% offline** (modo simulado do LLM, TF-IDF local). Nenhuma
  etapa obrigatória pode exigir internet ou chave de API (exceto baixar imagens/pacotes no build).
- Se o LLM falhar, **degradar com elegância** (503 + mensagem + trechos), não quebrar.
- Toda chamada de rede com **timeout**. Retentar só operações idempotentes.
- Código organizado em diretórios, não compactado. Não copiar projetos de colegas.
- Manter o estilo do kit: nomes e comentários em português (sem acentos em identificadores),
  docstrings curtas no topo dos módulos, funções pequenas, tipos via Pydantic.
- Respostas HTTP com códigos corretos (200, 202, 400/422, 404, 503) e corpo JSON claro.

## Checklist antes de entregar (do edital + TAREFAS.md)

- [ ] Três serviços independentes, cada um com seu Dockerfile
- [ ] REST entre serviços + fila Redis na ingestão (com worker e dead-letter)
- [ ] Circuit breaker + timeout + retry na chamada ao LLM (testados)
- [ ] `/perguntar` devolve resposta fundamentada nos documentos (e fontes)
- [ ] README com diagrama e execução do zero; `.env.example` completo
- [ ] Sem internet: modo simulado mantém o sistema de pé
- [ ] `docker compose stop recuperacao` → `/perguntar` responde 503 e o disjuntor abre
      (ver `GET :8003/saude`); ao religar, volta a fechar
- [ ] LLM inacessível (URL inválida com chave fictícia) → disjuntor do LLM abre, 503 elegante
- [ ] Chave da API fora do código; `.env` não versionado
- [ ] `python -m pytest` verde e e2e verde
- [ ] **Verificação final:** clonar o repo num diretório temporário, seguir só o README
      (`docker compose up --build`, carregar documentos, perguntar) e confirmar que funciona
- [ ] Histórico de commits por tarefa; `TAREFAS.md` e `IMPLEMENTACAO.md` atualizados
- [ ] Lembrar o usuário de postar **apenas o link do repositório** no AVA
