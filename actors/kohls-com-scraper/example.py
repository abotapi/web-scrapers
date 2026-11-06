"""Kohl's Scraper: minimal example. Docs: https://apify.com/abotapi/kohls-com-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/kohls-com-scraper").call(
    run_input={
        "mode": "urls",
        "searchTerms": ["womens jeans"],
        "urls": [{"url": "https://www.kohls.com/search.jsp?search=womens+jeans&PPP=120"}, {"url": "https://www.kohls.com/catalog/mens-clothing.jsp"}, {"url": "https://www.kohls.com/product/prd-7327369/nike-v5-rnr-womens-running-shoes.jsp"}],
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyCountry": "US"},
        "maxReviews": 10,
        "changeScope": "all",
        "maxItems": 10,
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
