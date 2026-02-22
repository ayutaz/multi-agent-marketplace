# はじめに

Magentic Marketplace でシミュレーションを実行するには、Python 3.10 以上、[uv](https://docs.astral.sh/uv/) パッケージマネージャー、および [Docker](https://www.docker.com/get-started/) が必要です。

## インストール

1. **リポジトリをクローン**

   ```bash
   git clone https://github.com/microsoft/multi-agent-marketplace.git
   cd multi-agent-marketplace
   ```

2. **依存関係をインストール**

   ```bash
   uv sync --all-extras
   source .venv/bin/activate
   ```

3. **環境変数を設定**

   ```bash
   # サンプル環境ファイルをコピー
   cp sample.env .env

   # .env を編集して API キーを追加し、モデルを変更
   ```

4. **データベースサーバーを起動**

   Docker を使って実験データを保存する Postgres データベースを起動します。

   ```bash
   docker compose up -d
   ```

## 実験を実行

これで実験を実行する準備が整いました！

```bash
magentic-marketplace run data/mexican_3_9
```
