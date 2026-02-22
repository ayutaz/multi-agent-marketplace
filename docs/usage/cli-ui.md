# `ui`: マーケットプレイス UI の起動

ブラウザでマーケットプレイスビジュアライザーを起動します。デフォルトでは [http://localhost:5000/](http://localhost:5000/) で表示されます。この UI を使って、実験の完了後または実行中に顧客とビジネスの会話を確認できます。

<img src="/ui.png" style="border: 2px solid #F6F6F7; border-radius: 10px;">

**使い方:**

```bash
magentic-marketplace ui my_experiment
```

**主な引数:**

`experiment_name` _(必須)_

&nbsp;&nbsp;&nbsp;&nbsp;実験名（PostgreSQL のスキーマ名）。

`--db-type` _(任意)_

&nbsp;&nbsp;&nbsp;&nbsp;データベースの種類: `sqlite` または `postgres`（デフォルト: `postgres`）。postgres の場合、実験名はデータベース内のスキーマ名です。sqlite の場合、データベースファイルへのパスです。
