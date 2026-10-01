# Too Good To Go Scraper

Scrape Too Good To Go (TGTG) stores and surprise bags by location or item: price, value, savings, quantity, pickup windows, ratings, favorites and store details. Availability monitoring (NEW, UPDATED, REAPPEARED, EXPIRED), detail enrichment, incremental runs, MCP export.

**[Open Too Good To Go Scraper on Apify](https://apify.com/abotapi/toogoodtogo-surprise-bag-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~toogoodtogo-surprise-bag-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Berlin"], "itemInputs": ["123456789"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `radiusKm` | integer | Radius (km) |
| `dietCategories` | array | Diet categories |
| `searchPhrase` | string | Search phrase (optional) |
| `withStockOnly` | boolean | Only bags in stock |
| `weCareOnly` | boolean | Only We Care partners |
| `favoritesOnly` | boolean | Only account favorites |
| `itemInputs` | array | Item links or ids |
| `accessToken` | string | Access token (paste) |
| `refreshToken` | string | Refresh token (paste) |
| `sessionCookie` | string | Session cookie header (optional paste) |
| `email` | string | Account email (login in-run) |
| `loginPollingId` | string | Polling id (two-phase login, optional) |
| `loginPin` | string | Login PIN (two-phase login, optional) |
| `allowAutoSignup` | boolean | Prepare access automatically |
| `fetchDetails` | boolean | Detail enrichment |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per location |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/toogoodtogo-surprise-bag-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `itemId` | string |
| `url` | string |
| `title` | string |
| `itemName` | string |
| `subtitle` | string |
| `description` | string |
| `itemType` | string |
| `category` | string |
| `price` | float |
| `currency` | string |
| `value` | integer |
| `valueCurrency` | string |
| `savingsPercent` | float |
| `quantityAvailable` | integer |
| `maxPerOrder` | null |
| `pickupStart` | null |
| `pickupEnd` | null |
| `soldOutAt` | null |
| `purchaseEnd` | null |
| `lastItemAt` | null |
| `favoriteCount` | integer |
| `favorite` | boolean |
| `ratingAverage` | null |
| `ratingCount` | null |
| `dietTags` | list |
| `itemTags` | list |
| `packagingOption` | string |
| `canUserSupplyPackaging` | boolean |
| `imageUrl` | string |
| `inSalesWindow` | boolean |
| `distanceKm` | float |
| `storeId` | string |
| `storeName` | string |
| `branch` | string |
| `cuisines` | list |
| `street` | string |
| `city` | string |
| `postalCode` | string |
| `country` | string |

---

[← All scrapers](../../README.md)
