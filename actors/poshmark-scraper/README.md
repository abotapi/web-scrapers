# Poshmark Scraper

Scrape Poshmark fashion-resale listings: keyword search, brand and category browse, sold listings with sold dates, seller closet stats (followers, following). Filters for department, condition and availability. Incremental monitoring, resume, MCP export.

**[Open Poshmark Scraper on Apify](https://apify.com/abotapi/poshmark-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~poshmark-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQueries": ["tote bag"], "availability": "available", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQueries` | array | Keyword searches |
| `brands` | array | Brands |
| `closets` | array | Seller closets |
| `availability` | string | Availability |
| `department` | string | Department |
| `condition` | string | Condition |
| `listingInputs` | array | Links |
| `urls` | array | Links (alias) |
| `fetchDetails` | boolean | Detail enrichment |
| `maxItems` | integer | Max items |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/poshmark-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `kind` | string |
| `recordId` | string |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `brandPath` | string |
| `size` | string |
| `sizeDisplay` | string |
| `condition` | string |
| `conditionLabel` | string |
| `price` | integer |
| `originalPrice` | integer |
| `currency` | string |
| `availability` | string |
| `soldAt` | null |
| `soldQuantity` | null |
| `listedAt` | string |
| `createdAt` | string |
| `updatedAt` | string |
| `statusChangedAt` | string |
| `department` | string |
| `category` | string |
| `subcategory` | string |
| `colors` | list |
| `styleTags` | list |
| `description` | string |
| `likeCount` | integer |
| `commentCount` | integer |
| `shareCount` | integer |
| `offerCount` | integer |
| `sellerUsername` | string |
| `sellerName` | string |
| `sellerUrl` | string |
| `coverImageUrl` | string |
| `pictureUrls` | list |
| `poshPassEligible` | boolean |

---

[← All scrapers](../../README.md)
