"""AllTrails Hiking Scraper: minimal example. Docs: https://apify.com/abotapi/alltrails-hiking-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/alltrails-hiking-scraper").call(
    run_input={
        "mode": "search",
        "regionPath": "California",
        "tags": ["backpacking"],
        "maxItems": 10,
        "maxPages": 1,
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["UNBLOCKER"]},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
