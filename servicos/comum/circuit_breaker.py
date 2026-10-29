"""
Circuit breaker de referencia - Aula 11.

Adaptado do modelo do kit para proteger chamadas remotas no servico de geracao:
  - thread-safe (as rotas sincronas do FastAPI rodam num pool de threads);
  - no estado "meio" deixa passar UMA unica chamada de teste por vez;
  - informa quantos segundos faltam para tentar de novo (header Retry-After).

Estados:
  fechado  -> deixa passar (normal)
  aberto   -> recusa na hora, sem tentar (servico esta quebrado)
  meio     -> deixa passar UMA chamada de teste para ver se voltou
"""
import threading
import time


class CircuitoAberto(Exception):
    """Levantada quando o disjuntor esta aberto e recusa a chamada."""


class CircuitBreaker:

    def __init__(self, limite_falhas=5, espera_segundos=30):
        self.limite_falhas = limite_falhas
        self.espera_segundos = espera_segundos
        self.falhas = 0
        self.estado = "fechado"
        self.aberto_em = 0.0
        self._em_teste = False
        self._trava = threading.Lock()

    def chamar(self, funcao, *args, **kwargs):
        with self._trava:
            if self.estado == "aberto":
                if time.time() - self.aberto_em >= self.espera_segundos:
                    self.estado = "meio"
                    self._em_teste = False
                else:
                    raise CircuitoAberto("disjuntor aberto: chamada recusada")
            if self.estado == "meio":
                if self._em_teste:
                    raise CircuitoAberto("disjuntor meio-aberto: chamada de teste em andamento")
                self._em_teste = True
        # a chamada em si fica fora da trava para nao serializar as requisicoes
        try:
            resultado = funcao(*args, **kwargs)
        except Exception:
            with self._trava:
                self._registrar_falha()
            raise
        with self._trava:
            self._registrar_sucesso()
        return resultado

    def segundos_para_tentar(self):
        """Quanto falta para o disjuntor aceitar a chamada de teste (0 se nao estiver aberto)."""
        if self.estado != "aberto":
            return 0.0
        return max(0.0, self.espera_segundos - (time.time() - self.aberto_em))

    def _registrar_falha(self):
        self.falhas += 1
        self._em_teste = False
        if self.falhas >= self.limite_falhas or self.estado == "meio":
            self.estado = "aberto"
            self.aberto_em = time.time()

    def _registrar_sucesso(self):
        self.falhas = 0
        self._em_teste = False
        self.estado = "fechado"
