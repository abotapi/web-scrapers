"""CVS Scraper: minimal example. Docs: https://apify.com/abotapi/cvs-product-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/cvs-product-scraper").call(
    run_input={
        "mode": "urls",
        "searchTerms": ["shampoo"],
        "urls": [{"url": "https://www.cvs.com/shop/l-a-girl-shimmer-spray-gold-prodid-186492"}, {"url": "https://www.cvs.com/search?q=shampoo"}],
        "maxItems": 10,
        "proxyConfiguration": {"useApifyProxy": True},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
