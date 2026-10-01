# Childcare AU Scraper

Scrape Australia’s largest childcare directory careforkids.com.au with long day care, preschool, family day care, OSHC, and vacation care services. Returns centre profiles with address, fees, ratings, vacancies, features, images, and ACECQA approval numbers.

**[Open Childcare AU Scraper on Apify](https://apify.com/abotapi/careforkids-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~careforkids-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": [{"suburb": "Sydney", "postcode": "2000"}], "careTypes": ["all"], "maxListings": 10, "maxReviewsPerCentre": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `locations` | array | Suburb  postcode pairs |
| `careTypes` | array | Care types |
| `verifiedOnly` | boolean | Verified centres only |
| `vacanciesOnly` | boolean | Centres with vacancies only |
| `minRating` | integer | Minimum parent rating |
| `maxDailyFee` | integer | Maximum average daily fee, AUD |
| `urls` | array | Search URLs (URL mode) |
| `maxListings` | integer | Max listings (total) |
| `fetchDetails` | boolean | Fetch detail pages (richer data) |
| `reviewsOnly` | boolean | Reviews-only output (one record per re |
| `maxReviewsPerCentre` | integer | Max reviews per centre (Reviews-only) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/careforkids-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `name` | string |
| `suburb` | string |
| `postcode` | string |
| `state` | string |
| `address` | string |
| `latitude` | float |
| `longitude` | float |
| `phone` | string |
| `rating` | integer |
| `reviewCount` | integer |
| `dailyFee` | integer |
| `hasVacancies` | boolean |
| `isVerified` | boolean |
| `isRecommended` | boolean |
| `listingType` | string |
| `careTypes` | list |
| `requestedCareType` | null |
| `services` | list |
| `nqsRating` | string |
| `hoursSummary` | string |
| `logoUrl` | string |
| `cardImageUrl` | string |
| `centreGroupId` | string |
| `description` | null |
| `descriptionHtml` | null |
| `contactName` | null |
| `contactTime` | null |
| `websiteUrl` | null |
| `facebookUrl` | null |
| `instagramUrl` | null |
| `serviceApprovalNumber` | null |
| `approvedPlaces` | null |
| `nqsRatingOverall` | null |
| `nqsRatingLabel` | null |
| `nqsAreaRatings` | list |
| `nqsLastUpdated` | null |
| `providerGroup` | null |
| `providerGroupId` | null |

---

[← All scrapers](../../README.md)
