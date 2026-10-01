# Wattpad Scraper

Scrape Wattpad stories by keyword, tag, category, language or URL. Extract authors, reads, votes, tags, completion status and chapter lists, with optional chapter text, full comment threads, inline paragraph comments and replies.

**[Open Wattpad Scraper on Apify](https://apify.com/abotapi/wattpad-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~wattpad-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "query": "werewolf", "category": "any", "filter": "all", "language": "any", "commentScope": "all", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `query` | string | Search keyword |
| `category` | string | Category |
| `filter` | string | Completion state |
| `language` | string | Language |
| `startUrls` | array | Story or chapter links |
| `tags` | array | Keep only stories carrying these tags |
| `mature` | boolean | Include mature-flagged stories |
| `fetchChapters` | boolean | Include the chapter list |
| `fetchChapterText` | boolean | Also download the full chapter text |
| `fetchComments` | boolean | Also download the comment thread |
| `commentScope` | string | Which comments to keep |
| `maxCommentsPerStory` | integer | Max comments per story |
| `includeReplies` | boolean | Also fetch replies to each comment |
| `maxRepliesPerComment` | integer | Max replies per comment |
| `maxItems` | integer | Max results |
| `maxPages` | integer | Max result pages per scope |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/wattpad-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `storyId` | string |
| `title` | string |
| `url` | string |
| `description` | string |
| `coverUrl` | string |
| `author` | string |
| `authorUrl` | string |
| `createdAt` | string |
| `modifiedAt` | string |
| `isCompleted` | boolean |
| `isMature` | boolean |
| `rating` | integer |
| `language` | string |
| `categories` | list |
| `tags` | list |
| `numParts` | integer |
| `readCount` | integer |
| `voteCount` | integer |
| `commentCount` | integer |
| `wordCount` | integer |
| `copyright` | integer |
| `firstPartId` | string |
| `chapters` | list |
| `chaptersReturned` | integer |
| `scanComplete` | boolean |
| `scrapedAt` | string |
| `sourceUrl` | string |
| `enrichmentSkipped` | boolean |

---

[← All scrapers](../../README.md)
