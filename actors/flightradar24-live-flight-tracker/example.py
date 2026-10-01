"""Flightradar24 Scraper: minimal example. Docs: https://apify.com/abotapi/flightradar24-live-flight-tracker

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/flightradar24-live-flight-tracker").call(
    run_input={
        "mode": "live",
        "bounds": ["55.0,45.0,-6.0,10.0"],
        "airports": ["LHR"],
        "boardMode": "departures",
        "historyQueries": ["G-TUKR"],
        "fetchBy": "reg",
        "maxItems": 10,
        "proxy": {"useApifyProxy": True},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
