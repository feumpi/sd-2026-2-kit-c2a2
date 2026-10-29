"""
Servico 2 - RECUPERACAO: dada uma pergunta, acha os trechos mais relevantes.

TAREFA 2: busca por similaridade do cosseno sobre o indice do servico de ingestao.

Rodar: uvicorn servicos.recuperacao.app:app --port 8002
"""
import os

import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from servicos.comum.embeddings import Vetorizador, similaridade

app = FastAPI(title="Recuperacao - C2.A2")
URL_INGESTAO = os.getenv("URL_INGESTAO", "http://localhost:8001")
TIMEOUT_INGESTAO = float(os.getenv("TIMEOUT_INGESTAO", "5"))


class Consulta(BaseModel):
    pergunta: str = Field(min_length=1)
    top_k: int = Field(default=3, ge=1, le=20)


def ler_indice() -> list[dict]:
    try:
        r = requests.get(f"{URL_INGESTAO}/indice", timeout=TIMEOUT_INGESTAO)
        r.raise_for_status()
    except requests.RequestException as erro:
        raise HTTPException(503, f"servico de ingestao indisponivel: {erro}") from erro
    return r.json()["itens"]


def ranquear(pergunta: str, itens: list[dict], top_k: int) -> list[dict]:
    """Ordena os itens pela similaridade com a pergunta e devolve os top_k."""
    if not itens:
        return []
    # mesmos textos na mesma ordem -> mesmo vocabulario usado pela ingestao
    vetorizador = Vetorizador()
    vetorizador.ajustar([i["texto"] for i in itens])
    vetor_pergunta = vetorizador.vetorizar(pergunta)

    pontuados = []
    for item in itens:
        vetor = item.get("vetor")
        if not vetor or len(vetor) != len(vetor_pergunta):
            vetor = vetorizador.vetorizar(item["texto"])
        pontuados.append({"texto": item["texto"], "origem": item["origem"],
                          "score": round(similaridade(vetor_pergunta, vetor), 4)})
    pontuados.sort(key=lambda r: r["score"], reverse=True)
    return pontuados[:top_k]


@app.post("/buscar")
def buscar(consulta: Consulta):
    """Devolve os top_k trechos mais parecidos com a pergunta."""
    itens = ler_indice()
    return {"pergunta": consulta.pergunta,
            "resultados": ranquear(consulta.pergunta, itens, consulta.top_k)}


@app.get("/saude")
def saude():
    return {"status": "ok"}
