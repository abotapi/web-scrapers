# Nitori Japan Furniture & Home Goods Scraper

Scrape Nitori Japan (nitori-net.jp) furniture and home goods by keyword, category or pasted link. Filter by category, brand, colour and price. Returns name, code, price, original price, images, variants, specifications, delivery and assembly terms and reviews. Incremental mode tracks daily changes.

**[Open Nitori Japan Furniture & Home Goods Scraper on Apify](https://apify.com/abotapi/nitori-net-jp-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~nitori-net-jp-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["ソファ"], "minRating": "0", "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | Store links or product codes |
| `categories` | array | Category |
| `brands` | array | Brand |
| `colors` | array | Colour |
| `minPrice` | integer | Minimum price (JPY) |
| `maxPrice` | integer | Maximum price (JPY) |
| `onSaleOnly` | boolean | Only reduced-price products |
| `inStockOnly` | boolean | Only products that can be ordered |
| `minRating` | string | Minimum average rating |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch product details |
| `includeReviews` | boolean | Include customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max result pages per keyword or link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/nitori-net-jp-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `name` | string |
| `summary` | string |
| `url` | string |
| `brand` | string |
| `brandCode` | string |
| `price` | integer |
| `priceFormatted` | string |
| `currency` | string |
| `priceMin` | integer |
| `priceMax` | integer |
| `onSale` | boolean |
| `isOutlet` | boolean |
| `taxExempt` | boolean |
| `rating` | float |
| `reviewCount` | integer |
| `image` | string |
| `images` | list |
| `colorSwatchImages` | list |
| `badges` | list |
| `breadcrumb` | list |
| `skuCode` | string |
| `variantName` | string |
| `originalPrice` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `discountDate` | null |
| `loyaltyPoints` | integer |
| `loyaltyPointsTotal` | integer |
| `categoryCode` | string |
| `categoryName` | string |
| `categoryUrl` | string |
| `description` | string |
| `shortDescription` | string |
| `catchCopy` | string |
| `specifications` | object |
| `dimensions` | string |
| `packingSize` | string |
| `weight` | string |
| `material` | string |

---

[← All scrapers](../../README.md)
