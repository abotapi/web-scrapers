# Zomato Scraper

Scrape restaurants and reviews from zomato.com. Get names, cuisines, ratings and votes, cost for two, address and coordinates, phone, per-vertical ratings, delivery info, plus per-review rating, author, date, text, photos and tags. Search a city feed or paste URLs.

**[Open Zomato Scraper on Apify](https://apify.com/abotapi/zomato-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~zomato-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "cities": ["ncr"], "context": "delivery", "maxReviews": 10, "reviewsSort": "popular", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `cities` | array | Cities |
| `context` | string | Feed |
| `query` | string | Keyword (optional) |
| `offersOnly` | boolean | Offers only |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch full details |
| `fetchReviews` | boolean | Fetch reviews |
| `maxReviews` | integer | Max reviews per restaurant |
| `reviewsSort` | string | Reviews sort |
| `maxItems` | integer | Max restaurants |
| `maxPages` | integer | Max pages per feed |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/zomato-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `name` | string |
| `url` | string |
| `cuisines` | list |
| `cuisineString` | string |
| `locality` | object |
| `costForTwoText` | string |
| `costText` | string |
| `rating` | object |
| `ratingsByVertical` | object |
| `timing` | object |
| `thumbnail` | string |
| `deliveryTime` | string |
| `hasOnlineOrdering` | boolean |
| `isServiceable` | boolean |
| `hasGold` | null |
| `distance` | string |
| `isPromoted` | boolean |
| `promoOffer` | string |
| `hasPromo` | boolean |
| `source` | string |
| `detailScraped` | boolean |
| `statusText` | string |
| `isDeliveryOnly` | boolean |
| `isPermanentlyClosed` | boolean |
| `isTemporarilyClosed` | boolean |
| `isOpeningSoon` | integer |
| `address` | string |
| `city` | string |
| `cityId` | integer |
| `country` | string |
| `zipcode` | string |
| `latitude` | float |
| `longitude` | float |
| `mapImageUrl` | string |
| `isDarkKitchen` | boolean |
| `phones` | list |
| `chainName` | string |
| `chainUrl` | string |
| `establishments` | null |

---

[← All scrapers](../../README.md)
