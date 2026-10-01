"""Idealo.de Scraper: minimal example. Docs: https://apify.com/abotapi/idealo-de-price-comparison-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/idealo-de-price-comparison-scraper").call(
    run_input={
        "mode": "url",
        "searchQuery": "iphone 15",
        "urls": ["https://www.idealo.de/preisvergleich/ProductCategory/5292.html"],
        "maxItems": 10,
        "maxPages": 1,
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "DE"},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
