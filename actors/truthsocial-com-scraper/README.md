# Truth Social Scraper

Scrape public Truth Social profiles, posts, media, metrics, author data, and complete source objects using profile URLs, post URLs, or search queries.

**[Open Truth Social Scraper on Apify](https://apify.com/abotapi/truthsocial-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~truthsocial-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"startUrls": [{"url": "https://truthsocial.com/@realDonaldTrump"}], "profileContentType": "postsAndReplies", "maxItems": 10, "maxPages": 1, "countryCode": "US", "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `startUrls` | array | Profile or post URLs |
| `profileContentType` | string | Profile content |
| `maxPostsPerProfile` | integer | Max posts/replies per profile |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages |
| `includeRaw` | boolean | Include source objects |
| `countryCode` | string | Residential country code |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/truthsocial-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `sourceQuery` | null |
| `postId` | string |
| `id` | string |
| `uri` | string |
| `postUrl` | string |
| `content` | string |
| `contentHtml` | string |
| `createdAt` | string |
| `editedAt` | null |
| `language` | string |
| `repliesCount` | integer |
| `reTruthsCount` | integer |
| `likesCount` | integer |
| `favouritesCount` | integer |
| `quotesCount` | null |
| `inReplyToId` | null |
| `inReplyToAccountId` | null |
| `sensitive` | boolean |
| `spoilerText` | string |
| `visibility` | string |
| `isReblog` | boolean |
| `rebloggedByAcct` | null |
| `media` | list |
| `mediaUrls` | list |
| `tags` | list |
| `mentions` | list |
| `poll` | null |
| `card` | null |
| `cardUrl` | null |
| `cardTitle` | null |
| `authorId` | string |
| `authorUsername` | string |
| `authorAcct` | string |
| `authorDisplayName` | string |
| `authorUrl` | string |
| `account` | object |
| `upvotesCount` | integer |
| `downvotesCount` | integer |
| `pinned` | boolean |

---

[← All scrapers](../../README.md)
