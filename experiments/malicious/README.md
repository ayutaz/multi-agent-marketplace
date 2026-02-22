# 悪意のある説明文の実験

## セットアップ
`run_n_experiments.py` でモデルを設定します:
```python
# クローズドソースモデルの場合（デフォルト）:
MODELS = [
    {"provider": "openai", "model": "gpt-4.1"},
    {"provider": "openai", "model": "gpt-4o"},
    {"provider": "gemini", "model": "gemini-2.5-flash"},
    {"provider": "anthropic", "model": "claude-sonnet-4-5"},
]

# オープンソースモデルの場合（上記をコメントアウトし、ファイル内のqwenモデルのコメントを解除してください）
```

## 実行
```bash
python run_n_experiments.py
python analyze_results.py
python plot_results.py
```

結果は `results/` に保存されます。
