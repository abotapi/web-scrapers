# OfferUp Scraper

Scrape OfferUp listings by keyword, location and radius. Returns 40+ fields per item: price, condition, GPS, full photo set, category tree and rich seller profiles (rating, items sold, join date, verification). Search and URL modes, 5 sort orders, price and condition filters.

**[Open OfferUp Scraper on Apify](https://apify.com/abotapi/offerup-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~offerup-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQueries": ["iphone"], "location": "Miami, FL", "sortBy": "best_match", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQueries` | array | Search queries |
| `location` | string | Location (city, ZIP or 'lat,lon') |
| `radiusMiles` | integer | Search radius (miles) |
| `priceMin` | integer | Minimum price (USD) |
| `priceMax` | integer | Maximum price (USD) |
| `condition` | array | Condition |
| `priceDropOnly` | boolean | Price drops only |
| `sortBy` | string | Sort by |
| `urls` | array | OfferUp URLs |
| `fetchDetails` | boolean | Fetch full details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per query |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/offerup-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `price` | integer |
| `priceText` | string |
| `isFirmPrice` | null |
| `conditionText` | null |
| `locationName` | string |
| `flags` | list |
| `vehicleMiles` | null |
| `imageUrl` | string |
| `imageWidth` | integer |
| `imageHeight` | integer |
| `description` | null |
| `conditionCode` | null |
| `originalPrice` | null |
| `isOnSpecial` | null |
| `savingsAmount` | null |
| `discountPercent` | null |
| `quantity` | null |
| `postDate` | null |
| `latitude` | null |
| `longitude` | null |
| `distanceMiles` | null |
| `categoryL1Id` | null |
| `categoryL1Name` | null |
| `categoryL2Id` | null |
| `categoryL2Name` | null |
| `categoryL3Id` | null |
| `categoryL3Name` | null |
| `categoryName` | null |
| `photos` | null |
| `badges` | null |
| `discussionCount` | null |
| `isLocal` | null |
| `isMerchantItem` | null |
| `localPickupEnabled` | null |
| `shippingEnabled` | null |
| `canShipToBuyer` | null |
| `shippingPrice` | null |

---

[← All scrapers](../../README.md)
