"""
Servico 1 - INGESTAO: recebe documentos, gera embeddings e armazena.

TAREFA 1: o indice e persistido em disco (ver indice.py) e sobrevive a reinicios.
TAREFA 4: POST /indexar nao indexa na hora - enfileira no Redis e devolve 202
com o id da tarefa. O worker (worker.py) consome a fila e grava o indice.

Rodar: uvicorn servicos.ingestao.app:app --port 8001
       python -m servicos.ingestao.worker
"""
from typing import Annotated

import redis
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel, Field

from servicos.ingestao import fila, indice

app = FastAPI(title="Ingestao - C2.A2")
redis_cliente = fila.conectar()


class Documento(BaseModel):
    texto: str = Field(min_length=1)
    origem: str = "desconhecida"


@app.post("/indexar", status_code=202)
def indexar(docs: Annotated[list[Documento], Body(min_length=1)]):
    """Enfileira os documentos; acompanhe o processamento em GET /tarefas/{id}."""
    try:
        tarefa_id = fila.enfileirar(redis_cliente, [d.model_dump() for d in docs])
    except redis.RedisError as erro:
        raise HTTPException(503, f"fila indisponivel: {erro}") from erro
    return {"tarefa": tarefa_id, "estado": "pendente", "documentos": len(docs),
            "acompanhar": f"/tarefas/{tarefa_id}"}


@app.get("/tarefas/{tarefa_id}")
def tarefa(tarefa_id: str):
    try:
        dados = fila.consultar_tarefa(redis_cliente, tarefa_id)
    except redis.RedisError as erro:
        raise HTTPException(503, f"fila indisponivel: {erro}") from erro
    if dados is None:
        raise HTTPException(404, "tarefa inexistente ou expirada")
    return {"tarefa": tarefa_id, **dados}


@app.get("/indice")
def ler_indice():
    """Consumido pelo servico de recuperacao."""
    itens = indice.carregar()
    return {"total": len(itens),
            "itens": [{"texto": i["texto"], "origem": i["origem"],
                       "vetor": i["vetor"]} for i in itens]}


@app.get("/saude")
def saude():
    try:
        na_fila = redis_cliente.llen(fila.FILA)
    except redis.RedisError:
        na_fila = "redis indisponivel"
    return {"status": "ok", "documentos": len(indice.carregar()), "fila": na_fila}
