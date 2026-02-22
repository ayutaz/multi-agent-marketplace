# `run`: マーケットプレイス実験の実行

YAML 設定ファイルを使用してマーケットプレイスシミュレーションを実行します。`/businesses` と `/customers` サブディレクトリを含むディレクトリへのパスを指定する必要があります。設定例についてはリポジトリの [data](https://github.com/microsoft/multi-agent-marketplace/tree/main/data) フォルダを参照してください。

**使い方:**

```bash
magentic-marketplace run data/mexican_3_9 --experiment-name my_experiment
```

**主な引数:**

`data_dir` _(必須)_

&nbsp;&nbsp;&nbsp;&nbsp;`businesses/` と `customers/` サブディレクトリを含むデータディレクトリへのパス。

`--experiment-name` _(任意)_

&nbsp;&nbsp;&nbsp;&nbsp;この実験の名前。指定しない場合、一意の名前が自動生成されます。

`--override-db` _(任意)_

&nbsp;&nbsp;&nbsp;&nbsp;同名の実験が既に存在する場合、上書きします。

`--search-algorithm` _(任意)_

&nbsp;&nbsp;&nbsp;&nbsp;顧客エージェントの検索アルゴリズム（デフォルト: `lexical`）。

`--search-bandwidth` _(任意)_

&nbsp;&nbsp;&nbsp;&nbsp;顧客エージェントの検索帯域幅（デフォルト: `10`）。

`--customer-max-steps` _(任意)_

&nbsp;&nbsp;&nbsp;&nbsp;顧客エージェントが停止するまでの最大ステップ数（デフォルト: `100`）。

**その他のオプション:** `magentic-marketplace run --help` で追加の引数を確認できます。
