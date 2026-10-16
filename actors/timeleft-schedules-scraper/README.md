# Timeleft Scraper

Scrape Timeleft (timeleft.com) event schedules across 200 cities: dinners, drinks, coffees, runs, walks and brunches with dates, zones, group sizes, booking cutoffs and booking headcounts. Self-registers a free app account; no subscription needed for schedules.

**[Open Timeleft Scraper on Apify](https://apify.com/abotapi/timeleft-schedules-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~timeleft-schedules-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"cities": ["Paris", "New York", "London"], "eventTypes": ["dinner", "drinks"], "maxItems": 10, "accountKey": "default", "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `cities` | array | Cities |
| `eventTypes` | array | Event types |
| `maxItems` | integer | Max items |
| `fetchHeadcounts` | boolean | Fetch booking headcounts |
| `accountKey` | string | Account key |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/timeleft-schedules-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `dayEventId` | string |
| `city` | string |
| `country` | string |
| `cityLatitude` | float |
| `cityLongitude` | float |
| `cityUserCount` | integer |
| `cityImageUrl` | string |
| `date` | string |
| `dateISO` | string |
| `eventType` | string |
| `eventCode` | string |
| `tags` | string |
| `status` | string |
| `zoneId` | string |
| `dayUsersBooked` | integer |
| `groupSize` | integer |
| `maxParticipants` | null |
| `genderMix` | string |
| `ageRestrictions` | integer |
| `payment` | string |
| `waitlistOnlyGenders` | string |
| `hasBookingGate` | boolean |
| `partnerImageUrl` | string |
| `bookingCutoffISO` | string |
| `isAfterBookingCutoff` | boolean |
| `lateBookingWaitlistEligible` | boolean |
| `isFreeForMe` | boolean |
| `coverPath` | string |
| `coverUrl` | string |
| `introTitle` | string |
| `introDescription` | string |
| `canShare` | boolean |
| `scrapedAt` | string |

---

[← All scrapers](../../README.md)
