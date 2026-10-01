# Lemon8 Profile Scraper

Scrape Lemon8 user profiles with automated multi-profile discovery. Extract profile data, detailed posts, engagement metrics, comments, and high-quality images and videos with download support. Built for influencer research, content analysis, and media archiving.

**[Open Lemon8 Profile Scraper on Apify](https://apify.com/abotapi/lemon8-profile-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~lemon8-profile-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"username": "sydneydelreyy", "region": "us", "limit": 10, "proxy": {"useApifyProxy": true, "apifyProxyCountry": "US"}, "dev_dataset_name": "default"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `username` * | string | Username |
| `startUrls` | array | Start URLs |
| `profileUrl` | string | Profile URL |
| `region` | string | Region |
| `limit` | integer | Post Limit |
| `getDetails` | boolean | Get Detailed Post Data |
| `detailsLimit` | integer | Details Post Limit |
| `commentExpansionTimeout` | integer | Comment Expansion Timeout (seconds) |
| `getFollowing` | boolean | Scrape Following Profiles |
| `followingLimit` | integer | Following Profiles Limit |
| `saveImages` | boolean | Save Images |
| `saveVideos` | boolean | Save Videos |
| `proxy` | object | Proxy Configuration |
| `dev_transform_fields` | array | Transform Fields |
| `dev_dataset_name` | string | Custom Dataset Name |
| `dev_dataset_clear` | boolean | Clear Dataset Before Insert |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/lemon8-profile-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `author` | object |
| `title` | string |
| `content` | string |
| `postUrl` | string |
| `imageUrl` | string |
| `statistics` | object |
| `images` | list |
| `isVideo` | boolean |
| `videoData` | null |
| `details` | object |
| `allComments` | list |
| `comments` | list |
| `commentStats` | object |

---

[← All scrapers](../../README.md)
