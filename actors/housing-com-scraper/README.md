# Housing.com Scraper

Scrape residential property listings from Housing.com across 750+ cities. Extract structured data for properties available to buy or rent, including prices, locations, property details, and more.

**[Open Housing.com Scraper on Apify](https://apify.com/abotapi/housing-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~housing-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "service": "buy", "city": "Mumbai"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `urls` | array | Search URLs |
| `service` | string | Service |
| `city` | string | City |
| `locality` | string | Locality |
| `min_price` | integer | Min Price (INR) |
| `max_price` | integer | Max Price (INR) |
| `min_bhk` | number | Min BHK |
| `max_bhk` | number | Max BHK |
| `property_type` | string | Property Type |
| `max_properties` | integer | Max Properties |
| `max_pages` | integer | Max Pages |
| `dataset_name` | string | Dataset Name |
| `clear_dataset` | boolean | Clear Dataset |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/housing-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `listingId` | string |
| `title` | string |
| `subtitle` | string |
| `address` | string |
| `propertyType` | string |
| `price_display` | string |
| `price_values` | list |
| `currency` | string |
| `area_value` | integer |
| `area_unit` | string |
| `latitude` | float |
| `longitude` | float |
| `features` | list |
| `bhk_configs` | list |
| `amenities` | list |
| `sellers` | list |
| `seller_firms` | list |
| `highlights` | list |
| `emi` | string |
| `images` | list |
| `image_count` | integer |
| `url` | string |
| `scraped_at` | string |

---

[← All scrapers](../../README.md)
