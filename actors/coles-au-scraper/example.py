"""Coles AU Scraper: minimal example. Docs: https://apify.com/abotapi/coles-au-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/coles-au-scraper").call(
    run_input={
        "inputMode": "search",
        "mode": "search",
        "queries": ["milk"],
        "categories": ["dairy-eggs-fridge"],
        "sortBy": "relevance",
        "minRating": "0",
        "maxReviewsPerProduct": 10,
        "maxItems": 10,
        "maxPages": 1,
        "proxy": {"useApifyProxy": True},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
