# Magentic Marketplace

[ドキュメント](https://microsoft.github.io/multi-agent-marketplace/) | [論文](https://arxiv.org/abs/2510.25779)


**Magentic Marketplace** は、AI駆動のマーケットプレイスをシミュレートするためのPythonフレームワークです。LLMベースの買い手エージェントと売り手エージェントを設定し、リアルなマーケットプレイスシミュレーションを実行し、福利厚生、公平性、効率性などの経済的な成果を測定できます。

<div align="center">

   <video src="https://github.com/user-attachments/assets/5b897387-d96c-4e7a-9bd2-b6c53eaeabb9" style="max-height: 450px;">
   </video>
</div>


## これで何ができるのか？

- **LLMモデルの評価** - 異なるモデル（OpenAI、Claude、Gemini、ローカルモデル）がマーケットプレイスエージェントとしてどのように機能するかを比較
- **マーケット設計のテスト** - 異なる検索アルゴリズム、通信プロトコル、マーケットプレイスルールを実験
- **エージェント行動の研究** - 福利厚生の成果を測定し、バイアスを特定し、操作への耐性をテスト
- **新しいドメインへの拡張** - レストラン/請負業者以外の他の二面市場にフレームワークを適用

## クイックスタート

1. 環境を設定する

   ```bash
   # リポジトリをクローン
   git clone https://github.com/microsoft/multi-agent-marketplace.git
   cd multi-agent-marketplace

   # `uv` で依存関係をインストール。https://docs.astral.sh/uv/ からインストール
   uv sync --all-extras
   source .venv/bin/activate

   # .env に環境変数を設定。お好みのエディタで編集
   cp sample.env .env

   # データベースサーバーを起動
   docker compose up -d
   ```

2. シミュレーションを実行し、結果を分析する

   ```bash
   # 実験を実行（実験名はオプション）
   magentic-marketplace run data/mexican_3_9 --experiment-name test_exp

   # 結果を分析
   magentic-marketplace analyze test_exp
   ```

   Pythonスクリプトから実験を実行することもできます。[experiments/example.py](experiments/example.py) を参照してください。

   `magentic-marketplace --help` でその他のCLIオプションを確認できます。

## よくある質問

- [自分のLLMをテストするには？](https://microsoft.github.io/multi-agent-marketplace/usage/env.html)
- [ログにアクセスして評価するには？](https://microsoft.github.io/multi-agent-marketplace/usage/cli-analyze.html)

[**詳細はドキュメントをご覧ください。**](https://microsoft.github.io/multi-agent-marketplace/)

## 引用

この研究を使用する場合は、以下を引用してください：

```
@misc{bansal-arxiv-2025,
      title={Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets},
      author={Gagan Bansal and Wenyue Hua and Zezhou Huang and Adam Fourney and Amanda Swearngin and Will Epperson and Tyler Payne and Jake M. Hofman and Brendan Lucier and Chinmay Singh and Markus Mobius and Akshay Nambi and Archana Yadav and Kevin Gao and David M. Rothschild and Aleksandrs Slivkins and Daniel G. Goldstein and Hussein Mozannar and Nicole Immorlica and Maya Murad and Matthew Vogel and Subbarao Kambhampati and Eric Horvitz and Saleema Amershi},
      year={2025},
      eprint={2510.25779},
      archivePrefix={arXiv},
      primaryClass={cs.MA},
      url={https://arxiv.org/abs/2510.25779},
}
```
