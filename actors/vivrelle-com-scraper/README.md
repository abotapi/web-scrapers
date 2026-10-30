# Vivrelle Scraper

Scrape Vivrelle luxury handbag and jewelry rentals by keyword, filter or URL. Extract product names, brands, membership tiers, retail values, monthly rental prices by tier, availability and full image galleries.

**[Open Vivrelle Scraper on Apify](https://apify.com/abotapi/vivrelle-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~vivrelle-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["chanel flap"], "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `collection` | string | Collection |
| `categories` | array | Item types |
| `brands` | array | Brands |
| `colors` | array | Colors |
| `occasions` | array | Occasions and edits |
| `materials` | array | Materials |
| `tiers` | array | Membership tiers |
| `newArrivals` | boolean | New arrivals only |
| `minRetailValue` | number | Minimum retail value (USD) |
| `maxRetailValue` | number | Maximum retail value (USD) |
| `urls` | array | Vivrelle URLs |
| `fetchDetails` | boolean | Fetch item details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/vivrelle-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `url` | string |
| `slug` | string |
| `sku` | string |
| `itemId` | string |
| `productId` | string |
| `title` | string |
| `brand` | string |
| `category` | string |
| `collectionType` | string |
| `itemType` | string |
| `categoryTrail` | list |
| `tier` | string |
| `retailValue` | integer |
| `retailValueText` | string |
| `monthlyPrice` | integer |
| `monthlyPriceCurrency` | string |
| `tierPrices` | object |
| `borrowed` | boolean |
| `availability` | string |
| `colors` | list |
| `description` | string |
| `sizeAndMeasurements` | string |
| `conditionNotes` | string |
| `imageUrl` | string |
| `hoverImageUrl` | string |
| `imageUrls` | list |
| `imageCount` | integer |
| `isPrivee` | boolean |
| `raw` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
