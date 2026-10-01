# Pocket Casts Podcast Scraper

Scrape Pocket Casts podcast data, including listener ratings, full episode archives, publishing cadence, seasons, transcript availability, direct audio URLs, regional category charts, and global episode search.

**[Open Pocket Casts Podcast Scraper on Apify](https://apify.com/abotapi/pocketcasts-podcast-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~pocketcasts-podcast-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "searchTerms": ["true crime"], "categories": ["comedy"], "region": "us", "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `searchTerms` | array | Search terms |
| `categories` | array | Categories |
| `region` | string | Region |
| `customRegion` | string | Custom region code (advanced) |
| `urls` | array | Podcast URLs or UUIDs |
| `maxPodcasts` | integer | Max podcasts |
| `maxEpisodes` | integer | Max episodes (episode search) |
| `maxEpisodesPerPodcast` | integer | Max episodes per podcast |
| `includeEpisodes` | boolean | Include episodes |
| `includeRatings` | boolean | Include ratings |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/pocketcasts-podcast-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `uuid` | string |
| `url` | string |
| `title` | string |
| `author` | string |
| `slug` | string |
| `description` | string |
| `descriptionHtml` | string |
| `category` | string |
| `explicit` | boolean |
| `showType` | string |
| `audioOnly` | boolean |
| `isPrivate` | boolean |
| `transcriptEligible` | boolean |
| `episodeFrequency` | string |
| `estimatedNextEpisodeAt` | string |
| `episodeCount` | integer |
| `hasSeasons` | boolean |
| `seasonCount` | integer |
| `hasMoreEpisodes` | boolean |
| `fundings` | list |
| `ratingAverage` | float |
| `ratingTotal` | integer |
| `feedUrl` | null |
| `itunesId` | null |
| `website` | null |
| `episodeCountReturned` | integer |
| `episodes` | list |

---

[← All scrapers](../../README.md)
