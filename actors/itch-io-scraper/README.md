# itch.io Game Scraper

Scrape itch.io games by genre, tag, platform, price band or keyword, plus creator catalogues and game jam results. Returns price and pay-what-you-want floor, rating, tags, platforms, files and the full review thread with creator replies. Incremental mode tracks changes.

**[Open itch.io Game Scraper on Apify](https://apify.com/abotapi/itch-io-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~itch-io-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "browse", "queries": ["horror"], "creators": ["gbpatch"], "jams": ["gmtk-2024"], "jamScope": "in-progress", "jamEntries": "any", "sortBy": "popular", "platform": "any", "price": "any", "maxReviewsPerGame": 10, "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search keywords |
| `creators` | array | Creators |
| `jams` | array | Jams |
| `jamScope` | string | Jam listing (used when no jams are nam |
| `urls` | array | Site links |
| `genres` | array | Genres |
| `tags` | array | Tags |
| `jamEntries` | string | Jam entries |
| `sortBy` | string | Sort by |
| `platform` | string | Platform |
| `price` | string | Price |
| `hasDemo` | boolean | Has a demo |
| `minRating` | integer | Minimum rating (0 to 5) |
| `minRatingCount` | integer | Minimum number of ratings |
| `fetchDetails` | boolean | Fetch details and reviews |
| `maxReviewsPerGame` | integer | Max reviews per game |
| `includeJamEntries` | boolean | Also return each jam's ranked results |
| `maxJamEntries` | integer | Max ranked entries per jam |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max result pages per scope |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/itch-io-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `gameId` | integer |
| `title` | string |
| `url` | string |
| `slug` | string |
| `developerName` | string |
| `developerUrl` | string |
| `developerSlug` | string |
| `developerId` | integer |
| `shortText` | string |
| `coverImageUrl` | string |
| `genre` | string |
| `platforms` | list |
| `rating` | null |
| `ratingCount` | null |
| `scrapedAt` | string |
| `sourceUrl` | string |
| `priceUsd` | null |
| `priceLabel` | null |
| `isOnSale` | boolean |
| `salePercent` | null |
| `recordId` | string |

---

[← All scrapers](../../README.md)
