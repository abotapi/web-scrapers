# Gumtree AU Scraper

Scrape gumtree.com.au classifieds across every vertical: for-sale goods, motors, real estate, jobs and services. Get title, description, price, all photos, GPS coordinates, category attributes, and seller profile + aggregate rating. Search by category + location + keyword, or paste any Gumtree URL.

**[Open Gumtree AU Scraper on Apify](https://apify.com/abotapi/gumtree-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~gumtree-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "category": "all", "location": "Sydney", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | 1. Search mode |
| `urls` | array | Search or listing URLs (URL mode) |
| `category` | string | Category / vertical |
| `location` | string | Location |
| `keywords` | string | Keyword |
| `adType` | string | Ad type |
| `sortBy` | string | Sort order |
| `minPrice` | integer | Minimum price (AUD) |
| `maxPrice` | integer | Maximum price (AUD) |
| `radius` | integer | Search radius (km) |
| `fetchDetails` | boolean | Fetch full listing detail (description |
| `maxItems` | integer | Max listings |
| `maxPages` | integer | Max result pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/gumtree-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `description` | string |
| `detailFetched` | boolean |
| `detailStatus` | null |
| `fullDescription` | null |
| `latitude` | null |
| `longitude` | null |
| `postcode` | null |
| `suburb` | null |
| `state` | null |
| `mapAddress` | null |
| `price` | integer |
| `priceText` | string |
| `priceType` | string |
| `currency` | string |
| `minimumOfferPrice` | null |
| `previousPriceString` | null |
| `isFree` | boolean |
| `isNegotiable` | boolean |
| `isSwapTrade` | boolean |
| `isWanted` | boolean |
| `isUrgent` | boolean |
| `isPriceDrop` | boolean |
| `isTopAd` | boolean |
| `isFeatured` | boolean |
| `isHighlighted` | boolean |
| `isPremium` | boolean |
| `isB2CPlus` | boolean |
| `isDriveAway` | boolean |
| `isPostedByCarDealer` | boolean |
| `isAuctionAd` | boolean |
| `adType` | string |
| `categoryId` | null |
| `categoryName` | null |
| `vertical` | string |
| `location` | string |
| `locationArea` | string |
| `locationState` | string |

---

[← All scrapers](../../README.md)
