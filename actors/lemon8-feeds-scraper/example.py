"""Lemon8 Feed Scraper: minimal example. Docs: https://apify.com/abotapi/lemon8-feeds-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/lemon8-feeds-scraper").call(
    run_input={
        "category": 0,
        "startUrls": ["https://www.lemon8-app.com/feed/outfits?region=au", "https://www.lemon8-app.com/feed/outfits", "https://www.lemon8-app.com/@lylassecret10/7699504612750934559?region=us", "https://www.lemon8-app.com/@lylassecret10?region=us", "https://www.lemon8-app.com/@lylassecret10/7699504612750934559?region=us&share_token=x"],
        "region": "us",
        "limit": 10,
        "proxy": {"useApifyProxy": True, "apifyProxyCountry": "US"},
        "dev_dataset_name": "default",
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
