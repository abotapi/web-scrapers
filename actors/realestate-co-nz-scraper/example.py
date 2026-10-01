"""RealestateCo NZ Scraper: minimal example. Docs: https://apify.com/abotapi/realestate-co-nz-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/realestate-co-nz-scraper").call(
    run_input={
        "mode": "location",
        "locations": [{"region": "Auckland"}],
        "listingType": "buy",
        "sort": "latest",
        "maxPages": 1,
        "maxListings": 10,
        "outputFormat": ["json"],
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
