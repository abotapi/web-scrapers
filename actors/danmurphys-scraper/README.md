# Dan Murphy’s Scraper

Scrape Dan Murphy’s products by category, keyword, or specials. Extract 45+ fields, including regular, sale and member prices, case and unit pricing, stock, ratings, reviews, country, variety, and ABV. Incremental mode tracks changes.

**[Open Dan Murphy’s Scraper on Apify](https://apify.com/abotapi/danmurphys-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~danmurphys-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "department": "beer", "sortBy": "Relevance", "maxPages": 1, "maxProducts": 10, "proxyConfiguration": {"useApifyProxy": true}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `department` | string | Department |
| `subDepartment` | string | Sub-department (optional) |
| `searchTerm` | string | Keyword search (optional) |
| `brand` | string | Brand filter (optional) |
| `urls` | array | Category / product URLs |
| `specialsOnly` | boolean | Specials only |
| `memberOffersOnly` | boolean | Member offers only |
| `minPrice` | number | Minimum price (AUD) |
| `maxPrice` | number | Maximum price (AUD) |
| `country` | string | Country (optional) |
| `region` | string | Region (optional) |
| `style` | string | Style (optional) |
| `variety` | string | Variety / type (optional) |
| `sortBy` | string | Sort order |
| `fetchDetails` | boolean | Fetch product details (charged per pro |
| `maxPages` | integer | Max pages per scope (0  unlimited) |
| `maxProducts` | integer | Max products per scope (0  unlimited) |
| `proxyConfiguration` | object | Proxy configuration |
| `changeScope` | string | Change scope (incremental mode only) |
| `compactUpdates` | boolean | Compact UPDATED rows (incremental mode |
| `expireAfterMissedScans` | integer | Expire after N missed scans (increment |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/danmurphys-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `stockcode` | string |
| `name` | string |
| `url` | string |
| `description` | string |
| `brand` | string |
| `department` | string |
| `price` | integer |
| `wasPrice` | float |
| `isOnSpecial` | boolean |
| `isOnOffer` | boolean |
| `isMemberOffer` | boolean |
| `memberOfferLabel` | string |
| `promotionType` | string |
| `packMessage` | string |
| `casePrice` | float |
| `casePackMessage` | string |
| `singlePrice` | float |
| `inAnySixPrice` | float |
| `unit` | string |
| `packageSize` | string |
| `abv` | string |
| `standardDrinks` | string |
| `country` | string |
| `style` | string |
| `closure` | string |
| `size` | string |
| `award` | string |
| `rating` | integer |
| `reviewCount` | integer |
| `isNew` | boolean |
| `stockQty` | integer |
| `purchasable` | boolean |
| `deliveryOnly` | boolean |
| `sash` | string |
| `badges` | list |
| `imageUrl` | string |
| `imageLarge` | string |
| `scrapedAt` | string |
| `categoryUrl` | string |
| `changeType` | string |

---

[← All scrapers](../../README.md)
