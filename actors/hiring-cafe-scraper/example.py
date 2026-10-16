"""Hiring.Cafe Jobs Scraper: minimal example. Docs: https://apify.com/abotapi/hiring-cafe-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/hiring-cafe-scraper").call(
    run_input={
        "startUrls": [{"url": "https://hiringcafe.com/classic"}, {"url": "https://hiringcafe.com/classic?searchState=%7B%22searchQuery%22%3A%22software%20engineer%22%7D"}, {"url": "https://hiringcafe.com/classic?searchState=%7B%22searchQuery%22%3A%22software%20engineer%22%7D&page=2"}, {"url": "https://hiringcafe.com/?searchState=%7B%22searchQuery%22%3A%22software%20engineer%22%7D"}, {"url": "https://hiringcafe.com/?searchState=eyJzZWFyY2hRdWVyeSI6InNvZnR3YXJlIGVuZ2luZWVyIn0%3D"}, {"url": "https://hiringcafe.com/job/bt38fz2pqe76nimr"}],
        "workplaceType": "Any",
        "commitmentType": "Any",
        "seniorityLevel": "Any",
        "sortBy": "default",
        "maxItems": 10,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
