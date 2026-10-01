# AU Residential Property Scraper

Scrape Australian property listings with rich detail-page enrichment. Each listing record comes back with far more than the usual "address + price + beds". You get the full picture that a buyer would see on the site.

**[Open AU Residential Property Scraper on Apify](https://apify.com/abotapi/property-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~property-au-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "listing", "search": "southbank", "listing_type": "buy", "sortBy": "NEW_DESC", "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Scraping Mode |
| `search` | string | Location Search |
| `urls` | array | Search Page URLs |
| `listing_type` | string | Listing Type |
| `propertyTypes` | array | Property Types |
| `priceMin` | integer | Minimum Price |
| `priceMax` | integer | Maximum Price |
| `bedroomsMin` | integer | Minimum Bedrooms |
| `bathroomsMin` | integer | Minimum Bathrooms |
| `landSizeMin` | integer | Minimum Land Size (m²) |
| `carSpacesMin` | integer | Minimum Car Spaces |
| `keywords` | string | Keywords |
| `excludeUnderOffer` | boolean | Exclude Under Offer |
| `sortBy` | string | Sort Order |
| `max_properties` | integer | Max Properties |
| `max_pages` | integer | Max Pages |
| `proxy` | object | Proxy Configuration |
| `dataset_name` | string | Dataset Name (optional) |
| `clear_dataset` | boolean | Clear Named Dataset |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/property-au-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `address` | string |
| `suburb` | string |
| `state` | string |
| `postcode` | string |
| `latitude` | float |
| `longitude` | float |
| `listing_type` | string |
| `listing_status` | string |
| `property_type` | string |
| `price` | string |
| `price_details` | string |
| `features` | object |
| `description` | string |
| `timeline` | list |
| `value_estimates` | object |
| `schools` | object |
| `planning_overlays` | object |
| `land_description` | string |
| `council` | string |
| `internet` | object |
| `market_insights` | object |
| `media` | object |
| `property_url` | string |
| `rea_url` | string |
| `breadcrumbs` | list |
| `status` | string |
| `source_listing` | string |
| `source_listing_type` | string |
| `scraped_at` | string |

---

[← All scrapers](../../README.md)
