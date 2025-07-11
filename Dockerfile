# Use a imagem oficial do Airflow como base
FROM apache/airflow:3.0.0

USER root

# 1. Instalar pacotes do sistema (Chrome e dependências)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      wget \
      unzip \
      gnupg2 \
      default-jdk \
      chromium \
      chromium-driver && \
    rm -rf /var/lib/apt/lists/*

# 2. Copiar e instalar dependências Python
COPY requirements.txt /tmp/requirements.txt

USER 50000

RUN pip install --no-cache-dir -r /tmp/requirements.txt

#USER ${AIRFLOW_UID:-50000}:${AIRFLOW_GID:-0}

# Opcional: definir variáveis de ambiente para Selenium
ENV SELENIUM_BROWSER=Chrome \
    CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/bin/chromedriver
