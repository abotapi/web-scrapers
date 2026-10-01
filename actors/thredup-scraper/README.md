# ThredUp Scraper

Scrape ThredUp resale listings by keyword, department, brand, size, condition, price or URL. Extract 35+ fields including brand, price, original price, MSRP, size, colours, materials, condition, category and all photos. Supports filters and sorting.

**[Open ThredUp Scraper on Apify](https://apify.com/abotapi/thredup-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~thredup-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQueries": ["nike dress"], "department": "women", "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQueries` | array | Search keywords |
| `department` | string | Department |
| `categories` | array | Categories |
| `brands` | array | Brands |
| `materials` | array | Materials |
| `styles` | array | Style tags |
| `condition` | array | Condition tags |
| `clearanceOnly` | boolean | Clearance items only |
| `priceMin` | integer | Minimum price (USD) |
| `priceMax` | integer | Maximum price (USD) |
| `sortBy` | string | Sort by |
| `urls` | array | ThredUp URLs |
| `fetchDetails` | boolean | Fetch full details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per query |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/thredup-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `itemNumber` | integer |
| `sku` | null |
| `url` | string |
| `title` | string |
| `description` | string |
| `brand` | string |
| `brandId` | integer |
| `brandStyleName` | null |
| `price` | float |
| `originalPrice` | float |
| `msrp` | integer |
| `clearance` | boolean |
| `newWithTags` | boolean |
| `condition` | string |
| `sizeDisplay` | string |
| `department` | string |
| `merchandisingDepartment` | string |
| `category` | string |
| `categoryTags` | list |
| `departmentTags` | list |
| `styleTags` | list |
| `colorNames` | list |
| `materials` | list |
| `availability` | string |
| `state` | string |
| `accessLevels` | list |
| `favoriteCount` | integer |
| `isP2P` | boolean |
| `clusterId` | null |
| `clusterItemCount` | null |
| `warehouseId` | integer |
| `supplierId` | integer |
| `photoIds` | list |
| `imageUrls` | list |
| `imageUrl` | string |
| `fullDescription` | null |
| `measurements` | null |
| `detailRaw` | null |

---

[← All scrapers](../../README.md)
