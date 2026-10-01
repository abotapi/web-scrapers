# Rover Pet Care Scraper

Scrape Rover.com pet-care providers: sitter search by city, rates per stay type, ratings and review history, verification badges, repeat clients, response times, service policies and availability signals.

**[Open Rover Pet Care Scraper on Apify](https://apify.com/abotapi/rover-pet-care-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~rover-pet-care-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["San Francisco, CA, USA"], "serviceType": "overnight-boarding", "petType": "dog", "maxReviewsPerSitter": 10, "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `serviceType` | string | Service type |
| `petType` | string | Pet type |
| `urls` | array | URLs |
| `minRating` | integer | Minimum rating |
| `minPrice` | integer | Minimum rate |
| `maxPrice` | integer | Maximum rate |
| `starSitter` | boolean | Star Sitters only |
| `fetchDetails` | boolean | Fetch full profiles |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerSitter` | integer | Max reviews per sitter |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/rover-pet-care-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `shortName` | string |
| `headline` | string |
| `url` | string |
| `imageUrl` | string |
| `serviceType` | string |
| `currencyCode` | string |
| `pricePerUnit` | integer |
| `priceUnit` | string |
| `neighborhood` | string |
| `city` | string |
| `state` | string |
| `zip` | string |
| `latitude` | float |
| `longitude` | float |
| `distanceMi` | float |
| `ratingsAverage` | integer |
| `ratingsCount` | integer |
| `testimonialsCount` | integer |
| `yearsOfExperience` | integer |
| `yearsOfExperienceText` | string |
| `description` | string |
| `engagementLabel` | string |
| `availabilityUpdatedText` | string |
| `availabilityUpdatedDaysAgo` | integer |
| `badgeTitle` | string |
| `badgeSlug` | string |
| `cancellationPolicy` | string |
| `repeatClients` | integer |
| `browsableServiceSlugs` | list |
| `firstName` | string |
| `fullDescription` | string |
| `memberSince` | string |
| `responseRatePercent` | integer |
| `responseRateText` | string |
| `responseTimeText` | string |
| `photoUpdateRatePercent` | integer |
| `imagesCount` | integer |
| `verificationBadges` | list |

---

[← All scrapers](../../README.md)
