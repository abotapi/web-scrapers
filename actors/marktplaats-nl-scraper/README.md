# Marktplaats.nl Scraper

Scrape Marktplaats.nl listings by keyword or URL. Extract title, price, condition, location and coordinates, photos, seller details, ratings and reviews, shipping, views, and category-specific attributes for cars, bikes, electronics, and more.

**[Open Marktplaats.nl Scraper on Apify](https://apify.com/abotapi/marktplaats-nl-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~marktplaats-nl-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["fiets"], "sellerType": "any", "sortBy": "OPTIMIZED", "sortOrder": "DECREASING", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}, "residentialCountries": ["NL", "BE", "DE", "FR", "GB"]}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `categoryId` | integer | Category ID |
| `minPrice` | integer | Min price (EUR) |
| `maxPrice` | integer | Max price (EUR) |
| `postcode` | string | Postcode |
| `distanceMeters` | integer | Distance (meters) |
| `urls` | array | Listing or result-page URLs |
| `sellerType` | string | Seller type |
| `sortBy` | string | Sort by |
| `sortOrder` | string | Sort order |
| `fetchDetails` | boolean | Fetch full detail pages |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings |
| `proxy` | object | Proxy configuration |
| `residentialCountries` | array | Premium connection fallback countries |
| `maxResidentialRequests` | integer | Premium connection request budget |
| `backupProxyUrl` | string | Backup proxy URL |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/marktplaats-nl-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `itemId` | string |
| `item_id` | string |
| `listingId` | string |
| `adId` | string |
| `title` | string |
| `description` | string |
| `descriptionHtml` | string |
| `categorySpecificDescription` | string |
| `category_specific_description` | string |
| `url` | string |
| `vipUrl` | string |
| `vip_url` | string |
| `inputUrl` | null |
| `price` | object |
| `priceInfo_priceCents` | integer |
| `priceInfo_priceType` | string |
| `priceInfo_suppressZeroCents` | null |
| `price_info` | object |
| `priceCents` | integer |
| `priceNumeric` | integer |
| `priceType` | string |
| `priceTypeOriginal` | string |
| `currency` | string |
| `categoryId` | integer |
| `category_id` | integer |
| `category` | object |
| `searchCategory` | integer |
| `searchQuery` | string |
| `searchType` | string |
| `search_type` | string |
| `adType` | string |
| `priorityProduct` | string |
| `priority_product` | string |
| `reserved` | boolean |
| `thinContent` | boolean |
| `thin_content` | boolean |
| `videoOnVip` | boolean |
| `video_on_vip` | boolean |
| `urgencyFeatureActive` | boolean |

---

[← All scrapers](../../README.md)
