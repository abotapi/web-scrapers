# ImmobilienScout24.de Scraper

$0.9💰/1K for Gold discount. Extract property listings from immobilienscout24.de, Germany's #1 real estate platform with 9,000+ active listings per city. Get fully-detailed listings including price, GPS coordinates, amenities, images, agent contacts, and more.

**[Open ImmobilienScout24.de Scraper on Apify](https://apify.com/abotapi/immoscout24-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~immoscout24-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "location", "locations": [{"state": "berlin", "city": "Berlin"}], "listingType": "buy", "propertyType": "apartment", "sortBy": "default", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "DE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | 1. Search mode |
| `locations` | array | Locations to search (Location mode) |
| `listingType` | string | Listing Type (Location mode) |
| `propertyType` | string | Property Type |
| `priceMin` | integer | Price Min () |
| `priceMax` | integer | Price Max () |
| `roomsMin` | integer | Rooms Min |
| `roomsMax` | integer | Rooms Max |
| `livingSpaceMin` | integer | Living Space Min (m²) |
| `livingSpaceMax` | integer | Living Space Max (m²) |
| `constructionYearMin` | integer | Construction Year From |
| `constructionYearMax` | integer | Construction Year To |
| `equipment` | array | Amenities |
| `noCommission` | boolean | Commission-free only |
| `sortBy` | string | Sort By |
| `urls` | array | Search URLs (URL mode) |
| `maxPages` | integer | Max Pages |
| `maxListings` | integer | Max Listings |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/immoscout24-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `listingType` | string |
| `propertyType` | string |
| `title` | string |
| `addressFull` | string |
| `street` | string |
| `houseNumber` | string |
| `postcode` | string |
| `city` | string |
| `quarter` | string |
| `latitude` | float |
| `longitude` | float |
| `priceValue` | integer |
| `priceCurrency` | string |
| `priceDisplay` | string |
| `marketingType` | string |
| `rooms` | integer |
| `livingSpace` | float |
| `constructionYear` | null |
| `balcony` | boolean |
| `builtInKitchen` | boolean |
| `garden` | boolean |
| `lift` | boolean |
| `guestToilet` | boolean |
| `cellar` | boolean |
| `barrierFree` | boolean |
| `hasCourtage` | boolean |
| `hasFloorplan` | boolean |
| `hasVideo` | boolean |
| `imageCount` | integer |
| `images` | list |
| `floorplanUrl` | string |
| `contactName` | string |
| `contactPhone` | string |
| `contactCompany` | string |
| `projectName` | string |
| `projectUrl` | string |
| `tags` | list |
| `isNew` | boolean |

---

[← All scrapers](../../README.md)
