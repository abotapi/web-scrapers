# Zap Imóveis Scraper

Scrape Zap Imóveis sale, rental and new-development listings by city, filters or URL. Extract 80+ fields including prices, fees, addresses, GPS, agencies, CRECI, amenities, nearby POIs, scores, H3 location data and media.

**[Open Zap Imóveis Scraper on Apify](https://apify.com/abotapi/zapimoveis-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~zapimoveis-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Sao Paulo, SP"], "businessType": "SALE", "listingType": "USED", "propertyType": "ANY", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "BR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search Mode |
| `locations` | array | Locations |
| `businessType` | string | Sale or Rental |
| `listingType` | string | Listing Type |
| `propertyType` | string | Property Type |
| `minPrice` | integer | Min Price (BRL) |
| `maxPrice` | integer | Max Price (BRL) |
| `minBedrooms` | integer | Min Bedrooms |
| `minBathrooms` | integer | Min Bathrooms |
| `minParkingSpaces` | integer | Min Parking Spaces |
| `minUsableArea` | integer | Min Usable Area (m²) |
| `maxUsableArea` | integer | Max Usable Area (m²) |
| `sortBy` | string | Sort By |
| `urls` | array | Listing URLs |
| `maxPages` | integer | Max Pages Per Search |
| `maxListings` | integer | Max Listings |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/zapimoveis-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `price` | integer |
| `currency` | string |
| `business` | string |
| `listing_type` | string |
| `property_type` | string |
| `unit_types` | list |
| `bedrooms` | integer |
| `bathrooms` | integer |
| `suites` | integer |
| `parking_spaces` | integer |
| `usable_area` | integer |
| `total_area` | integer |
| `city` | string |
| `state_code` | string |
| `neighborhood` | string |
| `street` | string |
| `zip_code` | string |
| `latitude` | null |
| `longitude` | null |
| `monthly_condo_fee` | integer |
| `iptu` | null |
| `seller_name` | string |
| `seller_tier` | string |
| `seller_license_number` | string |
| `seller_legacy_zap_id` | integer |
| `phones` | list |
| `whatsapp` | string |
| `lqs` | null |
| `created_at` | string |
| `updated_at` | null |
| `identity` | object |
| `source_context` | object |
| `timestamps` | object |
| `content` | object |
| `pricing` | object |
| `availability` | object |
| `location` | object |

---

[← All scrapers](../../README.md)
