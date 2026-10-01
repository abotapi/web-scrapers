"""Mercado Livre Brazil Scraper: minimal example. Docs: https://apify.com/abotapi/mercadolivre-com-br-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/mercadolivre-com-br-scraper").call(
    run_input={
        "mode": "search",
        "queries": ["notebook"],
        "condition": "any",
        "sortBy": "relevance",
        "maxReviewsPerProduct": 10,
        "maxItems": 10,
        "maxPages": 1,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "BR"},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
