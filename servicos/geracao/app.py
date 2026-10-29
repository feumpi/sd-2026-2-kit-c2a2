"""
Servico 3 - GERACAO: monta o prompt com o contexto e chama o LLM.

TAREFA 3: a chamada ao LLM e protegida por tempo-limite (LLM_TIMEOUT, em llm.py),
retentativa com backoff (resiliencia.py) e circuit breaker. A chamada ao servico
de recuperacao tambem tem tempo-limite e um disjuntor proprio. Quando uma
dependencia falha, o servico degrada com elegancia: 503 com mensagem clara.

Rodar: uvicorn servicos.geracao.app:app --port 8003
"""
import logging
import os

import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from servicos.comum import llm
from servicos.comum.circuit_breaker import CircuitBreaker, CircuitoAberto
from servicos.geracao.resiliencia import com_retentativa

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("geracao")

app = FastAPI(title="Geracao - C2.A2")
URL_RECUPERACAO = os.getenv("URL_RECUPERACAO", "http://localhost:8002")
TIMEOUT_RECUPERACAO = float(os.getenv("TIMEOUT_RECUPERACAO", "5"))
TOP_K = int(os.getenv("TOP_K", "3"))

disjuntor_llm = CircuitBreaker(
    limite_falhas=int(os.getenv("LLM_LIMITE_FALHAS", "3")),
    espera_segundos=float(os.getenv("LLM_ESPERA_DISJUNTOR", "20")))
disjuntor_recuperacao = CircuitBreaker(
    limite_falhas=int(os.getenv("RECUPERACAO_LIMITE_FALHAS", "3")),
    espera_segundos=float(os.getenv("RECUPERACAO_ESPERA_DISJUNTOR", "20")))


class Pergunta(BaseModel):
    pergunta: str = Field(min_length=1)


def buscar_trechos(pergunta: str) -> list[dict]:
    r = requests.post(f"{URL_RECUPERACAO}/buscar",
                      json={"pergunta": pergunta, "top_k": TOP_K},
                      timeout=TIMEOUT_RECUPERACAO)
    r.raise_for_status()
    return r.json()["resultados"]


def chamar_llm(pergunta: str, contexto: list) -> str:
    return llm.gerar(pergunta, contexto)


gerar_com_retentativa = com_retentativa(
    chamar_llm,
    tentativas=int(os.getenv("LLM_RETENTATIVAS", "3")),
    base=float(os.getenv("LLM_BACKOFF_BASE", "0.5")))


def indisponivel(mensagem, disjuntor, **extras):
    """Resposta de degradacao: 503 + Retry-After + o que ja se sabe."""
    espera = max(1, round(disjuntor.segundos_para_tentar()) or 5)
    return JSONResponse(status_code=503, headers={"Retry-After": str(espera)},
                        content={"erro": mensagem, "disjuntor": disjuntor.estado, **extras})


@app.post("/perguntar")
def perguntar(p: Pergunta):
    try:
        resultados = disjuntor_recuperacao.chamar(buscar_trechos, p.pergunta)
    except CircuitoAberto:
        return indisponivel("servico de recuperacao indisponivel (disjuntor aberto); "
                            "tente novamente em instantes", disjuntor_recuperacao,
                            pergunta=p.pergunta)
    except requests.RequestException as erro:
        log.warning("falha ao consultar a recuperacao: %s", erro)
        return indisponivel("servico de recuperacao indisponivel", disjuntor_recuperacao,
                            pergunta=p.pergunta)

    # trechos sem nenhuma palavra em comum com a pergunta nao fundamentam resposta
    relevantes = [r for r in resultados if r.get("score", 1) > 0]
    contexto = [r["texto"] for r in relevantes]
    fontes = list(dict.fromkeys(r["origem"] for r in relevantes))
    if not contexto:
        return {"pergunta": p.pergunta, "contexto": [], "fontes": [],
                "resposta": "Nao encontrei nos documentos indexados nada sobre essa pergunta."}

    try:
        resposta = disjuntor_llm.chamar(gerar_com_retentativa, p.pergunta, contexto)
    except CircuitoAberto:
        return indisponivel("LLM indisponivel (disjuntor aberto); seguem os trechos "
                            "recuperados", disjuntor_llm,
                            pergunta=p.pergunta, contexto=contexto, fontes=fontes)
    except Exception as erro:
        log.warning("falha ao chamar o LLM apos as retentativas: %s", erro)
        return indisponivel("LLM indisponivel no momento; seguem os trechos recuperados",
                            disjuntor_llm,
                            pergunta=p.pergunta, contexto=contexto, fontes=fontes)

    return {"pergunta": p.pergunta, "resposta": resposta,
            "contexto": contexto, "fontes": fontes}


@app.get("/saude")
def saude():
    return {"status": "ok",
            "llm": "api" if llm.API_KEY else "simulado",
            "disjuntores": {"llm": disjuntor_llm.estado,
                            "recuperacao": disjuntor_recuperacao.estado}}
