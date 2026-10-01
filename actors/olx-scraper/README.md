# OLX Scraper

Fast OLX scraper across 9 countries, including Poland, Romania, Portugal, Ukraine, Bulgaria, Kazakhstan, Uzbekistan, India and Brazil. Search or paste OLX URLs to extract structured listing data with pagination and multi-market support.

**[Open OLX Scraper on Apify](https://apify.com/abotapi/olx-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~olx-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "country": "pl", "sortBy": "default", "maxListings": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `urls` | array | URLs (URL mode only) |
| `country` | string | Country |
| `query` | string | Search query (free text) |
| `categoryId` | integer | Category ID |
| `cityId` | integer | City ID (Pattern A only) |
| `locationId` | integer | Location ID (India only) |
| `priceMin` | integer | Minimum price |
| `priceMax` | integer | Maximum price |
| `sortBy` | string | Sort order |
| `extraFilters` | object | Extra filters (advanced passthrough) |
| `fetchDetails` | boolean | Fetch full details per listing |
| `maxListings` | integer | Maximum listings |
| `maxPages` | integer | Maximum pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/olx-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `country` | string |
| `url` | string |
| `title` | string |
| `description` | string |
| `createdAt` | string |
| `createdAtFirst` | null |
| `lastRefreshTime` | string |
| `validToTime` | string |
| `displayDate` | null |
| `price` | integer |
| `priceCurrency` | string |
| `priceDisplay` | string |
| `priceNegotiable` | boolean |
| `offerType` | string |
| `categoryId` | string |
| `categoryName` | string |
| `categoryPath` | null |
| `city` | string |
| `region` | string |
| `district` | null |
| `fullLocation` | string |
| `latitude` | float |
| `longitude` | float |
| `mapZoom` | integer |
| `mapShowDetailed` | boolean |
| `sellerId` | string |
| `sellerUuid` | string |
| `sellerName` | string |
| `sellerType` | string |
| `sellerTag` | null |
| `sellerLogo` | null |
| `sellerCreatedAt` | string |
| `sellerLastLogin` | null |
| `sellerOtherAdsEnabled` | boolean |
| `kycVerified` | null |
| `businessFlag` | boolean |
| `partnerCode` | null |
| `shopId` | null |
| `hasPhone` | boolean |

---

[← All scrapers](../../README.md)
