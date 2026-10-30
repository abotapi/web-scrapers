# Vestiaire Collective Scraper

Scrape Vestiaire Collective, the luxury resale marketplace: listings with prices in 7 markets, full product details with seller statistics, sold-item comparables, sale campaigns and the journal news feed. Search, URL and journal modes with sorting, filters and scheduled change tracking.

**[Open Vestiaire Collective Scraper on Apify](https://apify.com/abotapi/vestiaire-collective-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~vestiaire-collective-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["chanel bag"], "market": "AU", "sort": "relevance", "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `searchTerms` | array | Keywords |
| `urls` | array | Vestiaire Collective links (any mix) |
| `journalCategories` | array | Journal categories (optional) |
| `market` | string | Market |
| `sort` | string | Sort |
| `soldOnly` | boolean | Sold listings only |
| `conditions` | array | Condition |
| `universes` | array | Department |
| `priceRanges` | array | Price ranges |
| `editorPicks` | array | Curator picks |
| `fetchDetails` | boolean | Fetch product details |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/vestiaire-collective-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordId` | string |
| `productId` | string |
| `kind` | string |
| `url` | string |
| `slug` | string |
| `title` | string |
| `brand` | string |
| `brandId` | integer |
| `description` | string |
| `currency` | string |
| `price` | integer |
| `priceCents` | integer |
| `wasPrice` | integer |
| `discountPercent` | integer |
| `colorName` | string |
| `colorNames` | list |
| `colors` | list |
| `model` | string |
| `modelId` | integer |
| `size` | null |
| `sizeStandard` | null |
| `likes` | integer |
| `sold` | boolean |
| `stock` | boolean |
| `shouldBeGone` | boolean |
| `localEligible` | boolean |
| `directShippingEligible` | boolean |
| `editorPicks` | list |
| `pictureUrls` | list |
| `imageUrl` | string |
| `imageCount` | integer |
| `sellerId` | integer |
| `sellerName` | string |
| `sellerIsOfficialStore` | boolean |
| `country` | string |
| `universeId` | integer |
| `createdAt` | string |
| `personalizationType` | string |
| `market` | string |
| `condition` | string |

---

[← All scrapers](../../README.md)
