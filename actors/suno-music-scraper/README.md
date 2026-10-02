# Suno Scraper

Collect public Suno music data: songs with lyrics, style tags, model version, play and like counts, audio, video and cover art links, plus playlist and creator records. Choose the curated Explore sections, specific playlists, or a creator's full public catalogue.

**[Open Suno Scraper on Apify](https://apify.com/abotapi/suno-music-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~suno-music-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "explore", "exploreFeeds": ["trending"], "profileSortBy": "upvote_count", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `exploreFeeds` | array | Sections to read (optional) |
| `playlistUrls` | array | Playlist links or ids |
| `profileUrls` | array | Profile links or handles |
| `profileSortBy` | string | Profile ordering |
| `followProfilePlaylists` | boolean | Also read the playlists linked on the  |
| `includeLyrics` | boolean | Include lyrics |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max pages per source |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/suno-music-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `url` | string |
| `title` | string |
| `createdAt` | string |
| `status` | string |
| `entityType` | string |
| `creatorHandle` | string |
| `creatorDisplayName` | string |
| `creatorUserId` | string |
| `creatorProfileUrl` | string |
| `creatorAvatarImageUrl` | string |
| `creatorIsVerified` | boolean |
| `playCount` | integer |
| `upvoteCount` | integer |
| `dislikeCount` | null |
| `commentCount` | integer |
| `flagCount` | integer |
| `durationSeconds` | float |
| `styleTags` | string |
| `displayTags` | list |
| `lyrics` | string |
| `modelName` | string |
| `modelVersion` | null |
| `isInstrumental` | null |
| `isRemix` | boolean |
| `canRemix` | boolean |
| `hasStems` | boolean |
| `generationType` | string |
| `isPublic` | boolean |
| `isExplicit` | boolean |
| `allowComments` | boolean |
| `hasHook` | boolean |
| `isContestEntry` | boolean |
| `imageUrl` | string |
| `imageLargeUrl` | string |
| `videoUrl` | string |
| `audioUrl` | string |
| `mediaUrls` | list |
| `albums` | list |

---

[← All scrapers](../../README.md)
