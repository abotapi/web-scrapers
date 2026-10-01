# Coles AU Scraper

Scrape Coles.com.au grocery products and customer reviews. Search by keyword, browse categories, or use product/search URLs. Returns name, brand, price, was price, unit price, size, specials, availability, aisle/category, nutrition, allergens, ingredients, ratings, and reviews.

**[Open Coles AU Scraper on Apify](https://apify.com/abotapi/coles-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~coles-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"inputMode": "search", "mode": "search", "queries": ["milk"], "categories": ["dairy-eggs-fridge"], "sortBy": "relevance", "minRating": "0", "maxReviewsPerProduct": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `inputMode` | string | What do you want to scrape |
| `mode` | string | Legacy input mode |
| `queries` | array | Keywords (optional) |
| `categories` | array | Category slugs (optional) |
| `specialsCategory` | string | Specials / offers category |
| `urls` | array | Coles Australia URLs / product ids |
| `sortBy` | string | Sort by |
| `minRating` | string | Minimum average rating |
| `specialsOnly` | boolean | Only products on special |
| `excludeSpecialsCategories` | array | Exclude specials categories |
| `excludeCategories` | array | Skip these departments |
| `minPrice` | integer | Minimum price (AUD) |
| `maxPrice` | integer | Maximum price (AUD) |
| `fetchDetails` | boolean | Fetch product details |
| `fetchReviews` | boolean | Fetch customer reviews |
| `maxReviewsPerProduct` | integer | Max reviews per product |
| `maxItems` | integer | Max products |
| `maxPages` | integer | Max pages per search or category |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/coles-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `name` | string |
| `title` | string |
| `brand` | string |
| `description` | string |
| `size` | string |
| `url` | string |
| `price` | float |
| `isOnSpecial` | boolean |
| `comparablePrice` | string |
| `unitPrice` | float |
| `unitOfMeasure` | string |
| `unitMeasure` | string |
| `isWeighted` | boolean |
| `currency` | string |
| `isAvailable` | boolean |
| `availabilityType` | string |
| `availableQuantity` | integer |
| `retailLimit` | integer |
| `promotionalLimit` | integer |
| `ageRestricted` | boolean |
| `deliveryRestrictions` | list |
| `freshnessGuarantee` | string |
| `aisle` | string |
| `category` | string |
| `subCategory` | string |
| `departments` | list |
| `departmentIds` | list |
| `isOnlineOnly` | boolean |
| `department` | string |
| `productClass` | string |
| `image` | string |
| `variantCount` | integer |
| `sponsored` | boolean |
| `featured` | boolean |
| `longDescription` | string |
| `gtin` | string |
| `countryOfOrigin` | string |
| `countryOfOriginStatement` | string |
| `lastUpdated` | string |

---

[← All scrapers](../../README.md)
