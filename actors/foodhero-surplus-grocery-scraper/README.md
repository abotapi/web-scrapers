# FoodHero Scraper

Scrape FoodHero surplus grocery deals across Canada by area, store or offer ID. Extract products, brands, regular and discounted prices, savings, portions left, best-before dates and CO2 savings, plus store names, chains, addresses, coordinates and types.

**[Open FoodHero Scraper on Apify](https://apify.com/abotapi/foodhero-surplus-grocery-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~foodhero-surplus-grocery-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["45.5019,-73.5674"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Areas to search |
| `radiusKm` | integer | Radius (km) |
| `searchStoreName` | string | Store name contains |
| `includeSoldOutOffers` | boolean | Include sold-out deals |
| `enrichStoreDetails` | boolean | Add store phone, website and descripti |
| `urls` | array | Store or offer ids |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per area |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/foodhero-surplus-grocery-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `storeId` | string |
| `storeUrl` | string |
| `storeName` | string |
| `chainId` | string |
| `bannerId` | string |
| `storeTypeId` | string |
| `storeType` | string |
| `storeLogoUrl` | string |
| `address` | string |
| `street` | string |
| `city` | string |
| `state` | string |
| `postalCode` | string |
| `country` | string |
| `latitude` | float |
| `longitude` | float |
| `distanceKm` | float |
| `phone` | null |
| `website` | null |
| `timezone` | string |
| `productCount` | integer |
| `storeOfferCount` | integer |
| `offerId` | string |
| `url` | string |
| `productName` | string |
| `productBrand` | string |
| `productDescription` | string |
| `productSize` | string |
| `productImageUrl` | string |
| `departmentName` | string |
| `uniqueProductId` | string |
| `price` | float |
| `discountPrice` | float |
| `discountPercent` | integer |
| `currency` | string |
| `itemLeft` | integer |
| `isSoldOut` | boolean |
| `isLastCall` | boolean |
| `isFrozen` | boolean |

---

[← All scrapers](../../README.md)
