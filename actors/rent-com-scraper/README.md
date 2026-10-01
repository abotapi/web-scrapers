# Rent.com Scraper

Extract rental listings from rent.com. Get comprehensive data including monthly rent ranges, full address with GPS, beds/baths/sqft ranges, three contact phone channels, special offers, pet policy, photos, amenities, floor plans, and per-day office hours. Apartments, houses, condos, and townhomes.

**[Open Rent.com Scraper on Apify](https://apify.com/abotapi/rent-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~rent-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": [{"city": "Los Angeles", "state": "CA"}], "propertyType": "apartments", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `locations` | array | Locations to search |
| `propertyType` | string | Property type |
| `bedrooms` | string | Bedrooms |
| `maxPrice` | integer | Max monthly rent (USD) |
| `petFriendly` | boolean | Pet-friendly only |
| `furnished` | boolean | Furnished only |
| `luxury` | boolean | Luxury only |
| `dealsOnly` | boolean | Special deals only |
| `incomeRestricted` | boolean | Income-restricted only |
| `urls` | array | Search URLs (URL mode) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (total) |
| `fetchDetails` | boolean | Fetch detail pages (richer data, slowe |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/rent-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `name` | string |
| `propertyType` | string |
| `listingTier` | string |
| `isLuxury` | null |
| `verified` | boolean |
| `fullAddress` | string |
| `street` | null |
| `city` | string |
| `state` | string |
| `stateName` | string |
| `zip` | string |
| `latitude` | float |
| `longitude` | float |
| `bedsMin` | integer |
| `bedsMax` | integer |
| `bedsLabel` | string |
| `bathsMin` | integer |
| `bathsMax` | integer |
| `bathsLabel` | string |
| `sqftMin` | integer |
| `sqftMax` | integer |
| `priceMin` | integer |
| `priceMax` | integer |
| `priceLabel` | string |
| `availability` | string |
| `unitsAvailableText` | string |
| `phone` | string |
| `phoneText` | string |
| `phoneSem` | string |
| `phoneSemText` | string |
| `specialOffer` | null |
| `specialOfferCategory` | null |
| `deals` | list |
| `categoryBadges` | list |
| `amenitiesHighlighted` | list |
| `amenitiesAll` | list |
| `petsCats` | boolean |
| `petsDogs` | boolean |

---

[← All scrapers](../../README.md)
