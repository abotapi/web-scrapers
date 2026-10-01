"""Commercial Property AU Scraper: minimal example. Docs: https://apify.com/abotapi/realcommercial-au-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/realcommercial-au-scraper").call(
    run_input={
        "mode": "location",
        "locations": [{"suburb": "Melbourne", "state": "VIC"}],
        "listingType": "for-sale",
        "sortBy": "date-desc",
        "maxListings": 10,
        "maxPages": 1,
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
