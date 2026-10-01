# Real Estate AU Scraper

Extract detailed Australian real estate property listings with 30+ structured fields, including price, description, indoor and outdoor features, coordinates, nearby schools, agent contact details, images, and listing price history where available.

**[Open Real Estate AU Scraper on Apify](https://apify.com/abotapi/realestate-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~realestate-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "location", "locations": [{"suburb": "Sydney", "state": "NSW"}], "listingType": "buy", "sortBy": "list-date", "dateRange": "6months", "maxListings": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `locations` | array | Locations to search (Location mode) |
| `listingType` | string | Listing Type (Location mode) |
| `sortBy` | string | Sort Order |
| `dateRange` | string | Sold Date Range |
| `propertyTypes` | array | Property Types |
| `priceMin` | integer | Minimum Price |
| `priceMax` | integer | Maximum Price |
| `bedroomsMin` | integer | Minimum Bedrooms |
| `bedroomsMax` | integer | Maximum Bedrooms |
| `bathroomsMin` | integer | Minimum Bathrooms |
| `includeSurrounding` | boolean | Include Surrounding Suburbs |
| `urls` | array | Search URLs (URL mode) |
| `includeNearbySchools` | boolean | Include Nearby Schools |
| `includePriceHistory` | boolean | Include Price History |
| `includePcaInsights` | boolean | Include Market Insights & Forecast |
| `maxListings` | integer | Maximum Listings |
| `maxPages` | integer | Maximum Pages per Location |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/realestate-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `propertyId` | string |
| `url` | string |
| `listingType` | string |
| `propertyType` | string |
| `status` | object |
| `address` | object |
| `coordinates` | object |
| `price` | object |
| `features` | object |
| `description` | string |
| `headline` | string |
| `propertyFeatures` | list |
| `propertyFeaturesStructured` | object |
| `media` | object |
| `agent` | object |
| `agents` | list |
| `agency` | object |
| `inspectionTimes` | list |
| `constructionStatus` | string |
| `productDepth` | string |
| `featured` | boolean |
| `agencyListingId` | string |
| `channel` | string |
| `isBuy` | boolean |
| `isRent` | boolean |
| `isSold` | boolean |
| `isProject` | boolean |
| `tier` | object |
| `scrapedAt` | string |
| `auctionDate` | string |
| `auctionDateDisplay` | string |
| `badge` | string |
| `dateListed` | string |
| `dateListedPrecision` | string |

---

[← All scrapers](../../README.md)
