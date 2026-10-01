# A101 Turkey Scraper

Scrape A101.com.tr products across A101 Ekstra and A101 Kapıda. Extract 80+ fields including prices, discounts, brands, barcodes, categories, images, stock, campaigns, promotions, variants, badges, origin, and descriptions. Supports search, URLs, filters, and sorting.

**[Open A101 Turkey Scraper on Apify](https://apify.com/abotapi/a101-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~a101-product-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["kahve"], "channel": "ekstra", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `queries` | array | Search queries |
| `channel` | string | Catalogue |
| `minPrice` | integer | Min price (TRY) |
| `maxPrice` | integer | Max price (TRY) |
| `brand` | string | Brand |
| `inStockOnly` | boolean | In-stock products only |
| `sortBy` | string | Sort order |
| `specialsCategory` | string | Specials / deals view |
| `urls` | array | A101 URLs |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max products |
| `fetchDetails` | boolean | Fetch details |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/a101-product-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `product_id` | string |
| `base_id` | string |
| `barcode` | string |
| `title` | string |
| `seo_name` | string |
| `url` | string |
| `country` | string |
| `brand` | string |
| `brand_id` | string |
| `brand_url` | string |
| `category` | string |
| `category_path` | string |
| `categories` | list |
| `currency` | string |
| `current_price` | integer |
| `original_price` | integer |
| `discounted_price` | integer |
| `current_price_text` | string |
| `original_price_text` | string |
| `discount_rate` | null |
| `discount_rate_text` | null |
| `is_on_special` | boolean |
| `savings_amount` | null |
| `savings_percent` | null |
| `promo_label` | null |
| `specials_category` | null |
| `price_range` | string |
| `in_stock` | boolean |
| `is_enabled` | boolean |
| `min_quantity` | integer |
| `max_quantity` | integer |
| `daily_max_quantity` | integer |
| `base_unit` | string |
| `vat_rate` | integer |
| `return_days` | integer |
| `channels` | list |
| `channel_names` | list |
| `channel_scope` | string |
| `origin_country_id` | string |
| `origin_country` | string |

---

[← All scrapers](../../README.md)
