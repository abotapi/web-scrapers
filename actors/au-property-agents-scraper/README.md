# Real Estate AU Agents Scraper

Scrape Australian real estate agent and agency profiles by suburb or profile URLs. Returns names, roles, agencies, performance stats, median sold price, days advertised, properties sold, ratings, full reviews, and contact details.

**[Open Real Estate AU Agents Scraper on Apify](https://apify.com/abotapi/au-property-agents-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~au-property-agents-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "location", "searchType": "agent", "locations": [{"suburb": "Sydney CBD", "state": "NSW"}], "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `searchType` | string | Search for (Location mode) |
| `locations` | array | Locations to search (Location mode) |
| `includeSurrounding` | boolean | Include Surrounding Suburbs |
| `urls` | array | Profile or search URLs (URL mode) |
| `fetchDetails` | boolean | Fetch full profile details |
| `maxReviews` | integer | Maximum reviews per record |
| `maxItems` | integer | Maximum records |
| `maxPages` | integer | Maximum search result pages |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/au-property-agents-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `agentId` | string |
| `name` | string |
| `firstName` | string |
| `jobTitle` | string |
| `yearsExperience` | integer |
| `description` | string |
| `url` | string |
| `source` | string |
| `rating` | object |
| `reviewSummary` | string |
| `salesSummary` | object |
| `agencyId` | string |
| `agency` | object |
| `social` | object |
| `profileImageUrl` | string |
| `coverPhotoUrl` | string |
| `scrapedAt` | string |
| `startYearInIndustry` | integer |
| `mostActiveLocation` | object |
| `phone` | object |
| `stats` | object |
| `communityInvolvement` | string |
| `compliments` | list |
| `video` | object |
| `reviews` | list |

---

[← All scrapers](../../README.md)
