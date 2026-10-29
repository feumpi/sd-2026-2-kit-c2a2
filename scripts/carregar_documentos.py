"""
Envia os documentos de uma pasta para o servico de ingestao e espera o worker indexar.

Uso: python scripts/carregar_documentos.py [--url http://localhost:8001] [--pasta documentos]
"""
import argparse
import sys
import time
from pathlib import Path

import requests


def ler_documentos(pasta: Path) -> list[dict]:
    return [{"texto": arquivo.read_text(encoding="utf-8").strip(), "origem": arquivo.name}
            for arquivo in sorted(pasta.glob("*.txt"))]


def carregar(url: str, pasta: Path, espera_maxima: float = 30) -> dict:
    """Enfileira os documentos e acompanha a tarefa ate concluir (ou falhar)."""
    documentos = ler_documentos(pasta)
    if not documentos:
        raise SystemExit(f"nenhum .txt encontrado em {pasta}")
    r = requests.post(f"{url}/indexar", json=documentos, timeout=10)
    r.raise_for_status()
    tarefa = r.json()
    print(f"{len(documentos)} documento(s) enfileirado(s) - tarefa {tarefa['tarefa']}")

    limite = time.monotonic() + espera_maxima
    while time.monotonic() < limite:
        estado = requests.get(f"{url}{tarefa['acompanhar']}", timeout=5).json()
        if estado["estado"] != "pendente":
            return estado
        time.sleep(0.5)
    raise SystemExit("tempo esgotado esperando o worker - ele esta rodando?")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--url", default="http://localhost:8001", help="URL da ingestao")
    parser.add_argument("--pasta", default="documentos", type=Path)
    args = parser.parse_args()

    estado = carregar(args.url, args.pasta)
    if estado["estado"] != "concluida":
        print(f"falhou: {estado.get('erro')}", file=sys.stderr)
        sys.exit(1)
    print(f"indexacao concluida: {estado['novos']} novo(s), {estado['total']} no indice")


if __name__ == "__main__":
    main()
