# Houzz Pro Scraper

Pull Houzz pro listings across global sites. Search by category and location, keyword, or URL, plus review mode for specific pros. Returns 35+ fields including ratings, reviews, awards, services, address, GPS, contacts, social links, project counts, and featured review.

**[Open Houzz Pro Scraper on Apify](https://apify.com/abotapi/houzz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~houzz-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "site": "houzz.com", "category": "interior-designers", "reviewSort": "NEWEST", "maxReviewsPerPro": 10, "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `site` | string | Country |
| `category` | string | Category |
| `queries` | array | Keywords (free-text) |
| `locations` | array | Locations |
| `reviewSort` | string | Review sort order |
| `maxReviewsPerPro` | integer | Max reviews per pro |
| `urls` | array | Directory URLs |
| `minRating` | integer | Minimum rating |
| `minReviewCount` | integer | Minimum review count |
| `verifiedOnly` | boolean | Verified pros only |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max pros total |
| `fetchDetails` | boolean | Fetch full profile per pro |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/houzz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `userId` | integer |
| `professionalId` | integer |
| `proId` | integer |
| `displayName` | string |
| `userName` | string |
| `proType` | integer |
| `proCategory` | null |
| `proTypeDisplayName` | string |
| `proSkuId` | integer |
| `isInactivePro` | null |
| `country` | string |
| `state` | string |
| `city` | string |
| `zip` | string |
| `address` | string |
| `address1` | null |
| `address2` | null |
| `formattedAddress` | string |
| `locationLabel` | string |
| `latitude` | float |
| `longitude` | float |
| `formattedPhone` | string |
| `fax` | null |
| `email` | null |
| `domain` | null |
| `website` | null |
| `houzzLink` | string |
| `numReviews` | integer |
| `reviewRating` | integer |
| `aspectCommunication` | null |
| `aspectOnTime` | null |
| `aspectQuality` | null |
| `aspectValue` | null |
| `featuredReview` | object |
| `featuredReviewText` | string |
| `mostRecentReview` | object |
| `mostRecentReviewText` | string |
| `isProVerified` | boolean |
| `hasVerifiedKyc` | boolean |

---

[← All scrapers](../../README.md)
