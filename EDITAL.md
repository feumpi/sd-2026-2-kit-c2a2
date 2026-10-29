---
documento: Edital do Trabalho C2.A2
titulo: RAG Distribuído em Microsserviços
disciplina: Sistemas Distribuídos e Computação em Nuvem
professor: Prof. M.Sc. Howard Roatti
contato_professor: howardcruzroatti@gmail.com
valor_total: 5.0
entrega: 2026-10-29 (Aula 12)
prazo_formacao_grupos: 2026-09-30
ultima_atualizacao: 2026-08-01
kit_de_partida: https://github.com/howardroatti/sd-2026-2-kit-c2a2
linguagem_padrao: Python
apresentacao_oral: false
avaliacao_substitutiva: false
penalidade_atraso: 0.5 ponto por dia
---

# Trabalho C2.A2 — RAG Distribuído em Microsserviços

- **Disciplina:** Sistemas Distribuídos e Computação em Nuvem
- **Professor:** Prof. M.Sc. Howard Roatti
- **Valor:** 5,0 pontos
- **Entrega:** 29/10/2026 (Aula 12)
- **Última atualização do edital:** 01/08/2026

## Contexto

RAG (geração aumentada por recuperação) é a técnica que permite um modelo de linguagem responder com base em documentos SEUS, sem precisar ser retreinado. Do ponto de vista de sistemas distribuídos, é um caso perfeito: três responsabilidades distintas que precisam conversar entre si, com uma dependência externa lenta e instável (a API do LLM) que precisa ser protegida.

## Edital

> **Atenção:** Leia todo o edital antes de começar. Só será corrigido o trabalho que seguir estas orientações; caso contrário, a avaliação será desconsiderada.

### Item 0 — Formação de grupos

A formação de grupos é LIVRE (inclusive individual). Se optar por grupo, envie os nomes dos componentes ao professor até **30/09/2026** no endereço **howardcruzroatti@gmail.com**.

### Item 1 — Tema

O tema é fixo: um sistema de perguntas e respostas com recuperação (RAG) sobre um conjunto de documentos, decomposto em microsserviços. O modelo de embeddings e o cliente de LLM já vêm prontos no kit.

### Item 2 — Decomposição em três microsserviços

Decompor o sistema em TRÊS microsserviços independentes:

| # | Serviço | Responsabilidade |
|---|---------|------------------|
| 1 | Ingestão/embeddings | Recebe documentos e os indexa em armazenamento vetorial. |
| 2 | Recuperação | Dada uma pergunta, busca os trechos mais relevantes. |
| 3 | Geração | Monta o prompt com os trechos e chama o LLM por API. |

### Item 3 — Comunicação

Comunicar os serviços por REST ou gRPC, e usar mensageria (fila) em ao menos uma etapa do fluxo.

### Item 4 — Resiliência

Proteger a chamada ao LLM com:

- CIRCUIT BREAKER;
- tempo-limite (timeout);
- retentativa (retry).

### Item 5 — Fluxo ponta a ponta

Garantir o fluxo completo de ponta a ponta: uma pergunta entra e uma resposta fundamentada nos documentos sai.

### Item 6 — README com diagrama

Escrever um README com um diagrama (mesmo simples) da arquitetura dos três serviços.

### Item 7 — Extensões opcionais

Não valem nota extra, mas enriquecem o trabalho e o seu portfólio:

- Reordenar os trechos recuperados por relevância (reranking).
- Citar no resultado quais documentos embasaram a resposta.
- Persistir os vetores em disco ou em um banco vetorial, em vez de memória.
- Avaliar a qualidade da resposta com um critério automático simples.

### Item 8 — Entregáveis

- Todo o código no repositório do GitHub do grupo, organizado em diretórios (não compactado).
- README explicando a arquitetura e como executar o projeto do zero.
- No AVA, poste APENAS o link do repositório do GitHub (se o AVA exigir arquivo, envie um documento com o link).
- Entrega no repositório, SEM apresentação oral.

### Item 9 — Distribuição da pontuação (total 5,0)

| Nota | Critério | O que se avalia |
|------|----------|-----------------|
| 1,5 | Arquitetura e decomposição em serviços | Arquitetura: três serviços independentes, bem separados. |
| 1,5 | Comunicação funcionando (REST / gRPC / mensageria) | Comunicação: REST/gRPC entre serviços + mensageria em uma etapa. |
| 1,0 | Resiliência e tratamento de falhas | Resiliência: circuit breaker, tempo-limite e retentativa na chamada ao LLM. |
| 1,0 | Execução reproduzível (README, container, deploy) | Execução: README com diagrama; o fluxo completo funciona do zero. |
| **5,0** | **TOTAL** | *Sofisticação do modelo de IA NÃO pontua.* |

> **Nota:** A qualidade ou a sofisticação do modelo de IA NÃO compõe a nota. A inteligência artificial é a carga de trabalho do sistema, não o objeto de avaliação. Todo contato com IA neste trabalho é chamada de biblioteca ou de API: não é necessário treinar modelos nem dominar matemática de aprendizado de máquina.

### Item 10 — Kit de partida

URL: https://github.com/howardroatti/sd-2026-2-kit-c2a2

- Faça um fork (cópia) do kit e estude-o ANTES de começar o seu projeto.
- O modelo de IA já vem pronto; concentre o esforço na engenharia distribuída.
- Não deixe para a última hora: o projeto cresce ao longo do bloco.
- Não serão aceitos projetos idênticos ou cópias parciais.

## Observações importantes

- Se for em grupo, todos os componentes devem participar do desenvolvimento; membros que não contribuírem podem ter a nota individual ajustada.
- O trabalho NÃO possui avaliação substitutiva.
- Atrasos serão tolerados, porém com perda de 0,5 ponto por dia de atraso.
- Mantenha o GitHub atualizado com commits ao longo do período (e não um único commit no final).

## FAQ — Perguntas Frequentes

### Preciso saber machine learning?

Não. O modelo já vem pronto e configurado no kit. Todo contato com IA é chamada de biblioteca ou de API — você não treina modelos nem precisa de matemática de ML.

### Preciso de internet ou GPU no laboratório?

Não. O kit funciona 100% offline: o modelo é treinado localmente (scikit-learn) e o cliente de LLM tem modo simulado quando não há chave de API.

### O trabalho é em grupo?

Grupos livres, a critério de vocês — inclusive individual. Se optarem por grupo, todos os componentes devem participar do desenvolvimento.

### Tem apresentação?

Não. A entrega é no repositório do GitHub, sem apresentação oral. A avaliação recai sobre o sistema funcionando, a arquitetura e as decisões de projeto.

### Posso usar IA para me ajudar a programar?

Sim, é realista e permitido. O que se avalia é o sistema funcionando e as decisões de arquitetura — que você precisa saber explicar.

### Posso usar outra linguagem?

O kit é em Python porque é o ecossistema usado nas aulas. Se quiser outra linguagem, combine com o professor antes de começar.

### Existe avaliação substitutiva para o trabalho?

Não. O trabalho não possui avaliação substitutiva.

### E se eu atrasar a entrega?

Atrasos serão tolerados, porém com perda de 0,5 ponto por dia de atraso.

## Roteiro sugerido de execução

1. Não tente fazer os três serviços ao mesmo tempo: entregue a ingestão primeiro (Aula 8).
2. Teste o circuit breaker de verdade — desligue a internet e veja o que acontece.
3. NUNCA coloque a chave da API do LLM no código; use variável de ambiente.
4. Se o LLM externo falhar, o sistema deve degradar com elegância, não quebrar.

> **Verificação final:** Antes de entregar, apague a pasta do projeto, clone do zero e siga o SEU próprio README. Se funcionar, está pronto para entrega.

## Checklist de requisitos obrigatórios (derivado do edital)

- [ ] Três microsserviços independentes: ingestão/embeddings, recuperação, geração (Item 2)
- [ ] Comunicação entre serviços via REST ou gRPC (Item 3)
- [ ] Mensageria (fila) em ao menos uma etapa do fluxo (Item 3)
- [ ] Circuit breaker na chamada ao LLM (Item 4)
- [ ] Tempo-limite na chamada ao LLM (Item 4)
- [ ] Retentativa na chamada ao LLM (Item 4)
- [ ] Fluxo ponta a ponta: pergunta → resposta fundamentada nos documentos (Item 5)
- [ ] README com diagrama da arquitetura dos três serviços (Item 6)
- [ ] README explicando como executar o projeto do zero (Item 8)
- [ ] Código no GitHub, organizado em diretórios, não compactado (Item 8)
- [ ] Commits distribuídos ao longo do período (Observações)
- [ ] Chave da API do LLM em variável de ambiente, nunca no código (Roteiro)
- [ ] Link do repositório postado no AVA (Item 8)
