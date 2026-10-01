# Hipflat Scraper

Scrape hipflat.co.th property listings and new-project data across Thailand: price, price per m², beds, baths, area, floor, type, address, GPS, amenities, photos, full description and project facts. Buy and rent; search and URL modes; project records with available units; sorts and filters.

**[Open Hipflat Scraper on Apify](https://apify.com/abotapi/hipflat-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~hipflat-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Bangkok"], "dealType": "buy", "propertyType": "condo", "sortBy": "relevance", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "TH"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `dealType` | string | Deal type |
| `propertyType` | string | Property type |
| `minPrice` | integer | Min price (THB) |
| `maxPrice` | integer | Max price (THB) |
| `bedrooms` | integer | Bedrooms |
| `minBathrooms` | integer | Min bathrooms |
| `minArea` | integer | Min area (m2) |
| `maxArea` | integer | Max area (m2) |
| `sortBy` | string | Sort order |
| `urls` | array | Hipflat URLs |
| `includeProjectDetails` | boolean | Fetch full project record for each pro |
| `fetchDetails` | boolean | Fetch full detail for each listing |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/hipflat-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `listingId` | string |
| `url` | string |
| `title` | string |
| `dealType` | string |
| `propertyType` | string |
| `priceText` | string |
| `price` | integer |
| `currency` | string |
| `address` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `areaText` | string |
| `area` | integer |
| `areaUnit` | string |
| `description` | string |
| `images` | list |
| `mainImage` | string |
| `imageCount` | integer |
| `isPremium` | boolean |
| `sourceUrl` | string |
| `scrapedAt` | string |
| `record_type` | string |
| `record_id` | string |
| `id` | string |
| `listing_id` | string |
| `propertyUrl` | string |
| `source_url` | string |
| `loaded_url` | string |
| `canonical_url` | string |
| `name` | string |
| `deal_type` | string |
| `property_type` | string |
| `property_types` | list |
| `price_text` | string |
| `price_min` | integer |
| `price_max` | integer |
| `floor_area` | integer |
| `image_urls` | list |
| `video_urls` | list |

---

[← All scrapers](../../README.md)
