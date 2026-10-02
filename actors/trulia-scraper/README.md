# Trulia Scraper

Scrape Trulia.com property listings by location, filters, or URL. Extract prices, beds, baths, square footage, addresses, GPS coordinates, photos, agents, and brokers, plus detailed price and tax history, property features, and open house information.

**[Open Trulia Scraper on Apify](https://apify.com/abotapi/trulia-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~trulia-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchLocation": "New_York,NY", "searchListingType": "FOR_SALE", "searchSort": "RECOMMENDED", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Start mode |
| `searchLocation` | string | Location |
| `searchListingType` | string | Listing type |
| `searchKeyword` | string | Keyword (optional) |
| `searchSort` | string | Sort by |
| `startUrls` | array | Trulia URLs |
| `fetchDetails` | boolean | Fetch property details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/trulia-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `typedHomeId` | string |
| `legacyId` | string |
| `compositeId` | string |
| `url` | string |
| `urlPath` | string |
| `listingType` | string |
| `unifiedListingType` | string |
| `propertyType` | string |
| `price` | integer |
| `formattedPrice` | string |
| `currencyCode` | string |
| `priceTypeDescription` | null |
| `streetAddress` | string |
| `city` | string |
| `state` | string |
| `zipCode` | string |
| `neighborhood` | string |
| `formattedLocation` | string |
| `latitude` | float |
| `longitude` | float |
| `bedrooms` | null |
| `bedroomsFormatted` | string |
| `bathrooms` | null |
| `bathroomsFormatted` | null |
| `floorSpace` | string |
| `lotSize` | null |
| `currentStatus` | object |
| `tags` | list |
| `priceChange` | null |
| `description` | object |
| `listingAgentName` | string |
| `brokerName` | string |
| `listingSummary` | list |
| `dateListed` | string |
| `providerListingId` | null |
| `heroImage` | string |
| `photos` | list |
| `tracking` | object |
| `provider` | object |

---

[← All scrapers](../../README.md)
