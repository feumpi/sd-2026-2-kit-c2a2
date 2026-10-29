"""
Retentativa com espera progressiva (backoff exponencial + jitter) - Aula 11.

So retenta falhas TRANSITORIAS (tempo-limite, conexao recusada, HTTP 5xx e 429).
Erros do cliente (4xx) nao melhoram tentando de novo, entao sobem na hora.
Retentar a geracao e seguro porque ela nao tem efeito colateral (idempotente).
"""
import logging
import random
import time

import requests

log = logging.getLogger(__name__)


def eh_transitoria(erro: Exception) -> bool:
    if isinstance(erro, (requests.Timeout, requests.ConnectionError)):
        return True
    if isinstance(erro, requests.HTTPError) and erro.response is not None:
        codigo = erro.response.status_code
        return codigo >= 500 or codigo == 429
    return False


def espera_backoff(tentativa: int, base: float) -> float:
    """Espera antes da proxima tentativa: base, 2*base, 4*base... mais um jitter de ate base."""
    return base * 2 ** (tentativa - 1) + random.uniform(0, base)


def com_retentativa(funcao, tentativas=3, base=0.5):
    """Devolve uma versao de `funcao` que retenta falhas transitorias com backoff."""
    def envolvida(*args, **kwargs):
        for tentativa in range(1, tentativas + 1):
            try:
                return funcao(*args, **kwargs)
            except Exception as erro:
                if tentativa == tentativas or not eh_transitoria(erro):
                    raise
                espera = espera_backoff(tentativa, base)
                log.warning("tentativa %d/%d falhou (%s); nova tentativa em %.2fs",
                            tentativa, tentativas, erro, espera)
                time.sleep(espera)
    return envolvida
