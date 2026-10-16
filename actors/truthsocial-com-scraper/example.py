"""Truth Social Scraper: minimal example. Docs: https://apify.com/abotapi/truthsocial-com-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/truthsocial-com-scraper").call(
    run_input={
        "startUrls": [{"url": "https://truthsocial.com/@realDonaldTrump"}, {"url": "https://truthsocial.com/@realDonaldTrump/with_replies"}, {"url": "https://truthsocial.com/@realDonaldTrump/media"}, {"url": "https://truthsocial.com/@realDonaldTrump/posts/116813202769287423"}, {"url": "https://truthsocial.com/@realDonaldTrump/116813202769287423"}, {"url": "https://truthsocial.com/users/realDonaldTrump/statuses/116813202769287423"}, {"url": "https://truthsocial.com/group/wine-with-devin-nunes"}, {"url": "https://truthsocial.com/group/wine-with-devin-nunes/posts/117121586897225540"}],
        "profileContentType": "postsAndReplies",
        "maxItems": 10,
        "maxPages": 1,
        "countryCode": "US",
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
