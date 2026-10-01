"""Ip Location Check Scraper: minimal example. Docs: https://apify.com/abotapi/ip-location-check

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/ip-location-check").call(
    run_input={
        "ipAddresses": ["8.8.8.8", "1.1.1.1"],
        "language": "en",
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
