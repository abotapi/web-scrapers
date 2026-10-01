# RealestateCo NZ Scraper

Search and extract all real estate properties for sale, rent, and sold across New Zealand from realestate.co.nz.

**[Open RealestateCo NZ Scraper on Apify](https://apify.com/abotapi/realestate-co-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~realestate-co-nz-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "location", "locations": [{"region": "Auckland"}], "listingType": "buy", "sort": "latest", "maxPages": 1, "maxListings": 10, "outputFormat": ["json"]}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `locations` | array | Locations to search |
| `listingType` | string | Listing Type |
| `propertyTypes` | array | Property Types (Optional) |
| `priceMin` | integer | Minimum Price (Optional) |
| `priceMax` | integer | Maximum Price (Optional) |
| `bedroomsMin` | integer | Minimum Bedrooms (Optional) |
| `bathroomsMin` | integer | Minimum Bathrooms (Optional) |
| `includeNeighbouringSuburbs` | boolean | Include Neighbouring Suburbs |
| `sort` | string | Sort Order |
| `maxPages` | integer | Maximum Pages per Location |
| `urls` | array | Search List URLs |
| `maxListings` | integer | Maximum Listings |
| `outputFormat` | array | Output Formats |
| `resumeFromCheckpoint` | boolean | Resume from checkpoint |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/realestate-co-nz-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `listingUrl` | string |
| `listingNo` | string |
| `address` | object |
| `price` | object |
| `features` | object |
| `propertyType` | string |
| `sourcePropertyType` | string |
| `listingType` | string |
| `listingCategoryCode` | string |
| `status` | string |
| `heading` | string |
| `description` | string |
| `images` | list |
| `floorPlans` | list |
| `agents` | list |
| `office` | object |
| `location` | object |
| `openHomes` | list |
| `schools` | list |
| `auctionDate` | string |
| `auctionLocation` | string |
| `publishedDate` | string |
| `createdDate` | string |
| `isFeatured` | boolean |
| `isShowcased` | boolean |
| `isNewConstruction` | boolean |
| `isMortgageeSale` | boolean |
| `isCoastalWaterfront` | boolean |
| `maxTenants` | integer |
| `heroImageUrl` | string |
| `source` | object |

---

[← All scrapers](../../README.md)
