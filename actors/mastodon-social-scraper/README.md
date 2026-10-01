# Mastodon Scraper

Scrape trending Mastodon profiles and related posts from any Mastodon instance. Returns rich profile data, follower counts, bios, avatars, fields, and thread replies. Supports nested profile reviews or flat review output.

**[Open Mastodon Scraper on Apify](https://apify.com/abotapi/mastodon-social-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~mastodon-social-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "profiles", "instanceUrl": "https://mastodon.social", "profileSource": "both", "keywords": ["news"], "maxProfiles": 10, "maxReviewsPerProfile": 10, "maxReviews": 10, "maxPosts": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Output mode |
| `instanceUrl` | string | Mastodon instance |
| `profileSource` | string | Trending profile source |
| `onlyLocal` | boolean | Local accounts only |
| `urls` | array | Profile or post URLs (optional) |
| `keywords` | array | Keywords (keyword mode) |
| `includeReplies` | boolean | Include replies |
| `maxProfiles` | integer | Max profiles |
| `maxReviewsPerProfile` | integer | Max posts per profile |
| `maxRepliesPerPost` | integer | Max replies per post |
| `maxReviews` | integer | Max reviews (reviews mode) |
| `maxPosts` | integer | Max posts (keyword mode) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/mastodon-social-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `acct` | string |
| `username` | string |
| `displayName` | string |
| `bio` | string |
| `bioHtml` | string |
| `followersCount` | integer |
| `followingCount` | integer |
| `statusesCount` | integer |
| `url` | string |
| `avatar` | string |
| `header` | string |
| `bot` | boolean |
| `locked` | boolean |
| `group` | boolean |
| `discoverable` | boolean |
| `createdAt` | string |
| `lastStatusAt` | string |
| `fields` | list |
| `emojis` | list |
| `account` | object |
| `reviews` | list |
| `reviewCount` | integer |

---

[← All scrapers](../../README.md)
