# Python API の使い方

Python スクリプトから Python API を使って、プログラムで実験を実行できます。

```python
import asyncio

from dotenv import load_dotenv
from magentic_marketplace.experiments.run_analytics import run_analytics
from magentic_marketplace.experiments.run_experiment import run_marketplace_experiment

# モデルと実験の設定を読み込む
load_dotenv()

async def main():
    experiment_name = "example_experiment"

    await run_marketplace_experiment(
        data_dir="data/mexican_3_9",
        experiment_name=experiment_name,
        customer_max_steps=100,
        override=True,
    )
    results = await run_analytics(
        experiment_name,
        db_type="postgres",
        save_to_json=False,
        print_results=False
    )

    print("Results: ", results)

if __name__ == "__main__":
    print("Running example experiment...")
    asyncio.run(main())
```
