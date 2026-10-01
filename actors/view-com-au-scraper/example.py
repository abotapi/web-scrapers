"""View.com.au Scraper: minimal example. Docs: https://apify.com/abotapi/view-com-au-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/view-com-au-scraper").call(
    run_input={
        "mode": "location",
        "locations": [{"suburb": "Melbourne", "state": "VIC", "postcode": "3000"}],
        "listingType": "buy",
        "sort": "date-desc",
        "maxListings": 10,
        "maxPages": 1,
        "outputFormat": ["json"],
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
