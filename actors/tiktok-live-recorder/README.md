# Tiktok Live Recorder Scraper

Record TikTok live streams to MP4 with full metadata, all stream quality URLs, and crash-resilient segmented recording, at a fraction of the cost.

**[Open Tiktok Live Recorder Scraper on Apify](https://apify.com/abotapi/tiktok-live-recorder?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~tiktok-live-recorder/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"username": "tiktok", "liveUrl": "https://www.tiktok.com/@tiktok/live"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `username` | string | Username |
| `roomId` | string | Room ID |
| `liveUrl` | string | Live URL |
| `duration` | integer | Max duration (seconds) |
| `segmentDuration` | number | Segment length (minutes) |
| `cookies` | object | TikTok session cookies |
| `proxyConfiguration` | object | Proxy & connection |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/tiktok-live-recorder?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `username` | string |
| `roomId` | string |
| `startedAt` | null |
| `endedAt` | null |
| `durationSeconds` | integer |
| `fileKey` | null |
| `fileSizeBytes` | integer |
| `status` | string |

---

[← All scrapers](../../README.md)
