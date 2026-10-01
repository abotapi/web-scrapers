"""Wine-Searcher Scraper: minimal example. Docs: https://apify.com/abotapi/wine-searcher-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/wine-searcher-scraper").call(
    run_input={
        "inputType": "auto",
        "wineNames": ["Domaine Leflaive Puligny-Montrachet Les Pucelles 2020", "Petrus 2015"],
        "urls": ["https://www.wine-searcher.com/find/petrus/2015"],
        "lwins": ["11316442021", "11084042019", "1131644"],
        "maxItems": 10,
        "proxy": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "FR"},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
