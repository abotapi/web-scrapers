# Nuuly Scraper

Scrape Nuuly clothing rental products by category, brand or URL. Extract product names, brands, retail prices, rental availability, sizes, colors, fabric details, product images and member reviews.

**[Open Nuuly Scraper on Apify](https://apify.com/abotapi/nuuly-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~nuuly-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "browseSlugs": ["dresses"], "sort": "popular", "maxReviews": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `browseSlugs` | array | Categories or brands |
| `brands` | array | Filter by brand |
| `occasions` | string | Occasion |
| `length` | string | Length |
| `material` | string | Material |
| `silhouettes` | string | Silhouette |
| `color` | string | Color |
| `sort` | string | Sort |
| `inStock` | boolean | Available to rent only |
| `urls` | array | Catalog links |
| `fetchDetails` | boolean | Fetch product details |
| `maxReviews` | integer | Max reviews per product |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per listing |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/nuuly-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `url` | string |
| `productSlug` | string |
| `styleNumber` | string |
| `skuId` | null |
| `title` | string |
| `brand` | string |
| `vendorBrands` | list |
| `colorCode` | string |
| `colorName` | string |
| `retailPrice` | integer |
| `salePrice` | integer |
| `listPrice` | integer |
| `discountPercent` | null |
| `availableToRent` | boolean |
| `availabilityStatus` | string |
| `isVintage` | boolean |
| `previouslyRented` | null |
| `ratingAverage` | float |
| `ratingCount` | integer |
| `ratingHistogram` | object |
| `fitRatingAverage` | float |
| `sizeDisplayName` | null |
| `description` | string |
| `additionalDescription` | string |
| `fabricCare` | string |
| `modelNotes` | string |
| `colors` | list |
| `sizes` | list |
| `attributes` | list |
| `imageUrl` | string |
| `imageUrls` | list |
| `reviews` | list |
| `reviewsTotal` | integer |
| `scrapedAt` | string |
| `choiceId` | string |
| `merchandiseClass` | string |
| `brandSlug` | string |

---

[← All scrapers](../../README.md)
