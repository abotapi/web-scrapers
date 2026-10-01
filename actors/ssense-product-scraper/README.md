# SSENSE Scraper

Scrape SSENSE by keyword, category, designer or URL. Every row carries the selling price and the regular price, the discount percent, stock state and images. Sale axes, designer pages and recurring change tracking are first-class.

**[Open SSENSE Scraper on Apify](https://apify.com/abotapi/ssense-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ssense-product-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["sneakers"], "gender": "men", "sortResultsBy": "site_order", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | SSENSE URLs |
| `gender` | string | Section |
| `category` | string | Category |
| `designerSlugs` | array | Designers |
| `saleOnly` | boolean | Sale only |
| `minPriceUsd` | integer | Minimum price (USD) |
| `maxPriceUsd` | integer | Maximum price (USD) |
| `onSaleOnly` | boolean | Discounted rows only |
| `sortResultsBy` | string | Order the returned rows by |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ssense-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `rowType` | string |
| `productId` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `brandId` | string |
| `sku` | string |
| `gender` | string |
| `categoryIds` | list |
| `price` | integer |
| `regularPrice` | integer |
| `onSale` | boolean |
| `discountPercent` | null |
| `currency` | string |
| `inStock` | boolean |
| `imageUrl` | string |
| `description` | string |
| `category` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
