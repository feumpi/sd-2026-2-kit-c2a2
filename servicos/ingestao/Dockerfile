# Servico de ingestao - build a partir da raiz do repositorio:
#   docker build -f servicos/ingestao/Dockerfile .
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
COPY servicos/ingestao servicos/ingestao

RUN useradd --create-home app
# volume do indice persistido (compartilhado com o worker no compose)
ENV DIR_DADOS=/dados
RUN mkdir /dados && chown app /dados
VOLUME /dados
USER app

EXPOSE 8001
CMD ["uvicorn", "servicos.ingestao.app:app", "--host", "0.0.0.0", "--port", "8001"]
