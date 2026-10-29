"""
Fila de ingestao no Redis - TAREFA 4 (Aula 8).

Produtor (rota POST /indexar) -> fila:ingestao -> consumidor (worker.py).

  fila:ingestao              tarefas aguardando processamento
  fila:ingestao:processando  tarefa que o worker pegou e ainda nao terminou
  fila:ingestao:dlq          dead-letter: tarefas que falharam MAX_TENTATIVAS vezes
  tarefa:{id}                hash com o estado da tarefa (pendente/concluida/falhou)
"""
import json
import os
import time
import uuid

import redis

FILA = "fila:ingestao"
PROCESSANDO = "fila:ingestao:processando"
DLQ = "fila:ingestao:dlq"
MAX_TENTATIVAS = int(os.getenv("INGESTAO_MAX_TENTATIVAS", "3"))
VALIDADE_TAREFA = 24 * 60 * 60  # segundos que o estado da tarefa fica consultavel


def conectar() -> redis.Redis:
    return redis.Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"),
                                decode_responses=True, socket_timeout=10,
                                socket_connect_timeout=5)


def chave_tarefa(tarefa_id: str) -> str:
    return f"tarefa:{tarefa_id}"


def atualizar_tarefa(r: redis.Redis, tarefa_id: str, **campos) -> None:
    r.hset(chave_tarefa(tarefa_id), mapping={k: str(v) for k, v in campos.items()})
    r.expire(chave_tarefa(tarefa_id), VALIDADE_TAREFA)


def enfileirar(r: redis.Redis, documentos: list[dict]) -> str:
    """Coloca os documentos na fila e devolve o identificador da tarefa."""
    tarefa_id = uuid.uuid4().hex
    atualizar_tarefa(r, tarefa_id, estado="pendente", documentos=len(documentos),
                     tentativas=0, criada_em=time.time())
    r.lpush(FILA, json.dumps({"id": tarefa_id, "documentos": documentos, "tentativas": 0}))
    return tarefa_id


def consultar_tarefa(r: redis.Redis, tarefa_id: str) -> dict | None:
    dados = r.hgetall(chave_tarefa(tarefa_id))
    return dados or None
