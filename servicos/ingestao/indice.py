"""
Indice vetorial persistido em arquivo JSON - TAREFA 1.

O indice fica em DIR_DADOS/indice.json (padrao: ./dados). A escrita e atomica:
grava num arquivo temporario e troca com os.replace, entao quem le enxerga
sempre o indice antigo inteiro ou o novo inteiro, nunca um arquivo pela metade.

Cada documento tem id = sha256(origem + texto). Indexar o mesmo documento de
novo nao duplica nada (operacao idempotente).
"""
import hashlib
import json
import logging
import os
from pathlib import Path

from servicos.comum.embeddings import Vetorizador

log = logging.getLogger(__name__)


def caminho_indice() -> Path:
    return Path(os.getenv("DIR_DADOS", "dados")) / "indice.json"


def id_documento(texto: str, origem: str) -> str:
    return hashlib.sha256(f"{origem}\n{texto}".encode("utf-8")).hexdigest()


def carregar() -> list[dict]:
    """Le o indice do disco. Arquivo ausente = indice vazio."""
    caminho = caminho_indice()
    if not caminho.exists():
        return []
    try:
        return json.loads(caminho.read_text(encoding="utf-8"))["itens"]
    except (json.JSONDecodeError, KeyError, TypeError) as erro:
        # guarda o arquivo estragado para analise em vez de sobrescreve-lo
        destino = caminho.with_suffix(".corrompido")
        os.replace(caminho, destino)
        log.error("indice corrompido (%s); movido para %s", erro, destino)
        return []


def salvar(itens: list[dict]) -> None:
    caminho = caminho_indice()
    caminho.parent.mkdir(parents=True, exist_ok=True)
    temporario = caminho.with_suffix(".json.tmp")
    with open(temporario, "w", encoding="utf-8") as arquivo:
        json.dump({"itens": itens}, arquivo, ensure_ascii=False)
        arquivo.flush()
        os.fsync(arquivo.fileno())
    os.replace(temporario, caminho)


def revetorizar(itens: list[dict]) -> None:
    """O vocabulario do TF-IDF muda a cada documento novo: recalcula todos os vetores."""
    vetorizador = Vetorizador()
    vetorizador.ajustar([i["texto"] for i in itens])
    for item in itens:
        item["vetor"] = vetorizador.vetorizar(item["texto"])


def adicionar(documentos: list[dict]) -> dict:
    """Acrescenta documentos ({texto, origem}) ao indice persistido, sem duplicar."""
    itens = carregar()
    ids = {i["id"] for i in itens}
    novos = 0
    for doc in documentos:
        doc_id = id_documento(doc["texto"], doc["origem"])
        if doc_id in ids:
            continue
        ids.add(doc_id)
        itens.append({"id": doc_id, "texto": doc["texto"], "origem": doc["origem"]})
        novos += 1
    if novos:
        revetorizar(itens)
        salvar(itens)
    return {"novos": novos, "total": len(itens)}
