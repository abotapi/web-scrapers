# StockX Scraper

Scrape StockX market data by keyword, category or URL. Every row carries lowest ask, highest bid, last sale, bid ask spread, ask counts, 72 hour and 90 day sales volume, 12 month average price, volatility and premium over retail. Pick a size and every row becomes that size's own order book.

**[Open StockX Scraper on Apify](https://apify.com/abotapi/stockx-market-data-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~stockx-market-data-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["air jordan 1"], "market": "US", "orderBy": "featured", "sortResultsBy": "site_order", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `urls` | array | StockX URLs |
| `category` | string | Category |
| `brands` | array | Brands |
| `models` | array | Models |
| `productLines` | array | Product lines |
| `gender` | string | Gender |
| `color` | string | Colour |
| `activity` | string | Activity |
| `shoeHeight` | string | Shoe height |
| `market` | string | Market and currency |
| `sizeScale` | string | Size scale (turns on per size rows) |
| `size` | string | Size (needs a size scale) |
| `minPriceUsd` | integer | Minimum lowest ask (USD) |
| `maxPriceUsd` | integer | Maximum lowest ask (USD) |
| `availableNow` | boolean | Available now only |
| `xpressShipOnly` | boolean | Xpress Ship only |
| `belowRetailOnly` | boolean | Below retail only |
| `minLastSaleUsd` | integer | Minimum last sale (USD) |
| `minSalesLast72Hours` | integer | Minimum sales in the last 72 hours |
| `hasLiveAskOnly` | boolean | Has a live ask |
| `hasLiveBidOnly` | boolean | Has a live bid |
| `orderBy` | string | Ask StockX to order results by |
| `sortResultsBy` | string | Order the returned rows by |
| `fetchDetails` | boolean | Fetch full product details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per source |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/stockx-market-data-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `productId` | string |
| `urlKey` | string |
| `url` | string |
| `title` | string |
| `shortName` | string |
| `model` | string |
| `brand` | string |
| `primaryCategory` | string |
| `productCategory` | string |
| `browseVerticals` | list |
| `categoryPath` | list |
| `gender` | string |
| `condition` | string |
| `listingType` | string |
| `releaseDate` | string |
| `description` | string |
| `imageUrl` | string |
| `thumbnailUrl` | string |
| `rowType` | string |
| `variantId` | null |
| `size` | null |
| `sizeType` | string |
| `sizeConversions` | list |
| `requestedSize` | null |
| `variantCount` | integer |
| `lowestAsk` | integer |
| `lowestAskUpdatedAt` | string |
| `highestBid` | integer |
| `highestBidUpdatedAt` | string |
| `lastSale` | integer |
| `bidAskSpread` | integer |
| `salesLast72Hours` | integer |
| `salesLast90Days` | integer |
| `averagePriceLast90Days` | integer |
| `salesLast12Months` | integer |
| `averagePriceLast12Months` | integer |
| `priceVolatility` | integer |
| `pricePremium` | float |
| `standardAskCount` | integer |
| `standardLowestAsk` | integer |

---

[← All scrapers](../../README.md)
