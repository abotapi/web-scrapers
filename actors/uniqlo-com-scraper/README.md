# UNIQLO Scraper

Scrape UNIQLO products across 21 country storefronts in local currency. Price with pre discount original price, per size and colour stock, images, fabric and care, breadcrumbs, ratings and full reviews. Search by keyword, category and native filters, or paste product and category links.

**[Open UNIQLO Scraper on Apify](https://apify.com/abotapi/uniqlo-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~uniqlo-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "country": "us", "queries": ["shirt"], "sortBy": "recommended", "maxReviewsPerProduct": 10, "reviewsSort": "newest", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `country` | string | Country |
| `language` | string | Language (optional) |
| `queries` | array | Keywords |
| `categories` | array | Categories |
| `colors` | array | Colors |
| `sizes` | array | Sizes |
| `flags` | array | Promotions and product labels |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `sortBy` | string | Sort order |
| `urls` | array | Storefront links |
| `fetchDetails` | boolean | Fetch product details and variants |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `reviewsSort` | string | Review order |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/uniqlo-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `uniqueKey` | string |
| `productId` | string |
| `styleCode` | string |
| `name` | string |
| `url` | string |
| `country` | string |
| `countryName` | string |
| `language` | string |
| `department` | string |
| `genderCategory` | string |
| `sizeGender` | string |
| `price` | float |
| `basePrice` | float |
| `promoPrice` | null |
| `originalPrice` | null |
| `discountAmount` | null |
| `discountPercent` | null |
| `isOnSale` | boolean |
| `currency` | string |
| `currencySymbol` | string |
| `taxPolicy` | string |
| `isDualPrice` | boolean |
| `priceGroup` | string |
| `promotionText` | null |
| `rating` | integer |
| `reviewCount` | integer |
| `ratingBreakdown` | null |
| `fitRating` | null |
| `colors` | list |
| `colorCount` | integer |
| `sizes` | list |
| `sizeCount` | integer |
| `images` | list |
| `mainImage` | string |
| `subImages` | list |
| `flags` | list |
| `flagCodes` | list |
| `isNew` | boolean |
| `isNewColor` | boolean |

---

[← All scrapers](../../README.md)
