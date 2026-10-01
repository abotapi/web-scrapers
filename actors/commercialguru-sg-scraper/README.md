# CommercialGuru SG Property Listings & Agent Contacts Scraper

Scrape commercialguru.com.sg Singapore listings at scale. Extract prices, PSF, floor area, tenure, property type, images, agent contacts, coordinates, nearby MRT stations and more. Ideal for commercial real estate analytics, investment research and market intelligence.

**[Open CommercialGuru SG Property Listings & Agent Contacts Scraper on Apify](https://apify.com/abotapi/commercialguru-sg-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~commercialguru-sg-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "listing_type": "sale", "sort": "date", "sort_order": "desc", "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "SG"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `listing_type` | string | Listing Type |
| `property_type` | string | Property Type |
| `locations` | array | Locations |
| `search` | string | Location Search |
| `district` | string | District Code |
| `min_price` | integer | Min Price (SGD) |
| `max_price` | integer | Max Price (SGD) |
| `min_floor_area` | integer | Min Floor Area (sqft) |
| `max_floor_area` | integer | Max Floor Area (sqft) |
| `sort` | string | Sort By |
| `sort_order` | string | Sort Order |
| `urls` | array | Search URLs |
| `enable_coordinates` | boolean | Enable Coordinate Enrichment |
| `fetch_details` | boolean | Fetch detail pages |
| `max_properties` | integer | Max Properties |
| `max_pages` | integer | Max Pages |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/commercialguru-sg-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `title` | string |
| `address` | string |
| `listing_type` | string |
| `property_type` | string |
| `property_type_group` | string |
| `price` | integer |
| `price_formatted` | string |
| `currency` | string |
| `price_psf` | string |
| `floor_area` | integer |
| `tenure` | string |
| `developer` | string |
| `is_developer_listing` | boolean |
| `agent_name` | string |
| `agent_id` | integer |
| `agent_license` | string |
| `agency_name` | string |
| `district` | string |
| `district_code` | string |
| `region` | string |
| `nearby_mrt` | string |
| `badges` | list |
| `posted_date` | string |
| `posted_unix` | integer |
| `recency` | string |
| `images` | list |
| `image_count` | integer |
| `url` | string |
| `status` | string |

---

[← All scrapers](../../README.md)
