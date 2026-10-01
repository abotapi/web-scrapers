# Reverb Music Gear and Sold Price Guide Scraper

Scrape reverb.com music gear: guitars, amps, synths, pedals, drums and pro audio. Search live listings by brand, category, condition, price, year, region and shipping, or paste links. Uniquely returns the sold Price Guide per gear model: median, low, high and quartile realised prices.

**[Open Reverb Music Gear and Sold Price Guide Scraper on Apify](https://apify.com/abotapi/reverb-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~reverb-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["Fender Stratocaster"], "sortBy": "relevance", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `urls` | array | Reverb links or listing ids |
| `make` | string | Brand |
| `category` | string | Category |
| `minYear` | integer | Earliest year |
| `maxYear` | integer | Latest year |
| `conditions` | array | Condition (search mode) |
| `minPrice` | integer | Minimum price (USD, search mode) |
| `maxPrice` | integer | Maximum price (USD, search mode) |
| `itemRegion` | string | Seller country (search mode) |
| `shipsTo` | string | Ships to (search mode) |
| `shopSlug` | string | Shop (search mode) |
| `handmadeOnly` | boolean | Handmade only (search mode) |
| `freeShippingOnly` | boolean | Free shipping only (search mode) |
| `preferredSellersOnly` | boolean | Preferred sellers only (search mode) |
| `sortBy` | string | Sort by (search mode) |
| `includeSoldPriceGuide` | boolean | Include the sold Price Guide |
| `fetchDetails` | boolean | Read each listing's own item page |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max pages per keyword or link |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/reverb-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `listingId` | string |
| `sku` | string |
| `slug` | string |
| `url` | string |
| `comparisonShoppingPageId` | string |
| `priceGuideId` | null |
| `title` | string |
| `make` | string |
| `brandSlug` | string |
| `model` | string |
| `year` | string |
| `finish` | string |
| `categories` | list |
| `categoryUuids` | list |
| `rootCategory` | string |
| `description` | string |
| `descriptionHtml` | string |
| `upc` | string |
| `handmade` | null |
| `originCountryCode` | string |
| `videos` | list |
| `condition` | string |
| `conditionSlug` | string |
| `conditionUuid` | string |
| `price` | float |
| `priceCents` | integer |
| `currency` | string |
| `priceDisplay` | string |
| `taxIncluded` | boolean |
| `buyerPrice` | float |
| `buyerPriceCurrency` | string |
| `listingCurrency` | string |
| `originalPrice` | null |
| `priceDropPercent` | null |
| `state` | string |
| `isLive` | boolean |
| `inventory` | integer |
| `hasInventory` | boolean |
| `offersEnabled` | boolean |

---

[← All scrapers](../../README.md)
