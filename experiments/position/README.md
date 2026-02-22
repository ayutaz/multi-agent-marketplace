# 位置バイアス実験

## セットアップ
`run_n_experiments.py` でモデルを設定します:
```python
# クローズドソースモデルの場合（デフォルト）:
MODELS = [
    {"provider": "openai", "model": "gpt-4.1"},
    {"provider": "openai", "model": "gpt-4o"},
]

# オープンソースモデルの場合（上記をコメントアウトし、ファイル内のqwenモデルのコメントを解除してください）
```

## 実行
```bash
python run_n_experiments.py
python generate_position_data.py
python generate_proposal_data.py
python plot_position_bias.py
python plot_proposal_bias.py
```

結果は `results/` に保存されます。
