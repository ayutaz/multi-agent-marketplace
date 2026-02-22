# Marketplace Visualizer

マーケットプレイスの結果を可視化します!

## クイックスタート

このビジュアライザーは、実験完了後のデータベースに対して動作します。

まず、実験を実行してスキーマ名を取得します:

```bash
cd multi-agent-marketplace
docker compose up -d

magentic-marketplace run data/mexican_3_9 --experiment-name myexperiment123
```

次に、ビジュアライザーを起動できます:

```bash
magentic-marketplace ui myexperiment123
```

## 開発

変更を加えるには、まずフロントエンドのコードをインストールしてから、開発モードでサーバーを実行する必要があります

```bash
cd marketplace-visualizer
uv sync
npm install
npm run build # 出力ファイルをビルド
```

次に、開発モードでUIを起動します

```bash
cd marketplace-visualizer
npm run dev
```

さらにバックエンドサーバーも起動します:

```bash
magentic-marketplace ui <schema-name>
```
