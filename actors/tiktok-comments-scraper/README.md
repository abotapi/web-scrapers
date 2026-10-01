# TikTok Comments Scraper

Scrape comments from TikTok videos using one or more video URLs or IDs. Extract comment text, author, likes, reply count and timestamp in clean structured data. Supports multiple videos in a single run with no login required.

**[Open TikTok Comments Scraper on Apify](https://apify.com/abotapi/tiktok-comments-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~tiktok-comments-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "videos", "usernames": ["tiktok"], "proxyTier": "datacenter", "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `videoUrls` | array | Video URLs or IDs |
| `usernames` | array | Usernames |
| `maxVideosPerUser` | integer | Max videos per username (search mode) |
| `minCommentLikes` | integer | Minimum comment likes |
| `commentKeyword` | string | Comment text contains |
| `excludeReplies` | boolean | Exclude replies |
| `commentsSinceDays` | integer | Only comments from the last N days |
| `fetchReplies` | boolean | Fetch replies |
| `maxRepliesPerComment` | integer | Max replies per comment |
| `replyPatienceSeconds` | integer | Seconds per reply page |
| `maxCommentsPerVideo` | integer | Max comments per video |
| `maxPagesPerVideo` | integer | Max pages per video |
| `pagePatienceSeconds` | integer | Seconds per page |
| `maxAttemptsPerPage` | integer | Max requests per page (optional ceilin |
| `concurrency` | integer | Parallel requests |
| `proxyTier` | string | Proxy tier |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/tiktok-comments-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `sourceMode` | string |
| `commentId` | string |
| `videoId` | string |
| `videoUrl` | string |
| `isReply` | boolean |
| `replyToCommentId` | null |
| `text` | string |
| `authorUsername` | string |
| `authorNickname` | string |
| `authorUid` | string |
| `authorAvatarUrl` | string |
| `authorRegion` | string |
| `diggCount` | integer |
| `replyCommentTotal` | null |
| `createTime` | integer |
| `createTimeIso` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
