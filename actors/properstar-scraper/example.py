"""Properstar Scraper: minimal example. Docs: https://apify.com/abotapi/properstar-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/properstar-scraper").call(
    run_input={
        "startUrls": ["https://www.properstar.co.uk/united-kingdom/london/buy/apartment-house", "https://www.properstar.co.uk/united-kingdom/london/buy/apartment-house?p=2", "https://www.properstar.co.uk/united-kingdom/london/rent/apartment-house", "https://www.properstar.co.uk/united-kingdom/buy/apartment-house", "https://www.properstar.co.uk/united-kingdom/london/buy/apartment-house?price=500000-1000000&bedrooms=2", "https://www.properstar.co.uk/united-kingdom/london/buy/apartment-house?sort=price-asc", "https://www.properstar.co.uk/united-kingdom/london/buy", "https://www.properstar.co.uk/switzerland/buy/apartment-house", "https://www.properstar.co.uk/listing/121377505", "https://www.properstar.co.uk/agency/the-private-realtor-ltd/6482545"],
        "transactionType": "any",
        "maxItems": 10,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
