# Castorama.fr Scraper

Scrape Castorama.fr DIY and home-improvement products by keyword, category, or URL. Extract prices, original prices, promotions, seller details, categories, specifications, ratings, and customer reviews. Incremental mode tracks product and price changes over time.

**[Open Castorama.fr Scraper on Apify](https://apify.com/abotapi/castorama-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~castorama-fr-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["perceuse"], "minRating": "0", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords or category links |
| `brand` | string | Brand |
| `sellerCastoramaOnly` | boolean | Only sold directly by Castorama |
| `minPrice` | integer | Minimum price (EUR) |
| `maxPrice` | integer | Maximum price (EUR) |
| `minRating` | string | Minimum average rating |
| `urls` | array | Castorama France links |
| `onPromotionOnly` | boolean | Only products on promotion |
| `inStockOnly` | boolean | Only purchasable products |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per keyword / category / lin |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/castorama-fr-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `ean` | string |
| `title` | string |
| `brand` | string |
| `price` | float |
| `currency` | string |
| `originalPrice` | float |
| `discountAmount` | integer |
| `discountPercentage` | integer |
| `isOnSpecial` | boolean |
| `promotionLabel` | string |
| `sellerId` | string |
| `sellerName` | string |
| `soldByCastorama` | boolean |
| `categoryPath` | list |
| `category` | string |
| `categoryNames` | list |
| `availability` | object |
| `images` | list |
| `url` | string |
| `image` | string |
| `specifications` | list |
| `description` | string |
| `manufacturerRaw` | object |
| `offersRaw` | list |
| `searchMode` | string |
| `scrapedAt` | string |
| `rating` | float |
| `reviewCount` | integer |
| `reviews` | list |

---

[← All scrapers](../../README.md)
