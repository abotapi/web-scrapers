# Immowelt.de Scraper

Scrape detailed property listings from Immowelt.de into clean structured data. Extract prices, GPS coordinates, rooms, living area, photos, energy class, property features, agent contact details, and more.

**[Open Immowelt.de Scraper on Apify](https://apify.com/abotapi/immowelt-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~immowelt-de-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "filter", "locations": [{"state": "berlin", "city": "Berlin"}], "listingType": "Buy", "propertyType": "Apartment", "sortBy": "Default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "DE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | 1. Search mode |
| `locations` | array | Locations to search (Filter mode) |
| `listingType` | string | Buy or rent (Filter mode) |
| `propertyType` | string | Property type (Filter mode) |
| `priceMin` | integer | Min price,  (Filter mode) |
| `priceMax` | integer | Max price,  (Filter mode) |
| `roomsMin` | integer | Min rooms (Filter mode) |
| `roomsMax` | integer | Max rooms (Filter mode) |
| `livingSpaceMin` | integer | Min living space, m² (Filter mode) |
| `livingSpaceMax` | integer | Max living space, m² (Filter mode) |
| `constructionYearMin` | integer | Built from year (Filter mode) |
| `constructionYearMax` | integer | Built until year (Filter mode) |
| `sortBy` | string | Sort order (Filter mode) |
| `urls` | array | Search URLs (URL mode) |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max total listings |
| `includeCoordinates` | boolean | Add GPS coordinates |
| `fetchDetails` | boolean | Visit each listing's detail page |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/immowelt-de-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `legacyId` | string |
| `url` | string |
| `listingType` | string |
| `origin` | string |
| `propertyType` | string |
| `title` | string |
| `priceValue` | integer |
| `priceCurrency` | string |
| `priceDisplay` | string |
| `pricePerSqm` | string |
| `rooms` | integer |
| `livingSpace` | integer |
| `plotArea` | null |
| `floor` | null |
| `constructionYear` | null |
| `energyClass` | string |
| `energyValue` | null |
| `country` | string |
| `city` | string |
| `district` | string |
| `postcode` | string |
| `street` | null |
| `latitude` | float |
| `longitude` | float |
| `addressPublished` | boolean |
| `agentName` | string |
| `agentCompany` | string |
| `agentType` | string |
| `agentPhones` | list |
| `agentWebsite` | string |
| `agentProfileUrl` | string |
| `agentRating` | null |
| `agentReviews` | null |
| `agentAddress` | string |
| `imageCount` | integer |
| `images` | list |
| `imagesAnnotated` | list |
| `hasFloorplan` | boolean |
| `has3DTour` | boolean |

---

[← All scrapers](../../README.md)
