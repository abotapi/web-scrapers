# ViewStats Scraper

Scrape YouTube channel analytics from ViewStats. Look up channels by handle, URL, or keyword search. Returns subscribers, views, rankings, growth from weekly to all-time, revenue estimates, historical time series, longs vs shorts, featured video, and similar channels.

**[Open ViewStats Scraper on Apify](https://apify.com/abotapi/viewstats-channel-analytics?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~viewstats-channel-analytics/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "channels", "channels": ["@MrBeast"], "searchTerms": ["mrbeast"], "statsRange": "365", "statsGroupBy": "monthly", "maxItems": 10, "proxy": {"useApifyProxy": true}, "residentialCountries": ["US", "GB", "DE", "CA", "FR"]}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `channels` | array | Channels |
| `searchTerms` | array | Search terms |
| `maxChannelsPerSearch` | integer | Max channels per search term |
| `includeProfileDetails` | boolean | Include profile details |
| `includeSimilarChannels` | boolean | Include similar channels |
| `includeStatsTimeSeries` | boolean | Include daily/monthly time-series |
| `statsRange` | string | Time-series range |
| `statsGroupBy` | string | Time-series granularity |
| `maxItems` | integer | Max channels to output |
| `proxy` | object | Proxy |
| `residentialCountries` | array | Residential fallback countries |
| `maxResidentialRequests` | integer | Residential request budget |
| `backupProxyUrl` | string | Backup proxy URL |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/viewstats-channel-analytics?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `channelId` | string |
| `handle` | string |
| `displayName` | string |
| `url` | string |
| `youtubeUrl` | string |
| `verified` | boolean |
| `country` | string |
| `avatarUrl` | string |
| `bannerUrl` | string |
| `subscriberCount` | integer |
| `viewCount` | integer |
| `videoCount` | integer |
| `totalFollowing` | integer |
| `globalSubscribersRanking` | integer |
| `globalViewsRanking` | integer |
| `countrySubscriberRanking` | integer |
| `categorySubscriberRanking` | integer |
| `vpv90` | integer |
| `recentTests` | integer |
| `totalTests` | integer |
| `description` | string |
| `dateCreated` | string |
| `viewstatsRanking` | integer |
| `averages` | object |
| `uploadFrequencyPerMonth` | integer |
| `growth` | object |
| `estimatedRevenueLowUsdMonthly` | integer |
| `estimatedRevenueHighUsdMonthly` | integer |
| `longsAndShorts` | object |
| `featuredVideo` | object |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
