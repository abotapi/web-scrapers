# Switch Scraper

Scrape Switch designer handbag and jewelry rental listings by keyword, filter or URL. Extract product names, brands, retail values, member purchase prices, Core or Select membership tiers, availability and product images.

**[Open Switch Scraper on Apify](https://apify.com/abotapi/joinswitch-rental-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~joinswitch-rental-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["chanel bag"], "tier": "any", "availability": "any", "sort": "recommended", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `brands` | array | Brands |
| `categories` | array | Categories |
| `occasions` | array | Occasions |
| `shop` | string | Collection (shop) |
| `tier` | string | Rental tier |
| `availability` | string | Availability |
| `sort` | string | Sort results by |
| `urls` | array | Switch URLs |
| `minRetailValue` | number | Minimum retail value (USD) |
| `maxRetailValue` | number | Maximum retail value (USD) |
| `fetchDetails` | boolean | Fetch piece details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/joinswitch-rental-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `slug` | string |
| `url` | string |
| `title` | string |
| `brand` | string |
| `brandSlug` | string |
| `brandId` | string |
| `retailValue` | integer |
| `memberPurchasePrice` | integer |
| `currency` | string |
| `tier` | string |
| `availability` | string |
| `isSoldOut` | boolean |
| `stockStatus` | integer |
| `isNew` | boolean |
| `isFeatured` | boolean |
| `selectPiece` | string |
| `favoritesCount` | integer |
| `notifyCount` | integer |
| `description` | string |
| `condition` | string |
| `authenticity` | string |
| `categoryId` | string |
| `occasionId` | string |
| `shopId` | string |
| `sku` | string |
| `dateAdded` | string |
| `updatedAt` | string |
| `inventoryUpdatedOn` | string |
| `lowestTierId` | integer |
| `imageUrl` | string |
| `imageUrlHover` | string |
| `imageUrls` | list |
| `imageCount` | integer |
| `recordId` | string |
| `category` | string |
| `occasion` | string |
| `shop` | string |
| `scrapedAt` | string |
| `metaTitle` | string |

---

[← All scrapers](../../README.md)
