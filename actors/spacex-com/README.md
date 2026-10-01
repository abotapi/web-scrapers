# SpaceX Launches Scraper

Pull the full SpaceX launch catalog from spacex.com in clean JSON. Filter by vehicle, mission type, status, launch site, or date range. Returns vehicle, mission status, sites, date/time, images, mission links, and optional write-ups, webcasts, timelines, and carousel imagery.

**[Open SpaceX Launches Scraper on Apify](https://apify.com/abotapi/spacex-com?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~spacex-com/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "statusFilter": "all", "sortBy": "date-desc", "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `vehicle` | string | Vehicle |
| `missionType` | string | Mission type |
| `statusFilter` | string | Launch status |
| `launchSiteContains` | string | Launch site contains |
| `dateFrom` | string | Launch date from |
| `dateTo` | string | Launch date to |
| `sortBy` | string | Sort by |
| `urls` | array | Mission URLs |
| `fetchDetails` | boolean | Fetch mission details |
| `maxListings` | integer | Max launches |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/spacex-com?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `documentId` | string |
| `correlationId` | string |
| `endDate` | null |
| `endTime` | null |
| `title` | string |
| `shortTitle` | null |
| `link` | string |
| `callToAction` | string |
| `missionStatus` | string |
| `vehicle` | string |
| `returnSite` | string |
| `launchSite` | string |
| `launchDate` | string |
| `launchTime` | string |
| `missionType` | string |
| `directToCell` | boolean |
| `isLive` | boolean |
| `returnDateTime` | null |
| `showLaunchTimeInsteadOfWindow` | string |
| `imageDesktop` | object |
| `imageMobile` | object |
| `ongoingMissionImageDesktop` | null |
| `ongoingMissionImageMobile` | null |
| `videoDesktop` | null |
| `videoMobile` | null |
| `override` | object |
| `missionId` | string |
| `url` | string |
| `launchDateTime` | string |
| `imageDesktopUrl` | string |
| `imageMobileUrl` | string |
| `ongoingMissionImageDesktopUrl` | null |
| `ongoingMissionImageMobileUrl` | null |
| `hasDetails` | boolean |
| `videoDesktopUrl` | null |
| `videoMobileUrl` | null |
| `videoUrls` | list |
| `primaryVideoUrl` | null |

---

[← All scrapers](../../README.md)
