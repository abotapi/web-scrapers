# Dot Property Scraper

Scrape Philippines property listings from dotproperty.com.ph and lamudi.com.ph with exact map-pin coordinates, price, beds, baths, areas, facilities, full photo galleries, and agent contact details. Covers houses, condos, apartments, townhouses, villas, land, offices and commercial units, for.

**[Open Dot Property Scraper on Apify](https://apify.com/abotapi/dotproperty-com-ph-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~dotproperty-com-ph-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "sites": ["dotproperty", "lamudi"], "operation": "sale", "propertyTypes": ["properties"], "locations": ["Metro Manila"], "sort": "newest", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": [], "apifyProxyCountry": "PH"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `sites` | array | Portals |
| `operation` | string | Rent or sale |
| `propertyTypes` | array | Property types |
| `locations` | array | Locations |
| `minPrice` | integer | Min price (PHP) |
| `maxPrice` | integer | Max price (PHP) |
| `minBedrooms` | integer | Min bedrooms |
| `minSqm` | integer | Min floor area (sqm) |
| `sort` | string | Sort results (Dot Property) |
| `urls` | array | Search or listing URLs |
| `maxItems` | integer | Max listings |
| `maxPages` | integer | Max pages per search |
| `fetchDetails` | boolean | Fetch detail pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/dotproperty-com-ph-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `listing_id` | string |
| `url` | string |
| `source` | string |
| `price` | integer |
| `usable_area_sqm` | integer |
| `agent_name` | string |
| `agent_verified` | boolean |
| `latitude` | float |
| `longitude` | float |
| `agent_phone` | string |
| `title` | string |
| `land_area_sqm` | integer |
| `facilities` | list |
| `images` | list |
| `image_count` | integer |
| `og_image` | string |
| `description` | string |
| `listing_id_text` | string |
| `agent_listing_count` | integer |
| `agent_url` | string |
| `breadcrumbs` | list |
| `currency` | string |
| `location_source` | string |

---

[← All scrapers](../../README.md)
