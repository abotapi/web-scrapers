# KREAM Korea Scraper

Scrape KREAM (kream.co.kr) sneaker and fashion resale data by keyword search, filters, sorts, or product URLs. Extract 34+ fields, including lowest ask, highest bid, market price, premium, retail price, style code, sizes, and optional price history.

**[Open KREAM Korea Scraper on Apify](https://apify.com/abotapi/kream-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~kream-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["nike"], "sort": "popularity", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keywords` | array | Keywords |
| `urls` | array | KREAM URLs |
| `sort` | string | Sort by |
| `quickDelivery` | boolean | Quick delivery only |
| `belowRetail` | boolean | Below retail only |
| `excludeSoldOut` | boolean | Exclude sold out |
| `category` | string | Category slug |
| `gender` | string | Gender |
| `fetchDetails` | boolean | Fetch full details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per keyword |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/kream-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | integer |
| `url` | string |
| `productName` | string |
| `productNameKo` | string |
| `brand` | string |
| `brandId` | integer |
| `category` | string |
| `categoryName` | string |
| `styleCode` | string |
| `colorway` | string |
| `gender` | string |
| `releaseDate` | null |
| `retailPrice` | integer |
| `retailPriceFormatted` | string |
| `currency` | string |
| `imageUrl` | string |
| `imageUrls` | list |
| `lowestAsk` | integer |
| `highestBid` | integer |
| `marketPrice` | integer |
| `lastSalePrice` | integer |
| `totalSales` | integer |
| `changeValue` | integer |
| `changePercentage` | integer |
| `premium` | integer |
| `premiumPercentage` | float |
| `hasImmediateDelivery` | boolean |
| `wishCount` | integer |
| `reviewCount` | integer |
| `haveCount` | integer |
| `isActive` | boolean |
| `isTradable` | boolean |
| `sizes` | list |
| `sizeOptions` | list |

---

[← All scrapers](../../README.md)
