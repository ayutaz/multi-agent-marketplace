# 実験データ

実験には、YAML形式のエージェントプロファイルデータが必要であり、`businesses/` と `customers/` ディレクトリに整理されています。

## 顧客

```yaml
id: customer_0001
name: Customer 1
request: I want to buy...
menu_features:
  - Item_00: 0.00
  - Item_01: 0.00
amenity_features:
  - Amenity_03
```

**フィールド:**

- `id` (string): 顧客の一意な識別子
- `name` (string): 顧客の表示名
- `request` (string): 顧客が探しているもの
- `menu_features` (list): 希望するメニュー項目と期待価格
- `amenity_features` (list): 希望するアメニティ

## ビジネス

```yaml
id: business_0001
name: Business 1
description: Business 1
rating: 1.0
progenitor_customer: customer_0001
menu_features:
  Item_22: 1.0
  Item_21: 1.09
  Item_24: 0.99
amenity_features:
  Free Wifi: false
  Outdoor Seating: false
  Takes Reservations: false
  Offers Delivery: true
min_price_factor: 0.8
```

**フィールド:**

- `id` (string): ビジネスの一意な識別子
- `name` (string): ビジネスの表示名
- `description` (string): ビジネスの説明
- `rating` (float): ビジネスの評価（0-1のスケール）
- `progenitor_customer` (string): 関連する顧客ID（データ生成時に使用）
- `menu_features` (dict): メニュー項目と価格
- `amenity_features` (dict): 利用可能なアメニティ（真偽値）
- `min_price_factor` (float): 最低価格倍率

## ディレクトリ構造

```
experiment_data/
├── businesses/
│   ├── business_0001.yaml
│   ├── business_0002.yaml
│   └── ...
└── customers/
    ├── customer_0001.yaml
    ├── customer_0002.yaml
    └── ...
```
