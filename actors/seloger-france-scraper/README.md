# SeLoger Scraper

Scrape SeLoger.com properties for sale and rent. Search by location with price, room and property type filters. Extract prices, areas, rooms, energy ratings, coordinates, images, descriptions, transport links and agent details.

**[Open SeLoger Scraper on Apify](https://apify.com/abotapi/seloger-france-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~seloger-france-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Paris"], "distributionType": "Buy", "estateTypes": ["House", "Apartment"], "sortBy": "Default", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `locations` | array | Locations to search |
| `distributionType` | string | Transaction Type |
| `estateTypes` | array | Property Types |
| `priceMin` | integer | Min Price (EUR) |
| `priceMax` | integer | Max Price (EUR) |
| `roomsMin` | integer | Min Rooms |
| `bedroomsMin` | integer | Min Bedrooms |
| `spaceMin` | integer | Min Area (m2) |
| `sortBy` | string | Sort By |
| `urls` | array | Search URLs |
| `maxItems` | integer | Max Items (total) |
| `maxPages` | integer | Max Pages (per location) |
| `getDetails` | boolean | Get Full Details |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/seloger-france-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `legacy_id` | string |
| `title` | string |
| `headline` | string |
| `description` | string |
| `price` | string |
| `price_numeric` | integer |
| `price_per_m2` | string |
| `currency` | string |
| `distribution_type` | string |
| `property_type` | string |
| `property_type_label` | string |
| `rooms` | integer |
| `bedrooms` | integer |
| `area_m2` | integer |
| `floor` | string |
| `city` | string |
| `zipcode` | string |
| `district` | string |
| `country` | string |
| `transport` | list |
| `energy_class` | string |
| `agent_name` | string |
| `agent_phone` | string |
| `agent_address` | string |
| `has_3d_visit` | boolean |
| `is_new` | boolean |
| `publisher_type` | string |
| `images` | list |
| `floorplans` | list |
| `image_count` | integer |
| `url` | string |
| `portal` | string |
| `created_at` | string |
| `updated_at` | string |
| `source` | string |
| `latitude` | float |
| `longitude` | float |
| `coord_precision` | string |

---

[← All scrapers](../../README.md)
