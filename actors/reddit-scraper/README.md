# Reddit Scraper

Scrape Reddit posts, comments, and media from any subreddit or user profile — no login or API keys required. Search by keyword, sort by hot/new/top/rising, and optionally pull full comment threads and media URLs. Fast and resource-efficient.

**[Open Reddit Scraper on Apify](https://apify.com/abotapi/reddit-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~reddit-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"target": "python", "limit": 10, "sort": "new", "timeframe": "all", "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `target` * | string | Subreddit or Username |
| `isUser` | boolean | Is Username |
| `limit` | integer | Post Limit |
| `sort` | string | Sort By |
| `timeframe` | string | Timeframe (for 'top' sort) |
| `scrapeComments` | boolean | Scrape Comments |
| `commentsLimit` | integer | Comments Per Post |
| `extractMediaUrls` | boolean | Extract Media URLs |
| `downloadMedia` | boolean | Download Media Files |
| `proxy` | object | Proxy Configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/reddit-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `title` | string |
| `author` | string |
| `subreddit` | string |
| `created_utc` | string |
| `permalink` | string |
| `url` | string |
| `score` | integer |
| `upvote_ratio` | float |
| `num_comments` | integer |
| `num_crossposts` | integer |
| `selftext` | string |
| `post_type` | string |
| `is_nsfw` | boolean |
| `is_spoiler` | boolean |
| `flair` | string |
| `total_awards` | integer |
| `has_media` | boolean |
| `media_urls` | object |
| `type` | string |

---

[← All scrapers](../../README.md)
