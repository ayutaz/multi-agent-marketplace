# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

Magentic Marketplace は、Microsoft Research によるオープンソースの Python フレームワーク。LLM ベースの Buyer/Seller エージェントが自律的に対話する両面マーケットプレイスのシミュレーション環境を提供する。

## リポジトリ構成

モノレポ構成で、2つのパッケージを含む:
- `packages/magentic-marketplace/` — Python バックエンド（FastAPI + SQLAlchemy）
- `packages/marketplace-visualizer/` — React/TypeScript フロントエンド（Vite + Tailwind）

Pythonパッケージのソースは `packages/magentic-marketplace/src/magentic_marketplace/` 配下にある。

## 開発コマンド

### セットアップ
```bash
uv sync --all-extras          # 依存関係インストール（uvパッケージマネージャ使用）
cp sample.env .env             # 環境変数テンプレートをコピーし、APIキーを設定
docker compose up -d           # PostgreSQL + pgAdmin 起動
```

### コード品質チェック（poethepoet タスクランナー）
```bash
poe check-all       # format + lint + type + spell の全チェック
poe fix-all         # format と lint の自動修正

poe format          # ruff format --check --diff
poe format-fix      # ruff format
poe lint            # ruff check
poe lint-fix        # ruff check --fix --unsafe-fixes
poe type            # pyright packages
poe spell           # codespell
```

### テスト
```bash
pytest                                          # 全テスト実行
pytest packages/magentic-marketplace/tests      # パスを明示的に指定
pytest -k "test_function_name"                  # 単一テスト実行
```

テストは `dev.env` を自動的に読み込む（pytest-dotenv）。一部テストには PostgreSQL が必要（`@pytest.mark.postgres`）、`@pytest.mark.rnr` は sentence-transformers 等のオプション依存が必要。asyncio_mode は auto 設定。

### フロントエンド（marketplace-visualizer）
```bash
cd packages/marketplace-visualizer
npm install
npm run dev          # 開発サーバー
npm run build        # tsc --noEmit && vite build
npm run check        # type-check + lint + format:check
npm run fix          # lint:fix + format
```

### 実験の実行
```bash
magentic-marketplace run data/mexican_3_9 --experiment-name my_exp
magentic-marketplace analyze my_exp
magentic-marketplace ui my_exp
```

## アーキテクチャ

### 3つのコアモジュール（`src/magentic_marketplace/`）

**platform/** — インフラ層
- `server/` — FastAPI サーバー（エージェント登録、アクション実行のルート）
- `database/` — データベース抽象層（PostgreSQL と SQLite の2バックエンド対応）。`models.py` に AgentRow, ActionRow 等の ORM モデル
- `client/` — エージェントがサーバーと通信するための HTTP クライアント
- `launcher.py` — MarketplaceLauncher（サーバー起動、DB初期化、実験オーケストレーション）

**marketplace/** — ドメイン層
- `protocol/` — SimpleMarketplaceProtocol が利用可能なアクション（Search, SendMessage, FetchMessages）を定義
- `protocol/search/` — 検索アルゴリズムの実装（lexical, rnr, filtered, optimal, simple）
- `agents/` — CustomerAgent と BusinessAgent。`base.py` の BaseSimpleMarketplaceAgent を継承
- `actions/` — アクションクラスとメッセージタイプ（TextMessage, OrderProposal, Payment）
- `llm/` — マルチプロバイダ LLM 統合（OpenAI, Anthropic, Gemini）。`llm/base.py` の ProviderClient 基底クラスから各プロバイダクライアントを実装
- `shared/models.py` — Business, Customer の Pydantic モデル

**experiments/** — 実験実行・分析
- `run_experiment.py` — シミュレーション実行のエントリポイント
- `run_analytics.py` — メトリクス計算・分析
- `run_audit.py` — マーケットプレイス行動の監査

**ui/** — ビジュアライゼーション
- `server.py` — 分析結果表示用の FastAPI サーバー。ビルド済みフロントエンドを `ui/static/` から配信

### マーケットプレイスの取引フロー

Customer が Search → ビジネス一覧取得 → TextMessage で問い合わせ → Business が OrderProposal で見積もり → Customer が Payment で支払い → 取引完了

### データ形式

実験データは YAML ファイルで定義（`data/` 配下）。各データセットは `businesses/` と `customers/` ディレクトリを含み、エージェントプロファイルを個別ファイルで管理。

## コーディング規約

- Python: ruff（line-length=88, double quotes, space indent）、pyright で型チェック
- ruff lint ルール: E, W, F, I, B, C4, UP, D（docstrings 必須）。E501（行長制限）は無視
- フロントエンド: ESLint + Prettier、Tailwind CSS
- PR は 300 LOC 以下推奨（Copilot ルール準拠）

## 環境変数（.env）

LLM プロバイダ設定: `LLM_PROVIDER`（openai/anthropic/gemini）、`LLM_MODEL`、`LLM_MAX_CONCURRENCY`（デフォルト64）
DB設定: `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_MAX_CONNECTIONS`

## CI

GitHub Actions: `test.yml`（pytest）、`ruff.yml`（lint）、`pyright.yml`（型チェック）、`emoji-check.yml`（絵文字禁止）、`pr-size-check.yml`（PRサイズ制限）
