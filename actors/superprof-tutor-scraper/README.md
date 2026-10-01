# Superprof Scraper

Scrape Superprof tutors by subject and location, or paste tutor URLs. One rich record per tutor: name, photo, price, rating, reviews count, subjects, city, geo, response time, lesson type and more. Filter by price, rating and lesson type.

**[Open Superprof Scraper on Apify](https://apify.com/abotapi/superprof-tutor-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~superprof-tutor-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "subjects": ["Mathematics"], "locations": ["United States"], "lessonType": "any", "sortBy": "relevance", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `subjects` | array | Subjects |
| `locations` | array | Locations |
| `urls` | array | Tutor or results URLs |
| `lessonType` | string | Lesson type |
| `minPrice` | integer | Min hourly price |
| `maxPrice` | integer | Max hourly price |
| `minRating` | integer | Min rating |
| `onlyWebcam` | boolean | Webcam tutors only |
| `onlyFirstLessonFree` | boolean | First lesson free only |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch full tutor profiles |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/superprof-tutor-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id_annonce` | string |
| `teacherName` | string |
| `title` | string |
| `url` | string |
| `landing_url` | string |
| `type` | string |
| `price` | integer |
| `price_1H` | integer |
| `prices` | object |
| `teacherCity` | string |
| `city` | string |
| `country` | null |
| `teacherPhoto` | string |
| `lat` | null |
| `lng` | null |
| `subjects` | list |
| `subjects_raw` | list |
| `badge` | string |
| `is_ambassador` | boolean |
| `is_available` | boolean |
| `search_url` | string |
| `sex` | string |
| `is_superprof` | boolean |
| `is_star` | boolean |
| `is_verified_member` | boolean |
| `stat_count_reviews` | integer |
| `stat_count_favorite` | null |
| `stat_count_total_links` | null |
| `stat_stars` | integer |
| `response_rate` | null |
| `response_time_sec` | integer |
| `offer_lesson_first_is_free` | boolean |
| `offer_lesson_first_lesson_duration` | string |
| `stat_count_recommendations` | integer |
| `status` | string |
| `price_5H` | integer |
| `price_10H` | integer |
| `price_webcam` | integer |
| `price_with_travel` | null |
| `offers` | list |

---

[← All scrapers](../../README.md)
