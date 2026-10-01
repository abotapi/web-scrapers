# BIG W Marketplace Scraper

Scrape BIG W Marketplace seller listings from bigw.com.au: name, brand, price, was-price, saving, condition, category, images, specs, GTIN/EAN/MPN, rating and customer reviews. Search by keyword with brand, category, price and rating filters, or paste product / search URLs.

**[Open BIG W Marketplace Scraper on Apify](https://apify.com/abotapi/bigw-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bigw-marketplace-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["piano keyboard"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | BIG W URLs |
| `marketplaceOnly` | boolean | Marketplace sellers only |
| `brand` | string | Brand |
| `category` | string | Category id |
| `specialsCategory` | string | Specials / offers |
| `deal` | string | Deal type (advanced) |
| `sortBy` | string | Sort by |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `minRating` | integer | Minimum rating |
| `includeOutOfStock` | boolean | Include out-of-stock products |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bigw-marketplace-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `articleId` | string |
| `gtin` | null |
| `ean` | string |
| `mpn` | string |
| `barcodes` | list |
| `name` | string |
| `title` | string |
| `brand` | string |
| `sellerType` | string |
| `sellerName` | string |
| `productChannel` | string |
| `isMarketplace` | boolean |
| `condition` | string |
| `listingStatus` | string |
| `url` | string |
| `price` | integer |
| `wasPrice` | float |
| `rrp` | null |
| `saving` | float |
| `savingsPercent` | integer |
| `isOnSpecial` | boolean |
| `unitPrice` | null |
| `currency` | string |
| `priceLabel` | string |
| `priceLabelType` | string |
| `clearance` | boolean |
| `onlineOnlyPromotion` | boolean |
| `promotions` | list |
| `paymentOptions` | object |
| `rating` | null |
| `description` | string |
| `imageUrl` | string |
| `images` | list |
| `category` | string |
| `categories` | list |
| `categoryPath` | string |
| `variants` | null |
| `colours` | null |
| `sizes` | null |
| `specifications` | object |

---

[← All scrapers](../../README.md)
