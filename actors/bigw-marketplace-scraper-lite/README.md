# BIG W Marketplace Scraper Lite

Scrape BIG W products & specials from bigw.com.au: name, title, brand, seller, price, was/original price, discount %, offer label, unit price, images, specs, GTIN/EAN, variants, rating & reviews. Filter by specials (on-special, clearance, flash deals), keyword, category & price, or paste URLs.

**[Open BIG W Marketplace Scraper Lite on Apify](https://apify.com/abotapi/bigw-marketplace-scraper-lite?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~bigw-marketplace-scraper-lite/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["piano keyboard"], "sortBy": "relevance", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}, "changeScope": "all"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | BIG W URLs |
| `marketplaceOnly` | boolean | Marketplace sellers only |
| `soldBy` | string | Sold by |
| `fulfilment` | string | Collection |
| `brand` | string | Brand |
| `category` | string | Category (name or id) |
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
| `deliveryPostcode` | string | Delivery postcode |
| `verifyHomeDelivery` | boolean | Verify home delivery |
| `proxy` | object | Proxy configuration |
| `allowBackupConnection` | boolean | Allow the backup connection for delive |
| `changeScope` | string | What counts as a change (incremental m |
| `compactUpdates` | boolean | Compact update rows (incremental mode  |
| `expireAfterMissedScans` | integer | Expire after N missed full scans (incr |
| `baselineDatasetId` | string | Start from an existing dataset (option |
| `earlierHistoryStoreId` | string | Continue from the BIG W Marketplace Sc |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/bigw-marketplace-scraper-lite?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `articleId` | string |
| `gtin` | string |
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
| `price` | float |
| `wasPrice` | null |
| `rrp` | null |
| `saving` | null |
| `savingsPercent` | null |
| `isOnSpecial` | boolean |
| `unitPrice` | null |
| `pricePerUnitPrice` | null |
| `pricePerUnitQuantity` | null |
| `pricePerUnitUnit` | null |
| `currency` | string |
| `priceLabel` | null |
| `priceLabelType` | null |
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

---

[← All scrapers](../../README.md)
