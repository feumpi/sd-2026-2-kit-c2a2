"""
Servico 1 - INGESTAO: recebe documentos, gera embeddings e armazena.

TAREFA 1: o indice e persistido em disco (ver indice.py) e sobrevive a reinicios.

Rodar: uvicorn servicos.ingestao.app:app --port 8001
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field

from servicos.ingestao import indice

app = FastAPI(title="Ingestao - C2.A2")


class Documento(BaseModel):
    texto: str = Field(min_length=1)
    origem: str = "desconhecida"


@app.post("/indexar")
def indexar(docs: list[Documento]):
    resultado = indice.adicionar([d.model_dump() for d in docs])
    return {"indexados": resultado["total"], "novos": resultado["novos"]}


@app.get("/indice")
def ler_indice():
    """Consumido pelo servico de recuperacao."""
    itens = indice.carregar()
    return {"total": len(itens),
            "itens": [{"texto": i["texto"], "origem": i["origem"],
                       "vetor": i["vetor"]} for i in itens]}


@app.get("/saude")
def saude():
    return {"status": "ok", "documentos": len(indice.carregar())}
