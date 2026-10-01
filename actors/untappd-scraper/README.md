# Untappd Beer Scraper

Scrape Untappd beers, breweries, venues and check-ins by keyword, brewery, Top Rated chart or pasted link. Returns rating, rating count, style, ABV, IBU, brewery, check-in counters and recent check-ins with comments. Incremental mode tracks changes.

**[Open Untappd Beer Scraper on Apify](https://apify.com/abotapi/untappd-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~untappd-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "entityType": "beer", "queries": ["hazy ipa"], "breweries": ["Dogfish Head Craft Brewery"], "sortBy": "popularity", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `entityType` | string | What to search for |
| `queries` | array | Search keywords |
| `breweries` | array | Breweries |
| `includeBreweryBeers` | boolean | Also return every beer the brewery mak |
| `urls` | array | Site links |
| `styles` | array | Beer styles |
| `country` | string | Country |
| `minRating` | integer | Minimum rating (0 to 5) |
| `minRatingCount` | integer | Minimum number of ratings |
| `minAbv` | integer | Minimum ABV (%) |
| `maxAbv` | integer | Maximum ABV (%) |
| `inProductionOnly` | boolean | Only beers still in production |
| `excludeHomebrew` | boolean | Exclude homebrew |
| `minCheckins` | integer | Minimum total check-ins |
| `sortBy` | string | Sort by |
| `fetchDetails` | boolean | Fetch details and check-ins |
| `maxCheckinsPerEntity` | integer | Max check-ins per record |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max result pages per keyword, brewery  |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/untappd-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `entityType` | string |
| `beerId` | integer |
| `name` | string |
| `slug` | string |
| `url` | string |
| `style` | string |
| `styleId` | integer |
| `parentStyleId` | integer |
| `abv` | float |
| `ibu` | integer |
| `rating` | float |
| `ratingCount` | integer |
| `popularity` | integer |
| `inProduction` | boolean |
| `isHomebrew` | boolean |
| `hasCommunityAward` | boolean |
| `thcMg` | null |
| `cbdMg` | null |
| `labelImage` | string |
| `labelImageHd` | string |
| `breweryId` | integer |
| `breweryName` | string |
| `breweryUrl` | string |
| `breweryLabelImage` | string |
| `breweryLatitude` | float |
| `breweryLongitude` | float |
| `alsoKnownAs` | list |
| `chartRank` | null |
| `sourceUrl` | null |
| `scrapedAt` | string |
| `recordId` | string |

---

[← All scrapers](../../README.md)
