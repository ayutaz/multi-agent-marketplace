# エージェント

エージェントは、マーケットプレイス内で意思決定を行い、相互にやり取りする自律的なアクターです。各エージェントはプロファイルを持ち、連続的なループで動作し、プラットフォームを通じてアクションを実行します。

## マーケットプレイスエージェント

このマーケットプレイスでは、相互にやり取りする2つの基本的なエージェント、CustomerAgent と BusinessAgent を作成しました。各エージェントは [BaseAgent](https://github.com/microsoft/multi-agent-marketplace/blob/main/packages/magentic-marketplace/src/magentic_marketplace/platform/agent/base.py) クラスを継承しており、エージェントの登録を処理した後、`step()` 関数を継続的に呼び出すことでエージェントループを管理します。

### エージェントのライフサイクル

1. **初期化**: プロファイルとサーバーURLを使用してエージェントを作成
2. **登録**: エージェントがマーケットプレイスサーバーに登録
3. **アクティブループ**: エージェントが `step()` メソッドを繰り返し実行
4. **シャットダウン**: エージェントがシャットダウンシグナルを受信し、正常に切断

## [CustomerAgent](https://github.com/microsoft/multi-agent-marketplace/blob/main/packages/magentic-marketplace/src/magentic_marketplace/marketplace/agents/customer/agent.py)

顧客エージェントはショッピング行動を実装します。ビジネスの検索、問い合わせの送信、提案の評価、購入の実行を行います。

```python
class CustomerAgent(BaseSimpleMarketplaceAgent):
    async def step(self):
        # LLMを使用して次のアクションを決定
        action = await self._generate_customer_action()

        # 選択されたアクションを実行
        if action:
            await self._execute_customer_action(action)
```

## [BusinessAgent](https://github.com/microsoft/multi-agent-marketplace/blob/main/packages/magentic-marketplace/src/magentic_marketplace/marketplace/agents/business/agent.py)

サービス行動を実装します。顧客からのメッセージの監視、問い合わせへの応答、注文提案の作成、支払いの処理を行います。

```python
class BusinessAgent(BaseSimpleMarketplaceAgent):
    async def step(self):
        # 顧客からの新しいメッセージを取得
        messages = await self.fetch_messages()

        # 各顧客に対して処理・応答
        if messages:
            await self._handle_customer_messages(messages)
        else:
            await asyncio.sleep(self._polling_interval)
```
