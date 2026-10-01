"""Naver Land Scraper: minimal example. Docs: https://apify.com/abotapi/naver-land-listings

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/naver-land-listings").call(
    run_input={
        "searchKeywords": ["잠실"],
        "startUrls": ["https://new.land.naver.com/complexes?ms=2AM2Zq,3zhF96,16&a=APT:ABYG:JGC&e=RETAIL", "https://new.land.naver.com/complexes/111380", "https://new.land.naver.com/article/2651481309"],
        "maxItems": 10,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "KR"},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
