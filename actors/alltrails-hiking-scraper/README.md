# AllTrails Hiking Scraper

Scrape AllTrails, the world's largest hiking platform: trails with difficulty, length, elevation gain, route type, ratings, review counts, dog and kid friendly attributes, trail conditions and hiker reviews. Browse any region or paste links, with recurring change monitoring.

**[Open AllTrails Hiking Scraper on Apify](https://apify.com/abotapi/alltrails-hiking-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~alltrails-hiking-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "regionPath": "California", "tags": ["backpacking"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["UNBLOCKER"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Collection mode |
| `regionPath` | string | Region to browse |
| `tags` | array | Trail tag grids |
| `urls` | array | Grid or trail links |
| `followSubGrids` | boolean | Follow additional grids |
| `fetchDetails` | boolean | Read trail details and reviews |
| `fetchPhotos` | boolean | Fetch community photos |
| `maxPhotos` | integer | Maximum photos per trail |
| `storeTracksInKV` | boolean | Save GPS tracks to key-value store |
| `difficulty` | array | Difficulty filter |
| `minRating` | number | Minimum rating |
| `minReviews` | integer | Minimum review count |
| `activityFilter` | array | Activities |
| `routeTypeFilter` | array | Route types |
| `lengthMin` | number | Minimum length (metres) |
| `lengthMax` | number | Maximum length (metres) |
| `elevationGainMin` | number | Minimum elevation gain (metres) |
| `elevationGainMax` | number | Maximum elevation gain (metres) |
| `featuresFilter` | array | Trail features |
| `maxItems` | integer | Maximum trail records |
| `maxPages` | integer | Maximum grid pages |
| `proxyConfiguration` | object | Connection settings |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/alltrails-hiking-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `name` | string |
| `url` | string |
| `slug` | string |
| `difficulty` | string |
| `difficultyGrade` | integer |
| `rating` | float |
| `ratingCount` | integer |
| `reviewTextCount` | integer |
| `lengthMeters` | float |
| `lengthMiles` | float |
| `elevationGainMeters` | float |
| `durationMinutes` | integer |
| `routeType` | string |
| `activities` | list |
| `features` | list |
| `areaName` | string |
| `areaSlug` | string |
| `cityName` | string |
| `stateName` | string |
| `countryName` | string |
| `lat` | float |
| `lng` | float |
| `imageUrl` | string |
| `sourceType` | string |
| `sourceUrl` | string |
| `position` | integer |
| `scrapedAt` | string |
| `photos` | list |

---

[← All scrapers](../../README.md)
