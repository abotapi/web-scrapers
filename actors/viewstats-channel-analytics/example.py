"""ViewStats Scraper: minimal example. Docs: https://apify.com/abotapi/viewstats-channel-analytics

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/viewstats-channel-analytics").call(
    run_input={
        "mode": "channels",
        "channels": ["@MrBeast"],
        "searchTerms": ["mrbeast"],
        "statsRange": "365",
        "statsGroupBy": "monthly",
        "maxItems": 10,
        "proxy": {"useApifyProxy": True},
        "residentialCountries": ["US", "GB", "DE", "CA", "FR"],
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
