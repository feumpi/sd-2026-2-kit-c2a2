---
documento: Ebook / guia de estudo da disciplina
titulo: Sistemas Distribuídos e Computação em Nuvem
subtitulo: Um guia de estudo cloud-native, com Inteligência Artificial como serviço
autor: Prof. M.Sc. Howard Roatti
instituicao: FAESA — Faculdades Integradas Espírito-Santenses
semestre: 2026/2
total_aulas: 17
blocos:
  - id: C1
    nome: Comunicação distribuída
    aulas: 1-7
    trabalho_pratico: C1.A2 — Serviço de Inferência Distribuído
    kit: sd-2026-2-kit-c1a2
  - id: C2
    nome: Coordenação e consistência
    aulas: 8-12
    trabalho_pratico: C2.A2 — RAG Distribuído em Microsserviços
    kit: sd-2026-2-kit-c2a2
  - id: C3
    nome: Nuvem, implantação e segurança
    aulas: 13-17
    trabalho_pratico: C3.A2 — Plataforma de IA como Serviço
    kit: sd-2026-2-kit-c3a2
avaliacoes:
  - {id: C1.A1, tipo: prova escrita individual estilo ENADE, valor: 5.0, data: 2026-09-17, aula: 7}
  - {id: C1.A2, tipo: trabalho prático, valor: 5.0, data: 2026-09-17, aula: 7}
  - {id: C2.A1, tipo: prova escrita individual estilo ENADE, valor: 5.0, data: 2026-10-29, aula: 12}
  - {id: C2.A2, tipo: trabalho prático, valor: 5.0, data: 2026-10-29, aula: 12}
  - {id: C3.A1, tipo: prova escrita individual estilo ENADE, valor: 5.0, data: 2026-11-26, aula: 17}
  - {id: C3.A2, tipo: projeto integrador, valor: 5.0, data: 2026-11-26, aula: 17}
enade_2026: 2026-11-29
---

# Sistemas Distribuídos e Computação em Nuvem

*Um guia de estudo cloud-native, com Inteligência Artificial como serviço*

- **Autor:** Prof. M.Sc. Howard Roatti
- **Instituição:** FAESA — Faculdades Integradas Espírito-Santenses
- **Semestre:** 2026/2

> **Nota de conversão:** Este arquivo é uma conversão em Markdown do ebook original (PDF). Todo o conteúdo textual foi preservado; os cabeçalhos de página repetidos foram removidos e as caixas visuais (EM RESUMO, FOCO ENADE, NO SEU TRABALHO, QUESTÕES, GLOSSÁRIO) foram convertidas em seções padronizadas, iguais em todas as aulas.

## Cronograma das aulas (índice rápido)

| Aula | Bloco | Data | Título | Trabalho relacionado |
|------|-------|------|--------|----------------------|
| 1 | C1 | 06/08/2026 | Abertura, diagnóstico e ambiente | C1.A2 |
| 2 | C1 | 13/08/2026 | Modelos de arquitetura e sockets (TCP/UDP) | C1.A2 |
| 3 | C1 | 20/08/2026 | Concorrência: um servidor para vários clientes | C1.A2 |
| 4 | C1 | 27/08/2026 | Do RPC ao gRPC: chamada remota moderna | C1.A2 |
| 5 | C1 | 10/09/2026 | Serviços web: REST e OpenAPI com FastAPI | C1.A2 |
| 6 | C1 | Estudo Dirigido (EAD) | IA como serviço distribuído (marco do curso) | C1.A2 |
| 7 | C1 | 17/09/2026 | Revisão e Avaliação C1.A1 + entrega do C1.A2 | C1.A2 |
| 8 | C2 | 24/09/2026 | Mensageria, eventos e API Gateway | C2.A2 |
| 9 | C2 | 01/10/2026 | Tempo e ordenação: relógios lógicos | C2.A2 |
| 10 | C2 | 08/10/2026 | Replicação, consistência e o teorema CAP | C2.A2 |
| 11 | C2 | 22/10/2026 | Consenso (Raft) e resiliência | C2.A2 |
| 12 | C2 | 29/10/2026 | Revisão e Avaliação C2.A1 + entrega do C2.A2 | C2.A2 |
| 13 | C3 | 05/11/2026 | Computação em nuvem, containers e o primeiro deploy | C3.A2 |
| 14 | C3 | 12/11/2026 | Orquestração, serverless e computação na borda | C3.A2 |
| 15 | C3 | 19/11/2026 | Observabilidade: enxergar o que acontece no sistema | C3.A2 |
| 16 | C3 | Estudo Dirigido (EAD) | Segurança, LGPD e revisão geral para o ENADE | C3.A2 |
| 17 | C3 | 26/11/2026 | Avaliação C3.A1, entrega do C3.A2 e tendências | C3.A2 |

## Sumário original (com páginas do PDF)

- Apresentação — p. 2
  - Sobre este livro — p. 2
  - Como o livro está organizado — p. 2
  - Uma palavra sobre o ENADE — p. 2
  - Sobre a Inteligência Artificial neste livro — p. 3
- Sumário — p. 4
- **Parte C1 — Comunicação distribuída** — p. 6
  - Abertura, diagnóstico e ambiente — p. 7
  - Modelos de arquitetura e sockets (TCP/UDP) — p. 10
  - Concorrência: um servidor para vários clientes — p. 13
  - Do RPC ao gRPC: chamada remota moderna — p. 16
  - Serviços web: REST e OpenAPI com FastAPI — p. 19
  - IA como serviço distribuído (marco do curso) — p. 22
  - Revisão e Avaliação C1.A1 + entrega do C1.A2 — p. 25
- **Parte C2 — Coordenação e consistência** — p. 29
  - Mensageria, eventos e API Gateway — p. 30
  - Tempo e ordenação: relógios lógicos — p. 33
  - Replicação, consistência e o teorema CAP — p. 36
  - Consenso (Raft) e resiliência — p. 39
  - Revisão e Avaliação C2.A1 + entrega do C2.A2 — p. 42
- **Parte C3 — Nuvem, implantação e segurança** — p. 46
  - Computação em nuvem, containers e o primeiro deploy — p. 47
  - Orquestração, serverless e computação na borda — p. 50
  - Observabilidade: enxergar o que acontece no sistema — p. 53
  - Segurança, LGPD e revisão geral para o ENADE — p. 55
  - Avaliação C3.A1, entrega do C3.A2 e tendências — p. 58
- Apêndice A — Mapa de revisão para o ENADE — p. 62
- Apêndice B — Bibliografia e materiais de apoio — p. 65
  - Básica — p. 65
  - Complementar — p. 65
  - Materiais abertos — p. 65

---

# Apresentação

## Sobre este livro

Este ebook acompanha a disciplina Sistemas Distribuídos e Computação em Nuvem. Ele foi escrito a partir das apresentações de aula, mas traz mais profundidade: onde o slide apresenta um tópico em uma linha, aqui você encontra a explicação completa, com exemplos e o porquê de cada decisão de projeto.

A ordem dos capítulos segue exatamente a ordem das 17 aulas do semestre, organizadas em três blocos — C1 (comunicação), C2 (coordenação) e C3 (nuvem e operação). Você pode ler em sequência, acompanhando as aulas, ou usar o livro como referência para revisar um tópico específico.

## Como o livro está organizado

Cada capítulo abre com o que você será capaz de fazer ao final dele. Em seguida vêm as seções de conteúdo, escritas em linguagem direta. Ao longo do texto você encontra estas marcações:

- Os termos-chave aparecem em negrito na primeira vez que são explicados. São exatamente os termos que reaparecem nas caixas ao final do capítulo — quando você reencontrar um deles na revisão, já terá visto sua explicação no texto.
- O quadro **EM RESUMO** condensa a ideia central de cada seção em uma frase — é o que você leva para a prova.
- A caixa **FOCO ENADE** destaca o que costuma ser cobrado no Exame Nacional de Desempenho dos Estudantes, com os termos-chave que você precisa dominar.
- O **GLOSSÁRIO** ao final de cada capítulo reúne, em uma linha cada, as definições dos termos novos.

Os capítulos que fecham cada bloco (7, 12 e 17) são de revisão e trazem **QUESTÕES COMENTADAS** no formato do ENADE, resolvidas passo a passo.

## Uma palavra sobre o ENADE

O ENADE 2026 será aplicado em 29 de novembro e inclui os cursos de Análise e Desenvolvimento de Sistemas, Ciência da Computação e Sistemas de Informação — ou seja, todos os cursos desta turma. Sistemas distribuídos, redes, computação em nuvem, segurança da informação e bancos de dados distribuídos são eixos recorrentes da prova.

Por isso, as caixas FOCO ENADE não são enfeite: elas apontam, aula a aula, exatamente o que tem maior probabilidade de aparecer no exame. O Apêndice A reúne todos esses pontos em um mapa único, que serve como roteiro final de revisão.

## Sobre a Inteligência Artificial neste livro

A IA aparece o tempo todo, mas sempre como carga de trabalho — um serviço a ser servido, escalado e protegido — e nunca como objeto de estudo em si. Você não precisará treinar modelos nem dominar a matemática de aprendizado de máquina. Todo contato com IA se resume a chamar uma biblioteca ou uma API. O que se aprende aqui é a engenharia de sistemas distribuídos que sustenta qualquer aplicação de IA moderna.

---

# PARTE C1 — Comunicação distribuída

**Aulas 1 a 7**

Como dois programas conversam de forma confiável através da rede. Dos sockets à IA servida por API, passando por concorrência, gRPC e REST.

---

## Aula 1 — Abertura, diagnóstico e ambiente

- **Bloco:** C1
- **Data:** 06/08/2026

### Objetivos (neste capítulo você vai aprender a)

- Explicar o que é um sistema distribuído e por que quase todo software hoje é um.
- Reconhecer o desafio que só existe quando há rede no meio: a falha parcial.
- Deixar seu ambiente pronto: máquina virtual, Python, Git e GitHub.

### O que muda quando existe uma rede no meio

Um programa comum roda inteiro dentro de uma máquina: se algo dá errado, o processo simplesmente para, e você vê o erro. Um **sistema distribuído** é diferente por natureza — ele é formado por vários computadores independentes que cooperam pela rede e se apresentam ao usuário como se fossem um sistema único. Quando você abre o aplicativo do banco, dezenas de máquinas em lugares diferentes trabalham para responder ao seu toque na tela, mas você enxerga apenas o saldo.

Essa cooperação pela rede traz três ganhos que um programa isolado nunca teria. O primeiro é a **escalabilidade**: a capacidade de atender a uma demanda crescente acrescentando mais máquinas, em vez de depender de um único computador cada vez maior. O segundo é a disponibilidade, já que o serviço pode continuar de pé mesmo que uma máquina caia. O terceiro é a proximidade do usuário, colocando servidores em várias regiões. Em troca, aceita-se um custo que não existe no programa local: a rede é lenta, imprevisível e, principalmente, falha — e não falha de forma limpa.

### Latência e transparência

Duas ideias acompanham todo o curso. A primeira é a **latência**: o tempo que uma mensagem leva para ir de um ponto a outro da rede. Diferente do acesso à memória local, medido em nanossegundos, uma chamada de rede custa milissegundos — e esse tempo é variável, porque a mensagem disputa a rede com todo o resto. Boa parte das decisões de projeto que veremos existe para esconder ou reduzir a latência.

A segunda ideia é a **transparência**: o esforço de esconder do usuário a complexidade da distribuição. Há vários tipos — transparência de acesso (usar um recurso remoto como se fosse local), de localização (não precisar saber em qual máquina o dado está) e de replicação (não perceber que existem várias cópias). Quanto maior a transparência, mais simples o sistema parece por fora, e mais trabalho ele exige por dentro.

### Falha parcial: o problema central da disciplina

Num sistema centralizado, a falha é total: ou tudo funciona, ou tudo para, e fica evidente qual foi o caso. Num sistema distribuído surge a **falha parcial** — uma parte do sistema para enquanto o resto continua funcionando. Pior que isso é a ambiguidade que ela cria. Quando um serviço A envia um pedido a um serviço B e não recebe resposta, A não tem como saber o que aconteceu: B pode ter caído, pode estar apenas lento, ou a resposta pode ter se perdido no caminho de volta. Do ponto de vista de A, essas três situações são indistinguíveis.

Guarde esta ideia, porque praticamente todo o resto da disciplina é uma resposta a ela. Os relógios lógicos, o teorema CAP, o consenso, os padrões de resiliência — tudo existe porque a falha parcial é real e inevitável. Aprender sistemas distribuídos é, em boa medida, aprender a projetar contando com ela.

### O que você vai construir e onde guardá-lo

O fio condutor prático do curso é uma plataforma de IA como serviço. Ela nasce como um simples par cliente-servidor trocando mensagens e, aula após aula, ganha interfaces modernas, uma fila, microsserviços, containers e, por fim, é publicada na nuvem. A IA entra apenas como a tarefa que esse sistema executa: você chama um modelo pronto, nunca o treina. Desde o primeiro dia, todo esse código é versionado num **repositório** — a pasta controlada pelo Git onde você guarda o histórico do projeto e o envia para o GitHub. Trabalhar em repositório não é burocracia: é como equipes reais colaboram e como você provará, ao final, tudo o que construiu.

### No seu trabalho — C1.A2: Serviço de Inferência Distribuído

O trabalho da primeira verificação — o C1.A2 — Serviço de Inferência Distribuído — começa hoje pela base: preparar o ambiente e criar o repositório onde ele vai crescer. O kit de partida já traz o modelo de IA pronto e o esqueleto do projeto.

- Clonar o repositório sd-2026-2-kit-c1a2 e criar o seu repositório de entrega.
- Rodar o exemplo mínimo cliente-servidor que acompanha o kit.
- Ler o TAREFAS.md, que lista o núcleo obrigatório item a item.

**Repositório do kit:** `sd-2026-2-kit-c1a2`

### Em resumo

- Sistema distribuído = várias máquinas cooperando que parecem uma só.
- A dificuldade não é a rede ser lenta: é você não saber o que aconteceu do outro lado.
- Você aprende sistemas distribuídos construindo um serviço de IA de verdade.

### Foco ENADE

Questões introdutórias pedem a definição de sistema distribuído e o contraste com sistemas centralizados, os tipos de transparência (acesso, localização, replicação) e as justificativas para distribuir — escalabilidade, disponibilidade e desempenho. A noção de falha parcial aparece disfarçada em estudos de caso, e a latência costuma justificar decisões de arquitetura.

**Costuma cair:**
- Conceito e caracterização de sistemas distribuídos.
- Vantagens e desafios: escalabilidade, disponibilidade e falha parcial.
- Diferença entre sistema centralizado e sistema distribuído.
- Tipos de transparência (acesso, localização, replicação).

**Termos-chave:** Sistema distribuído · Falha parcial · Transparência · Escalabilidade · Latência

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Um serviço A envia uma requisição ao serviço B e não recebe resposta no tempo esperado. Sobre essa situação em um sistema distribuído, assinale a alternativa correta.

- (A) A pode concluir com certeza que B falhou.
- (B) A pode concluir que a requisição certamente não foi processada.
- (C) A não distingue, apenas pela ausência de resposta, entre B ter caído, estar lento ou a resposta ter se perdido.
- (D) A deve encerrar todo o sistema, pois trata-se de falha total.
- (E) A situação não ocorre quando se utiliza TCP.

**Resolução.** É a definição de falha parcial: a ausência de resposta é ambígua. O TCP não elimina o problema, pois B pode cair após receber o pedido. As demais alternativas afirmam certezas que A não possui.

**Resposta:** Alternativa C.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Sistema distribuído | Computadores independentes que cooperam e se apresentam como um sistema único. |
| Falha parcial | Uma parte do sistema falha enquanto o restante continua funcionando. |
| Latência | Tempo que uma mensagem leva para ir de um ponto a outro da rede. |
| Transparência | Esconder do usuário a complexidade da distribuição. |
| Repositório | Pasta versionada pelo Git onde você guarda e envia seu código. |

---

## Aula 2 — Modelos de arquitetura e sockets (TCP/UDP)

- **Bloco:** C1
- **Data:** 13/08/2026

### Objetivos (neste capítulo você vai aprender a)

- Diferenciar os modelos cliente-servidor e ponto a ponto (P2P).
- Explicar, com suas palavras, a diferença prática entre TCP e UDP.
- Escrever um cliente e um servidor que trocam mensagens por socket.

### Cliente-servidor e ponto a ponto

Há duas formas básicas de organizar quem fala com quem. No modelo **cliente-servidor**, os papéis são fixos: um lado pede (o cliente) e o outro responde (o servidor). É o modelo dominante na web e em quase todo serviço que você usa. No modelo ponto a ponto — ou **P2P**, de peer-to-peer — todos os participantes têm o mesmo papel e trocam informação diretamente entre si, sem um servidor central; o BitTorrent é o exemplo clássico, em que cada participante baixa e envia ao mesmo tempo.

A escolha tem consequências. O servidor central é simples de gerenciar e proteger, mas concentra carga e é um ponto único de falha. O P2P distribui a carga e não tem um centro que possa cair, mas é bem mais difícil de coordenar, versionar e proteger. A maioria dos sistemas que você vai construir é cliente-servidor; o P2P aparece quando escala e resiliência importam mais que controle.

### Socket: a ponta do cano

Toda comunicação em rede, por baixo, passa por sockets. Um **socket** é a ponta de uma conexão, identificada pela combinação de endereço IP e **porta** — o IP diz em qual máquina, e a porta diz qual programa dentro dela deve receber a mensagem. É por isso que um mesmo servidor pode rodar um site na porta 443 e um banco de dados na 5432 sem confusão: cada serviço escuta a sua. O servidor abre a porta e fica aguardando (as operações `bind`, `listen` e `accept`); o cliente se conecta àquela porta (`connect`); e então os dois trocam bytes. Tudo o que vem depois no curso — gRPC, REST, filas — roda sobre essa base.

### TCP ou UDP: garantia contra velocidade

Sobre o socket você escolhe o protocolo de transporte, e a escolha é um trade-off honesto. O **TCP** estabelece uma conexão antes de enviar dados, garante que eles cheguem na ordem certa e retransmite o que se perde; em troca, tudo isso custa tempo e alguns pacotes de controle. O **UDP** não estabelece conexão e não garante nada: é rápido e leve, mas pacotes podem se perder ou chegar fora de ordem, e cabe à sua aplicação lidar com isso.

A regra prática é clara. Use TCP quando não pode perder dado: um arquivo, uma mensagem de chat, uma transação bancária — nesses casos, receber tudo, na ordem, importa mais que a pressa. Use UDP quando o atraso é pior que a perda: voz, vídeo ao vivo, jogos online, telemetria de sensores — é melhor descartar um quadro atrasado do que travar a imagem esperando por ele. Muitos protocolos modernos, como o do vídeo em tempo real, escolhem UDP justamente por isso.

### No seu trabalho — C1.A2: Serviço de Inferência Distribuído

Sockets são o alicerce invisível do trabalho: as interfaces gRPC e REST que você vai expor rodam sobre eles. Você não os programa diretamente, mas entender esta camada explica por que uma chamada ao serviço pode ficar 'pendurada'.

- Compreender a base sobre a qual as interfaces do C1.A2 serão construídas — fundamento para o tempo-limite que você adicionará na fase de resiliência.

**Repositório do kit:** `sd-2026-2-kit-c1a2`

### Em resumo

- Cliente-servidor tem papéis fixos; em P2P todos fazem os dois papéis.
- Socket = IP + porta. O servidor espera na porta; o cliente conecta nela.
- TCP garante entrega e ordem, mas custa tempo. UDP é rápido, porém pode perder e desordenar.

### Foco ENADE

Um dos tópicos mais cobrados. Espere cenários (streaming, transferência de arquivo, telemetria) que pedem a escolha justificada entre TCP e UDP. Também são comuns questões sobre o conceito de socket e porta, sobre cliente-servidor versus P2P, e sobre as camadas do modelo TCP/IP.

**Costuma cair:**
- Modelo cliente-servidor comparado ao modelo P2P.
- Características de TCP e UDP e critério para escolher entre eles.
- Conceito de socket, porta e endereçamento.
- Camadas do modelo TCP/IP e encapsulamento.

**Termos-chave:** Cliente-servidor · P2P · Socket · Porta · TCP · UDP

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Uma aplicação de voz sobre IP prioriza baixa latência e tolera a perda ocasional de pequenos trechos de áudio. Qual protocolo de transporte é o mais adequado e por quê?

- (A) TCP, porque garante a entrega ordenada de todos os pacotes.
- (B) TCP, porque realiza controle de fluxo e congestionamento.
- (C) UDP, porque não retransmite pacotes perdidos, evitando o atraso acumulado.
- (D) UDP, porque confirma o recebimento de cada pacote enviado.
- (E) UDP, porque estabelece conexão prévia e reduz a latência.

**Resolução.** Em mídia de tempo real, o atraso é pior que a perda; o UDP não retransmite e mantém o fluxo fluido. As alternativas D e E descrevem o UDP incorretamente — ele não confirma recebimento nem estabelece conexão.

**Resposta:** Alternativa C.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Socket | Ponta de uma conexão de rede, identificada por IP e porta. |
| Porta | Número que identifica qual programa da máquina recebe a mensagem. |
| TCP | Protocolo com conexão que garante entrega e ordem das mensagens. |
| UDP | Protocolo sem conexão, rápido, que não garante entrega nem ordem. |
| P2P | Arquitetura em que todos os participantes têm o mesmo papel. |

---

## Aula 3 — Concorrência: um servidor para vários clientes

- **Bloco:** C1
- **Data:** 20/08/2026

### Objetivos (neste capítulo você vai aprender a)

- Explicar por que um servidor simples atende apenas um cliente por vez.
- Usar threads para atender vários clientes ao mesmo tempo.
- Identificar e corrigir uma condição de corrida em estado compartilhado.

### Por que um servidor simples atende um cliente por vez

As chamadas de rede como `accept()` e `recv()` são **bloqueantes**: elas param a execução do programa até que algo aconteça — uma conexão chegar, um dado ser recebido. Num servidor escrito de forma sequencial, isso significa que, enquanto ele atende um cliente, todos os outros ficam esperando na fila. Basta um cliente lento — ou mal-intencionado — para travar o atendimento de todos. Para um serviço real, com muitos usuários simultâneos, isso é inaceitável.

### Uma thread por cliente

A solução clássica é a concorrência: transformar cada atendimento em uma **thread**, uma linha de execução independente dentro do mesmo programa. Quando o servidor aceita uma conexão, ele entrega aquele cliente a uma thread própria e volta imediatamente para o `accept()`, pronto para o próximo. Assim, muitos clientes são atendidos ao mesmo tempo, e um cliente lento atrapalha apenas a sua própria thread. Vale distinguir concorrência de paralelismo: concorrência é lidar com várias tarefas em andamento (revezando o processador), enquanto paralelismo é executá-las literalmente ao mesmo tempo, em núcleos diferentes.

### O preço da concorrência: condição de corrida

A concorrência resolve um problema e cria outro. Se duas threads alteram a mesma variável ao mesmo tempo, o resultado fica imprevisível — é a **condição de corrida**. O exemplo clássico é um contador: duas threads leem o valor 41, ambas somam 1 e ambas gravam 42, quando o correto seria 43; uma das contagens se perdeu. O sintoma é traiçoeiro, porque o erro aparece só às vezes, dependendo do momento exato em que as threads se cruzam, o que torna a depuração difícil.

A proteção fundamental é a **exclusão mútua**: garantir que apenas uma thread por vez execute o trecho de código que mexe no dado compartilhado — a **seção crítica**. Na prática, isso é feito com um **lock** (uma trava): a thread adquire o lock ao entrar na seção crítica e o libera ao sair, de modo que as demais esperam a vez. Esta ideia — acesso concorrente a estado compartilhado — reaparece o semestre inteiro, agora entre máquinas diferentes em vez de threads: as réplicas de um banco de dados enfrentam uma versão distribuída exatamente do mesmo problema.

### No seu trabalho — C1.A2: Serviço de Inferência Distribuído

O seu serviço processa inferências em segundo plano com um worker, e a concorrência desta aula é o que o sustenta. A fila em si já vem pronta no kit; a teoria por trás dela virá na Aula 8.

- **TAREFA 3** — fazer o worker gravar o resultado processado para consulta posterior.
- **TAREFA 5** — tratamento de erro no worker (retentativa).

**Repositório do kit:** `sd-2026-2-kit-c1a2`

### Em resumo

- Um servidor sequencial atende um cliente por vez; os demais esperam.
- Uma thread por cliente libera o laço principal para aceitar o próximo.
- Concorrência sem controle corrompe dado compartilhado. Proteja a seção crítica com lock.

### Foco ENADE

Concorrência é tema recorrente. Domine a diferença entre concorrência e paralelismo e os conceitos de condição de corrida, exclusão mútua, seção crítica, lock e chamada bloqueante. Questões costumam mostrar um contador incorreto ou um cenário de acesso simultâneo e pedir o diagnóstico e a correção.

**Costuma cair:**
- Concorrência e paralelismo: diferença entre os dois.
- Condição de corrida, exclusão mútua e seção crítica.
- Threads e processos: quando usar cada um.
- Escalabilidade de servidores e gargalos.

**Termos-chave:** Thread · Condição de corrida · Exclusão mútua · Seção crítica · Lock · Bloqueante

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Duas threads incrementam a mesma variável sem sincronização e o total final fica menor que o esperado. Qual é o problema e a correção adequada?

- (A) Deadlock; aumentar o número de threads.
- (B) Condição de corrida; proteger a seção crítica com exclusão mútua.
- (C) Inanição (starvation); elevar a prioridade das threads.
- (D) Falha de rede; substituir o protocolo de transporte.
- (E) Cold start; pré-aquecer o serviço.

**Resolução.** Acesso concorrente não sincronizado a dado compartilhado é uma condição de corrida; corrige-se garantindo exclusão mútua na seção crítica, com um lock.

**Resposta:** Alternativa B.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Thread | Linha de execução independente dentro do mesmo programa. |
| Condição de corrida | Erro que ocorre quando duas threads alteram o mesmo dado ao mesmo tempo. |
| Seção crítica | Trecho de código que só pode ser executado por uma thread por vez. |
| Lock | Mecanismo que garante exclusão mútua na seção crítica. |
| Bloqueante | Chamada que para a execução até que a operação termine. |

---

## Aula 4 — Do RPC ao gRPC: chamada remota moderna

- **Bloco:** C1
- **Data:** 27/08/2026

### Objetivos (neste capítulo você vai aprender a)

- Explicar a ideia de chamada remota de procedimento (RPC).
- Escrever um contrato .proto com Protocol Buffers.
- Implementar um servidor e um cliente gRPC em Python.

### A ideia do RPC

A chamada remota de procedimento — **RPC**, de Remote Procedure Call — nasceu de um desejo simples: fazer uma função que está em outra máquina parecer uma função local. Em vez de escrever bytes no socket e interpretá-los na mão, você chama algo como `servico.somar(2, 3)` e o **middleware** (a camada de software que fica entre a sua aplicação e a rede) cuida de empacotar os argumentos, enviá-los, receber o resultado e devolvê-lo. A linha do tempo dessa ideia passa pelo RPC clássico, pelo CORBA, pelo **RMI** — a Invocação de Métodos Remotos do Java, que aplica a mesma ideia a objetos — e chega, hoje, ao **gRPC**. A ementa fala de RPC e RMI; tratamos ambos como a origem do gRPC.

### Serialização e o contrato: Protocol Buffers

Para trafegar pela rede, uma estrutura de dados precisa virar uma sequência de bytes e depois ser remontada do outro lado — esse processo de ida e volta é a **serialização**. No gRPC, o formato de serialização e o contrato do serviço são descritos num arquivo com a extensão `.proto`, usando **Protocol Buffers**. Nele você declara quais operações o serviço oferece e quais mensagens trafegam, com seus campos e tipos. Uma ferramenta lê esse arquivo e gera automaticamente o código de cliente e de servidor — os **stubs**, que são justamente os trechos que escondem a rede e fazem a chamada remota parecer local. O ponto importante é a inversão: o contrato existe antes do código, e os dois lados são obrigados a respeitá-lo.

### Por que o gRPC é usado hoje

Três características explicam a adoção. Primeiro, a serialização binária do Protocol Buffers é compacta — trafega muito menos bytes que texto como JSON ou XML. Segundo, o gRPC roda sobre HTTP/2, o que permite várias chamadas na mesma conexão, sem reabri-la a cada pedido. Terceiro, o contrato é tipado, então erros de tipo aparecem cedo, na geração dos stubs, e não em produção. Por isso o gRPC é a escolha natural para a comunicação interna entre serviços — inclusive entre os microsserviços de IA que você vai construir. Para o público externo, porém, o REST ainda costuma vencer pela simplicidade de consumo, como veremos a seguir.

### No seu trabalho — C1.A2: Serviço de Inferência Distribuído

Uma das duas interfaces exigidas pelo C1.A2 é gRPC. Com o contrato .proto e os stubs desta aula, você implementa o método do serviço.

- **TAREFA 4** — implementar o método gRPC `PreverLote` e regerar os stubs.

**Repositório do kit:** `sd-2026-2-kit-c1a2`

### Em resumo

- RPC faz uma chamada remota parecer uma chamada de função local.
- O .proto é o contrato: define mensagens e operações antes do código existir.
- gRPC = contrato tipado + formato binário + HTTP/2. Padrão para serviço falar com serviço.

### Foco ENADE

Espere questões sobre o conceito de RPC e de invocação remota de métodos (RMI), sobre transparência de acesso e sobre o papel do middleware e dos stubs. A serialização — converter estruturas de dados em bytes para trafegar na rede — costuma aparecer junto, assim como a comparação entre gRPC e outras formas de integração.

**Costuma cair:**
- Conceito de RPC e transparência de acesso.
- RMI e invocação de métodos remotos.
- Serialização e representação de dados na rede.
- Middleware de comunicação e stubs.

**Termos-chave:** RPC · RMI · gRPC · Protocol Buffers · Stub · Serialização · Middleware

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** No gRPC, qual é a função do arquivo com extensão .proto?

- (A) Conter a implementação completa do servidor.
- (B) Definir o contrato (mensagens e operações), a partir do qual se geram os stubs.
- (C) Ser gerado automaticamente após a implementação do servidor.
- (D) Eliminar a necessidade de comunicação em rede.
- (E) Armazenar as credenciais de autenticação do serviço.

**Resolução.** O .proto é o contrato e vem antes do código; a ferramenta gera, a partir dele, os stubs de cliente e de servidor.

**Resposta:** Alternativa B.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| RPC | Chamada de procedimento remoto: invocar uma função que está em outra máquina. |
| gRPC | Framework atual de RPC, binário, sobre HTTP/2, com contrato em .proto. |
| Protocol Buffers | Formato binário de serialização usado para definir o contrato. |
| Stub | Código gerado que representa o serviço remoto no cliente e no servidor. |
| Middleware | Camada de software que cuida da comunicação entre partes distribuídas. |

---

## Aula 5 — Serviços web: REST e OpenAPI com FastAPI

- **Bloco:** C1
- **Data:** 10/09/2026

### Objetivos (neste capítulo você vai aprender a)

- Explicar os princípios REST e a diferença para o SOAP.
- Construir uma API REST com FastAPI usando os verbos e códigos corretos.
- Ler e usar a documentação automática gerada pelo OpenAPI.

### Do SOAP ao REST

Serviços web permitem que sistemas diferentes conversem pela internet. A geração anterior, o **SOAP**, usava mensagens em XML e um contrato rígido descrito em WSDL; era poderoso, porém verboso e pesado, e ainda sobrevive em sistemas legados e bancários. O **REST** (Representational State Transfer), dominante hoje, é bem mais simples: em vez de uma camada extra sobre o protocolo, ele usa o próprio HTTP como ele já é. A ementa cita os dois, mas um serviço novo nasce REST — ou gRPC — e quase nunca SOAP. Saber os dois é útil para entender a evolução da chamada Arquitetura Orientada a Serviços (SOA) rumo aos microsserviços.

### Recursos, verbos e códigos de status

O REST organiza tudo em torno de **recursos**, que são substantivos e viram URLs: `/tarefas` para a coleção, `/tarefas/7` para um item específico. A ação desejada é dada pelo **verbo HTTP**: GET lê, POST cria, PUT atualiza e DELETE remove. E o resultado é comunicado pelo **código de status**: 200 para sucesso, 201 para recurso criado, 400 para erro do cliente, 404 para recurso inexistente, 500 para erro do servidor. Essa separação clara — a URL diz o quê, o verbo diz a ação, o status diz o resultado — é o que torna uma API REST previsível para quem a consome.

| Verbo | Ação | Idempotente? |
|-------|------|--------------|
| GET | Lê | Sim |
| POST | Cria | Não |
| PUT | Atualiza | Sim |
| DELETE | Remove | Sim |

| Código | Significado |
|--------|-------------|
| 200 | Sucesso |
| 201 | Recurso criado |
| 400 | Erro do cliente |
| 404 | Recurso inexistente |
| 500 | Erro do servidor |

Uma propriedade importante é a **idempotência**: uma operação é idempotente quando, repetida, leva ao mesmo estado final. GET, PUT e DELETE são idempotentes; POST não é, porque cada chamada cria um novo recurso. Guarde essa distinção: ela volta a importar quando falarmos de retentativa, porque só é seguro repetir automaticamente uma operação idempotente.

### OpenAPI: a documentação que não envelhece

Um bom serviço REST precisa de um contrato para quem vai consumi-lo. Com o FastAPI, esse contrato — no padrão **OpenAPI** — é gerado automaticamente a partir dos tipos declarados no seu código, e fica disponível numa página interativa. Como nasce do próprio código, a documentação não fica desatualizada, um problema crônico da era SOAP, em que o contrato e a implementação viviam divergindo.

### No seu trabalho — C1.A2: Serviço de Inferência Distribuído

A outra interface é REST. As rotas de submissão e de consulta do resultado são o coração da API do trabalho.

- **TAREFA 1** — `POST /predict` que enfileira a tarefa e devolve um identificador.
- **TAREFA 2** — `GET /resultado/{id}` para buscar o resultado quando pronto.
- **TAREFA 6** — registrar log de cada requisição.

**Repositório do kit:** `sd-2026-2-kit-c1a2`

### Em resumo

- REST usa o HTTP como ele já é: recursos em URLs e verbos para operar neles.
- A URL diz O QUE; o verbo diz A AÇÃO; o código de status diz O RESULTADO.
- Com FastAPI, o contrato da API nasce do código — e fica sempre atualizado.

### Foco ENADE

Web services aparecem com frequência: diferença entre SOAP e REST, os verbos HTTP e seus códigos de status, o conceito de idempotência e a documentação por OpenAPI. Saiba relacionar a Arquitetura Orientada a Serviços (SOA) com REST e com a interoperabilidade entre sistemas.

**Costuma cair:**
- Web services: SOAP e REST, diferenças e aplicabilidade.
- Verbos HTTP, códigos de status e idempotência.
- Arquitetura orientada a serviços (SOA) e interoperabilidade.
- Contratos de API e documentação (WSDL, OpenAPI).

**Termos-chave:** REST · SOAP · Recurso · Verbo HTTP · Código de status · OpenAPI · Idempotência

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Em uma API REST, para criar um novo recurso e sinalizar sucesso, o verbo e o código de status esperados são, respectivamente:

- (A) GET e 200 (OK).
- (B) POST e 201 (Created).
- (C) PUT e 204 (No Content).
- (D) POST e 404 (Not Found).
- (E) DELETE e 200 (OK).

**Resolução.** POST cria o recurso e 201 (Created) indica criação bem-sucedida. O 404 sinaliza recurso inexistente e não faz sentido como resposta de criação.

**Resposta:** Alternativa B.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| REST | Estilo de arquitetura que usa recursos em URLs e verbos HTTP. |
| SOAP | Protocolo de web service baseado em XML, com contrato em WSDL. |
| Recurso | Entidade exposta pela API e identificada por uma URL. |
| Código de status | Número devolvido pelo HTTP que informa o resultado da operação. |
| Idempotência | Propriedade de uma operação que, repetida, não altera o resultado final. |
| OpenAPI | Padrão de descrição de APIs REST, gerado automaticamente pelo FastAPI. |

---

## Aula 6 — IA como serviço distribuído (marco do curso)

- **Bloco:** C1
- **Data:** Estudo Dirigido (EAD)

### Objetivos (neste capítulo você vai aprender a)

- Dominar o vocabulário mínimo de IA necessário para operar um modelo.
- Servir um modelo de IA atrás de uma API REST.
- Reconhecer os problemas distribuídos que a IA cria: latência e cold start.

### O vocabulário mínimo de IA

Para servir um modelo você não precisa de matemática, mas precisa de cinco palavras. Um **modelo** é um arquivo já treinado que transforma uma entrada em uma saída. A **inferência** é o ato de usar esse modelo para obter uma resposta — na prática, é chamar uma função. Um **embedding** é a representação de um texto como uma lista de números que captura o seu significado, o que permite comparar textos por semelhança medindo a distância entre seus vetores. Um **token** é um pedaço de texto que o modelo processa por vez (uma palavra ou parte dela). E um **LLM** (Large Language Model, ou modelo de linguagem grande) é um modelo treinado em enormes volumes de texto, que consumiremos por API. Com esse vocabulário você opera qualquer serviço de IA sem abrir a 'caixa-preta'.

### Servir um modelo como serviço

A regra de ouro é carregar o modelo uma única vez, quando o serviço sobe, e mantê-lo em memória. Carregá-lo a cada requisição seria um erro grave de projeto, porque essa é uma operação cara — envolve ler um arquivo grande do disco e prepará-lo. Feito o carregamento na inicialização, a rota `/predict` apenas recebe a entrada e chama a inferência. Repare que a API é a mesma que você aprendeu na aula anterior: o que muda é a carga de trabalho que ela executa por baixo.

### Os problemas que a IA traz para o sistema

A inferência é lenta se comparada a uma consulta comum: pense em centenas de milissegundos ou segundos, não em microssegundos. Além disso, existe o **cold start** — a primeira chamada depois de o serviço subir é sempre a mais lenta, porque o ambiente ainda está sendo preparado (o modelo sendo carregado, a memória sendo alocada). Como a operação é lenta, deixar o cliente parado esperando pela resposta é um mau desenho; a solução, que veremos na próxima aula, é processar de forma assíncrona com uma fila. É justamente por ser uma carga pesada, lenta e realista que a IA é um caso de estudo tão bom para sistemas distribuídos — ela expõe, na prática, todos os problemas que a teoria descreve.

### No seu trabalho — C1.A2: Serviço de Inferência Distribuído

Aqui o C1.A2 ganha vida: o modelo (já pronto no kit) passa a ser servido de verdade, e as duas interfaces devem convergir para o mesmo resultado. É o marco de lançamento do trabalho.

- Carregar o modelo uma única vez, na subida do serviço.
- **TAREFA 7** — escrever o README explicando arquitetura e execução.
- Conferir que REST e gRPC devolvem o mesmo resultado para a mesma entrada.

**Repositório do kit:** `sd-2026-2-kit-c1a2`

### Em resumo

- Modelo é um arquivo; inferência é chamar uma função. Todo o resto é engenharia.
- Carregue o modelo na subida do serviço; a rota apenas chama a inferência.
- IA é uma carga lenta e pesada — e é exatamente por isso que ela é um ótimo caso de estudo.

### Foco ENADE

Aqui o ENADE cobra menos a IA em si e mais a arquitetura: separação de responsabilidades, desempenho e tempo de resposta de serviços, e o encaixe de 'tecnologias emergentes' (IA como serviço) no rol de aplicações de sistemas distribuídos. Domine os termos modelo, inferência, embedding, token, LLM e cold start no sentido operacional.

**Costuma cair:**
- Aplicações e casos de uso de sistemas distribuídos.
- Arquitetura de serviços e separação de responsabilidades.
- Desempenho, latência e tempo de resposta em serviços.
- Tecnologias emergentes: inteligência artificial como serviço.

**Termos-chave:** Inferência · Modelo · Embedding · Token · LLM · Cold start

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Um serviço de inferência está lento; verifica-se que o modelo é carregado do disco a cada requisição. A correção mais adequada é:

- (A) Substituir REST por SOAP na interface.
- (B) Carregar o modelo uma única vez, na inicialização, mantendo-o em memória.
- (C) Reduzir o número de rotas expostas.
- (D) Trocar o protocolo de transporte de TCP para UDP.
- (E) Remover a validação dos dados de entrada.

**Resolução.** Carregar o modelo é uma operação cara e deve ocorrer uma única vez, no startup. As demais alternativas não atacam a causa do problema.

**Resposta:** Alternativa B.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Modelo | Arquivo já treinado que transforma uma entrada em uma saída. |
| Inferência | Ato de usar o modelo para obter uma resposta. |
| Embedding | Representação de um texto como lista de números que captura significado. |
| Token | Pedaço de texto processado pelo modelo. |
| LLM | Modelo de linguagem grande, normalmente consumido por API. |
| Cold start | Lentidão da primeira execução, antes de o serviço estar aquecido. |

---

## Aula 7 — Revisão e Avaliação C1.A1 + entrega do C1.A2

- **Bloco:** C1
- **Data:** 17/09/2026
- **Avaliações:** C1.A1 (prova escrita, 5,0 pontos) e entrega do C1.A2 (trabalho prático, 5,0 pontos)

### Objetivos (neste capítulo você vai aprender a)

- Revisar de forma consolidada todos os conceitos da Verificação C1.
- Realizar a avaliação escrita C1.A1, no estilo ENADE (5,0 pontos).
- Entregar o trabalho prático C1.A2 (5,0 pontos).

### O caminho percorrido no bloco de comunicação

Este capítulo fecha a primeira verificação, dedicada à pergunta: como dois programas conversam de forma confiável através da rede? Percorremos do byte cru no socket até um serviço de IA publicado. Vimos os modelos cliente-servidor e P2P; a diferença entre TCP e UDP; a concorrência com threads e o risco de condição de corrida; a evolução do RPC até o gRPC, com seu contrato em Protocol Buffers; o estilo REST, com seus verbos e códigos de status; e, por fim, a IA servida por trás de uma API. Antes da avaliação, releia os quadros EM RESUMO de cada capítulo e confira se você sabe responder, com segurança:

1. por que TCP difere de UDP;
2. o que é falha parcial;
3. o que uma thread resolve e qual problema cria;
4. para que serve o arquivo .proto;
5. o que determina o verbo e o código de status de uma rota REST;
6. por que a inferência de IA muda o desenho do serviço.

### No seu trabalho — C1.A2: Serviço de Inferência Distribuído

Dia de entrega do C1.A2. Antes de submeter, rode o projeto do zero e confira contra a rubrica.

- Clonar do zero e seguir o próprio README — funciona?
- Conferir a rubrica: arquitetura, comunicação, resiliência e execução reproduzível.
- Entregar no repositório (sem apresentação oral).

**Repositório do kit:** `sd-2026-2-kit-c1a2`

### Questões comentadas (estilo ENADE)

*Questões novas, elaboradas para esta disciplina e inspiradas nos temas e formatos das provas reais do ENADE de Computação (edições 2021 e 2024).*

#### Questão comentada 1

**Enunciado.** Uma equipe desenvolve um serviço de transmissão de áudio ao vivo. Nos testes, a retransmissão de pacotes perdidos provocava travamentos e atraso acumulado, prejudicando mais a experiência do que a perda de trechos muito curtos. O protocolo de transporte mais adequado é:

- (A) TCP, por garantir entrega ordenada.
- (B) TCP, por realizar controle de fluxo.
- (C) UDP, por não retransmitir pacotes perdidos, evitando o atraso acumulado.
- (D) UDP, por confirmar cada pacote.
- (E) UDP, por estabelecer conexão prévia.

**Resolução.** Em tempo real, atraso é pior que perda; o UDP não retransmite e mantém o fluxo. D e E descrevem o UDP incorretamente.

**Resposta:** Alternativa C.

#### Questão comentada 2

**Enunciado.** Analise as afirmações sobre comunicação e concorrência:

- I. Um socket é identificado pela combinação de endereço IP e porta.
- II. Em um servidor sequencial, um cliente lento pode bloquear o atendimento dos demais.
- III. Uma condição de corrida só ocorre em sistemas com mais de uma máquina.
- IV. A exclusão mútua na seção crítica evita resultados imprevisíveis no acesso a dado compartilhado.

É correto o que se afirma em:

- (A) I e III.
- (B) II e III.
- (C) I, II e IV.
- (D) III e IV.
- (E) I, II, III e IV.

**Resolução.** I, II e IV são corretas. III é falsa: a condição de corrida ocorre entre threads na mesma máquina, não exige várias máquinas.

**Resposta:** Alternativa C.

#### Questão comentada 3

**Enunciado.** Avalie a asserção e a razão a seguir.

- **ASSERÇÃO:** É seguro reenviar automaticamente uma requisição idempotente que não obteve resposta.
- **PORQUE**
- **RAZÃO:** Uma operação idempotente, repetida, leva ao mesmo estado final.

A respeito dessas afirmações, assinale a opção correta:

- (A) A asserção e a razão são verdadeiras, e a razão justifica a asserção.
- (B) A asserção e a razão são verdadeiras, mas a razão não justifica a asserção.
- (C) A asserção é verdadeira e a razão é falsa.
- (D) A asserção é falsa e a razão é verdadeira.
- (E) A asserção e a razão são falsas.

**Resolução.** Ambas são verdadeiras e a razão explica a asserção: é justamente por levar ao mesmo estado final que a operação idempotente pode ser retentada com segurança.

**Resposta:** Alternativa A.

#### Questão comentada 4

**Enunciado.** Uma equipe precisa de comunicação interna de alto volume entre microsserviços, com contrato tipado e baixa sobrecarga de dados na rede. A tecnologia mais adequada é:

- (A) SOAP com XML.
- (B) gRPC com Protocol Buffers.
- (C) REST sobre JSON, exclusivamente.
- (D) Troca de arquivos por FTP.
- (E) Mensagens por e-mail.

**Resolução.** O gRPC oferece contrato tipado (.proto), serialização binária compacta e HTTP/2, ideal para comunicação interna de alto volume entre serviços.

**Resposta:** Alternativa B.

#### Questão comentada 5

**Enunciado.** Um servidor sequencial trava o atendimento quando um cliente demora a responder. A técnica que permite atender vários clientes simultaneamente, sem que um bloqueie os outros, é:

- (A) Reduzir o tamanho do buffer.
- (B) Usar uma thread por conexão aceita.
- (C) Trocar TCP por UDP.
- (D) Diminuir o número da porta.
- (E) Desativar o registro de log.

**Resolução.** Atribuir uma thread a cada conexão libera o laço principal para aceitar o próximo cliente; um cliente lento afeta apenas a sua própria thread.

**Resposta:** Alternativa B.

### Em resumo

- Do byte no socket até um serviço de IA publicado: esta foi a Verificação C1.
- Se você responde estas 6 com segurança, está pronto para a C1.A1.

### Foco ENADE

A prova C1.A1 integra todo o bloco. No ENADE, os temas de comunicação (socket, TCP/UDP, RPC/RMI, REST) e de concorrência (thread) aparecem quase sempre combinados em estudos de caso — treine a leitura do cenário antes de escolher a alternativa.

**Costuma cair:**
- Todo o conteúdo da Verificação C1 é cobrado de forma integrada.
- Comunicação entre processos: sockets, TCP/UDP, RPC/RMI e REST.
- Concorrência, threads e exclusão mútua.
- Arquiteturas cliente-servidor e orientada a serviços.

**Termos-chave:** Socket · TCP/UDP · Thread · RPC/gRPC · REST · Inferência

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| C1.A1 | Avaliação escrita individual, estilo ENADE, valendo 5,0 pontos. |
| C1.A2 | Trabalho prático entregue no repositório, valendo 5,0 pontos. |
| Rubrica | Tabela que define como os pontos do trabalho são distribuídos. |

---

# PARTE C2 — Coordenação e consistência

**Aulas 8 a 12**

Como coordenar máquinas que falham e que não compartilham um relógio. Mensageria, relógios lógicos, teorema CAP, consenso com Raft e padrões de resiliência.

---

## Aula 8 — Mensageria, eventos e API Gateway

- **Bloco:** C2
- **Data:** 24/09/2026

### Objetivos (neste capítulo você vai aprender a)

- Diferenciar comunicação síncrona de assíncrona e saber quando usar cada uma.
- Processar inferências de IA de forma assíncrona com fila e worker.
- Explicar o papel de um API Gateway numa arquitetura de microsserviços.

### Síncrono contra assíncrono

Na comunicação síncrona, o cliente faz a chamada e fica esperando a resposta; é simples, mas ele trava enquanto espera. Na assíncrona, o cliente entrega a tarefa, recebe imediatamente um comprovante (um identificador) e vai buscar o resultado depois. Para uma inferência de IA que leva segundos, segurar o cliente é um desperdício e um convite a problemas — se muitos clientes esperam ao mesmo tempo, o serviço satura. A comunicação assíncrona resolve isso ao quebrar o vínculo temporal entre o pedido e o processamento.

### A fila como amortecedor e o desacoplamento

O mecanismo por trás do assíncrono é a **fila** de mensagens. Um **produtor** coloca a tarefa na fila; um **worker** (o consumidor) a retira e processa. A palavra-chave aqui é desacoplamento: quem produz não precisa saber quem consome, nem quando, nem quantos consumidores existem. Esse desacoplamento traz dois benefícios enormes. O primeiro é a absorção de picos: se chegam mais pedidos do que a capacidade de processamento, eles se acumulam na fila em vez de derrubar o serviço. O segundo é a escalabilidade simples: para dar conta de mais carga, basta subir mais workers consumindo a mesma fila, sem mudar quem produz.

Mas e quando o processamento falha? Uma tarefa pode dar erro — uma entrada inválida, uma dependência fora do ar. A boa prática é reprocessar algumas vezes e, persistindo a falha, encaminhar a mensagem para uma fila de descarte, a **dead-letter**. Em vez de tentar para sempre (travando o worker) ou simplesmente perder a mensagem, a dead-letter a isola para análise posterior, mantendo o fluxo principal saudável.

Uma variação importante é o modelo publicar/assinar, ou **pub/sub**: enquanto na fila cada mensagem é consumida por um único worker, no pub/sub a mesma mensagem é entregue a todos os interessados. É a base da arquitetura orientada a eventos, muito usada em nuvem — um pedido concluído pode, ao mesmo tempo, atualizar o estoque, notificar o cliente e alimentar um relatório.

### API Gateway: a porta única

Quando o sistema passa a ter vários serviços, o cliente não deve conhecer o endereço de cada um. O **API Gateway** resolve isso sendo a porta de entrada única: ele recebe todas as requisições e as encaminha ao serviço certo, além de centralizar o que é comum a todos — autenticação, limite de requisições e registro de log. É também no gateway que aplicaremos a segurança, mais adiante. Um cuidado relacionado é o **versionamento**: acrescentar um campo novo a uma resposta é seguro, mas remover ou renomear um campo quebra os clientes existentes e exige publicar uma nova versão da API (por exemplo, `/v2`), mantendo a antiga no ar durante a transição.

### No seu trabalho — C2.A2: RAG Distribuído em Microsserviços

Começa o C2.A2 — RAG Distribuído em Microsserviços. A mensageria desta aula é a espinha do trabalho: ao menos uma etapa do fluxo deve passar por fila.

- Clonar o repositório sd-2026-2-kit-c2a2.
- **TAREFA 4** — mensageria: novo worker + `docker-compose.yml`.
- Iniciar o serviço de ingestão/embeddings.

**Repositório do kit:** `sd-2026-2-kit-c2a2`

### Em resumo

- Síncrono: espero a resposta. Assíncrono: recebo um protocolo e busco o resultado depois.
- A fila absorve picos de carga e desacopla quem pede de quem processa.
- Fila: um consumidor por mensagem. Pub/sub: vários interessados na mesma mensagem.
- O gateway é a porta única: o cliente fala com ele, e ele fala com os serviços.

### Foco ENADE

Cobrança típica: comunicação síncrona versus assíncrona, o papel do middleware orientado a mensagens (MOM), a diferença entre fila e pub/sub, os papéis de produtor e worker, o desacoplamento e o uso de dead-letter para falhas. Microsserviços, API Gateway e versionamento de contratos também são recorrentes.

**Costuma cair:**
- Comunicação síncrona e assíncrona entre processos.
- Middleware orientado a mensagens (MOM), filas e pub/sub.
- Arquitetura orientada a eventos e desacoplamento.
- Microsserviços, API Gateway e versionamento de contratos.

**Termos-chave:** Fila · Produtor · Worker · Pub/sub · Dead-letter · API Gateway · Versionamento

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Sobre a diferença entre uma fila de trabalho e o modelo publicar/assinar (pub/sub), assinale a alternativa correta.

- (A) Na fila as mensagens são descartadas; em pub/sub, persistidas.
- (B) Na fila, cada mensagem é consumida por um único consumidor; em pub/sub, a mesma mensagem é entregue a todos os assinantes interessados.
- (C) A fila exige consistência forte e o pub/sub, consistência eventual.
- (D) A fila só funciona com UDP e o pub/sub, apenas com TCP.
- (E) Não há diferença prática entre os dois modelos.

**Resolução.** A fila distribui trabalho (um consumidor por mensagem); o pub/sub distribui informação (vários assinantes recebem a mesma mensagem).

**Resposta:** Alternativa B.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Fila | Estrutura que guarda tarefas até que um consumidor as processe. |
| Worker | Processo que retira mensagens da fila e as executa. |
| Pub/sub | Modelo em que uma mensagem publicada chega a vários assinantes. |
| Dead-letter | Fila de descarte para mensagens que falharam repetidamente. |
| API Gateway | Serviço que recebe todas as requisições e as encaminha aos serviços internos. |

---

## Aula 9 — Tempo e ordenação: relógios lógicos

- **Bloco:** C2
- **Data:** 01/10/2026

### Objetivos (neste capítulo você vai aprender a)

- Explicar por que não existe relógio global confiável em sistemas distribuídos.
- Aplicar relógios de Lamport para ordenar eventos.
- Usar relógios vetoriais para identificar eventos concorrentes.

### Por que não existe um 'agora' comum

Cada máquina tem seu próprio relógio, e dois relógios nunca marcam exatamente o mesmo instante — eles andam em ritmos ligeiramente diferentes, um fenômeno chamado **clock drift** (desvio de relógio). Sincronizá-los pela rede não resolve o problema de vez, porque a própria mensagem de sincronização leva um tempo variável para chegar. A consequência prática é séria: você não pode confiar em carimbo de hora para decidir a ordem em que eventos aconteceram em máquinas diferentes. Se dois pedidos chegam quase juntos a servidores distintos, comparar os relógios físicos pode inverter a ordem real dos fatos.

### Relógio de Lamport

A saída é abandonar a hora real e ordenar por **causalidade** — a relação em que um evento influenciou a ocorrência de outro. O **relógio lógico** de **Lamport** faz isso com um contador por processo:

1. A cada evento local, o contador aumenta em 1.
2. Ao enviar uma mensagem, o processo manda junto o valor atual do seu contador.
3. Ao receber, o destinatário adota o maior entre o próprio contador e o valor recebido, e soma 1.

Essa regra — **máximo mais um**, isto é, `relógio = max(relógio_local, carimbo_recebido) + 1` — garante uma propriedade essencial, chamada 'aconteceu antes': se um evento A causou um evento B, então o número de A é menor que o de B. Atenção, porém: a recíproca não vale — um número menor não prova, sozinho, que houve relação de causa.

### Relógio vetorial e eventos concorrentes

Para saber com certeza se dois eventos têm relação de causa ou se são **eventos concorrentes** (independentes, sem que um tenha influenciado o outro), usa-se o **relógio vetorial**: em vez de um único número, cada processo mantém um vetor com um contador para cada processo do sistema. Comparando dois vetores posição a posição, é possível determinar três situações:

- um evento causou o outro (um vetor é menor ou igual em todas as posições);
- o inverso;
- os eventos são concorrentes (cada vetor é maior em alguma posição, sem dominar o outro).

Essa capacidade de detectar concorrência é a base para identificar conflitos entre réplicas — assunto do próximo capítulo, quando duas cópias de um dado são escritas ao mesmo tempo.

### No seu trabalho — C2.A2: RAG Distribuído em Microsserviços

O serviço de recuperação compara a pergunta com os documentos por similaridade. A teoria de ordenação desta aula reforça um cuidado: a recuperação deve depender do conteúdo, não da hora de cada máquina.

- **TAREFA 2** — busca por similaridade no serviço de recuperação.

**Repositório do kit:** `sd-2026-2-kit-c2a2`

### Em resumo

- Não existe relógio global confiável: por isso ordenamos por causalidade, não por hora.
- Lamport garante que causa vem antes do efeito, mas não distingue eventos concorrentes.
- O relógio vetorial diz se um evento causou o outro ou se ambos são concorrentes.

### Foco ENADE

Tema clássico e frequentemente mal estudado. Saiba calcular o valor de um relógio lógico de Lamport após envio e recebimento (a regra do máximo mais um) e saiba interpretar um relógio vetorial para classificar dois eventos como causais ou concorrentes. Termos: clock drift, causalidade, relação 'aconteceu antes'.

**Costuma cair:**
- Sincronização de relógios físicos e desvio (clock drift).
- Relógios lógicos de Lamport e relação 'aconteceu antes'.
- Relógios vetoriais e detecção de concorrência.
- Ordenação de eventos e exclusão mútua distribuída.

**Termos-chave:** Relógio lógico · Lamport · Relógio vetorial · Causalidade · Eventos concorrentes · Clock drift

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** No processo P1, um evento leva seu relógio de Lamport a 3. P1 então envia uma mensagem a P2 com o carimbo 3. No recebimento, o relógio de P2 valia 7. Após o recebimento, o relógio de P2 passa a valer:

- (A) 3.
- (B) 7.
- (C) 8.
- (D) 10.
- (E) 4.

**Resolução.** A regra de Lamport no recebimento é máximo(relógio local, carimbo) + 1 = máximo(7, 3) + 1 = 8.

**Resposta:** Alternativa C.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Relógio lógico | Contador que ordena eventos sem depender da hora real. |
| Lamport | Algoritmo de relógio lógico baseado em um contador por processo. |
| Relógio vetorial | Vetor de contadores que permite detectar eventos concorrentes. |
| Causalidade | Relação em que um evento influenciou a ocorrência de outro. |
| Eventos concorrentes | Eventos sem relação de causa entre si. |

---

## Aula 10 — Replicação, consistência e o teorema CAP

- **Bloco:** C2
- **Data:** 08/10/2026

### Objetivos (neste capítulo você vai aprender a)

- Explicar por que replicamos dados e qual problema isso cria.
- Enunciar o teorema CAP e aplicá-lo a decisões de projeto.
- Diferenciar consistência forte de consistência eventual.

### Por que replicar e qual o preço

**Replicação** é manter cópias do mesmo dado em máquinas diferentes. Faz-se isso por dois motivos: disponibilidade, para que o sistema continue respondendo se uma cópia cair; e desempenho, para que leituras sejam mais rápidas e mais próximas do usuário. O preço é manter todas as cópias iguais, o que é difícil sobretudo quando há escritas simultâneas em réplicas diferentes — e é justamente aí que entra o problema da concorrência distribuída que os relógios vetoriais ajudam a detectar.

### O teorema CAP

O **teorema CAP** formaliza um limite fundamental. Das três propriedades desejáveis:

- **C — Consistência:** toda leitura enxerga a escrita mais recente;
- **A — Disponibilidade:** todo pedido recebe resposta;
- **P — Tolerância a Partição de rede:** o sistema continua mesmo se a rede se dividir em grupos que não se comunicam;

não é possível garantir as três ao mesmo tempo quando há partição. E como **partições de rede** acontecem de fato, na prática o P não é opcional. O teorema, portanto, não é uma escolha de dois entre três feita no papel: é uma decisão concreta, tomada durante a falha, entre responder de forma consistente (recusando pedidos que não pode garantir) ou responder sempre (arriscando devolver dado desatualizado).

### Consistência forte, eventual e convergência

Essa decisão se traduz em dois modelos. Na **consistência forte**, depois que você escreve, toda leitura vê o valor novo — o que exige coordenação entre as réplicas e custa tempo. Na **consistência eventual**, as cópias podem divergir por um instante e só depois se acertam; nesse intervalo, uma leitura pode devolver dado antigo. O processo pelo qual as réplicas divergentes voltam a coincidir, sem intervenção externa, chama-se **convergência**: passado o período de propagação (e resolvidos eventuais conflitos), todas as cópias chegam ao mesmo valor. A escolha do modelo é do projeto, não da tecnologia, e precisa ser justificada pelo caso de uso: um saldo bancário exige consistência forte, pois divergir significaria permitir dois saques do mesmo dinheiro; já um contador de curtidas ou de visualizações tolera perfeitamente a consistência eventual, porque um número momentaneamente desatualizado não causa prejuízo.

### No seu trabalho — C2.A2: RAG Distribuído em Microsserviços

O índice vetorial do seu RAG é um dado replicável: pensar em consistência ajuda a decidir o que acontece se ele for atualizado durante uma consulta.

- **TAREFA 1** — persistir o índice para não perdê-lo ao reiniciar.
- Definir a consistência aceitável para o índice.

**Repositório do kit:** `sd-2026-2-kit-c2a2`

### Em resumo

- Replicar dá disponibilidade e desempenho, mas cria o problema de manter as cópias iguais.
- Durante uma partição de rede, você escolhe: ou responde certo, ou responde sempre.
- Dado crítico pede consistência forte; o resto costuma aceitar consistência eventual.

### Foco ENADE

O teorema CAP é dos temas mais cobrados. Saiba enunciá-lo e, principalmente, aplicá-lo: dado um cenário com partição de rede, indicar se sacrificar consistência forte ou disponibilidade, e justificar. Os conceitos de replicação, consistência eventual e convergência, além de bancos distribuídos e particionamento (sharding), completam o tópico.

**Costuma cair:**
- Replicação de dados: objetivos e estratégias.
- Teorema CAP e suas implicações de projeto.
- Modelos de consistência: forte, eventual e causal.
- Bancos de dados distribuídos e particionamento (sharding).

**Termos-chave:** Replicação · Teorema CAP · Partição de rede · Consistência forte · Consistência eventual · Convergência

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** De acordo com o teorema CAP, diante de uma partição de rede, um sistema distribuído precisa escolher entre:

- (A) Consistência e tolerância a partição.
- (B) Consistência e disponibilidade.
- (C) Disponibilidade e tolerância a partição.
- (D) Latência e vazão.
- (E) Replicação e particionamento.

**Resolução.** Como a partição (P) é inevitável durante a falha, a escolha real, naquele momento, é entre responder de forma consistente (C) ou permanecer disponível (A).

**Resposta:** Alternativa B.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Replicação | Manter cópias do mesmo dado em máquinas diferentes. |
| Teorema CAP | Durante uma partição, é preciso escolher entre consistência e disponibilidade. |
| Partição de rede | Falha em que o sistema fica dividido em grupos que não se comunicam. |
| Consistência forte | Toda leitura enxerga a escrita mais recente. |
| Consistência eventual | As cópias convergem para o mesmo valor depois de algum tempo. |

---

## Aula 11 — Consenso (Raft) e resiliência

- **Bloco:** C2
- **Data:** 22/10/2026

### Objetivos (neste capítulo você vai aprender a)

- Explicar o problema do consenso e como o Raft o resolve.
- Aplicar tempo-limite, retentativa com espera progressiva e disjuntor.
- Explicar por que a idempotência é essencial quando há retentativa.

### O problema do consenso

**Consenso** é fazer várias máquinas concordarem sobre um mesmo valor, mesmo diante de falhas. Ele aparece sempre que o sistema precisa de uma decisão única e coerente: quem é o líder, qual a ordem das operações, o que foi de fato confirmado. É difícil porque mensagens atrasam, se perdem e máquinas caem sem avisar. Um resultado teórico famoso, o FLP, mostra que num sistema totalmente assíncrono não existe algoritmo que garanta consenso em todos os casos — por isso, na prática, os algoritmos usam tempo-limite para contornar o impasse e seguir em frente.

### Como o Raft funciona

O **Raft** é um algoritmo de consenso projetado para ser compreensível. Cada máquina é seguidor, candidato ou líder. Se um seguidor fica sem notícia do líder por um tempo, ele se torna candidato e pede votos; quem receber votos da maioria vira o novo líder. Essa maioria tem nome: **quórum** — o número mínimo de máquinas (mais da metade) necessário para tomar uma decisão. Exigir quórum é o que impede a existência de dois líderes ao mesmo tempo, pois duas maiorias não podem coexistir. A partir daí, toda operação passa pelo líder, que a registra no seu **log replicado** e a copia para os seguidores; quando a maioria confirma o registro, a operação é considerada efetivada. É esse mecanismo que sustenta sistemas como o etcd, por trás do Kubernetes.

Resumo do fluxo:

1. Papéis possíveis: seguidor, candidato, líder.
2. Seguidor sem notícia do líder → vira candidato e pede votos.
3. Candidato com votos da maioria (quórum) → vira líder.
4. Líder registra cada operação no log replicado e a copia para os seguidores.
5. Maioria confirma o registro → operação efetivada.

### Projetar contando com a falha

Do lado prático, resiliência é o conjunto de padrões que mantêm o sistema de pé quando uma dependência falha. Três são essenciais:

- **Tempo-limite:** toda chamada de rede precisa de um tempo-limite — sem ele, uma chamada travada segura o serviço para sempre.
- **Retentativa com espera progressiva (backoff):** a retentativa ajuda em falhas passageiras, mas deve usar espera progressiva, aumentando o intervalo a cada tentativa, para não piorar a sobrecarga do serviço que já está sofrendo.
- **Circuit breaker (disjuntor):** abre após várias falhas seguidas, passando a recusar chamadas na hora; depois de um tempo, deixa passar uma chamada de teste para ver se o serviço voltou.

Isso evita a **falha em cascata** — o efeito dominó em que um serviço quebrado, por acúmulo de chamadas travadas, derruba todos os que dependem dele.

Um detalhe amarra resiliência e REST: só é seguro retentar operações idempotentes. A **idempotência**, que vimos no estilo REST, é o que garante que repetir uma chamada não produza efeito duplicado. Se você retenta algo que não é idempotente, corre o risco de executá-lo duas vezes — uma cobrança dobrada, por exemplo. A solução prática é o cliente enviar um identificador único que o servidor usa para reconhecer e ignorar repetições.

### No seu trabalho — C2.A2: RAG Distribuído em Microsserviços

A chamada ao LLM é a dependência externa lenta e instável do RAG — exatamente o caso do circuit breaker desta aula.

- **TAREFA 3** — circuit breaker na chamada ao LLM, com tempo-limite e retentativa.

**Repositório do kit:** `sd-2026-2-kit-c2a2`

### Em resumo

- Consenso é fazer várias máquinas concordarem apesar de falhas e atrasos.
- O Raft elege um líder por maioria e só confirma o que a maioria registrou.
- Toda chamada tem tempo-limite; toda retentativa tem espera; o disjuntor corta o que já caiu.
- Só é seguro retentar aquilo que é idempotente.

### Foco ENADE

Dois eixos numa aula só. Do consenso: Raft, eleição de líder, quórum/maioria e log replicado. Da resiliência e dependabilidade: tipos de falha, tempo-limite, circuit breaker, falha em cascata e idempotência. Ambos são muito cobrados; a idempotência costuma aparecer ligada a retentativa.

**Costuma cair:**
- Problema do consenso, eleição de líder e quórum.
- Tolerância a falhas por replicação de máquina de estados.
- Tipos de falha, dependabilidade e mecanismos de recuperação.
- Padrões de resiliência e degradação controlada.

**Termos-chave:** Consenso · Raft · Quórum / maioria · Log replicado · Tempo-limite · Circuit breaker · Idempotência

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Em um cluster que utiliza o algoritmo Raft com 5 nós, o número mínimo de nós disponíveis e em acordo para eleger um líder e confirmar operações é:

- (A) 1.
- (B) 2.
- (C) 3.
- (D) 4.
- (E) 5.

**Resolução.** O Raft opera por quórum, que é a maioria. Em 5 nós, a maioria é 3 — o que impede que duas partes do cluster elejam líderes diferentes.

**Resposta:** Alternativa C.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Consenso | Fazer várias máquinas concordarem sobre um valor apesar de falhas. |
| Raft | Algoritmo de consenso baseado em eleição de líder e log replicado. |
| Quórum | Número mínimo de máquinas (maioria) necessário para decidir. |
| Circuit breaker | Padrão que interrompe chamadas a um serviço que está falhando. |
| Idempotência | Propriedade de operação que, repetida, mantém o mesmo resultado. |
| Falha em cascata | Falha que se propaga de um serviço para os demais. |

---

## Aula 12 — Revisão e Avaliação C2.A1 + entrega do C2.A2

- **Bloco:** C2
- **Data:** 29/10/2026
- **Avaliações:** C2.A1 (prova escrita, 5,0 pontos) e entrega do C2.A2 (trabalho prático, 5,0 pontos)

### Objetivos (neste capítulo você vai aprender a)

- Revisar de forma consolidada os conceitos da Verificação C2.
- Realizar a avaliação escrita C2.A1, no estilo ENADE (5,0 pontos).
- Entregar o trabalho prático C2.A2 (5,0 pontos).

### O que amarra o bloco de coordenação

A segunda verificação responde a uma pergunta mais profunda que a primeira: como coordenar máquinas que falham e que não compartilham um relógio? Vimos que a fila e a comunicação assíncrona desacoplam e absorvem carga; que os relógios de Lamport e vetoriais ordenam eventos sem depender da hora real; que o teorema CAP impõe uma escolha durante partições; que o Raft permite concordar por maioria; e que padrões como o circuit breaker e a idempotência mantêm o sistema de pé. Foi neste bloco que você construiu o **RAG** — a técnica de Retrieval-Augmented Generation, em que o sistema recupera trechos de documentos e os fornece a um LLM para gerar uma resposta fundamentada. São os conceitos mais abstratos do semestre e, não por acaso, os mais valorizados pelo ENADE.

### No seu trabalho — C2.A2: RAG Distribuído em Microsserviços

Dia de entrega do C2.A2. Feche o fluxo de ponta a ponta e documente a arquitetura dos três serviços.

- **TAREFA 5** — fluxo completo: pergunta entra, resposta fundamentada sai.
- **TAREFA 6** — README com diagrama dos três serviços.
- Conferir a rubrica e entregar.

**Repositório do kit:** `sd-2026-2-kit-c2a2`

### Questões comentadas (estilo ENADE)

*Questões novas, elaboradas para esta disciplina e inspiradas nos temas e formatos das provas reais do ENADE de Computação (edições 2021 e 2024).*

#### Questão comentada 1

**Enunciado.** No processo P1 um evento leva seu relógio de Lamport a 5. P1 envia uma mensagem a P2 com o carimbo 5; no recebimento, o relógio de P2 valia 2. Após o recebimento, o relógio de P2 é:

- (A) 2.
- (B) 5.
- (C) 6.
- (D) 7.
- (E) 3.

**Resolução.** máximo(2, 5) + 1 = 6. Aqui é o carimbo recebido (5) que 'puxa' o valor, por ser maior que o relógio local (2).

**Resposta:** Alternativa C.

#### Questão comentada 2

**Enunciado.** Um sistema de reserva de assentos de avião, replicado em dois data centers, sofre uma partição de rede entre eles. À luz do teorema CAP, a decisão mais adequada é:

- (A) Sacrificar a tolerância a partição.
- (B) Sacrificar a disponibilidade, mantendo a consistência, para não vender o mesmo assento duas vezes.
- (C) Sacrificar a consistência, permitindo vendas nos dois lados.
- (D) Sacrificar simultaneamente consistência e disponibilidade.
- (E) Não é possível decidir sem mais informações.

**Resolução.** Com a partição em curso, resta escolher entre C e A. Permitir vendas nos dois lados geraria overbooking; sacrifica-se a disponibilidade para preservar a consistência.

**Resposta:** Alternativa B.

#### Questão comentada 3

**Enunciado.** Um cluster usa o Raft com 5 nós. Qual o número mínimo de nós disponíveis e em acordo para eleger um líder e confirmar operações?

- (A) 1.
- (B) 2.
- (C) 3.
- (D) 4.
- (E) 5.

**Resolução.** O Raft opera por quórum (maioria). Em 5 nós, a maioria é 3, o que impede a existência de dois líderes simultâneos.

**Resposta:** Alternativa C.

#### Questão comentada 4

**Enunciado.** Analise as afirmações sobre replicação e consistência:

- I. Replicar dados pode aumentar a disponibilidade e reduzir a latência de leitura.
- II. Na consistência forte, uma leitura logo após a escrita sempre enxerga o valor novo.
- III. Na consistência eventual, as réplicas nunca chegam a convergir.
- IV. Manter réplicas idênticas é trivial quando há escritas concorrentes.

É correto o que se afirma em:

- (A) I e II.
- (B) I, II e IV.
- (C) II e III.
- (D) I e IV.
- (E) III e IV.

**Resolução.** I e II são corretas. III é falsa: na consistência eventual as réplicas convergem após um tempo. IV é falsa: manter réplicas iguais sob escrita concorrente é difícil.

**Resposta:** Alternativa A.

#### Questão comentada 5

**Enunciado.** Avalie a asserção e a razão a seguir.

- **ASSERÇÃO:** Processar inferências de IA de forma assíncrona, por fila, melhora a resiliência do serviço sob picos de carga.
- **PORQUE**
- **RAZÃO:** A fila desacopla o produtor do consumidor e absorve picos, acumulando tarefas em vez de derrubar o serviço.

A respeito dessas afirmações, assinale a opção correta:

- (A) A asserção e a razão são verdadeiras, e a razão justifica a asserção.
- (B) A asserção e a razão são verdadeiras, mas a razão não justifica a asserção.
- (C) A asserção é verdadeira e a razão é falsa.
- (D) A asserção é falsa e a razão é verdadeira.
- (E) A asserção e a razão são falsas.

**Resolução.** Ambas são verdadeiras e a razão explica a asserção: é o desacoplamento e a absorção de picos pela fila que tornam o serviço mais resiliente.

**Resposta:** Alternativa A.

### Em resumo

- A C2 responde a uma pergunta: como coordenar máquinas que falham e não compartilham relógio?
- Se você responde estas 6 com segurança, está pronto para a C2.A1.

### Foco ENADE

A prova C2.A1 cobra este bloco em nível operacional — o que acontece com o sistema — e não em demonstração formal. É exatamente o recorte que o ENADE costuma adotar: fila, Lamport, CAP, Raft, circuit breaker e idempotência aplicados a cenários.

**Costuma cair:**
- Todo o conteúdo da Verificação C2 é cobrado de forma integrada.
- Comunicação assíncrona, filas e arquitetura orientada a eventos.
- Relógios lógicos, replicação, consistência, CAP e consenso.
- Tolerância a falhas e padrões de resiliência.

**Termos-chave:** Fila · Lamport · CAP · Raft · Circuit breaker · Idempotência

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| C2.A1 | Avaliação escrita individual, estilo ENADE, valendo 5,0 pontos. |
| C2.A2 | Trabalho prático RAG distribuído, valendo 5,0 pontos. |
| RAG | Geração de resposta apoiada em documentos recuperados por busca vetorial. |

---

# PARTE C3 — Nuvem, implantação e segurança

**Aulas 13 a 17**

Como colocar e manter um sistema distribuído no ar. Containers, nuvem, serverless, observabilidade, segurança e LGPD.

---

## Aula 13 — Computação em nuvem, containers e o primeiro deploy

- **Bloco:** C3
- **Data:** 05/11/2026

### Objetivos (neste capítulo você vai aprender a)

- Diferenciar os modelos de serviço IaaS, PaaS, SaaS e FaaS.
- Explicar o que é um container e por que ele resolve o 'na minha máquina funciona'.
- Publicar o seu serviço de IA em nuvem, com URL pública.

### Os modelos de serviço em nuvem

A computação em nuvem se organiza em camadas de responsabilidade. No **IaaS** (Infraestrutura como Serviço) você aluga a máquina e cuida de todo o resto — sistema operacional, atualizações, aplicação. No **PaaS** (Plataforma como Serviço) você entrega apenas o código e a plataforma cuida de executá-lo; Render e Railway são exemplos. No **SaaS** (Software como Serviço) você apenas usa um software pronto, como o Gmail. E no **FaaS** (Função como Serviço) você entrega uma função que roda somente quando é chamada. Quanto mais adiante nessa lista, menos infraestrutura você gerencia — e menos controle detém. A escolha certa depende de quanto controle o seu caso exige e de quanta operação você quer evitar.

| Modelo | Você entrega / gerencia | Exemplo citado |
|--------|-------------------------|----------------|
| IaaS | Aluga a máquina e cuida de SO, atualizações e aplicação | — |
| PaaS | Entrega apenas o código; a plataforma executa | Render, Railway |
| SaaS | Apenas usa um software pronto | Gmail |
| FaaS | Entrega uma função que roda só quando chamada | — |

### Elasticidade e custo

A característica que define a nuvem é a **elasticidade**: a capacidade de crescer e encolher a quantidade de recursos conforme a demanda, automaticamente. É isso que a distingue de um servidor alugado de tamanho fixo, que fica ocioso na baixa e insuficiente no pico. Como a cobrança na nuvem é pelo uso, uma decisão de arquitetura vira diretamente uma decisão de custo — um serviço que não libera recursos ociosos, ou que faz trabalho desnecessário, aparece na fatura. Pensar em custo passou a fazer parte da engenharia, prática hoje chamada de FinOps.

### Containers: o fim do 'na minha máquina funciona'

O **container** empacota o código junto com suas dependências e configuração, de modo que o serviço roda igual na sua máquina, na do colega e na nuvem. Vale distinguir dois termos que costumam se confundir: a **imagem** é o molde imutável que você constrói, e o container é a execução daquela imagem — uma imagem pode gerar muitos containers idênticos. A receita que descreve como construir a imagem é o **Dockerfile**, um arquivo de texto com os passos (a partir de qual base, quais dependências instalar, qual comando executar). Diferente de uma máquina virtual, que carrega um sistema operacional completo, o container compartilha o núcleo do sistema hospedeiro — por isso é muito mais leve e sobe em segundos, e não em minutos.

### No seu trabalho — C3.A2: Plataforma de IA como Serviço

Começa o C3.A2 — Plataforma de IA como Serviço, o projeto integrador. Hoje você conteineriza os serviços e faz o primeiro deploy.

- Clonar o repositório sd-2026-2-kit-c3a2.
- **TAREFA 3** — um Dockerfile por serviço.
- **TAREFA 5** — primeiro deploy em nuvem free tier.

**Repositório do kit:** `sd-2026-2-kit-c3a2`

### Em resumo

- IaaS entrega máquina; PaaS entrega plataforma; SaaS entrega software; FaaS entrega execução.
- Nuvem é elástica e cobra pelo uso: decisão de arquitetura vira decisão de custo.
- A imagem empacota o ambiente inteiro: acaba o 'na minha máquina funciona'.

### Foco ENADE

Nuvem é um eixo garantido. Domine os modelos de serviço (IaaS, PaaS, SaaS, FaaS) e de implantação (pública, privada, híbrida), o conceito de elasticidade e a diferença entre virtualização por máquina virtual e por container — com os termos imagem e Dockerfile.

**Costuma cair:**
- Modelos de serviço em nuvem: IaaS, PaaS, SaaS e FaaS.
- Modelos de implantação: nuvem pública, privada e híbrida.
- Elasticidade, escalabilidade e economia de escala.
- Virtualização e containers: diferenças e vantagens.

**Termos-chave:** IaaS · PaaS · SaaS · FaaS · Elasticidade · Container · Imagem · Dockerfile

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Uma empresa quer publicar sua aplicação entregando apenas o código-fonte, sem gerenciar sistema operacional nem provisionar servidores. O modelo de serviço em nuvem adequado é:

- (A) IaaS.
- (B) PaaS.
- (C) SaaS.
- (D) Instalação local (on-premise).
- (E) Colocation.

**Resolução.** Em PaaS o cliente entrega o código e a plataforma cuida de executá-lo, incluindo o sistema operacional. O IaaS ainda exigiria gerenciar o SO; o SaaS é software pronto.

**Resposta:** Alternativa B.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| IaaS | Modelo em que se contrata infraestrutura (máquinas, rede, disco). |
| PaaS | Modelo em que se entrega o código e a plataforma cuida da execução. |
| FaaS | Modelo em que se entrega uma função executada sob demanda. |
| Elasticidade | Capacidade de crescer e encolher conforme a demanda. |
| Imagem | Molde imutável com aplicação, dependências e configuração. |
| Container | Instância em execução de uma imagem. |

---

## Aula 14 — Orquestração, serverless e computação na borda

- **Bloco:** C3
- **Data:** 12/11/2026

### Objetivos (neste capítulo você vai aprender a)

- Subir um sistema de vários containers com um único comando.
- Explicar descoberta de serviços e o papel de um orquestrador como o Kubernetes.
- Explicar o modelo serverless, o cold start e a computação na borda.

### Orquestração: de containers a sistema

Ter os containers prontos não basta: é preciso subi-los, conectá-los e ordená-los — isso é **orquestração**. Subir cada um à mão é lento e propenso a erro, e os serviços precisam se encontrar apesar de o IP mudar a cada execução. O **Docker Compose** descreve todo o sistema num único arquivo e o sobe com um comando; os containers ficam numa rede interna e se localizam pelo nome do serviço — a forma mais simples de **descoberta de serviços**, o mecanismo pelo qual um serviço encontra o endereço de outro sem precisar de IPs fixos. Quando uma máquina só não basta, entra o **Kubernetes**, que distribui containers por um conjunto de máquinas, reinicia o que cai, cria réplicas e faz balanceamento de carga automaticamente. Nesta disciplina você usa Compose e entende o conceito de Kubernetes, sem precisar operá-lo.

### Serverless e seus limites

No modelo **serverless** você publica uma função e ela executa quando um evento a dispara; se não há chamadas, nada roda e nada é cobrado, e a escala é automática. Existe servidor, sim — a diferença é que você não o gerencia. O preço é o **cold start** — a primeira chamada após um período parado é mais lenta, porque a plataforma precisa provisionar o ambiente — e os limites de tempo e memória por execução. Por isso o serverless brilha em cargas intermitentes e é inadequado para processos longos e contínuos, que pedem um container sempre de pé.

### Computação na borda

A computação na borda — **edge computing** — executa o código perto do usuário, e não num data center distante, com o objetivo direto de reduzir a latência, já que a distância física custa tempo. Essa ideia se apoia na **CDN** (Content Delivery Network), uma rede de servidores espalhados geograficamente que guardam cópias de conteúdo próximas de quem acessa. Um padrão comum é ler na borda e escrever na origem: aproveita-se a proximidade para validação, cache e filtragem, deixando para o centro apenas o que realmente precisa ser centralizado.

### No seu trabalho — C3.A2: Plataforma de IA como Serviço

A orquestração desta aula é o que faz o sistema inteiro subir com um único comando.

- **TAREFA 4** — docker-compose completo, subindo todos os serviços juntos.
- Opcional: um componente serverless ou na borda.

**Repositório do kit:** `sd-2026-2-kit-c3a2`

### Em resumo

- Compose orquestra em uma máquina; Kubernetes orquestra em um conjunto delas.
- Serverless: você publica a função; a nuvem cuida de executar e escalar.
- Serverless é ótimo para carga intermitente; ruim para processo longo e contínuo.
- Na borda o código roda perto do usuário, cortando latência.

### Foco ENADE

Cobrança frequente: orquestração de containers, escalabilidade horizontal, descoberta de serviços e balanceamento de carga (com Docker Compose e Kubernetes). O modelo serverless, o cold start, a arquitetura orientada a eventos e a computação na borda (edge computing, CDN, IoT) aparecem como 'tecnologias emergentes'.

**Costuma cair:**
- Orquestração de containers e escalabilidade horizontal.
- Descoberta de serviços e balanceamento de carga.
- Modelo FaaS, computação sem servidor e arquitetura orientada a eventos.
- Computação na borda, CDN e Internet das Coisas.

**Termos-chave:** Orquestração · Docker Compose · Kubernetes · Descoberta de serviços · Serverless · Cold start · Edge computing · CDN

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Sobre o modelo serverless (FaaS), assinale a alternativa correta.

- (A) Não existe servidor algum envolvido na execução.
- (B) A função executa sob demanda e não é cobrada quando ociosa, ao custo de cold start.
- (C) É o modelo ideal para processos longos e contínuos.
- (D) Elimina a necessidade de qualquer conexão de rede.
- (E) Garante consistência forte entre réplicas.

**Resolução.** O serverless executa por evento, cobra pelo uso e sofre cold start; por isso é inadequado a processos longos e contínuos, que pedem um container sempre de pé.

**Resposta:** Alternativa B.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Orquestração | Coordenar a execução de vários containers como um sistema só. |
| Kubernetes | Orquestrador que distribui containers por um conjunto de máquinas. |
| Descoberta de serviços | Mecanismo pelo qual um serviço encontra o endereço de outro. |
| Serverless | Modelo em que se publicam funções sem gerenciar servidores. |
| Cold start | Atraso da primeira execução após um período de inatividade. |
| Edge computing | Execução de código próximo ao usuário para reduzir latência. |

---

## Aula 15 — Observabilidade: enxergar o que acontece no sistema

- **Bloco:** C3
- **Data:** 19/11/2026

### Objetivos (neste capítulo você vai aprender a)

- Diferenciar log, métrica e rastreamento (trace).
- Explicar por que rastreamento distribuído é indispensável em microsserviços.
- Instrumentar o seu sistema e seguir uma requisição de ponta a ponta.

### Os três pilares da observabilidade

Operar um sistema distribuído exige enxergar o que acontece dentro dele, e isso se apoia em três pilares. O **log** é o registro textual do que ocorreu em um ponto do código — útil para saber o que aconteceu, mas isolado. A **métrica** é um número agregado ao longo do tempo, como requisições por segundo ou latência média — útil para enxergar tendências e disparar alertas. E o **trace** (rastreamento) reconstrói o caminho completo de uma única requisição atravessando vários serviços. Sem os três, a depuração vira adivinhação: o log conta o que houve num ponto, a métrica mostra a tendência geral, mas só o trace liga os pontos.

| Pilar | O que é | Para que serve |
|-------|---------|----------------|
| Log | Registro textual do que ocorreu em um ponto do código | Saber o que aconteceu (isolado) |
| Métrica | Número agregado ao longo do tempo | Enxergar tendências e disparar alertas |
| Trace | Caminho completo de uma requisição entre serviços | Ligar os pontos e achar o gargalo |

### Por que o rastreamento distribuído é indispensável

Num sistema de um serviço só, o log basta para achar o problema. Mas quando uma requisição passa pelo gateway, entra numa fila, é processada por um worker e chama um LLM externo, ela percorre quatro lugares — e o log isolado de cada um não conta a história completa. O rastreamento distribuído amarra todas as etapas por meio de um identificador de **correlação**: um mesmo código único acompanha a requisição por todos os serviços, permitindo descobrir exatamente em qual trecho o tempo foi gasto e onde está o **gargalo** — o ponto mais lento, que limita o desempenho de todo o fluxo.

### OpenTelemetry como padrão

O **OpenTelemetry** se tornou o padrão aberto para instrumentar aplicações, independente de fornecedor: você instrumenta o código uma vez e envia os dados para a ferramenta de análise que preferir, sem ficar preso a um produto específico. A lição de projeto é que instrumentar faz parte do desenvolvimento, e não algo que se improvisa depois que o incidente já aconteceu — quem só pensa em observabilidade durante a crise descobre, tarde demais, que não tem os dados para entender o que houve.

### No seu trabalho — C3.A2: Plataforma de IA como Serviço

Observabilidade é requisito do trabalho: sem rastreamento, você não sabe onde o sistema é lento.

- **TAREFA 7** — rastreamento distribuído cobrindo gateway → fila → worker.

**Repositório do kit:** `sd-2026-2-kit-c3a2`

### Em resumo

- Log conta o que houve; métrica mostra a tendência; rastreamento mostra o caminho.
- O rastreamento amarra as etapas de uma requisição por um identificador comum.
- OpenTelemetry padroniza a instrumentação e evita amarrar você a um fornecedor.

### Foco ENADE

Observabilidade conecta-se a monitoramento, gerenciamento e desempenho de sistemas distribuídos, e às práticas de DevOps. Distinga os três pilares — log, métrica e trace — e domine a ideia de correlação de eventos, de identificação de gargalo e do padrão OpenTelemetry.

**Costuma cair:**
- Monitoramento, gerenciamento e desempenho de sistemas distribuídos.
- Rastreamento distribuído e correlação de eventos.
- Métricas de qualidade de serviço: latência, vazão e disponibilidade.
- Práticas de DevOps e operação de serviços.

**Termos-chave:** Log · Métrica · Trace / rastreamento · OpenTelemetry · Correlação · Gargalo

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Uma requisição atravessa quatro serviços e apresenta lentidão intermitente. Para descobrir em qual etapa o tempo é consumido, o recurso de observabilidade mais adequado é:

- (A) Ler o log isolado de cada serviço.
- (B) Acompanhar a métrica agregada de uso de CPU.
- (C) O rastreamento distribuído (trace), que correlaciona as etapas por um identificador comum.
- (D) Aumentar o detalhamento do log apenas no gateway.
- (E) Substituir os containers por máquinas virtuais.

**Resolução.** Apenas o rastreamento reconstrói o caminho de uma requisição entre serviços e revela em qual trecho está o gargalo.

**Resposta:** Alternativa C.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Log | Registro textual de um evento ocorrido no código. |
| Métrica | Valor numérico agregado e acompanhado ao longo do tempo. |
| Trace | Registro do caminho completo de uma requisição entre serviços. |
| OpenTelemetry | Padrão aberto de instrumentação de aplicações. |
| Correlação | Identificador comum que liga as etapas de uma mesma requisição. |

---

## Aula 16 — Segurança, LGPD e revisão geral para o ENADE

- **Bloco:** C3
- **Data:** Estudo Dirigido (EAD)

### Objetivos (neste capítulo você vai aprender a)

- Aplicar criptografia, TLS e autenticação com JWT.
- Reconhecer as obrigações da LGPD num pipeline que processa dados pessoais.
- Revisar de forma integrada os temas de sistemas distribuídos cobrados no ENADE.

### Criptografia: o essencial para usar bem

Você não precisa implementar algoritmos, mas precisa saber escolher. A **criptografia simétrica** usa a mesma chave para cifrar e decifrar: é rápida, ideal para grandes volumes, mas exige que as duas partes combinem a chave com antecedência e em segredo. A **criptografia assimétrica** usa um par de chaves, uma pública e uma privada: o que uma cifra, só a outra decifra — o que resolve o problema da troca inicial da chave, porém é mais lenta. E o **hash** é um resumo de tamanho fixo e de mão única: serve para verificar integridade (se o dado mudou, o resumo muda) e para guardar senhas, mas não para cifrar, pois não há como reverter. Na prática, os sistemas combinam as três: assimétrica para acertar com segurança uma chave de sessão, simétrica para cifrar o tráfego, hash para garantir integridade — é exatamente assim que o TLS opera.

| Mecanismo | Chaves | Vantagem | Limitação / uso |
|-----------|--------|----------|-----------------|
| Simétrica | Mesma chave para cifrar e decifrar | Rápida, ideal para grandes volumes | Exige combinar a chave antes e em segredo |
| Assimétrica | Par pública/privada | Resolve a troca inicial da chave | Mais lenta |
| Hash | Nenhuma (mão única) | Verifica integridade; guarda senhas | Não cifra (não é reversível) |

### TLS, autenticação e autorização

O **TLS/HTTPS** — o 'S' do HTTPS — cifra o tráfego e comprova a identidade do servidor por meio de um certificado digital. Sobre ele, dois conceitos que costumam ser confundidos: a autenticação responde 'quem é você', enquanto a autorização responde 'o que você pode fazer'. O **JWT** (JSON Web Token) é um token assinado que carrega a identidade do usuário e pode ser verificado pela própria assinatura, sem consultar o banco a cada requisição. E o princípio de **Zero Trust** estabelece que nada é confiável só por estar na rede interna: todo pedido é autenticado e autorizado, como se viesse de fora.

### LGPD e anonimização no pipeline de IA

Dado pessoal é qualquer informação que identifique alguém, direta ou indiretamente, e a **LGPD** (Lei Geral de Proteção de Dados) impõe princípios claros: finalidade declarada e coleta do mínimo necessário. Num pipeline de IA há um cuidado específico: o texto enviado a uma API de LLM sai da sua infraestrutura e vai para um terceiro. Daí a importância da **anonimização** — remover ou mascarar, antes do envio, os elementos que identificam a pessoa (nome, CPF, e-mail), de modo que o dado deixe de ser pessoal. Some a isso jamais registrar dado pessoal em log e definir um prazo de retenção. Ignorar essas medidas não é apenas má engenharia — é descumprimento legal, com sanções previstas em lei.

### Preparação final para o ENADE

Esta aula acontece na véspera do ENADE. Vale um sobrevoo por todo o semestre:

- **Comunicação:** sockets, TCP/UDP, RPC/RMI, REST, SOAP;
- **Concorrência;**
- **Coordenação:** relógios, consenso, quórum;
- **Dados:** replicação, CAP, consistência;
- **Nuvem:** modelos de serviço, containers, virtualização;
- **Segurança:** criptografia, TLS, autenticação, LGPD.

O melhor roteiro de revisão é reler todos os quadros EM RESUMO e todas as caixas FOCO ENADE deste livro, além das QUESTÕES COMENTADAS dos capítulos 7, 12 e 17.

### No seu trabalho — C3.A2: Plataforma de IA como Serviço

Segurança e LGPD fecham a parte técnica do projeto integrador.

- **TAREFA 1** — autenticação JWT no gateway.
- **TAREFA 2** — limite de requisições (rate limit).
- **TAREFA 8** — HTTPS no serviço publicado.
- **TAREFA 9** — seção de conformidade LGPD no README.

**Repositório do kit:** `sd-2026-2-kit-c3a2`

### Em resumo

- Assimétrica acerta a chave; simétrica transporta os dados; hash garante integridade.
- TLS protege o caminho; autenticação identifica; autorização define o permitido.
- Colete o mínimo, declare a finalidade e não vaze dado pessoal em log nem para o LLM.
- O ENADE cobra os fundamentos: leia os quadros 'EM RESUMO' de todas as 15 aulas anteriores.

### Foco ENADE

Segurança da informação é eixo próprio no exame: criptografia simétrica, assimétrica e hash; TLS/HTTPS e certificados; autenticação, autorização, JWT e Zero Trust; e LGPD, com seus princípios de finalidade e necessidade e o recurso da anonimização. Questões de ética e legislação são comuns.

**Costuma cair:**
- Criptografia simétrica, assimétrica e funções de hash.
- Protocolos seguros: TLS/HTTPS e certificados digitais.
- Autenticação, autorização e controle de acesso.
- LGPD, privacidade e proteção de dados pessoais.

**Termos-chave:** Criptografia simétrica · Criptografia assimétrica · Hash · TLS/HTTPS · JWT · Zero Trust · LGPD · Anonimização

### Questão de autoavaliação (estilo ENADE)

**Enunciado.** Um sistema de RAG envia trechos de documentos com dados pessoais a uma API pública de LLM. À luz da LGPD, a medida mais adequada é:

- (A) Ampliar o tempo-limite da requisição.
- (B) Anonimizar os dados pessoais antes do envio e restringir o tratamento à finalidade declarada.
- (C) Aumentar o número de réplicas do serviço.
- (D) Converter a comunicação de REST para gRPC.
- (E) Armazenar os dados pessoais também nos logs, para auditoria.

**Resolução.** Aplicam-se os princípios da finalidade e da necessidade (mínimo necessário); anonimiza-se antes do envio. Gravar dado pessoal em log agrava a exposição.

**Resposta:** Alternativa B.

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| Criptografia simétrica | Usa a mesma chave para cifrar e decifrar. |
| Criptografia assimétrica | Usa um par de chaves, pública e privada. |
| Hash | Resumo de mão única usado para verificar integridade. |
| TLS | Protocolo que cifra a comunicação e autentica o servidor. |
| JWT | Token assinado que carrega a identidade do usuário. |
| LGPD | Lei brasileira de proteção de dados pessoais. |

---

## Aula 17 — Avaliação C3.A1, entrega do C3.A2 e tendências

- **Bloco:** C3
- **Data:** 26/11/2026
- **Avaliações:** C3.A1 (prova escrita, 5,0 pontos) e entrega do C3.A2 (projeto integrador, 5,0 pontos)

### Objetivos (neste capítulo você vai aprender a)

- Revisar de forma consolidada os conceitos da Verificação C3.
- Realizar a avaliação escrita C3.A1, no estilo ENADE (5,0 pontos).
- Entregar o projeto integrador C3.A2 (5,0 pontos) e conhecer as tendências da área.

### O semestre inteiro em uma página

Vale olhar para trás e ver o caminho. O bloco C1 respondeu como dois programas conversam: sockets, gRPC, REST e a IA como serviço. O bloco C2 respondeu como coordenar máquinas que falham: filas, relógios lógicos, CAP, Raft e resiliência. O bloco C3 respondeu como colocar e manter tudo isso no ar: containers, nuvem, orquestração, observabilidade, TLS/JWT e LGPD. Do primeiro socket ao sistema publicado, você construiu, do zero, uma plataforma distribuída de IA — que vale mais em uma entrevista de emprego do que muitos certificados.

### Para onde a área está indo

Encerramos com as tendências que devem moldar os próximos anos:

- A arquitetura orientada a eventos consolida-se como padrão de integração em nuvem.
- Serverless e borda continuam crescendo, movidos pela lógica de processar perto do usuário e pagar só pelo uso.
- O **data mesh** propõe uma mudança de organização: em vez de um time central dono de todos os dados, cada domínio (vendas, estoque, pagamentos) trata os seus dados como um produto, com dono e contrato próprios.
- Os sistemas **AI-native** são aqueles concebidos com a inteligência artificial no centro da arquitetura, e não como um recurso acrescentado depois.
- Zero Trust e observabilidade, por fim, deixaram de ser diferenciais e passaram a requisitos padrão de qualquer sistema sério.

### No seu trabalho — C3.A2: Plataforma de IA como Serviço

Dia de entrega do projeto integrador C3.A2 — material de portfólio. Finalize a resiliência e o relatório de trade-offs.

- **TAREFA 6** — resiliência (tempo-limite, retentativa, circuit breaker).
- **TAREFA 10** — relatório de trade-offs (CAP, custo, latência).
- Conferir a URL pública no ar e entregar.

**Repositório do kit:** `sd-2026-2-kit-c3a2`

### Questões comentadas (estilo ENADE)

*Questões novas, elaboradas para esta disciplina e inspiradas nos temas e formatos das provas reais do ENADE de Computação (edições 2021 e 2024).*

#### Questão comentada 1

**Enunciado.** Analise as afirmações sobre modelos de computação em nuvem, segundo o NIST:

- I. No SaaS, o usuário utiliza aplicações executadas na infraestrutura do provedor, sem gerenciar a infraestrutura subjacente.
- II. No IaaS, o cliente provisiona processamento, armazenamento e rede, e gerencia o sistema operacional.
- III. No PaaS, o cliente é responsável por manter o hardware físico do data center.
- IV. A elasticidade permite ajustar os recursos conforme a demanda.

É correto o que se afirma em:

- (A) I e III.
- (B) I, II e IV.
- (C) II e III.
- (D) III e IV.
- (E) I, II, III e IV.

**Resolução.** I, II e IV são corretas. III é falsa: em qualquer modelo de nuvem, é o provedor — e não o cliente — que mantém o hardware físico.

**Resposta:** Alternativa B.

#### Questão comentada 2

**Enunciado.** Analise as afirmações sobre mecanismos criptográficos em uma comunicação segura:

- I. A criptografia assimétrica pode ser usada para estabelecer com segurança a chave simétrica da sessão.
- II. Uma função de hash como o SHA-256 permite verificar a integridade dos dados.
- III. A criptografia simétrica dispensa qualquer segredo compartilhado.
- IV. O TLS combina criptografia assimétrica e simétrica.

É correto o que se afirma em:

- (A) I e III.
- (B) II e III.
- (C) I, II e IV.
- (D) I e IV.
- (E) I, II, III e IV.

**Resolução.** I, II e IV são corretas. III é falsa: a criptografia simétrica depende de uma chave secreta compartilhada entre as partes.

**Resposta:** Alternativa C.

#### Questão comentada 3

**Enunciado.** Assinale a alternativa correta sobre a diferença entre containers e máquinas virtuais.

- (A) O container inclui um sistema operacional completo, o que o torna mais pesado que a VM.
- (B) O container compartilha o núcleo do sistema operacional hospedeiro, sendo mais leve e de inicialização mais rápida que a VM.
- (C) A máquina virtual dispensa hipervisor, ao contrário do container.
- (D) Container e máquina virtual são termos equivalentes.
- (E) O container não permite empacotar as dependências da aplicação.

**Resolução.** O container virtualiza no nível do sistema operacional e compartilha o kernel; a VM virtualiza o hardware e carrega um SO completo, sendo mais pesada.

**Resposta:** Alternativa B.

#### Questão comentada 4

**Enunciado.** Uma requisição atravessa gateway, fila, worker e uma API externa, com lentidão intermitente. Para localizar em qual etapa o tempo é gasto, o recurso mais adequado é:

- (A) O log isolado de cada serviço.
- (B) A métrica agregada de uso de CPU.
- (C) O rastreamento distribuído, correlacionando as etapas por um identificador comum.
- (D) Aumentar o número de réplicas.
- (E) Substituir os containers por máquinas virtuais.

**Resolução.** Somente o rastreamento distribuído reconstrói o percurso da requisição e aponta o gargalo; log e métrica, isolados, não fazem isso.

**Resposta:** Alternativa C.

#### Questão comentada 5

**Enunciado.** Avalie a asserção e a razão a seguir.

- **ASSERÇÃO:** Antes de enviar textos de clientes a uma API pública de LLM, deve-se anonimizar os dados pessoais.
- **PORQUE**
- **RAZÃO:** A LGPD estabelece os princípios da finalidade e da necessidade, limitando o tratamento ao mínimo necessário para a finalidade declarada.

A respeito dessas afirmações, assinale a opção correta:

- (A) A asserção e a razão são verdadeiras, e a razão justifica a asserção.
- (B) A asserção e a razão são verdadeiras, mas a razão não justifica a asserção.
- (C) A asserção é verdadeira e a razão é falsa.
- (D) A asserção é falsa e a razão é verdadeira.
- (E) A asserção e a razão são falsas.

**Resolução.** Ambas são verdadeiras e a razão justifica a asserção: é para atender aos princípios da finalidade e da necessidade que se anonimiza o dado antes de enviá-lo a terceiros.

**Resposta:** Alternativa A.

### Em resumo

- A C3 transformou o seu protótipo local em um sistema publicado, observável e seguro.
- De um socket na Aula 2 a uma plataforma de IA em nuvem na Aula 17.
- O futuro próximo combina eventos, borda, dados como produto e IA no centro da arquitetura.

### Foco ENADE

A prova C3.A1 integra nuvem, containers, orquestração, serverless, observabilidade e segurança (TLS/JWT, LGPD). Some a consciência das tendências (eventos, borda, data mesh, AI-native): questões de 'panorama' recompensam quem enxerga o quadro completo.

**Costuma cair:**
- Todo o conteúdo da Verificação C3 é cobrado de forma integrada.
- Computação em nuvem, containers e orquestração.
- Serverless, borda e arquitetura orientada a eventos.
- Segurança da informação, criptografia e LGPD.

**Termos-chave:** IaaS/PaaS/SaaS/FaaS · Container · Orquestração · Observabilidade · TLS/JWT · LGPD

### Glossário do capítulo

| Termo | Definição |
|-------|-----------|
| C3.A1 | Avaliação escrita individual, estilo ENADE, valendo 5,0 pontos. |
| C3.A2 | Projeto integrador entregue no repositório, valendo 5,0 pontos. |
| Data mesh | Abordagem em que cada domínio é dono de seus dados, tratados como produto. |
| AI-native | Sistema concebido com a IA como parte central da arquitetura. |

---

# Apêndice A — Mapa de revisão para o ENADE

O ENADE 2026 (29 de novembro) inclui os cursos de Análise e Desenvolvimento de Sistemas, Ciência da Computação e Sistemas de Informação. A tabela abaixo reúne, capítulo a capítulo, os temas com maior probabilidade de aparecer e os termos-chave correspondentes. Use-a como roteiro final de revisão.

| Aula | Temas cobrados no ENADE | Termos-chave |
|------|-------------------------|--------------|
| 1 | Conceito e caracterização de sistemas distribuídos; Vantagens e desafios: escalabilidade, disponibilidade e falha parcial; Diferença entre sistema centralizado e sistema distribuído; Tipos de transparência (acesso, localização, replicação) | Sistema distribuído · Falha parcial · Transparência · Escalabilidade · Latência |
| 2 | Modelo cliente-servidor comparado ao modelo P2P; Características de TCP e UDP e critério para escolher entre eles; Conceito de socket, porta e endereçamento; Camadas do modelo TCP/IP e encapsulamento | Cliente-servidor · P2P · Socket · Porta · TCP · UDP |
| 3 | Concorrência e paralelismo: diferença entre os dois; Condição de corrida, exclusão mútua e seção crítica; Threads e processos: quando usar cada um; Escalabilidade de servidores e gargalos | Thread · Condição de corrida · Exclusão mútua · Seção crítica · Lock · Bloqueante |
| 4 | Conceito de RPC e transparência de acesso; RMI e invocação de métodos remotos; Serialização e representação de dados na rede; Middleware de comunicação e stubs | RPC · RMI · gRPC · Protocol Buffers · Stub · Serialização · Middleware |
| 5 | Web services: SOAP e REST, diferenças e aplicabilidade; Verbos HTTP, códigos de status e idempotência; Arquitetura orientada a serviços (SOA) e interoperabilidade; Contratos de API e documentação (WSDL, OpenAPI) | REST · SOAP · Recurso · Verbo HTTP · Código de status · OpenAPI · Idempotência |
| 6 | Aplicações e casos de uso de sistemas distribuídos; Arquitetura de serviços e separação de responsabilidades; Desempenho, latência e tempo de resposta em serviços; Tecnologias emergentes: inteligência artificial como serviço | Inferência · Modelo · Embedding · Token · LLM · Cold start |
| 7 | Todo o conteúdo da Verificação C1 é cobrado de forma integrada; Comunicação entre processos: sockets, TCP/UDP, RPC/RMI e REST; Concorrência, threads e exclusão mútua; Arquiteturas cliente-servidor e orientada a serviços | Socket · TCP/UDP · Thread · RPC/gRPC · REST · Inferência |
| 8 | Comunicação síncrona e assíncrona entre processos; Middleware orientado a mensagens (MOM), filas e pub/sub; Arquitetura orientada a eventos e desacoplamento; Microsserviços, API Gateway e versionamento de contratos | Fila · Produtor · Worker · Pub/sub · Dead-letter · API Gateway · Versionamento |
| 9 | Sincronização de relógios físicos e desvio (clock drift); Relógios lógicos de Lamport e relação 'aconteceu antes'; Relógios vetoriais e detecção de concorrência; Ordenação de eventos e exclusão mútua distribuída | Relógio lógico · Lamport · Relógio vetorial · Causalidade · Eventos concorrentes · Clock drift |
| 10 | Replicação de dados: objetivos e estratégias; Teorema CAP e suas implicações de projeto; Modelos de consistência: forte, eventual e causal; Bancos de dados distribuídos e particionamento (sharding) | Replicação · Teorema CAP · Partição de rede · Consistência forte · Consistência eventual · Convergência |
| 11 | Problema do consenso, eleição de líder e quórum; Tolerância a falhas por replicação de máquina de estados; Tipos de falha, dependabilidade e mecanismos de recuperação; Padrões de resiliência e degradação controlada | Consenso · Raft · Quórum / maioria · Log replicado · Tempo-limite · Circuit breaker · Idempotência |
| 12 | Todo o conteúdo da Verificação C2 é cobrado de forma integrada; Comunicação assíncrona, filas e arquitetura orientada a eventos; Relógios lógicos, replicação, consistência, CAP e consenso; Tolerância a falhas e padrões de resiliência | Fila · Lamport · CAP · Raft · Circuit breaker · Idempotência |
| 13 | Modelos de serviço em nuvem: IaaS, PaaS, SaaS e FaaS; Modelos de implantação: nuvem pública, privada e híbrida; Elasticidade, escalabilidade e economia de escala; Virtualização e containers: diferenças e vantagens | IaaS · PaaS · SaaS · FaaS · Elasticidade · Container · Imagem · Dockerfile |
| 14 | Orquestração de containers e escalabilidade horizontal; Descoberta de serviços e balanceamento de carga; Modelo FaaS, computação sem servidor e arquitetura orientada a eventos; Computação na borda, CDN e Internet das Coisas | Orquestração · Docker Compose · Kubernetes · Descoberta de serviços · Serverless · Cold start · Edge computing · CDN |
| 15 | Monitoramento, gerenciamento e desempenho de sistemas distribuídos; Rastreamento distribuído e correlação de eventos; Métricas de qualidade de serviço: latência, vazão e disponibilidade; Práticas de DevOps e operação de serviços | Log · Métrica · Trace / rastreamento · OpenTelemetry · Correlação · Gargalo |
| 16 | Criptografia simétrica, assimétrica e funções de hash; Protocolos seguros: TLS/HTTPS e certificados digitais; Autenticação, autorização e controle de acesso; LGPD, privacidade e proteção de dados pessoais | Criptografia simétrica · Criptografia assimétrica · Hash · TLS/HTTPS · JWT · Zero Trust · LGPD · Anonimização |
| 17 | Todo o conteúdo da Verificação C3 é cobrado de forma integrada; Computação em nuvem, containers e orquestração; Serverless, borda e arquitetura orientada a eventos; Segurança da informação, criptografia e LGPD | IaaS/PaaS/SaaS/FaaS · Container · Orquestração · Observabilidade · TLS/JWT · LGPD |

> **Dica de prova:** Os temas de sistemas distribuídos quase nunca vêm isolados no ENADE: eles aparecem em estudos de caso que combinam comunicação, coordenação e nuvem. Treine primeiro a leitura do cenário e só então escolha a alternativa. As três provas A1 da disciplina seguem esse mesmo formato, justamente para prepará-lo.

---

# Apêndice B — Bibliografia e materiais de apoio

## Básica

- COULOURIS, G.; DOLLIMORE, J.; KINDBERG, T. *Sistemas Distribuídos: conceitos e projeto*. 5. ed. Porto Alegre: Bookman, 2012.
- KLEPPMANN, M. *Designing Data-Intensive Applications*. O'Reilly, 2017.
- TANENBAUM, A. S.; VAN STEEN, M. *Distributed Systems*. 4. ed., 2023 (PDF gratuito dos autores).

## Complementar

- NEWMAN, S. *Building Microservices*. 2. ed. O'Reilly, 2021.
- RICHARDSON, C. *Microservices Patterns*. Manning, 2018.
- BURNS, B. *Designing Distributed Systems*. O'Reilly, 2018.
- Documentação oficial: gRPC, FastAPI, Docker, OpenTelemetry e do provedor de nuvem adotado.

## Materiais abertos

- MIT 6.824 — Distributed Systems (aulas e laboratórios abertos).
- Concurrent and Distributed Systems — University of Cambridge, Martin Kleppmann (notas e vídeos).
- Provas e gabaritos do ENADE de Computação (INEP) — edições de 2021 e 2024.

---

# Anexo de conversão — Índice de tarefas dos trabalhos práticos por aula

*Seção adicionada na conversão (não consta no original): consolida as menções "NO SEU TRABALHO" espalhadas pelas aulas.*

## C1.A2 — Serviço de Inferência Distribuído (kit `sd-2026-2-kit-c1a2`)

| Tarefa | Descrição | Aula |
|--------|-----------|------|
| TAREFA 1 | `POST /predict` que enfileira a tarefa e devolve um identificador | 5 |
| TAREFA 2 | `GET /resultado/{id}` para buscar o resultado quando pronto | 5 |
| TAREFA 3 | Worker grava o resultado processado para consulta posterior | 3 |
| TAREFA 4 | Método gRPC `PreverLote` e regerar os stubs | 4 |
| TAREFA 5 | Tratamento de erro no worker (retentativa) | 3 |
| TAREFA 6 | Registrar log de cada requisição | 5 |
| TAREFA 7 | README explicando arquitetura e execução | 6 |

## C2.A2 — RAG Distribuído em Microsserviços (kit `sd-2026-2-kit-c2a2`)

| Tarefa | Descrição | Aula |
|--------|-----------|------|
| TAREFA 1 | Persistir o índice para não perdê-lo ao reiniciar | 10 |
| TAREFA 2 | Busca por similaridade no serviço de recuperação | 9 |
| TAREFA 3 | Circuit breaker na chamada ao LLM, com tempo-limite e retentativa | 11 |
| TAREFA 4 | Mensageria: novo worker + `docker-compose.yml` | 8 |
| TAREFA 5 | Fluxo completo: pergunta entra, resposta fundamentada sai | 12 |
| TAREFA 6 | README com diagrama dos três serviços | 12 |

## C3.A2 — Plataforma de IA como Serviço (kit `sd-2026-2-kit-c3a2`)

| Tarefa | Descrição | Aula |
|--------|-----------|------|
| TAREFA 1 | Autenticação JWT no gateway | 16 |
| TAREFA 2 | Limite de requisições (rate limit) | 16 |
| TAREFA 3 | Um Dockerfile por serviço | 13 |
| TAREFA 4 | docker-compose completo, subindo todos os serviços juntos | 14 |
| TAREFA 5 | Primeiro deploy em nuvem free tier | 13 |
| TAREFA 6 | Resiliência (tempo-limite, retentativa, circuit breaker) | 17 |
| TAREFA 7 | Rastreamento distribuído cobrindo gateway → fila → worker | 15 |
| TAREFA 8 | HTTPS no serviço publicado | 16 |
| TAREFA 9 | Seção de conformidade LGPD no README | 16 |
| TAREFA 10 | Relatório de trade-offs (CAP, custo, latência) | 17 |
