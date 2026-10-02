# Tutti.ch Scraper

Scrape listings from tutti.ch across all 23 categories, including vehicles, property, electronics, furniture, fashion, and jobs. Search by keyword, category, city, or use tutti.ch URLs. Returns price, location, canton, seller details, images, and optional GPS, phone, photos, and attributes.

**[Open Tutti.ch Scraper on Apify](https://apify.com/abotapi/tutti-ch-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~tutti-ch-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keyword": "velo", "category": "all", "sortBy": "newest", "language": "de", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "CH"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keyword` | string | Keyword |
| `category` | string | Category |
| `locations` | array | Locations (city slugs) |
| `minPrice` | integer | Min price (CHF) |
| `maxPrice` | integer | Max price (CHF) |
| `urls` | array | tutti.ch URLs |
| `sortBy` | string | Sort by |
| `language` | string | Site language |
| `fetchDetails` | boolean | Fetch full details (extra cost) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (0  no limit) |
| `proxy` | object | Proxy |
| `maxResidentialPercent` | integer | Residential usage cap (%) |
| `residentialBudgetMb` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/tutti-ch-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `title` | string |
| `description` | null |
| `price` | string |
| `priceValue` | integer |
| `currency` | string |
| `categoryId` | string |
| `categoryLabel` | null |
| `parentCategoryId` | null |
| `parentCategoryLabel` | null |
| `locationName` | string |
| `postcode` | string |
| `canton` | string |
| `cantonName` | string |
| `latitude` | null |
| `longitude` | null |
| `street` | null |
| `sellerName` | string |
| `sellerType` | string |
| `sellerAccountId` | null |
| `sellerLogoUrl` | null |
| `sellerLocation` | null |
| `sellerProfileUrl` | null |
| `sellerSubscriptionClass` | null |
| `sellerBadgeUrl` | null |
| `memberSince` | null |
| `phone` | null |
| `externalUrl` | null |
| `highlighted` | boolean |
| `formattedSource` | null |
| `imageUrl` | string |
| `imageCount` | integer |
| `images` | list |
| `properties` | list |
| `timestamp` | string |
| `language` | string |
| `url` | string |

---

[← All scrapers](../../README.md)
