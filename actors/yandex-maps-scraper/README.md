# Yandex Maps Scraper

Scrape Yandex Maps businesses and places by keyword or URL for lead generation, research and market analysis. Парсер Яндекс Карт: сбор данных о компаниях и местах по запросу или ссылке для поиска клиентов, исследований и анализа рынка.

**[Open Yandex Maps Scraper on Apify](https://apify.com/abotapi/yandex-maps-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~yandex-maps-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"searchStringsArray": ["restaurants"], "startUrls": [{"url": "https://yandex.com/maps/org/no_plates_coffee/124606085044/"}, {"url": "https://yandex.com/maps/org/124606085044/"}, {"url": "https://yandex.com/maps/org/no_plates_coffee/124606085044/reviews/"}, {"url": "https://yandex.ru/maps/org/no_plates_coffee/124606085044/"}, {"url": "https://yandex.com/maps/?ll=-74.006%2C40.7128&z=12&text=coffee"}, {"url": "https://yandex.com/maps/?text=restaurants"}, {"url": "https://yandex.com/maps/202/new-york/search/restaurants/"}, {"url": "https://yandex.com/maps/202/new-york/category/coffee_shop/"}, {"url": "https://yandex.com/maps/?ol=biz&oid=1018907821"}, {"url": "https://yandex.com/maps/213/moscow/search/%D0%BA%D0%BE%D1%84%D0%B5/"}, {"url": "https://yandex.com/maps/213/moscow/search/coffee/?page=2"}, {"url": "https://m.yandex.com/maps/org/192990200894/"}], "location": "New York, NY", "maxReviews": 10, "maxPosts": 10, "language": "en-US", "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `searchStringsArray` | array | Search Terms |
| `startUrls` | array | Start URLs |
| `location` | string | Location |
| `filters` | array | Result filters |
| `maxResultsPerSearch` | integer | Max Results Per Search |
| `maxPagesPerSearch` | integer | Max Pages Per Search |
| `includeRaw` | boolean | Include Raw Payload |
| `fetchDetails` | boolean | Business details & reviews |
| `maxReviews` | integer | Max reviews per business |
| `maxPhotos` | integer | Max photos per business |
| `maxPosts` | integer | Max posts per business |
| `includeMenu` | boolean | Full menu |
| `includeChainBranches` | boolean | Chain branch count |
| `language` | string | Language / Locale |
| `proxyConfiguration` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/yandex-maps-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `source` | string |
| `id` | string |
| `title` | string |
| `scrapedAt` | string |
| `searchString` | string |
| `rank` | integer |
| `url` | string |
| `address` | string |
| `addressParts` | object |
| `country` | string |
| `categoryName` | string |
| `categories` | list |
| `phone` | string |
| `phones` | list |
| `website` | string |
| `totalScore` | float |
| `reviewsCount` | integer |
| `photosCount` | integer |
| `photoUrls` | list |
| `logoUrl` | string |
| `seoname` | string |
| `reviews` | list |
| `location` | object |
| `description` | string |
| `shortTitle` | string |
| `status` | string |
| `geoId` | integer |
| `regionId` | integer |
| `region` | string |
| `city` | string |
| `street` | string |
| `house` | string |
| `timezoneOffset` | integer |
| `latitude` | float |
| `longitude` | float |
| `isOpenNow` | boolean |
| `isVerifiedOwner` | boolean |
| `socialLinks` | list |
| `nearbyMetro` | list |
| `nearbyStops` | list |

---

[← All scrapers](../../README.md)
