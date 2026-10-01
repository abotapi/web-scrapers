# Clutch Scraper

Scrape Clutch company directories and profiles. Get names, ratings, review counts, hourly rate, min project size, employees, location, services, full reviews with reviewer details and per-criterion scores. Search and URL mode, 40+ fields per company.

**[Open Clutch Scraper on Apify](https://apify.com/abotapi/clutch-directory-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~clutch-directory-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "directory": "web-developers", "sortBy": "default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `directory` | string | Directory |
| `location` | string | Location |
| `agencySize` | string | Company size |
| `relatedServices` | string | Related service |
| `sortBy` | string | Sort by |
| `urls` | array | Clutch directory URLs |
| `minRating` | integer | Min rating |
| `minReviews` | integer | Min reviews |
| `fetchDetails` | boolean | Fetch full profile details (richer rec |
| `maxPages` | integer | Max pages per list |
| `maxListings` | integer | Max records |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/clutch-directory-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `kind` | string |
| `type` | string |
| `slug` | string |
| `name` | string |
| `title` | string |
| `url` | string |
| `clutchUrl` | string |
| `profileUrl` | string |
| `profileLink` | string |
| `logo` | string |
| `logoUrl` | string |
| `website` | string |
| `websiteUrl` | string |
| `tagline` | null |
| `description` | string |
| `summary` | string |
| `quote` | null |
| `rating` | float |
| `reviewCount` | integer |
| `numberOfProjects` | null |
| `minProjectSize` | string |
| `hourlyRate` | string |
| `employeeCount` | string |
| `employeesCount` | string |
| `priceRange` | string |
| `location` | string |
| `services` | list |
| `tags` | list |
| `verified` | boolean |
| `isVerified` | boolean |
| `isSponsor` | boolean |
| `position` | integer |
| `company` | object |
| `branding` | object |
| `contact` | object |
| `ratings` | object |
| `pricing` | object |
| `staffing` | object |
| `services_cluster` | object |

---

[← All scrapers](../../README.md)
