# テストの実行

全テストの実行:
```bash
uv run pytest tests
```

個別に実行:
```bash
# 検索
uv run pytest tests/protocol/test_search.py

# メッセージ送信
uv run pytest tests/protocol/test_send_message.py

# メッセージ取得
uv run pytest tests/protocol/test_fetch_messages.py
```
