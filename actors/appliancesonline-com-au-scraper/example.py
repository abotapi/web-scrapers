"""Appliances Online Scraper: minimal example. Docs: https://apify.com/abotapi/appliancesonline-com-au-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/appliancesonline-com-au-scraper").call(
    run_input={
        "mode": "categories",
        "searchInputs": ["washers-and-dryers/washing-machines"],
        "productInputs": ["176381", "appliancesonline.com.au/product/8kg-front-load-haier-washing-machine-hwm80-1403d/", "appliancesonline.com.au/filter/washers-and-dryers/washing-machines/", "appliancesonline.com.au/filter/clearance/"],
        "sortBy": "popularity",
        "maxReviewsPerProduct": 10,
        "maxItems": 10,
        "proxy": {"useApifyProxy": True},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
