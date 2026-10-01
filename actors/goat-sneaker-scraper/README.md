# GOAT Scraper

Scrape GOAT (goat.com), the sneaker and streetwear resale marketplace. Search or paste product, brand, collection and category URLs. 45+ fields per product: lowest ask, Instant Ship price, last sale and stock status for every size, retail, SKU, colorway, release date, images and story.

**[Open GOAT Scraper on Apify](https://apify.com/abotapi/goat-sneaker-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~goat-sneaker-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["air jordan 1"], "market": "US", "sortResultsBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | GOAT URLs |
| `brands` | array | Brands |
| `productCategory` | string | Product category |
| `activity` | string | Activity |
| `gender` | string | Gender |
| `condition` | string | Condition |
| `sizeUs` | string | US size |
| `minPriceUsd` | integer | Minimum price (USD) |
| `maxPriceUsd` | integer | Maximum price (USD) |
| `releaseYearFrom` | integer | Released from year |
| `releaseYearTo` | integer | Released up to year |
| `inStockOnly` | boolean | In stock only |
| `instantShipOnly` | boolean | Instant ship only |
| `underRetailOnly` | boolean | Under retail only |
| `market` | string | Ship-to market |
| `sortResultsBy` | string | Order results by |
| `fetchDetails` | boolean | Fetch full market data |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/goat-sneaker-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | integer |
| `slug` | string |
| `url` | string |
| `name` | string |
| `nickname` | string |
| `brand` | string |
| `sku` | string |
| `colorway` | string |
| `color` | string |
| `designer` | string |
| `silhouette` | string |
| `midsole` | string |
| `upperMaterial` | null |
| `productCategory` | string |
| `productType` | string |
| `activities` | list |
| `gender` | string |
| `genders` | list |
| `sizeUnit` | string |
| `sizeBrand` | string |
| `sizeRange` | list |
| `releaseDate` | string |
| `releaseYear` | integer |
| `releaseMonth` | integer |
| `season` | string |
| `retailPrice` | integer |
| `lowestAsk` | integer |
| `instantShipLowestAsk` | integer |
| `lowestAskSource` | string |
| `isUnderRetail` | boolean |
| `hasStock` | boolean |
| `status` | string |
| `isRaffleProduct` | boolean |
| `isFashionProduct` | boolean |
| `minimumOffer` | integer |
| `maximumOffer` | integer |
| `story` | string |
| `storyHtml` | string |
| `imageUrl` | string |
| `gridImageUrl` | string |

---

[← All scrapers](../../README.md)
