# GrabFood Restaurant Scraper

Scrape GrabFood restaurants across Southeast Asia, including SG, MY, TH, VN, PH, ID, KH, and MM. Search by keyword or URL and extract 45+ fields: restaurant name, address, GPS, cuisine, ratings, reviews, promos, delivery time, fees, opening hours, and full menus with item prices and images.

**[Open GrabFood Restaurant Scraper on Apify](https://apify.com/abotapi/grabfood-restaurants-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~grabfood-restaurants-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "region": "SG", "searchQueries": ["ramen"], "sortBy": "default", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `region` | string | Region |
| `searchQueries` | array | Search keywords |
| `startUrls` | array | GrabFood URLs |
| `cuisineFilter` | array | Cuisine filter |
| `minRating` | integer | Min rating |
| `minReviews` | integer | Min review count |
| `sortBy` | string | Sort results by |
| `fetchMenu` | boolean | Fetch full menu |
| `includeRatings` | boolean | Include rating fields |
| `maxItems` | integer | Max restaurants |
| `maxPages` | integer | Max pages |
| `proxyConfiguration` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/grabfood-restaurants-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `name` | string |
| `chainName` | string |
| `branchName` | string |
| `cuisine` | list |
| `address` | string |
| `rating` | float |
| `voteCount` | integer |
| `priceTag` | integer |
| `isOpen` | boolean |
| `isIntegrated` | boolean |
| `businessType` | string |
| `estimatedDeliveryTime` | integer |
| `estimatedDeliveryTimeRange` | string |
| `distanceInKm` | float |
| `hasPromo` | boolean |
| `promoLabels` | list |
| `deliveryOptions` | string |
| `deliveryFee` | object |
| `currency` | object |
| `openHours` | object |
| `photoHref` | string |
| `smallPhotoHref` | string |
| `iconHref` | string |
| `grabUrl` | string |
| `announcements` | list |
| `sourceQuery` | string |
| `sourceUrl` | null |
| `region` | string |
| `scrapedAt` | string |
| `fullAddress` | string |
| `street` | string |
| `suburb` | string |
| `postcode` | string |
| `city` | string |
| `countryCode` | string |
| `orderValueLimit` | integer |
| `menu` | list |
| `menuCategoryCount` | integer |
| `menuItemCount` | integer |

---

[← All scrapers](../../README.md)
