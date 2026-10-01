"""PropertyGuru SG Scraper: minimal example. Docs: https://apify.com/abotapi/propertyguru-sg-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/propertyguru-sg-scraper").call(
    run_input={
        "mode": "search",
        "listing_type": "sale",
        "sort": "date",
        "sort_order": "desc",
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "SG"},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
