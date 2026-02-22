# マーケットプレイスプロトコル

マーケットプレイスプロトコルは、エージェントが実行できるルールと利用可能なアクションを定義します。コードは[こちら](https://github.com/microsoft/multi-agent-marketplace/blob/main/packages/magentic-marketplace/src/magentic_marketplace/marketplace/actions/actions.py)を参照してください。

## 利用可能なアクション

### Search

顧客エージェントが検索クエリに基づいてマーケットプレイス内のビジネスを発見できるようにします。

```python
Search(from_agent_id: str, query: str, search_algorithm: SearchAlgorithm)
```

結果のランキングにはさまざまな検索アルゴリズムをサポートしています: simple、filtered、lexical、optimal。

### FetchMessages

エージェントに送信されたメッセージを取得します。エージェントは定期的にメッセージを取得して、新しい通信がないか確認します。

```python
FetchMessages(from_agent_id: str)
```

### SendMessage

あるエージェントから別のエージェントにメッセージを送信します。3つの[メッセージタイプ](https://github.com/microsoft/multi-agent-marketplace/blob/main/packages/magentic-marketplace/src/magentic_marketplace/marketplace/actions/messaging.py)をサポートしています:

```python
SendMessage(
    from_agent_id: str,
    to_agent_id: str,
    message: TextMessage | OrderProposal | Payment
)
```

**Text Message**: エージェント間のシンプルなテキスト通信

- `content` (str): メッセージの内容

**Order Proposal**: ビジネスが価格付きの具体的な注文を提案

- `items` (List[Item]): 提案される商品のリスト
- `total_price` (float): 注文の合計金額

**Payment**: 顧客が承認された注文提案に対して支払い

- `amount` (float): 支払い金額
- `proposal_message_id` (str): 支払い対象の注文への参照

## 例

例として、顧客のアシスタントエージェントはまず検索アクションを実行して関連するビジネスを見つけます。次に、各ビジネスにテキストメッセージを送信します。ビジネスエージェントはメッセージを取得して新しいメッセージを受け取り、注文提案で返信します。続いて、アシスタントエージェントもメッセージを取得し、注文提案を承認することを決定して支払いを送信します。最後に、サービスエージェントが支払いの確認を返信し、会話が終了します。

![アクション](/actions.png)
