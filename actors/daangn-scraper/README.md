# Daangn Scraper

Scrape Daangn (당근) marketplace listings by keyword and region. Returns 35+ fields per item including price, status, condition, full image set, region, category and seller profile (nickname, score, reviews). Search and URL modes, category and on-sale filters, price range and sort.

**[Open Daangn Scraper on Apify](https://apify.com/abotapi/daangn-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~daangn-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchQueries": ["노트북"], "locations": ["366"], "sortBy": "recommended", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchQueries` | array | Search queries |
| `locations` | array | Regions (region ids) |
| `categoryId` | integer | Category id |
| `onlyOnSale` | boolean | Only items on sale |
| `priceMin` | integer | Minimum price (KRW) |
| `priceMax` | integer | Maximum price (KRW) |
| `sortBy` | string | Sort by |
| `urls` | array | Daangn URLs |
| `fetchDetails` | boolean | Fetch full details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per query |
| `proxy` | object | Proxy configuration |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/daangn-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `nodeId` | string |
| `url` | string |
| `title` | string |
| `content` | string |
| `description` | string |
| `status` | string |
| `listingType` | string |
| `price` | integer |
| `priceText` | string |
| `isFree` | boolean |
| `currency` | string |
| `countryCode` | string |
| `createdAt` | string |
| `postedAt` | string |
| `publishedAt` | string |
| `boostedAt` | string |
| `thumbnail` | string |
| `imageUrl` | string |
| `images` | list |
| `locationName` | null |
| `location` | string |
| `regionSlug` | null |
| `searchQuery` | string |
| `region` | object |
| `category` | object |
| `user` | object |
| `tradingLocation` | object |
| `sellerName` | string |
| `condition` | string |
| `chatRoomsCount` | integer |
| `watchesCount` | integer |
| `readsCount` | integer |
| `favoriteCount` | integer |
| `chatCount` | integer |
| `viewCount` | integer |
| `sellerScore` | float |
| `sellerReviewCount` | integer |
| `sellerProfileUrl` | string |
| `sellerProfileImage` | string |

---

[← All scrapers](../../README.md)
