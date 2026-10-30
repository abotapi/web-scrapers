"""Fuel Price Scraper: minimal example. Docs: https://apify.com/abotapi/fuel-prices-anz-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/fuel-prices-anz-scraper").call(
    run_input={
        "suburb": "Sydney",
        "searchMode": "location",
        "startUrls": [{"url": "https://petrolspy.com.au/map/location/au/nsw/2000/sydney"}, {"url": "https://petrolspy.com.au/map/latlng/-33.8688/151.2093"}],
        "sortOrder": "asc",
        "maxItems": 10,
        "proxy": {"useApifyProxy": False},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
