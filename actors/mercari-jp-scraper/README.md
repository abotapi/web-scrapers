# Mercari Japan Scraper

Scrape Mercari Japan listings, sellers and reviews at scale. Extract names, prices, conditions, photos, shipping details, descriptions and seller profiles. Search by keyword with nine filters or paste Mercari URLs directly.

**[Open Mercari Japan Scraper on Apify](https://apify.com/abotapi/mercari-jp-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~mercari-jp-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["nintendo switch"], "status": "on_sale", "sortBy": "score-desc", "shippingPayer": "any", "reviewSubject": "seller", "reviewFame": ["good", "normal", "bad"], "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search Mode |
| `queries` | array | Search Keywords |
| `status` | string | Item Status |
| `sortBy` | string | Sort By |
| `minPrice` | integer | Min Price () |
| `maxPrice` | integer | Max Price () |
| `itemCondition` | array | Item Condition |
| `shippingPayer` | string | Shipping Paid By |
| `categoryIds` | array | Category IDs |
| `brandIds` | array | Brand IDs |
| `excludeKeyword` | string | Exclude Keyword |
| `urls` | array | Marketplace URLs |
| `sellerIds` | array | Seller IDs |
| `reviewSubject` | string | Review Subject |
| `reviewFame` | array | Review Rating Filter |
| `maxPages` | integer | Max Pages Per Search |
| `maxListings` | integer | Max Listings (Total) |
| `fetchDetails` | boolean | Fetch Item Details |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/mercari-jp-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `itemType` | string |
| `url` | string |
| `name` | string |
| `price` | integer |
| `currency` | string |
| `status` | string |
| `itemCondition` | string |
| `itemConditionId` | string |
| `categoryId` | string |
| `shippingMethodId` | string |
| `shippingPayer` | string |
| `shippingPayerId` | string |
| `thumbnail` | string |
| `thumbnails` | list |
| `photos` | list |
| `isLiked` | boolean |
| `isNoPrice` | boolean |
| `createdAtTs` | integer |
| `updatedAtTs` | integer |
| `createdAt` | string |
| `updatedAt` | string |
| `sellerId` | string |
| `shopName` | null |
| `itemBrandId` | null |
| `itemBrandName` | null |
| `description` | null |
| `metaTitle` | null |
| `metaSubtitle` | null |
| `numLikes` | null |
| `numComments` | null |
| `comments` | null |
| `hashtags` | null |
| `registeredPricesCount` | null |
| `itemConditionSubname` | null |
| `itemBrandSubName` | null |
| `categoryName` | null |
| `categoryParentId` | null |
| `categoryParentName` | null |
| `categoryRootId` | null |

---

[← All scrapers](../../README.md)
