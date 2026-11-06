# 2dehands & 2ememain Scraper

Scrape classifieds from 2dehands.be and 2ememain.be by keyword, filters, or URLs. Returns title, price, location, images, seller details, category, and full tag-based seller reviews. Supports sort, category, price filters, listing URLs, and search URLs.

**[Open 2dehands & 2ememain Scraper on Apify](https://apify.com/abotapi/2dehands-2ememain-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~2dehands-2ememain-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["bmw"], "domain": "2dehands.be", "sort": "optimized", "delivery": "any", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "BE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Mode |
| `queries` | array | Search keywords |
| `searchQuery` | string | Search keyword (alias) |
| `searchQueries` | array | Search keywords (alias list) |
| `listingIds` | array | Exact listing IDs |
| `startUrls` | array | Listing or search URLs |
| `domain` | string | Site |
| `minPrice` | integer | Minimum price (EUR) |
| `maxPrice` | integer | Maximum price (EUR) |
| `priceMinEur` | integer | Minimum price in EUR (alias) |
| `priceMaxEur` | integer | Maximum price in EUR (alias) |
| `sort` | string | Sort results |
| `sortBy` | string | Sort (alias) |
| `categoryId` | integer | Category ID (optional) |
| `postcode` | string | Belgian postcode |
| `radiusKm` | integer | Radius around the postcode (km) |
| `conditions` | array | Item condition |
| `delivery` | string | Delivery |
| `buyItNowOnly` | boolean | Fixed-price listings only |
| `postedAfter` | string | Posted on or after |
| `postedBefore` | string | Posted on or before |
| `fetchDetails` | boolean | Fetch full listing details |
| `scrapeDetails` | boolean | Fetch details (alias) |
| `includeReviews` | boolean | Include seller reviews |
| `maxReviews` | integer | Max reviews per listing |
| `maxItems` | integer | Max listings (the run cap) |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |
| `proxyConfiguration` | object | Proxy configuration (alias) |
| `onlyNewListings` | boolean | Only listings not seen before |
| `resetState` | boolean | Forget remembered listings first |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/2dehands-2ememain-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `sourceSite` | string |
| `itemId` | string |
| `id` | string |
| `listingId` | string |
| `title` | string |
| `description` | string |
| `categorySpecificDescription` | string |
| `thinContent` | boolean |
| `price` | integer |
| `priceCents` | integer |
| `priceType` | string |
| `city` | string |
| `countryName` | string |
| `countryAbbreviation` | null |
| `country` | string |
| `latitude` | float |
| `longitude` | float |
| `distanceMeters` | integer |
| `location` | string |
| `date` | string |
| `postedDate` | string |
| `postedAt` | string |
| `imageUrl` | string |
| `imageUrls` | list |
| `pictures` | list |
| `sellerId` | integer |
| `sellerName` | string |
| `sellerVerified` | boolean |
| `sellerWebsiteUrl` | boolean |
| `sellerInformation` | object |
| `categoryId` | integer |
| `priorityProduct` | string |
| `videoOnVip` | boolean |
| `urgencyFeatureActive` | boolean |
| `napAvailable` | boolean |
| `reserved` | boolean |
| `extendedAttributes` | list |
| `traits` | list |
| `verticals` | list |

---

[← All scrapers](../../README.md)
