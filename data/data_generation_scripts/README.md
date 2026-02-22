# 合成データ生成スクリプト

このフォルダには合成データ生成用のスクリプトが含まれています。以下のコマンドを実行して合成データセットを生成します:

```bash
python generate_customers_and_businesses.py <path_to_output_directory>
```

引数の詳細については以下を参照してください:
```bash
python generate_customers_and_businesses.py --help
```


### バリデーション
以下のコマンドを実行して、生成されたデータを検証できます:

```bash
python validate.py <path_to_input_directory>
```


### その他

特徴量ファイルは既に生成済みで `features` フォルダに格納されています。再生成したい場合は、以下のコマンドを実行してください:

```bash
python generate_items.py <path_to_output_file: e.g. features/items.yaml>
```

```bash
python generate_people.py <path_to_output_file: e.g. features/people.yaml>
```

### 請負業者データセット

アイテムの生成:
```bash
python generate_item_contractors.py <path_to_output_file>
```

ビジネスと顧客のYAMLファイルの生成:
```bash
python generate_customers_and_business_contractors.py -f <path_to_features_directory> -c <number_of_customers> <output_dir>
```
