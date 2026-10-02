# Housesigma Scraper

Scrape housesigma.com listings across Ontario, BC, and Alberta. Search by city or paste URLs to extract prices, addresses, photos, room dimensions, school scores, price history, HouseSigma estimates, and sold statistics.

**[Open Housesigma Scraper on Apify](https://apify.com/abotapi/housesigma-com?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~housesigma-com/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "province": "ON", "locations": ["Toronto"], "status": ["for-sale"], "sortBy": "newest", "agentCategory": "sold", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `province` | string | Province |
| `locations` | array | Cities or communities |
| `status` | array | Listing status |
| `propertyTypes` | array | Property types |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minBedrooms` | integer | Min bedrooms |
| `maxBedrooms` | integer | Max bedrooms |
| `minBathrooms` | integer | Min bathrooms |
| `minGarage` | integer | Min garage spaces |
| `minSqft` | integer | Min size (sqft) |
| `maxSqft` | integer | Max size (sqft) |
| `soldDays` | integer | Sold/leased within (days) |
| `sortBy` | string | Sort by |
| `urls` | array | HouseSigma URLs |
| `listings` | array | Listing IDs or links |
| `agents` | array | Agent profiles |
| `agentCategory` | string | Agent listings category |
| `fetchDetails` | boolean | Fetch full details |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max pages per area |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/housesigma-com?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `idListing` | string |
| `mlNum` | string |
| `url` | string |
| `status` | string |
| `saleOrLease` | string |
| `propertyType` | string |
| `address` | string |
| `addressFull` | string |
| `aptNumber` | null |
| `community` | string |
| `municipality` | string |
| `province` | string |
| `bedrooms` | integer |
| `bedroomsPlus` | integer |
| `bathrooms` | integer |
| `parking` | object |
| `priceListed` | integer |
| `priceListedText` | string |
| `priceAbbr` | string |
| `priceSold` | string |
| `latitude` | float |
| `longitude` | float |
| `sizeSqft` | null |
| `sizeText` | string |
| `lotFront` | integer |
| `lotDepth` | integer |
| `lotUnit` | string |
| `dateListed` | string |
| `dateUpdated` | string |
| `daysOnMarket` | integer |
| `dataSource` | string |
| `photo` | string |
| `listStatus` | object |
| `photos` | list |
| `virtualTour` | string |
| `keyFacts` | object |
| `propertyDetail` | object |
| `rooms` | list |
| `schools` | list |
| `priceHistory` | list |

---

[← All scrapers](../../README.md)
