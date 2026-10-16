# Showpo Scraper

Scrape Showpo women's fashion by keyword, collection or URL. Extract product prices, colors, sizes, stock availability, descriptions, images and customer reviews. Supports search filters, sorting and scheduled monitoring to track product, price and availability changes.

**[Open Showpo Scraper on Apify](https://apify.com/abotapi/showpo-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~showpo-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["dress"], "collections": ["dresses"], "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `searchTerms` | array | Keywords |
| `collections` | array | Collections |
| `urls` | array | Showpo links (any mix) |
| `fetchDetails` | boolean | Fetch product details |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/showpo-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `productId` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `color` | string |
| `attributes` | list |
| `price` | float |
| `listPrice` | float |
| `compareAtPrice` | null |
| `onSale` | boolean |
| `discountPercent` | integer |
| `currency` | string |
| `availableForSale` | boolean |
| `inventoryLevel` | integer |
| `gtin` | null |
| `condition` | null |
| `categories` | list |
| `description` | string |
| `imageUrl` | string |
| `imageUrls` | list |
| `ratingValue` | float |
| `reviewCount` | integer |
| `sizesAvailable` | list |
| `sizesUnavailable` | list |
| `descriptionHtml` | string |
| `subTitle` | string |
| `styleName` | string |
| `seoTitle` | null |
| `seoDescription` | null |
| `canonicalUrl` | null |
| `collections` | list |
| `options` | list |
| `variants` | list |
| `swatches` | list |
| `colorways` | list |
| `tags` | list |
| `sizingGuide` | null |
| `restockLabel` | null |
| `sizeInformation` | string |

---

[← All scrapers](../../README.md)
