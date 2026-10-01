"""Hipcamp Scraper: minimal example. Docs: https://apify.com/abotapi/hipcamp-camping-glamping-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/hipcamp-camping-glamping-scraper").call(
    run_input={
        "mode": "search",
        "regions": ["california"],
        "maxItems": 10,
        "proxyConfiguration": {"useApifyProxy": True},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
