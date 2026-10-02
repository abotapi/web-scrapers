# YesStyle Scraper

Scrape YesStyle products by keyword or URL. Extract prices, discounts, ratings, stock, images, categories, variants and customer reviews across K-beauty, fashion and lifestyle. Incremental mode tracks daily changes.

**[Open YesStyle Scraper on Apify](https://apify.com/abotapi/yesstyle-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~yesstyle-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["sheet mask"], "sortBy": "bestsellers", "reviewSort": "relevant", "reviewFilter": "all", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `queries` | array | Search keywords |
| `sortBy` | string | Sort keywords by |
| `urls` | array | YesStyle links |
| `minPrice` | string | Minimum price |
| `maxPrice` | string | Maximum price |
| `inStockOnly` | boolean | In stock only |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `reviewSort` | string | Review sort |
| `reviewFilter` | string | Review filter |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per listing |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/yesstyle-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `url` | string |
| `brand` | string |
| `name` | string |
| `price` | float |
| `currency` | string |
| `priceDisplay` | string |
| `originalPrice` | float |
| `discountPercent` | integer |
| `rating` | float |
| `imageUrl` | string |
| `badges` | list |
| `originCountry` | string |
| `brandId` | integer |
| `originalPriceDisplay` | string |
| `priceUsd` | float |
| `discountAmountUsd` | float |
| `reviewCount` | integer |
| `itemStatus` | string |
| `isNew` | boolean |
| `hasVideos` | boolean |
| `variant` | string |
| `variantProductIds` | list |
| `variantCount` | integer |
| `bestsellerRank` | integer |
| `promotions` | list |
| `sourceUrl` | string |
| `sourceQuery` | string |
| `searchRank` | integer |
| `productDescription` | string |
| `availability` | string |
| `condition` | string |
| `categories` | list |
| `categoryUrls` | list |
| `images` | list |
| `imageCount` | integer |
| `selectedOption` | string |
| `coverImageUrl` | string |
| `productDetails` | string |
| `productDetailSections` | object |

---

[← All scrapers](../../README.md)
