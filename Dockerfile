FROM python:3.8-slim

# Ustaw katalog roboczy
WORKDIR /app

# Instalacja zależności systemowych
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    fonts-liberation \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Zmienna środowiskowa dla Chromedrivera i Pythona
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH=$PATH:/usr/bin/chromedriver
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app"

# Kopiuj zależności Pythona i zainstaluj
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiuj kod projektu
COPY src/ ./src/
COPY tests/ ./tests/

# Domyślna komenda – uruchamia pytest i generuje raport HTML
CMD ["pytest", "tests/", "--html=report.html"]
