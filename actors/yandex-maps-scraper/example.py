"""Yandex Maps Scraper: minimal example. Docs: https://apify.com/abotapi/yandex-maps-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/yandex-maps-scraper").call(
    run_input={
        "searchStringsArray": ["restaurants"],
        "startUrls": [{"url": "https://yandex.com/maps/org/no_plates_coffee/124606085044/"}, {"url": "https://yandex.com/maps/org/124606085044/"}, {"url": "https://yandex.com/maps/org/no_plates_coffee/124606085044/reviews/"}, {"url": "https://yandex.ru/maps/org/no_plates_coffee/124606085044/"}, {"url": "https://yandex.com/maps/?ll=-74.006%2C40.7128&z=12&text=coffee"}, {"url": "https://yandex.com/maps/?text=restaurants"}, {"url": "https://yandex.com/maps/202/new-york/search/restaurants/"}, {"url": "https://yandex.com/maps/202/new-york/category/coffee_shop/"}, {"url": "https://yandex.com/maps/?ol=biz&oid=1018907821"}, {"url": "https://yandex.com/maps/213/moscow/search/%D0%BA%D0%BE%D1%84%D0%B5/"}, {"url": "https://yandex.com/maps/213/moscow/search/coffee/?page=2"}, {"url": "https://m.yandex.com/maps/org/192990200894/"}],
        "location": "New York, NY",
        "maxReviews": 10,
        "maxPosts": 10,
        "language": "en-US",
        "proxyConfiguration": {"useApifyProxy": True},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
