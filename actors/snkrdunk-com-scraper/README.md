# SNKRDUNK Scraper

Scrape SNKRDUNK (snkrdunk.com), Japan's sneaker and streetwear resale marketplace: JP and EN names, brand, style code, JPY price stats, listing and offer counts, favourites, sizes, used prices, MSRP, sales history. Keyword search with brand or category filters, or paste product and sitemap URLs.

**[Open SNKRDUNK Scraper on Apify](https://apify.com/abotapi/snkrdunk-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~snkrdunk-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "keywords": ["air force 1"], "sortDirection": "desc", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "JP"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `keywords` | array | Keywords |
| `brandIds` | array | Brand IDs (optional) |
| `categoryIds` | array | Category IDs (optional) |
| `sortDirection` | string | Sort direction |
| `urls` | array | Product or sitemap URLs |
| `fetchDetails` | boolean | Fetch full product details |
| `fetchUsedPrices` | boolean | Fetch per-size used prices |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/snkrdunk-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `styleCode` | string |
| `name` | string |
| `url` | string |
| `image` | string |
| `price` | integer |
| `priceCurrency` | string |
| `priceCurrencySymbol` | string |
| `priceSuffix` | string |
| `condition` | string |
| `isNew` | boolean |
| `isUsed` | boolean |
| `isSold` | boolean |
| `productType` | string |
| `productTypeGB` | string |
| `productTypeJP` | string |
| `brand` | string |
| `category` | string |
| `displaySize` | string |
| `searchKeyword` | string |
| `searchRank` | integer |
| `scrapedAt` | string |
| `nameJa` | string |
| `nameLocal` | string |
| `brandName` | string |
| `brandNameLocal` | string |
| `modelId` | string |
| `modelName` | string |
| `modelNameLocal` | string |
| `productCatalogId` | string |
| `regularPriceJpy` | integer |
| `releaseDate` | string |
| `imageUrl` | string |
| `minSize` | string |
| `maxSize` | string |
| `availableSizes` | list |
| `availableSizeCount` | integer |
| `accessories` | string |
| `appraisalPoints` | list |
| `labels` | list |

---

[← All scrapers](../../README.md)
