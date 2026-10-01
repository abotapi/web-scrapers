# YouTube Transcript & Subtitle Scraper

Extract transcripts and subtitles from YouTube videos in bulk using video, playlist, channel URLs, or keyword search. Returns timed transcript segments, plain text, SRT, and WebVTT subtitle files, with optional auto-translation to other languages.

**[Open YouTube Transcript & Subtitle Scraper on Apify](https://apify.com/abotapi/youtube-transcript-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~youtube-transcript-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "url", "videoUrls": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"], "searchQueries": ["python tutorial"], "maxVideos": 10, "languages": ["en"], "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `videoUrls` | array | Video / playlist / channel URLs |
| `searchQueries` | array | Keyword searches |
| `startSec` | integer | Time window - start (seconds) |
| `durationSec` | integer | Time window - duration (seconds) |
| `maxVideosPerSource` | integer | Max videos per source |
| `maxVideos` | integer | Max videos (overall) |
| `languages` | array | Preferred transcript languages |
| `translateToLanguage` | string | Translate transcript to |
| `preserveFormatting` | boolean | Preserve text formatting |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/youtube-transcript-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `videoId` | string |
| `videoUrl` | string |
| `videoTitle` | string |
| `channelName` | string |
| `channelUrl` | string |
| `durationSeconds` | null |
| `source` | string |
| `sourceType` | string |
| `fetchedAt` | string |
| `success` | boolean |
| `error` | null |
| `language` | string |
| `languageCode` | string |
| `isGenerated` | boolean |
| `isTranslated` | boolean |
| `translatedTo` | null |
| `charCount` | integer |
| `segmentCount` | integer |
| `transcript` | string |
| `segments` | list |
| `srt` | string |
| `vtt` | string |
| `trimmedStart` | integer |
| `trimmedDuration` | integer |

---

[← All scrapers](../../README.md)
