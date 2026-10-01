# Dzen.ru Scraper

Scrape Dzen.ru (ex Yandex.Zen): articles, videos and channels. Full article text with likes and comment counts, channel subscriber counts with their on-page publications, video metadata. Paste any Dzen link; incremental mode reports only new and changed content.

**[Open Dzen.ru Scraper on Apify](https://apify.com/abotapi/dzen-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~dzen-ru-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "feed", "searchQueries": ["грибы"], "searchType": "all", "channelSort": "newest", "channelContent": "articles", "commentsSort": "top", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyCountry": "RU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `searchQueries` | array | Search queries |
| `searchType` | string | Result type |
| `urls` | array | Dzen URLs |
| `channelSort` | string | Channel order (channel links) |
| `channelContent` | string | Channel content (channel links) |
| `fetchArticleText` | boolean | Full article text (channel links) |
| `includeComments` | boolean | Include comments |
| `maxCommentsPerPost` | integer | Max comments per post |
| `commentsSort` | string | Comment order |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max feed / search pages |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/dzen-ru-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `dzenType` | string |
| `title` | string |
| `url` | string |
| `publicationDate` | null |
| `textPreview` | string |
| `textContent` | string |
| `images` | list |
| `authorName` | string |
| `authorUrl` | null |
| `subscribers` | null |
| `likes` | integer |
| `commentsCount` | integer |
| `views` | null |
| `videoUrl` | null |
| `coverImage` | null |
| `verified` | boolean |
| `detailFetched` | boolean |
| `isPremium` | null |
| `timeToReadSeconds` | null |
| `shareUrl` | null |
| `commentsLink` | null |
| `comments` | list |

---

[← All scrapers](../../README.md)
