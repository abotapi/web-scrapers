# Commercial Property AU Scraper

Scrape Australian commercial property listings with full detail data. Extract descriptions, highlights, property attributes, GPS coordinates, nearby places, agents, agencies, images and rich listing metadata.

**[Open Commercial Property AU Scraper on Apify](https://apify.com/abotapi/realcommercial-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~realcommercial-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "location", "locations": [{"suburb": "Melbourne", "state": "VIC"}], "listingType": "for-sale", "sortBy": "date-desc", "maxListings": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `locations` | array | Locations to search (Location mode) |
| `listingType` | string | Listing Type (Location mode) |
| `propertyTypes` | array | Property Types |
| `sortBy` | string | Sort Order |
| `priceMin` | integer | Minimum Price |
| `priceMax` | integer | Maximum Price |
| `areaMin` | integer | Minimum Area (m²) |
| `areaMax` | integer | Maximum Area (m²) |
| `keywords` | string | Keywords |
| `urls` | array | Search URLs (URL mode) |
| `maxListings` | integer | Maximum Listings |
| `maxPages` | integer | Maximum Pages per Location |
| `proxyConfiguration` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/realcommercial-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `propertyId` | string |
| `url` | string |
| `listingType` | string |
| `propertyTypes` | list |
| `tenureType` | string |
| `title` | string |
| `description` | string |
| `descriptionMetadata` | object |
| `status` | string |
| `daysActive` | integer |
| `hasTour` | boolean |
| `product` | string |
| `address` | object |
| `price` | object |
| `attributes` | object |
| `media` | object |
| `agents` | list |
| `agency` | object |
| `websites` | list |
| `nearbyPlaces` | list |
| `lastUpdatedAt` | string |
| `canonicalPath` | string |
| `highQualityListing` | boolean |
| `propertyTypeObjects` | list |
| `tenureTypeDisplay` | string |
| `map` | object |
| `latitude` | float |
| `longitude` | float |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
