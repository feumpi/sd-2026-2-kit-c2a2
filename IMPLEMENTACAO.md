# IMPLEMENTACAO.md — Diário de desenvolvimento do C2.A2

Registro de como o projeto foi implementado, tarefa a tarefa: decisões, justificativas,
testes e desvios do plano em `CLAUDE.md`. Preencher ao concluir cada tarefa.

## Resumo

| # | Tarefa | Status | Commit(s) |
|---|--------|--------|-----------|
| 0 | Preparação (testes, dependências de dev) | concluída | `chore: prepara ambiente de testes` |
| 1 | Persistir o índice | concluída | `feat(ingestao): persiste o índice em arquivo JSON` |
| 2 | Busca por similaridade | concluída | `feat(recuperacao): implementa busca por similaridade` |
| 3 | Circuit breaker, timeout e retry no LLM | concluída | `feat(geracao): protege o LLM com retentativa, tempo-limite e disjuntor` |
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

## Tarefa 2 — Busca por similaridade

**O que foi feito:** `POST /buscar` lê o índice da ingestão por REST (`GET /indice`), vetoriza a
pergunta, calcula a similaridade do cosseno com cada trecho e devolve os `top_k` mais
parecidos, ordenados e com `texto`, `origem` e `score`.

**Decisões e justificativas:**
- **Mesmo espaço vetorial sem compartilhar código:** a recuperação não importa nada da
  ingestão. Ela reajusta um `Vetorizador` com os textos do índice **na mesma ordem**, o que
  gera exatamente o vocabulário usado pela ingestão, e reutiliza os vetores recebidos. Se a
  dimensão divergir (índice gerado por outra versão), revetoriza os itens localmente.
- A recuperação não guarda estado: lê o índice a cada consulta, então reflete atualizações
  da ingestão sem cache para invalidar. O ranqueamento depende só do conteúdo, nunca do
  relógio das máquinas (Aula 9).
- **Falha parcial** (Aula 1/11): a chamada à ingestão tem timeout (`TIMEOUT_INGESTAO`, 5 s).
  Se a ingestão estiver fora do ar, a rota responde **503** com mensagem clara, em vez de 500.
- Validação de entrada com Pydantic: pergunta não vazia e `1 <= top_k <= 20` (422 se inválido).
- Índice vazio não é erro: devolve `resultados: []`.

**Arquivos:** `servicos/recuperacao/app.py`, `tests/test_recuperacao.py`.

**Testes:** com os documentos reais de `documentos/` e o `requests.get` substituído por um
mock: pergunta sobre CAP traz `teorema_cap.txt` em primeiro, pergunta sobre Raft traz
`consenso_raft.txt`, ordenação e limite de `top_k`, índice vazio, dimensão divergente,
ingestão fora do ar (503) e `top_k` inválido (422). `python -m pytest`: 17 passaram.

## Tarefa 3 — Circuit breaker, tempo-limite e retentativa no LLM

**O que foi feito:** a chamada ao LLM no serviço de geração passou a ser protegida pelos três
padrões da Aula 11, compostos assim:

```
disjuntor_llm.chamar( com_retentativa( llm.gerar com tempo-limite ) )
```

- **Tempo-limite:** `LLM_TIMEOUT` (padrão 20 s), já aplicado no `requests.post` de `llm.py`.
  As chamadas entre serviços também têm tempo-limite (`TIMEOUT_RECUPERACAO`, `TIMEOUT_INGESTAO`).
- **Retentativa** (`servicos/geracao/resiliencia.py`): 3 tentativas com backoff exponencial e
  jitter (≈0,5 s, ≈1 s), configuráveis por `LLM_RETENTATIVAS` e `LLM_BACKOFF_BASE`. Só retenta
  falhas **transitórias**: tempo-limite, conexão recusada, HTTP 5xx e 429. Um 4xx (chave
  inválida, requisição malformada) não melhora repetindo e sobe na hora. Retentar é seguro
  porque gerar uma resposta não tem efeito colateral (é idempotente).
- **Circuit breaker:** a retentativa fica *dentro* do disjuntor, então uma sequência de
  tentativas esgotada conta como uma falha. Com 3 falhas seguidas (`LLM_LIMITE_FALHAS`) o
  circuito abre por 20 s (`LLM_ESPERA_DISJUNTOR`) e as perguntas são respondidas na hora, sem
  esperar pelo LLM. Isso evita falha em cascata.
- **Degradação elegante:** com o circuito aberto ou as retentativas esgotadas, a rota devolve
  **503** com header `Retry-After`, mensagem clara e os **trechos e fontes já recuperados**. O
  usuário ainda recebe algo útil e nunca vê um 500 com traceback.

**Decisões e justificativas:**
- **Adaptações no `CircuitBreaker` do kit:** ganhou uma `threading.Lock`, porque as rotas
  síncronas do FastAPI rodam num pool de threads e o contador de falhas sofria condição de
  corrida (Aula 3). No estado meio-aberto passa a deixar passar **uma única** chamada de
  teste, como descreve a Aula 11. Também ganhou `segundos_para_tentar()`, usado no `Retry-After`.
  A chamada protegida fica fora da trava para não serializar as requisições.
- **Segundo disjuntor**, na chamada geração → recuperação, atendendo ao item "derrube o
  serviço de recuperação: o disjuntor abre?" do `TAREFAS.md`. `GET /saude` expõe o estado dos
  dois disjuntores e o modo do LLM (`api` ou `simulado`).
- **Extensão opcional (citar fontes):** `/perguntar` devolve `fontes`, a lista das origens
  que embasaram a resposta. Trechos com score 0 (sem nenhum termo em comum com a pergunta)
  são descartados. Se não sobrar nenhum, o LLM nem é chamado e a resposta diz que não há base
  nos documentos.
- `llm.gerar` é chamado por meio de `chamar_llm`, que resolve `llm.gerar` em tempo de
  execução. Isso facilita os testes e mantém `llm.py` intocado.

**Arquivos:** `servicos/comum/circuit_breaker.py`, `servicos/geracao/resiliencia.py` (novo),
`servicos/geracao/app.py`, `tests/test_circuit_breaker.py`, `tests/test_geracao.py`.

**Testes:** disjuntor (abre no limite, recusa sem chamar, meio-aberto fecha com sucesso e
reabre com falha, sucesso zera falhas, uma única chamada de teste com threads concorrentes);
geração (modo simulado, falha transitória recuperada na 3ª tentativa com espera progressiva
e tempo-limite repassado, 4xx não retentado, disjuntor abre após 3×3 tentativas e a 4ª
pergunta não chega ao LLM, 503 com `Retry-After`, trechos e fontes, recuperação fora do ar
abre o segundo disjuntor, ausência de trechos relevantes, classificação de falhas e cálculo
do backoff). Relógio e `time.sleep` simulados. `python -m pytest`: 37 passaram.
