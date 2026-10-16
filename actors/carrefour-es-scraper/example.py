"""Carrefour Spain Scraper: minimal example. Docs: https://apify.com/abotapi/carrefour-es-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/carrefour-es-scraper").call(
    run_input={
        "mode": "search",
        "queries": ["leche"],
        "categories": ["https://www.carrefour.es/supermercado/lacteos-huevos/leche/cat20093/c", "Vinos"],
        "sortBy": "relevance",
        "minRating": "0",
        "maxReviews": 10,
        "maxItems": 10,
        "maxPages": 1,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "ES"},
        "maxResults": 10,
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
