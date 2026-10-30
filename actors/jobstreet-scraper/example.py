"""JobStreet Scraper: minimal example. Docs: https://apify.com/abotapi/jobstreet-scraper

pip install "apify-client>=3"
APIFY_TOKEN=<your token> python example.py
"""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("abotapi/jobstreet-scraper").call(
    run_input={
        "country": "MY",
        "keywords": "software engineer",
        "location": "Kuala Lumpur",
        "salaryType": "monthly",
        "requireContact": "off",
        "sortmode": "ListedDate",
        "urls": ["https://my.jobstreet.com/software-engineer-jobs/in-Kuala-Lumpur", "https://my.jobstreet.com/it-jobs", "https://my.jobstreet.com/jobs/in-Selangor", "https://my.jobstreet.com/jobs-in-information-communication-technology", "https://my.jobstreet.com/jobs-in-information-communication-technology/in-Kuala-Lumpur", "https://my.jobstreet.com/jobs-in-information-communication-technology/developers-programmers", "https://my.jobstreet.com/software-engineer-jobs/remote", "https://my.jobstreet.com/software-engineer-jobs-in-information-communication-technology/in-Kuala-Lumpur/full-time", "https://my.jobstreet.com/jobs?classification=6281&worktype=242&daterange=7&sortmode=ListedDate&page=2", "https://sg.jobstreet.com/jobs-in-accounting/in-Singapore", "https://ph.jobstreet.com/jobs-in-accounting/in-Manila", "https://id.jobstreet.com/jobs-in-accounting/in-Jakarta", "https://my.jobstreet.com/api/jobsearch/v5/search?siteKey=MY-Main&sourcesystem=houston&where=Kuala+Lumpur&keywords=software+engineer&page=1&pageSize=5"],
        "maxItems": 10,
        "maxPages": 1,
        "descriptionFormat": "all",
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": []},
    },
    logger=None,  # don't stream the run log to your console
)

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"{len(items)} items")
for item in items[:3]:
    print(json.dumps(item, ensure_ascii=False)[:300])
