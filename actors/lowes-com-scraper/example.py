"""Lowe's Scraper: minimal example. Docs: https://apify.com/abotapi/lowes-com-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/lowes-com-scraper").call(
    run_input={
        "mode": "urls",
        "searchTerms": ["drill"],
        "urls": [{"url": "https://www.lowes.com/search?searchTerm=drill"}, {"url": "https://www.lowes.com/pd/CRAFTSMAN-20-volt-Max-1-2-in-Keyless-Brushless-Cordless-Drill-1-Batteries-Included-Soft-Bag-Included/5016412045"}],
        "maxReviews": 10,
        "maxItems": 10,
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"},
        "changeScope": "all",
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
