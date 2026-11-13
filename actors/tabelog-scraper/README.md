# Tabelog Japan Scraper

Scrape Tabelog (tabelog.com) restaurants in Japan by keyword, area or URL. Extract names, cuisines, ratings, reviews, lunch and dinner budgets, stations, addresses, GPS, phone numbers, hours, seating, photos, smoking policies, closed days and reservation availability.

**[Open Tabelog Japan Scraper on Apify](https://apify.com/abotapi/tabelog-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~tabelog-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["ramen"], "locations": ["Tokyo"], "sortBy": "ranking", "smoking": "any", "maxReviews": 10, "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search keywords |
| `locations` | array | Areas |
| `sortBy` | string | Sort by |
| `minRating` | number | Minimum rating |
| `minReviews` | integer | Minimum reviews |
| `smoking` | string | Smoking policy |
| `reservableOnly` | boolean | Online reservation only |
| `urls` | array | Tabelog links |
| `fetchDetails` | boolean | Add restaurant details |
| `maxReviews` | integer | Max reviews per restaurant |
| `fullReviewText` | boolean | Full review text |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/tabelog-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `restaurantId` | string |
| `url` | string |
| `restaurantUrl` | string |
| `name` | string |
| `restaurantName` | string |
| `title` | string |
| `rank` | integer |
| `station` | string |
| `nearestStation` | string |
| `stationDistance` | string |
| `restaurantArea` | string |
| `searchArea` | string |
| `searchKeyword` | string |
| `genre` | string |
| `restaurantGenre` | string |
| `genres` | list |
| `categories` | list |
| `rating` | float |
| `restaurantRating` | float |
| `score` | float |
| `ratingLabel` | string |
| `reviewCount` | integer |
| `totalReviewCount` | integer |
| `dinnerBudget` | string |
| `budgetDinner` | string |
| `priceDinner` | string |
| `dinnerBudgetMin` | null |
| `dinnerBudgetMax` | integer |
| `lunchBudget` | string |
| `budgetLunch` | string |
| `priceLunch` | string |
| `lunchBudgetMin` | integer |
| `lunchBudgetMax` | integer |
| `closedDays` | string |
| `smokingPolicy` | string |
| `tags` | list |
| `awards` | list |
| `promotionTitle` | null |
| `imageUrl` | string |

---

[← All scrapers](../../README.md)
