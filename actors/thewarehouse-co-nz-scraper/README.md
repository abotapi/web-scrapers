# The Warehouse NZ Scraper

Scrape The Warehouse New Zealand search results, category pages, and direct product URLs. Extract prices, availability, brand, images, breadcrumbs, attributes, product details, and optional customer reviews. Supports search mode, URL mode, sorting, pagination, and MCP connector export.

**[Open The Warehouse NZ Scraper on Apify](https://apify.com/abotapi/thewarehouse-co-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~thewarehouse-co-nz-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["toaster"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "NZ"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `specialsCategory` | string | Specials category |
| `sortBy` | string | Sort by |
| `urls` | array | The Warehouse URLs |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `includeUnavailable` | boolean | Include unavailable products |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per query / URL |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/thewarehouse-co-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `url` | string |
| `productId` | string |
| `sku` | string |
| `gtin` | null |
| `mpn` | string |
| `title` | string |
| `brand` | string |
| `description` | string |
| `category` | null |
| `breadcrumbs` | list |
| `price` | float |
| `priceMax` | float |
| `priceText` | string |
| `currency` | string |
| `availability` | string |
| `condition` | null |
| `image` | string |
| `images` | list |
| `imageCount` | integer |
| `ratingValue` | float |
| `ratingCount` | null |
| `reviewCount` | null |
| `categoryPath` | list |
| `marketplaceProduct` | boolean |
| `sellerName` | null |
| `reviews` | null |
| `attributes` | object |
| `rawProduct` | object |
| `isOnSpecial` | boolean |
| `offerEndsAt` | null |
| `specialsCategory` | null |
| `features` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
