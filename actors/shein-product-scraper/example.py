"""SHEIN Scraper: minimal example. Docs: https://apify.com/abotapi/shein-product-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/shein-product-scraper").call(
    run_input={
        "urls": ["https://au.shein.com/RecommendSelection/Women-Clothing-sc-017172961.html", "https://au.shein.com/RecommendSelection/Home-Kitchen-sc-017185546.html", "https://au.shein.com/pdsearch/summer%20dress/", "https://au.shein.com/Women-Dresses-c-1727.html"],
        "storefront": "au",
        "sortBy": "relevance",
        "maxItems": 10,
        "maxPages": 1,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
