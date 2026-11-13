# Vinted France Scraper

Scrape Vinted.fr second-hand fashion listings by keyword, brand, price, condition, sort filters or URL. Extract titles, brands, prices, sizes, conditions, photos and seller ratings. Supports item and seller URLs, plus full seller feedback and review history.

**[Open Vinted France Scraper on Apify](https://apify.com/abotapi/vinted-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~vinted-fr-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["nike"], "sortBy": "relevance", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `categoryId` | string | Category (optional) |
| `brandId` | string | Brand (optional) |
| `conditions` | array | Condition (optional) |
| `brandIds` | array | Brands, several (optional) |
| `colorIds` | array | Colour ids (optional) |
| `sizeIds` | array | Size ids (optional) |
| `minPrice` | integer | Minimum price (EUR) |
| `maxPrice` | integer | Maximum price (EUR) |
| `sortBy` | string | Sort order |
| `urls` | array | URLs to scrape |
| `sellers` | array | Sellers |
| `fetchDetails` | boolean | Fetch item detail |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items total |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/vinted-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `itemId` | string |
| `title` | string |
| `url` | string |
| `path` | string |
| `brandTitle` | string |
| `priceAmount` | integer |
| `currency` | string |
| `isVisible` | null |
| `promoted` | boolean |
| `photos` | list |
| `photoCount` | integer |
| `image` | string |
| `favouriteCount` | integer |
| `viewCount` | null |
| `isClosed` | null |
| `isHeavyBulky` | null |
| `itemClosingAction` | null |
| `serviceFee` | float |
| `totalPrice` | float |
| `sellerId` | string |
| `sellerPhoto` | string |
| `isBusinessSeller` | boolean |
| `sellerUrl` | string |
| `seller` | object |
| `scrapedAt` | string |
| `description` | string |
| `mainImage` | string |
| `conditionSchema` | string |
| `categoryPath` | string |
| `category` | string |
| `colors` | list |
| `size` | string |
| `color` | string |
| `condition` | string |
| `catalogId` | string |
| `categoryId` | string |
| `isReserved` | boolean |
| `isHidden` | boolean |
| `instantBuy` | boolean |
| `canBuy` | boolean |

---

[← All scrapers](../../README.md)
