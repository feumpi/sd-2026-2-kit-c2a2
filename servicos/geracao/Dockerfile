# Servico de geracao - build a partir da raiz do repositorio:
#   docker build -f servicos/geracao/Dockerfile .
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# cada imagem leva apenas o codigo comum e o do proprio servico
COPY servicos/__init__.py servicos/
COPY servicos/comum servicos/comum
COPY servicos/geracao servicos/geracao

RUN useradd --create-home app
USER app

EXPOSE 8003
CMD ["uvicorn", "servicos.geracao.app:app", "--host", "0.0.0.0", "--port", "8003"]
