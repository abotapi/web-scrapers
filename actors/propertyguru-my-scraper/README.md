# PropertyGuru MY Scraper

Scrape PropertyGuru.com.my sale and rental listings with 30+ structured fields, including MYR price, built-up area, tenure, nearby transit, property details, agent information and GPS coordinates. Fast and reliable at scale.

**[Open PropertyGuru MY Scraper on Apify](https://apify.com/abotapi/propertyguru-my-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~propertyguru-my-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "listing_type": "sale", "sort": "date", "sort_order": "desc", "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "MY"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | 1. Search mode |
| `urls` | array | Search URLs (URL mode) |
| `listing_type` | string | Listing Type (Search mode) |
| `property_type` | string | Property Type |
| `state` | string | State / Federal Territory |
| `search` | string | Free-text Location |
| `min_price` | integer | Min Price (MYR) |
| `max_price` | integer | Max Price (MYR) |
| `bedrooms` | integer | Bedrooms |
| `sort` | string | Sort By |
| `sort_order` | string | Sort Order |
| `enable_detail_pages` | boolean | Fetch Detail Pages |
| `max_properties` | integer | Max Properties |
| `max_pages` | integer | Max Pages |
| `proxy` | object | Proxy configuration |
| `detail_concurrency` | integer | Detail Page Concurrency |
| `session_ttl_seconds` | integer | Session TTL (seconds) |
| `reuse_project_cache` | boolean | Reuse Project Cache |
| `dataset_name` | string | Dataset Name |
| `clear_dataset` | boolean | Clear Dataset |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/propertyguru-my-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

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
| `bedrooms` | integer |
| `bathrooms` | integer |
| `floor_area` | integer |
| `tenure` | string |
| `developer` | string |
| `is_developer_listing` | boolean |
| `agent_name` | string |
| `agent_id` | integer |
| `agent_license` | string |
| `state` | string |
| `region` | string |
| `city` | string |
| `badges` | list |
| `posted_date` | string |
| `posted_unix` | integer |
| `recency` | string |
| `images` | list |
| `image_count` | integer |
| `url` | string |
| `status` | string |
| `description` | string |
| `headline` | string |
| `latitude` | float |
| `longitude` | float |
| `postal_code` | string |
| `project_name` | string |
| `project_id` | string |
| `project_legacy_id` | integer |
| `project_status_code` | string |
| `total_units` | integer |

---

[← All scrapers](../../README.md)
