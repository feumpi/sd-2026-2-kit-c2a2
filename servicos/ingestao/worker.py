"""
Worker de ingestao - TAREFA 4 (Aula 8): consome a fila, vetoriza e persiste o indice.

Fila confiavel: a mensagem e movida atomicamente (BLMOVE) para a lista
"processando" e so sai de la depois de tratada. Se o worker cair no meio,
ela volta para a fila quando ele subir de novo. Reprocessar e seguro porque a
indexacao e idempotente (ids por hash do conteudo).

Falhas: a tarefa volta para a fila ate MAX_TENTATIVAS; depois vai para a
dead-letter (fila:ingestao:dlq) para analise, sem travar o fluxo principal.

Rodar: python -m servicos.ingestao.worker
"""
import json
import logging
import signal
import time

import redis

from servicos.ingestao import fila, indice

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("worker-ingestao")

_parar = False


def recuperar_pendentes(r: redis.Redis) -> int:
    """Devolve para a fila o que ficou em 'processando' de uma execucao anterior."""
    recuperadas = 0
    while r.lmove(fila.PROCESSANDO, fila.FILA, "RIGHT", "RIGHT") is not None:
        recuperadas += 1
    if recuperadas:
        log.warning("%d tarefa(s) interrompida(s) devolvida(s) a fila", recuperadas)
    return recuperadas


def _mandar_para_dlq(r, mensagem: str, tarefa_id, erro) -> None:
    r.lpush(fila.DLQ, json.dumps({"mensagem": mensagem, "erro": str(erro)}))
    if tarefa_id:
        fila.atualizar_tarefa(r, tarefa_id, estado="falhou", erro=erro)
    log.error("tarefa %s enviada para a dead-letter: %s", tarefa_id, erro)


def processar_uma(r: redis.Redis, timeout: float = 5) -> bool:
    """Processa uma mensagem da fila. Devolve False se a fila ficou vazia no timeout."""
    mensagem = r.blmove(fila.FILA, fila.PROCESSANDO, timeout, "RIGHT", "LEFT")
    if mensagem is None:
        return False
    try:
        try:
            tarefa = json.loads(mensagem)
            tarefa_id, documentos = tarefa["id"], tarefa["documentos"]
        except (json.JSONDecodeError, KeyError, TypeError) as erro:
            _mandar_para_dlq(r, mensagem, None, f"mensagem invalida: {erro}")
            return True

        try:
            resultado = indice.adicionar(documentos)
        except Exception as erro:
            tarefa["tentativas"] = tarefa.get("tentativas", 0) + 1
            if tarefa["tentativas"] >= fila.MAX_TENTATIVAS:
                _mandar_para_dlq(r, json.dumps(tarefa), tarefa_id, erro)
            else:
                log.warning("tarefa %s falhou (tentativa %d/%d): %s", tarefa_id,
                            tarefa["tentativas"], fila.MAX_TENTATIVAS, erro)
                fila.atualizar_tarefa(r, tarefa_id, estado="pendente",
                                      tentativas=tarefa["tentativas"], erro=erro)
                r.lpush(fila.FILA, json.dumps(tarefa))
            return True

        fila.atualizar_tarefa(r, tarefa_id, estado="concluida", novos=resultado["novos"],
                              total=resultado["total"], concluida_em=time.time())
        log.info("tarefa %s concluida: %d novo(s), %d no indice", tarefa_id,
                 resultado["novos"], resultado["total"])
        return True
    finally:
        r.lrem(fila.PROCESSANDO, 1, mensagem)


def _pedir_parada(sinal, quadro):
    global _parar
    log.info("sinal %s recebido; encerrando apos a tarefa atual", sinal)
    _parar = True


def main() -> None:
    signal.signal(signal.SIGTERM, _pedir_parada)
    signal.signal(signal.SIGINT, _pedir_parada)
    r = fila.conectar()
    recuperado = False
    log.info("worker de ingestao aguardando tarefas em %s", fila.FILA)
    while not _parar:
        try:
            if not recuperado:
                recuperar_pendentes(r)
                recuperado = True
            processar_uma(r, timeout=2)
        except redis.RedisError as erro:
            log.warning("redis indisponivel (%s); nova tentativa em 2s", erro)
            time.sleep(2)


if __name__ == "__main__":
    main()
