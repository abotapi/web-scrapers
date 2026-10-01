# 591.com.tw Scraper

Extract property listings from 591房屋交易網 591.com.tw, Taiwan’s largest real estate marketplace. Search by city or use 591 URLs. Covers rentals, sales, land, and commercial properties. Returns 50–60 fields, including price, area, GPS coordinates, nearby transit, and agent/owner contact details.

**[Open 591.com.tw Scraper on Apify](https://apify.com/abotapi/591-com-tw-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~591-com-tw-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "section": "rent", "regions": ["taipei-city"], "rentKind": "any", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `section` | string | Property section |
| `regions` | array | Regions (cities / counties) |
| `rentKind` | string | Rental type (Rent section only) |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minArea` | integer | Min area (坪 / ping) |
| `maxArea` | integer | Max area (坪 / ping) |
| `urls` | array | 591 list URLs |
| `fetchDetails` | boolean | Visit each listing's detail page |
| `maxListings` | integer | Max total listings |
| `maxPages` | integer | Max pages per region / URL |
| `proxy` | object | Proxy configuration |
| `maxResidentialRequests` | integer | Residential request budget |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/591-com-tw-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `section` | string |
| `listingType` | string |
| `url` | string |
| `title` | string |
| `price` | integer |
| `priceText` | string |
| `priceUnit` | string |
| `unitPrice` | null |
| `kind` | integer |
| `kindName` | string |
| `room` | null |
| `layout` | string |
| `area` | integer |
| `areaText` | string |
| `floor` | string |
| `fitment` | string |
| `address` | string |
| `communityName` | string |
| `communityId` | integer |
| `regionId` | integer |
| `regionName` | string |
| `tags` | list |
| `nearbyTransit` | list |
| `photos` | list |
| `coverPhoto` | string |
| `photoCount` | integer |
| `isVideo` | boolean |
| `browseCount` | integer |
| `contactRole` | string |
| `refreshedAt` | string |
| `descriptionHtml` | string |
| `description` | string |
| `deposit` | string |
| `shape` | string |
| `sectionId` | integer |
| `sectionName` | string |
| `latitude` | float |
| `longitude` | float |
| `leaseMinTerm` | null |

---

[← All scrapers](../../README.md)
