# Vivino Wine Scraper

Scrape Vivino.com for wine ratings, prices, taste profiles, food pairings, grapes, and reviews. Search by wine names or URLs, or discover wines by type, price, rating, country, and grape. Returns 50+ fields, including multi-merchant offers and value scores.

**[Open Vivino Wine Scraper on Apify](https://apify.com/abotapi/vivino-wine-data-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~vivino-wine-data-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "lookup", "wines": ["Dom Pérignon", "Opus One 2019", "https://www.vivino.com/cloudy-bay-sauvignon-blanc/w/18978"], "searchMode": "auto", "matchingMode": "basic", "sortBy": "relevance", "countryCode": "FR", "currencyCode": "EUR", "maxReviewsPerWine": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `wines` | array | Wine names or URLs |
| `searchMode` | string | Vintage handling (Lookup, name entries |
| `matchingMode` | string | Matching effort (Lookup, name entries) |
| `wineTypes` | array | Wine types |
| `minRating` | integer | Minimum rating |
| `priceMin` | integer | Minimum price |
| `priceMax` | integer | Maximum price |
| `originCountries` | array | Origin countries |
| `grapes` | array | Grape IDs |
| `sortBy` | string | Sort order |
| `countryCode` | string | Market country |
| `currencyCode` | string | Currency |
| `shipTo` | string | Ship-to country |
| `includeTasteProfile` | boolean | Include taste profile |
| `includeReviews` | boolean | Include reviews |
| `maxReviewsPerWine` | integer | Max reviews per wine |
| `maxItems` | integer | Max wines |
| `maxPages` | integer | Max discovery pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/vivino-wine-data-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `wineId` | integer |
| `vintageId` | integer |
| `vivino_url` | string |
| `name` | string |
| `winery` | string |
| `vintage` | integer |
| `wine_type` | string |
| `region` | string |
| `country` | string |
| `appellation` | string |
| `grape_varieties` | list |
| `average_rating` | float |
| `ratings_count` | integer |
| `wine_average_rating` | float |
| `wine_ratings_count` | integer |
| `price` | float |
| `currency` | string |
| `merchant_url` | string |
| `discounted_from` | integer |
| `discount_percent` | null |
| `is_on_sale` | boolean |
| `discount_amount` | null |
| `bottle_volume_ml` | integer |
| `vfm_score` | integer |
| `vfm_category` | integer |
| `is_natural` | boolean |
| `image_url` | string |
| `label_image_url` | string |
| `food_pairings` | list |
| `description` | string |
| `alcohol` | null |
| `winery_id` | integer |
| `winery_seo_name` | string |
| `region_id` | integer |
| `country_code` | string |
| `requested_vintage` | null |
| `matchScore` | integer |
| `lwin` | null |
| `lwin_canonical` | null |
| `taste_profile` | object |

---

[← All scrapers](../../README.md)
