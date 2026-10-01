# View.com.au Scraper

Scrape View.com.au properties for sale, rent and recently sold across Australia. Search by suburb, city, state or URL. Extract prices, full addresses, property details, agents and agencies, photos, GPS coordinates and market insights.

**[Open View.com.au Scraper on Apify](https://apify.com/abotapi/view-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~view-com-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "location", "locations": [{"suburb": "Melbourne", "state": "VIC", "postcode": "3000"}], "listingType": "buy", "sort": "date-desc", "maxListings": 10, "maxPages": 1, "outputFormat": ["json"], "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search Mode |
| `locations` | array | Locations |
| `listingType` | string | Listing Type |
| `propertyTypes` | array | Property Types (Optional) |
| `priceMin` | integer | Minimum Price (Optional) |
| `priceMax` | integer | Maximum Price (Optional) |
| `bedroomsMin` | integer | Minimum Bedrooms (Optional) |
| `bathroomsMin` | integer | Minimum Bathrooms (Optional) |
| `carsMin` | integer | Minimum Car Spaces (Optional) |
| `sort` | string | Sort Order (Optional) |
| `urls` | array | Search List URLs |
| `detailUrls` | array | Property Detail URLs |
| `maxListings` | integer | Maximum Listings |
| `maxPages` | integer | Maximum Pages per Location |
| `includeDetailPage` | boolean | Include Detail Page Data |
| `outputFormat` | array | Output Formats |
| `proxyConfiguration` | object | Proxy Configuration |
| `resumeFromCheckpoint` | boolean | Resume from Checkpoint |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/view-com-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `listingUrl` | string |
| `address` | object |
| `price` | object |
| `features` | object |
| `propertyType` | string |
| `sourcePropertyType` | string |
| `listingType` | string |
| `saleMethod` | string |
| `status` | string |
| `rank` | string |
| `images` | list |
| `agents` | list |
| `agency` | object |
| `location` | object |
| `inspections` | list |
| `createdAt` | string |
| `updatedAt` | string |
| `onMarketAt` | string |
| `lgaName` | string |
| `region` | string |
| `gnafId` | string |
| `listingSource` | string |
| `isNewConstruction` | boolean |
| `isHomeAndLand` | boolean |
| `isStreetHidden` | boolean |
| `propertyTypes` | list |
| `updatedText` | string |
| `heroImageUrl` | string |
| `imageUrlSlug` | string |
| `source` | object |

---

[← All scrapers](../../README.md)
