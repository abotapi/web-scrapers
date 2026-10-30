"""Cotton On Scraper: minimal example. Docs: https://apify.com/abotapi/cottonon-com-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/cottonon-com-scraper").call(
    run_input={
        "mode": "urls",
        "urls": ["https://cottonon.com/AU/co/women/womens-clothing/womens-tops/", "https://cottonon.com/AU/kids/kids-boys-1-8/boys-1-8-clothing/", "https://cottonon.com/AU/typo/typo-shop-all/", "https://cottonon.com/AU/factorie/f-shop-all/", "https://cottonon.com/AU/co/co-sale/", "https://cottonon.com/AU/co/co-gifts/", "https://cottonon.com/AU/hold-me-cami/2060406-02.html"],
        "searchTerms": ["denim shorts"],
        "market": "AU",
        "sort": "relevance",
        "maxReviews": 10,
        "maxItems": 10,
        "proxy": {"useApifyProxy": True},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
