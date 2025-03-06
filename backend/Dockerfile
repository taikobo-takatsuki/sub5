FROM python:3.10-slim

WORKDIR /app

# MeCabと依存ライブラリのインストール
RUN apt-get update && \
    apt-get install -y mecab libmecab-dev mecab-ipadic-utf8 build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# ポートを開放
EXPOSE 8000

# アプリケーションの実行
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 