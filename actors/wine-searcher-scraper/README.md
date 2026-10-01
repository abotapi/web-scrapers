# Wine-Searcher Scraper

Look up wines on wine-searcher.com by name, URL, or LWIN code. Returns 30+ fields, including critic scores, prices, grape, region, appellation, producer, label image, user ratings, food pairing, live offer counts, cheapest merchant offer, and optional critic review breakdown.

**[Open Wine-Searcher Scraper on Apify](https://apify.com/abotapi/wine-searcher-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~wine-searcher-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"inputType": "auto", "wineNames": ["Domaine Leflaive Puligny-Montrachet Les Pucelles 2020", "Petrus 2015"], "urls": ["https://www.wine-searcher.com/find/petrus/2015"], "lwins": ["11316442021", "11084042019", "1131644"], "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "FR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `inputType` * | string | Input type |
| `wineNames` | array | Wine names |
| `urls` | array | Wine-Searcher URLs |
| `lwins` | array | LWIN codes |
| `fetchOffers` | boolean | Fetch merchant offers and popularity |
| `fetchReviews` | boolean | Fetch critic reviews |
| `concurrency` | integer | Parallel lookups (no longer used) |
| `maxItems` | integer | Max wines |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/wine-searcher-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `inputValue` | string |
| `inputType` | string |
| `wineSearcherUrl` | string |
| `wineName` | string |
| `vintage` | integer |
| `appellation` | string |
| `region` | string |
| `origin` | string |
| `grapeVariety` | string |
| `producer` | string |
| `beverageType` | string |
| `style` | string |
| `description` | string |
| `labelImageUrl` | string |
| `score` | integer |
| `scoreBestRating` | integer |
| `criticReviewsCount` | integer |
| `criticReviews` | list |
| `avgPrice` | integer |
| `avgPriceCurrency` | string |
| `cheapestPriceAmount` | null |
| `cheapestPriceCurrency` | null |
| `cheapestPriceMerchant` | null |
| `cheapestPriceMerchantUrl` | null |
| `bottlesPerUnit` | null |
| `offers` | list |
| `offersCount` | integer |
| `highestPriceAmount` | null |
| `highestPriceCurrency` | null |
| `medianPriceAmount` | null |
| `merchantCount` | null |
| `wineryName` | string |
| `searchLocation` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
