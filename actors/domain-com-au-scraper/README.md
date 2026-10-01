# Domain.com.au Scraper

Extract enriched Domain.com.au property listings across buy, rent, and sold, with AI-enhanced content and deep structured data including descriptions, features, photos, GPS, agent contacts, suburb insights, school catchments, and complete sold and leased price history timelines.

**[Open Domain.com.au Scraper on Apify](https://apify.com/abotapi/domain-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~domain-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Sydney NSW 2000"], "sortBy": "default", "listingType": "buy", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Start here pick your search mode |
| `locations` | array | Suburbs / locations (search mode) |
| `sortBy` | string | Sort order |
| `urls` | array | Domain.com.au URLs (url mode) |
| `listingType` | string | Listing type |
| `propertyTypes` | array | Property types |
| `minBedrooms` | integer | Min bedrooms |
| `maxBedrooms` | integer | Max bedrooms |
| `minBathrooms` | integer | Min bathrooms |
| `minPrice` | integer | Min price (AUD) |
| `maxPrice` | integer | Max price (AUD) |
| `excludeUnderOffer` | boolean | Exclude under offer / under contract |
| `inspectionsOnly` | boolean | Open for inspection only (search mode) |
| `auctionsOnly` | boolean | Auctions only (search mode) |
| `fetchPropertyHistory` | boolean | Fetch property price history |
| `includePropertyInsights` | boolean | Include extra property insights (valua |
| `includeExtendedListing` | boolean | Include extended listing attributes (i |
| `maxListings` | integer | Max listings (0  no limit) |
| `maxPages` | integer | Max pages per search (0  no limit) |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/domain-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `listingType` | string |
| `displayAddress` | string |
| `street` | string |
| `suburb` | string |
| `state` | string |
| `postcode` | string |
| `latitude` | float |
| `longitude` | float |
| `price` | string |
| `priceGuide` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `parkingSpaces` | integer |
| `landSize` | null |
| `landSizeUnit` | null |
| `buildingSize` | integer |
| `buildingSizeUnit` | string |
| `propertyType` | string |
| `headline` | string |
| `description` | string |
| `structuredFeatures` | list |
| `saleMethod` | string |
| `isAuction` | boolean |
| `status` | string |
| `inspection` | object |
| `firstListedDate` | string |
| `lastSoldDate` | null |
| `soldDate` | null |
| `agencyName` | string |
| `agencyProfileUrl` | string |
| `agencyId` | string |
| `agencyAddress` | object |
| `agencyBrandColour` | null |
| `addressDisplayType` | string |
| `agents` | list |
| `suburbInsights` | null |
| `schools` | list |
| `priceHistory` | list |

---

[← All scrapers](../../README.md)
