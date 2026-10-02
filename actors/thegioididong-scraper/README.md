# Thegioididong Scraper

Scrape thegioididong.com products with full specifications, current & original price, discount, brand, category, variants, image gallery, description, customer rating and reviews. Search by keyword with brand, price, rating and sort filters, or paste product / category / search URLs.

**[Open Thegioididong Scraper on Apify](https://apify.com/abotapi/thegioididong-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~thegioididong-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["iphone 15"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "VN"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `specialsOnly` | boolean | Flash sale deals only |
| `urls` | array | Thế Giới Di Động URLs |
| `brand` | string | Brand |
| `sortBy` | string | Sort by |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `minRating` | integer | Minimum rating |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max listing pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/thegioididong-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `code` | string |
| `productCode` | string |
| `name` | string |
| `url` | string |
| `brand` | string |
| `category` | string |
| `color` | string |
| `price` | integer |
| `originalPrice` | integer |
| `discount` | string |
| `discountPercent` | integer |
| `savings` | integer |
| `isOnSpecial` | boolean |
| `promoGift` | null |
| `installmentOffer` | null |
| `currency` | string |
| `imageUrl` | string |
| `label` | null |
| `searchMode` | string |
| `source` | string |
| `description` | string |
| `rating` | integer |
| `reviewCount` | integer |
| `ratingBreakdown` | object |
| `sku` | string |
| `categoryPath` | list |
| `productId` | string |
| `images` | list |

---

[← All scrapers](../../README.md)
