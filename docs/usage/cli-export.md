# `export`: 結果のエクスポート

PostgreSQL の実験データを SQLite データベースファイルにエクスポートし、共有や移植を容易にします。

**使い方:**

```bash
magentic-marketplace export my_experiment
```

**主な引数:**

`experiment_name` _(必須)_

&nbsp;&nbsp;&nbsp;&nbsp;実験名（PostgreSQL のスキーマ名）。

`-o, --output-dir` _(任意)_

&nbsp;&nbsp;&nbsp;&nbsp;SQLite データベースファイルの出力ディレクトリ（デフォルト: カレントディレクトリ）。

`-f, --output-filename` _(任意)_

&nbsp;&nbsp;&nbsp;&nbsp;SQLite データベースの出力ファイル名（デフォルト: `<experiment_name>.db`）。
