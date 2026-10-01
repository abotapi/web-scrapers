# Next.co.uk Scraper

Scrape Next.co.uk: keyword search, category and product-listing walks, full product details (price, was-price, sizes, stock, composition, images). Monitoring (NEW, UPDATED), incremental runs, resume.

**[Open Next.co.uk Scraper on Apify](https://apify.com/abotapi/next-uk-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~next-uk-product-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQuery": "dresses", "links": ["https://www.next.co.uk/shop/gender-women-category-dresses", "https://www.next.co.uk/style/sv132147/y76826", "Y76826"], "sortBy": "relevance", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQuery` | string | Search query |
| `links` | array | Listing, style or product-ID entries |
| `sortBy` | string | Sort results by |
| `minPrice` | integer | Min price (GBP) |
| `maxPrice` | integer | Max price (GBP) |
| `onSaleOnly` | boolean | Reduced only |
| `fetchDetails` | boolean | Open each product for full detail |
| `maxItems` | integer | Max items |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/next-uk-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `id` | string |
| `title` | string |
| `url` | string |
| `price` | integer |
| `currency` | string |
| `wasPrice` | null |
| `priceMin` | integer |
| `priceMax` | integer |
| `sizes` | list |
| `outOfStockMarkers` | integer |
| `lowStock` | boolean |
| `images` | list |
| `composition` | string |
| `detailFetched` | boolean |
| `image` | string |

---

[← All scrapers](../../README.md)
