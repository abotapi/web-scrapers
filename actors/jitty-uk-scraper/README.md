# Jitty Scraper

Scrape residential property listings from Jitty.com across the UK. Search with 20+ property filters, including AI vision search, and extract clean structured data for homes, prices, locations, features and more.

**[Open Jitty Scraper on Apify](https://apify.com/abotapi/jitty-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~jitty-uk-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "location": "london", "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "GB"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `location` | string | Location |
| `radius_miles` | integer | Search Radius (miles) |
| `look_for` | string | AI Search |
| `property_type` | string | Property Type |
| `bedrooms` | integer | Min Bedrooms |
| `max_bedrooms` | integer | Max Bedrooms |
| `min_bathrooms` | integer | Min Bathrooms |
| `min_price` | integer | Min Price (GBP) |
| `max_price` | integer | Max Price (GBP) |
| `ownership` | string | Ownership |
| `condition` | string | Condition |
| `exterior_style` | string | Exterior Style |
| `date_added` | string | Date Added |
| `min_area_sqft` | integer | Min Area (sqft) |
| `max_area_sqft` | integer | Max Area (sqft) |
| `outside_space` | string | Outside Space |
| `interior_features` | array | Interior Features |
| `green_tech` | string | Green Tech |
| `urls` | array | Search URLs |
| `include_details` | boolean | Include Full Details |
| `max_properties` | integer | Max Properties |
| `max_pages` | integer | Max Pages |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/jitty-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `title` | string |
| `price` | string |
| `price_numeric` | integer |
| `currency` | string |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `property_type` | string |
| `tags` | list |
| `images` | list |
| `image_count` | integer |
| `url` | string |
| `address` | string |
| `latitude` | float |
| `longitude` | float |
| `location_source` | string |
| `living_spaces` | integer |
| `estate_agent` | string |
| `features` | list |

---

[← All scrapers](../../README.md)
