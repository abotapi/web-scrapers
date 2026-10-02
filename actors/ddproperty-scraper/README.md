# DDproperty Thailand Scraper

Scrape DDproperty.com Thailand listings at scale. Extract prices, property features, images, agent contacts, GPS coordinates, nearby BTS/MRT transit and more. Built for Thai real estate analytics, market research and investment analysis.

**[Open DDproperty Thailand Scraper on Apify](https://apify.com/abotapi/ddproperty-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ddproperty-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "listing_type": "sale", "sort": "date", "sort_order": "desc", "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "TH"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | 1. Search mode |
| `listing_type` | string | Listing type (Search mode) |
| `property_type` | string | Property type (Search mode) |
| `search` | string | Location search (Search mode) |
| `region` | string | Region / district / area code (Search  |
| `min_price` | integer | Min price (THB) (Search mode) |
| `max_price` | integer | Max price (THB) (Search mode) |
| `bedrooms` | integer | Bedrooms (Search mode) |
| `sort` | string | Sort by (Search mode) |
| `sort_order` | string | Sort order (Search mode) |
| `urls` | array | Search URLs (URL mode) |
| `max_properties` | integer | Max properties |
| `enable_detail_pages` | boolean | Fetch detail pages |
| `detail_concurrency` | integer | Detail page concurrency |
| `session_ttl_seconds` | integer | Session TTL (seconds) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ddproperty-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

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
| `price_per_sqm` | string |
| `currency` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `tenure` | string |
| `developer` | string |
| `is_developer_listing` | boolean |
| `agent_name` | string |
| `agent_id` | integer |
| `agency_id` | integer |
| `region` | string |
| `region_code` | string |
| `district` | string |
| `district_code` | string |
| `area` | string |
| `area_code` | string |
| `badges` | list |
| `posted_date` | string |
| `posted_unix` | integer |
| `recency` | string |
| `images` | list |
| `image_count` | integer |
| `url` | string |
| `status` | string |
| `latitude` | float |
| `longitude` | float |
| `description` | string |
| `facilities` | list |
| `highlights` | list |
| `images_full` | list |
| `floor_plans` | list |
| `location_source` | string |

---

[← All scrapers](../../README.md)
