# MUJI Scraper

Scrape MUJI products from the United States, Canada and Australia storefronts. Search by keyword or paste product, category and search links. Returns price, was-price and discount, per-variant stock, sizes, colours, media, materials and customer reviews, plus Incremental mode for change monitoring.

**[Open MUJI Scraper on Apify](https://apify.com/abotapi/muji-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~muji-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["aroma diffuser"], "country": "us", "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | MUJI links |
| `country` | string | Country storefront |
| `category` | string | Category |
| `color` | string | Colour |
| `size` | string | Size |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `inStockOnly` | boolean | Only products in stock |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per keyword or link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/muji-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `productGid` | string |
| `handle` | string |
| `title` | string |
| `url` | string |
| `country` | string |
| `countryName` | string |
| `currency` | string |
| `brand` | string |
| `category` | string |
| `productCategory` | null |
| `department` | null |
| `breadcrumb` | list |
| `collections` | list |
| `tags` | list |
| `price` | integer |
| `priceMax` | integer |
| `originalPrice` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `onSale` | boolean |
| `availableForSale` | boolean |
| `inStock` | boolean |
| `variantCount` | integer |
| `inStockVariantCount` | integer |
| `sizes` | list |
| `colors` | list |
| `options` | list |
| `variants` | list |
| `sku` | string |
| `featuredImage` | string |
| `images` | list |
| `thumbnails` | list |
| `videos` | list |
| `requiresShipping` | boolean |
| `shippingWeight` | integer |
| `shippingWeightUnit` | string |
| `rating` | float |
| `reviewCount` | integer |
| `ratingBreakdown` | null |

---

[← All scrapers](../../README.md)
