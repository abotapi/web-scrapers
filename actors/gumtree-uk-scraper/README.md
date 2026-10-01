# Gumtree UK Scraper

Scrape gumtree.com classifieds across motors, property, jobs, services, pets and goods for sale. Extract titles, descriptions, prices, photos, locations, listing attributes, seller ratings, star distributions and reviews. Supports keyword, category, location and URL modes.

**[Open Gumtree UK Scraper on Apify](https://apify.com/abotapi/gumtree-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~gumtree-uk-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "category": "all", "location": "London", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | 1. Search mode |
| `urls` | array | Search or listing URLs (URL mode) |
| `category` | string | Category / vertical |
| `location` | string | Location |
| `keywords` | string | Keyword |
| `sortBy` | string | Sort order |
| `minPrice` | integer | Minimum price (GBP) |
| `maxPrice` | integer | Maximum price (GBP) |
| `fetchDetails` | boolean | Fetch full listing detail (description |
| `revealSellerPhone` | boolean | Also reveal the seller's phone number |
| `maxItems` | integer | Max listings |
| `maxPages` | integer | Max result pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/gumtree-uk-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `url` | string |
| `title` | string |
| `price` | integer |
| `priceText` | string |
| `currency` | string |
| `categoryId` | string |
| `l1CategoryId` | string |
| `l2CategoryId` | string |
| `categoryName` | null |
| `vertical` | string |
| `adItemType` | string |
| `location` | string |
| `distance` | string |
| `postedDate` | string |
| `postedTimestamp` | string |
| `shortDescription` | string |
| `status` | string |
| `urgent` | boolean |
| `featured` | boolean |
| `premium` | boolean |
| `standout` | boolean |
| `bumpup` | boolean |
| `hasVideo` | boolean |
| `images` | list |
| `imageCount` | integer |
| `numberOfImages` | integer |
| `favouriteCount` | integer |
| `proAccount` | boolean |
| `attributes` | list |
| `description` | string |
| `latitude` | integer |
| `longitude` | integer |
| `postcode` | null |
| `area` | string |
| `subArea` | string |
| `address` | string |
| `detailFetched` | boolean |
| `seller` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
