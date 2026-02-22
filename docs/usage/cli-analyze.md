# `analyze`: 実験結果の分析

実験の完了後、このコマンドで結果を分析できます。デフォルトでは分析結果を表示し、JSONファイルに保存します。

**使い方:**

```bash
magentic-marketplace analyze my_experiment
```

**主な引数:**

`experiment-name` _(必須)_

&nbsp;&nbsp;&nbsp;&nbsp;実験名（PostgreSQL のスキーマ名）。

`--db-type` _(任意)_

&nbsp;&nbsp;&nbsp;&nbsp;データベースの種類: `sqlite` または `postgres`（デフォルト: `postgres`）。postgres の場合、実験名はデータベース内のスキーマ名です。sqlite の場合、データベースファイルへのパスです。

`--no-save-json` _(任意)_

&nbsp;&nbsp;&nbsp;&nbsp;分析結果のJSONファイルへの保存を無効にします。
