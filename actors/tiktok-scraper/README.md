# TikTok Profile Scraper

Scrape TikTok without login. Extract profiles, bios, follower stats and videos; search by hashtag or keyword; scrape individual videos with full engagement stats; or collect posts from the current trending feed.

**[Open TikTok Profile Scraper on Apify](https://apify.com/abotapi/tiktok-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~tiktok-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "profile", "usernames": ["tiktok"], "queries": ["#fyp"], "maxItems": 10, "proxyTier": "residential", "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `usernames` | array | Usernames or profile URLs |
| `queries` | array | Hashtags or search keywords |
| `videoUrls` | array | Video URLs |
| `maxItems` | integer | Max results per unit |
| `proxyTier` | string | Proxy tier |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/tiktok-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `sourceMode` | string |
| `secUid` | string |
| `uniqueId` | string |
| `nickname` | string |
| `signature` | string |
| `avatarUrl` | string |
| `followerCount` | integer |
| `followingCount` | integer |
| `heartCount` | integer |
| `videoCount` | integer |
| `diggCount` | integer |
| `verified` | boolean |
| `privateAccount` | boolean |
| `region` | null |
| `bioLink` | string |
| `url` | string |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
