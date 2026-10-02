# Zillow Scraper

Scrape zillow.com properties for sale, for rent and recently sold across the US: price, beds, baths, area, address, GPS, photos, home value and rent estimates. Optional property page read adds HOA fee, tax rate, MLS id, agent, brokerage and the fact sheet. 25 filters, or paste links.

**[Open Zillow Scraper on Apify](https://apify.com/abotapi/zillow-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~zillow-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Austin, TX"], "listingType": "FOR_SALE", "daysOnZillow": "ANY", "sortBy": "RECOMMENDED", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Start mode |
| `locations` | array | Locations |
| `listingType` | string | Looking for |
| `homeTypes` | array | Property types |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minBeds` | integer | Min bedrooms |
| `maxBeds` | integer | Max bedrooms |
| `minBaths` | integer | Min bathrooms |
| `minSqft` | integer | Min living area (sqft) |
| `maxSqft` | integer | Max living area (sqft) |
| `minLotSize` | integer | Min lot size (sqft) |
| `maxLotSize` | integer | Max lot size (sqft) |
| `minYearBuilt` | integer | Built after |
| `maxYearBuilt` | integer | Built before |
| `maxHoaFee` | integer | Max HOA fee per month |
| `keywords` | string | Keywords |
| `daysOnZillow` | string | Listed within |
| `sortBy` | string | Sort by |
| `hasPool` | boolean | Must have a pool |
| `hasGarage` | boolean | Must have a garage |
| `hasAirConditioning` | boolean | Must have air conditioning |
| `isWaterfront` | boolean | Waterfront only |
| `singleStoryOnly` | boolean | Single story only |
| `has3dTour` | boolean | Must have a 3D tour |
| `openHouseOnly` | boolean | Open house only |
| `priceReducedOnly` | boolean | Price reduced only |
| `startUrls` | array | Zillow links |
| `fetchDetails` | boolean | Read the property page for each result |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max reads per location |
| `proxy` | object | Connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/zillow-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `zpid` | string |
| `url` | string |
| `listingType` | string |
| `homeStatus` | string |
| `statusText` | string |
| `marketingStatus` | string |
| `propertyType` | string |
| `price` | integer |
| `formattedPrice` | string |
| `currency` | string |
| `taxAssessedValue` | integer |
| `priceChange` | integer |
| `priceChangeDate` | string |
| `streetAddress` | string |
| `city` | string |
| `state` | string |
| `zipCode` | string |
| `country` | string |
| `address` | string |
| `latitude` | float |
| `longitude` | float |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `livingArea` | integer |
| `lotAreaValue` | float |
| `lotAreaUnit` | string |
| `daysOnZillow` | integer |
| `brokerName` | string |
| `isZillowOwned` | boolean |
| `isNewConstruction` | boolean |
| `isUndisclosedAddress` | boolean |
| `has3dTour` | boolean |
| `hasVideo` | boolean |
| `heroImage` | string |
| `photos` | list |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
