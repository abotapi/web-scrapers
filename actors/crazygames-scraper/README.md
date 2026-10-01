# CrazyGames Scraper

Scrape CrazyGames games with ratings, upvotes and downvotes, total plays and likes, developer, category and tags, descriptions, controls, FAQ, release and update dates, platform support, multiplayer info and store links. Search by keyword, browse categories or the full catalogue, or paste links.

**[Open CrazyGames Scraper on Apify](https://apify.com/abotapi/crazygames-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~crazygames-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["car"], "sortBy": "popular", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search keywords |
| `categories` | array | Categories or tags |
| `sortBy` | string | Sort order |
| `minRating` | number | Minimum rating |
| `minTotalPlays` | integer | Minimum total plays |
| `minReleaseYear` | integer | Released in or after year |
| `multiplayerOnly` | boolean | Multiplayer games only |
| `mobileFriendlyOnly` | boolean | Mobile-friendly games only |
| `originalsOnly` | boolean | CrazyGames Originals only |
| `hotOnly` | boolean | Hot games only |
| `urls` | array | CrazyGames links |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `fetchDetails` | boolean | Include full game details |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/crazygames-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `name` | string |
| `slug` | string |
| `url` | string |
| `rating` | float |
| `upvotes` | integer |
| `downvotes` | integer |
| `ratingCount` | integer |
| `totalLikes` | integer |
| `totalPlays` | integer |
| `developer` | string |
| `developerId` | string |
| `category` | string |
| `categorySlug` | string |
| `tags` | list |
| `hierarchy` | list |
| `collection` | string |
| `descriptionFirst` | string |
| `descriptionRest` | string |
| `metaDescription` | string |
| `controls` | string |
| `faq` | list |
| `addedOn` | string |
| `basicLaunchOn` | string |
| `releaseYear` | integer |
| `lastFileUpdatedOn` | string |
| `lastSignificantUpdatedOn` | string |
| `loaderType` | string |
| `loaderTypeLabel` | string |
| `technology` | string |
| `orientation` | string |
| `status` | string |
| `isKids` | boolean |
| `isOriginal` | boolean |
| `hasIap` | boolean |
| `gameThumbLabels` | list |
| `mobileFriendly` | boolean |
| `iosFriendly` | boolean |
| `androidFriendly` | boolean |
| `iosAppFriendly` | boolean |

---

[← All scrapers](../../README.md)
