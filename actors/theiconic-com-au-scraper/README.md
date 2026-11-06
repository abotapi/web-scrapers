# THE ICONIC Scraper

Scrape THE ICONIC (theiconic.com.au) fashion products: name, brand, price, sale price, sizes with stock and price per size, images, colour variants, category path, materials, care and customer reviews. Search by keyword, category or brand, or paste product, search and sale links.

**[Open THE ICONIC Scraper on Apify](https://apify.com/abotapi/theiconic-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~theiconic-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["t-shirt"], "sortBy": "popularity", "maxReviews": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search keywords |
| `categories` | array | Category pages |
| `brands` | array | Brand pages |
| `sortBy` | string | Sort by |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `gender` | string | Gender |
| `size` | string | Size |
| `colour` | string | Colour |
| `onSaleOnly` | boolean | On sale only |
| `urls` | array | Links |
| `fetchDetails` | boolean | Fetch full product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviews` | integer | Max reviews per product |
| `maxPages` | integer | Max pages per list |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy |
| `baselineDatasetId` | string | Start from an existing dataset (option |
| `changeScope` | string | What counts as a change (incremental m |
| `compactUpdates` | boolean | Compact update rows (incremental mode  |
| `expireAfterMissedScans` | integer | Expire after N missed full scans (incr |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/theiconic-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `product_id` | string |
| `sku` | string |
| `name` | string |
| `brand` | string |
| `url` | string |
| `price` | integer |
| `special_price` | integer |
| `final_price` | integer |
| `markdown_price` | integer |
| `currency` | string |
| `is_on_sale` | boolean |
| `price_range` | object |
| `image` | string |
| `images` | list |
| `thumbnails` | list |
| `color_name` | string |
| `color_hex` | string |
| `variants_count` | integer |
| `variants_details` | list |
| `variants_message` | string |
| `sizes` | list |
| `size_universal` | list |
| `size_code` | list |
| `size_stock_status` | list |
| `size_price` | list |
| `size_sku` | list |
| `size_details` | list |
| `dispatch_time` | string |
| `supplier` | string |
| `gender` | string |
| `department` | string |
| `category` | string |
| `subcategory` | string |
| `category_path` | string |
| `breadcrumbs` | list |
| `description` | string |
| `composition_material` | string |
| `fabric_material` | string |
| `measurements` | string |
| `care_label` | string |

---

[← All scrapers](../../README.md)
