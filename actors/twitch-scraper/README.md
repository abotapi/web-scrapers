# Twitch ALL IN ONE URL Scraper

Scrape Twitch data at scale, including channels, live streams, clips, VODs, and top games. Extract HLS m3u8 stream URLs, clip MP4 downloads in multiple qualities, chapter markers, and metadata. Supports keyword search with rich, analytics-ready output.

**[Open Twitch ALL IN ONE URL Scraper on Apify](https://apify.com/abotapi/twitch-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~twitch-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "channel", "channels": ["shroud"], "clipPeriod": "LAST_WEEK", "gameSlug": "valorant", "streamSort": "VIEWER_COUNT", "searchQuery": "valorant", "maxResults": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `channels` | array | Channel logins |
| `clipPeriod` | string | Clips period (clips mode) |
| `gameSlug` | string | Game slug |
| `streamSort` | string | Stream sort |
| `searchQuery` | string | Search query |
| `videoIds` | array | Video IDs |
| `urls` | array | URLs |
| `includeMediaUrls` | boolean | Include playable media URLs |
| `maxResults` | integer | Max results |
| `maxPages` | integer | Max pages |
| `proxyConfiguration` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/twitch-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `login` | string |
| `displayName` | string |
| `url` | string |
| `description` | string |
| `createdAt` | string |
| `profileImageUrl` | string |
| `bannerImageUrl` | string |
| `primaryColorHex` | string |
| `isPartner` | boolean |
| `isAffiliate` | boolean |
| `isStaff` | boolean |
| `isSiteAdmin` | boolean |
| `isGlobalMod` | boolean |
| `isExtensionsDeveloper` | boolean |
| `chanlets` | null |
| `followersCount` | integer |
| `isLive` | boolean |
| `broadcastTitle` | string |
| `broadcastLanguage` | string |
| `broadcastGameName` | string |
| `broadcastGameSlug` | string |
| `lastBroadcastTitle` | string |
| `lastBroadcastStartedAt` | string |
| `socialMedias` | list |
| `scrapedAt` | string |
| `streamId` | string |
| `title` | string |
| `viewersCount` | integer |
| `streamStartedAt` | string |
| `streamLanguage` | string |
| `streamType` | string |
| `gameName` | string |
| `gameSlug` | string |
| `gameId` | string |
| `boxArtUrl` | string |
| `thumbnailUrl` | string |
| `tags` | list |
| `streamHlsUrl` | string |

---

[← All scrapers](../../README.md)
