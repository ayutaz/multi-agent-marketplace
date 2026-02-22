# 検討セットサイズ実験

## 実験の実行
```bash
python consideration_set_size.py --dataset <path/to/dataset> --model <model-name> --runs <num-runs> --search-limits <comma-separated-limits>
```

## 結果の分析
```bash
python analyze_consideration_set_size.py --input-dir <path/to/results> --data-dir <path/to/data>
```

## グラフの作成

```bash
uv sync --all-groups --all-extras
```

```bash
python create_plot.py --files-to-plot <csv-files> --plot-key "Welfare" --plot-label "Customer Welfare"
```
