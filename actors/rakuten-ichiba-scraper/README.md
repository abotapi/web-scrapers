# Rakuten Scraper

Scrape Rakuten Ichiba (rakuten.co.jp): name, JPY price, reference price and discount, Rakuten points, shipping, stock, shop, genre, tags, images, size/colour variants with per-variant price, specs, and customer reviews with star breakdown and shop replies. Search or paste URLs; incremental mode.

**[Open Rakuten Scraper on Apify](https://apify.com/abotapi/rakuten-ichiba-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~rakuten-ichiba-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["コーヒー"], "sortBy": "standard", "condition": "any", "maxItems": 10, "maxPages": 1, "maxReviewsPerItem": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `queries` | array | Search keywords |
| `genreIds` | array | Genre (category) IDs |
| `tagIds` | array | Tag IDs (brand and spec filters) |
| `shopUrlCodes` | array | Shop codes (whole catalogue) |
| `shopId` | integer | Restrict to one shop (numeric shop ID) |
| `sortBy` | string | Sort results by |
| `minPrice` | integer | Min price (JPY) |
| `maxPrice` | integer | Max price (JPY) |
| `minRating` | string | Minimum review rating |
| `condition` | string | Item condition |
| `urls` | array | Rakuten URLs |
| `maxItems` | integer | Max products (total) |
| `maxPages` | integer | Max result pages per search |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviewsPerItem` | integer | Max reviews per product |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/rakuten-ichiba-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `itemCode` | string |
| `itemUrl` | string |
| `url` | string |
| `variantId` | string |
| `name` | string |
| `subtitle` | null |
| `brand` | null |
| `productUrl` | null |
| `shopId` | string |
| `shopName` | string |
| `shopUrlCode` | string |
| `shopUrl` | string |
| `shopRating` | null |
| `shopReviewCount` | null |
| `shopIsExcellent` | boolean |
| `shopIs39` | boolean |
| `price` | integer |
| `currency` | string |
| `priceMin` | integer |
| `priceMax` | integer |
| `hasPriceRange` | boolean |
| `unitPriceDisplay` | string |
| `unitCount` | integer |
| `unitLabel` | string |
| `subscriptionPrice` | null |
| `originalPrice` | null |
| `originalPriceLabel` | null |
| `discountPercent` | null |
| `pointCount` | integer |
| `pointBaseMultiplier` | integer |
| `pointItemMultiplier` | null |
| `pointShopMultiplier` | null |
| `pointDealMultiplier` | null |
| `isSuperDeal` | boolean |
| `isSponsored` | boolean |
| `isSoldOut` | boolean |
| `availability` | string |
| `shippingFee` | integer |
| `isFreeShipping` | boolean |

---

[← All scrapers](../../README.md)
