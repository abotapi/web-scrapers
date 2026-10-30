# Woolworths AU Scraper

Scrape Woolworths Australia (woolworths.com.au) grocery products and reviews. Search by keyword or paste product / search links. Returns name, brand, price, was price, unit price, pack size, specials, availability, images, category, nutrition, allergens, ingredients, rating and customer reviews.

**[Open Woolworths AU Scraper on Apify](https://apify.com/abotapi/woolworths-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~woolworths-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["milk"], "sortBy": "relevance", "minRating": "0", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `specialsCategory` | string | Specials & offers category |
| `urls` | array | Woolworths Australia URLs / product co |
| `sortBy` | string | Sort by |
| `minRating` | string | Minimum average rating |
| `specialsOnly` | boolean | Only products on special |
| `excludeSpecialsCategories` | array | Exclude specials categories |
| `excludeCategories` | array | Skip these departments |
| `includeMarketplace` | boolean | Include marketplace (Everyday Market)  |
| `minPrice` | integer | Minimum price (AUD) |
| `maxPrice` | integer | Maximum price (AUD) |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/woolworths-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `stockcode` | string |
| `name` | string |
| `displayName` | string |
| `title` | string |
| `brand` | string |
| `url` | string |
| `price` | float |
| `isOnSpecial` | boolean |
| `isHalfPrice` | boolean |
| `isEdrSpecial` | boolean |
| `cupPrice` | float |
| `cupMeasure` | string |
| `cupString` | string |
| `packageSize` | string |
| `unit` | string |
| `currency` | string |
| `barcode` | string |
| `gtinFormat` | integer |
| `isAvailable` | boolean |
| `isInStock` | boolean |
| `isNew` | boolean |
| `isOnlineOnly` | boolean |
| `ageRestricted` | boolean |
| `isTobacco` | boolean |
| `departments` | list |
| `departmentIds` | list |
| `departmentNames` | list |
| `productLimit` | integer |
| `isMarketProduct` | boolean |
| `variety` | string |
| `sponsored` | boolean |
| `image` | string |
| `thumbnailImage` | string |
| `description` | string |
| `promoLabel` | string |
| `inStorePrice` | float |
| `inStoreIsOnSpecial` | boolean |
| `inStoreCupPrice` | float |
| `inStoreCupString` | string |
| `richDescription` | string |

---

[← All scrapers](../../README.md)
