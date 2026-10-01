# TaskRabbit Scraper

Scrape TaskRabbit taskers by US city and service. Extract hourly rates, ratings, reviews, completed tasks, elite status, and availability. Track NEW, UPDATED, REAPPEARED, and EXPIRED taskers with incremental runs, resume, and MCP export.

**[Open TaskRabbit Scraper on Apify](https://apify.com/abotapi/taskrabbit-tasker-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~taskrabbit-tasker-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Portland, OR"], "services": ["furniture assembly", "tv mounting"], "profileInputs": ["1883135"], "maxItems": 10, "maxReviewsPerTasker": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Cities |
| `services` | array | Services |
| `profileInputs` | array | Tasker links or ids |
| `urls` | array | Tasker links or ids (alias) |
| `maxItems` | integer | Max items |
| `includeProfiles` | boolean | Fetch full tasker profiles (rates and  |
| `includeReviews` | boolean | Also fetch tasker reviews |
| `maxReviewsPerTasker` | integer | Max reviews per tasker |
| `includeCityReviews` | boolean | Also return city service reviews (sear |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/taskrabbit-tasker-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `taskId` | integer |
| `displayName` | string |
| `citySlug` | string |
| `serviceSlug` | string |
| `cityName` | string |
| `metroId` | integer |
| `serviceName` | string |
| `v3CategoryId` | integer |
| `v3TaskTemplateId` | integer |
| `averageRating` | integer |
| `reviewsCount` | integer |
| `tasksCount` | integer |
| `elite` | boolean |
| `bio` | string |
| `imageUrl` | string |
| `source` | string |
| `slug` | string |
| `url` | string |
| `metroName` | string |
| `hoursWorked` | float |
| `positiveRating` | string |
| `onDuty` | boolean |
| `taskCountProfile` | integer |
| `rabbitSinceYear` | integer |
| `vehicleType` | string |
| `phoneNumberMasked` | string |
| `description` | string |
| `avatarUrl` | string |
| `categories` | list |
| `totalReviewCount` | integer |
| `ratingDistribution` | null |

---

[← All scrapers](../../README.md)
