# Fruugo Scraper

Scrape Fruugo marketplace products by keyword or URL across country storefronts. Extract product names, prices, currencies, merchants, seller counts, GTIN/EAN product identifiers and images.

**[Open Fruugo Scraper on Apify](https://apify.com/abotapi/fruugo-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~fruugo-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["lego"], "country": "AU", "sort": "recommended", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | Fruugo URLs |
| `country` | string | Country storefront |
| `sort` | string | Sort results by |
| `minPrice` | number | Minimum price |
| `maxPrice` | number | Maximum price |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/fruugo-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `url` | string |
| `productId` | string |
| `skuId` | null |
| `fruugoId` | string |
| `title` | string |
| `brand` | string |
| `category` | string |
| `breadcrumbs` | string |
| `price` | float |
| `priceCurrency` | string |
| `priceText` | string |
| `listPrice` | float |
| `discountPercent` | null |
| `availability` | string |
| `inStock` | boolean |
| `merchantName` | string |
| `sellerCount` | null |
| `shippingPrice` | float |
| `shippingText` | string |
| `description` | string |
| `ean` | null |
| `gtin` | string |
| `sku` | string |
| `imageUrl` | string |
| `imageUrls` | list |
| `attributes` | list |
| `returnDays` | integer |
| `country` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
