# Costco Australia Scraper

Scrape Costco.com.au products by keyword or product, search and category URLs. Extract prices, brands, ratings, review counts and text, stock, images, specifications, promotions and full product details in clean structured data.

**[Open Costco Australia Scraper on Apify](https://apify.com/abotapi/costco-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~costco-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["laptop"], "sortBy": "relevance", "minRating": "0", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `sortBy` | string | Sort by |
| `specialsCategory` | string | Specials / offers |
| `brand` | string | Brand |
| `category` | string | Category code |
| `minRating` | string | Minimum average rating |
| `urls` | array | Costco Australia URLs |
| `minPrice` | integer | Minimum price (AUD) |
| `maxPrice` | integer | Maximum price (AUD) |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/costco-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `code` | string |
| `name` | string |
| `title` | string |
| `englishName` | string |
| `url` | string |
| `brand` | string |
| `price` | float |
| `priceFormatted` | string |
| `currency` | string |
| `priceMin` | null |
| `priceMax` | null |
| `priceRange` | null |
| `priceHidden` | boolean |
| `membershipRequired` | boolean |
| `averageRating` | float |
| `numberOfReviews` | integer |
| `summary` | null |
| `description` | string |
| `ingredients` | null |
| `warranty` | null |
| `returns` | string |
| `categories` | list |
| `breadcrumbs` | list |
| `specs` | list |
| `productType` | string |
| `promotions` | list |
| `images` | list |
| `stockStatus` | string |
| `stockLevel` | integer |
| `isProductAvailable` | boolean |
| `purchasable` | boolean |
| `availableForPickup` | boolean |
| `warehouseFulfilled` | boolean |
| `departmentNumber` | string |
| `maxOrderQuantity` | integer |
| `minOrderQuantity` | integer |
| `requiresAgeVerification` | boolean |
| `hasVariants` | boolean |
| `searchMode` | string |
| `wasPrice` | null |

---

[← All scrapers](../../README.md)
