"""Local.ch Scraper: minimal example. Docs: https://apify.com/abotapi/local-ch-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/local-ch-scraper").call(
    run_input={
        "mode": "search",
        "category": "restaurant",
        "where": "zurich",
        "language": "de",
        "maxPages": 1,
        "maxListings": 10,
        "maxReviewsPerListing": 10,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "CH"},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
