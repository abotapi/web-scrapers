# Ip Location Check Scraper

Look up geographic locations for IP addresses. Supports batch lookups with country, city, subdivision, coordinates, and timezone data.

**[Open Ip Location Check Scraper on Apify](https://apify.com/abotapi/ip-location-check?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~ip-location-check/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"ipAddresses": ["8.8.8.8", "1.1.1.1"], "language": "en"}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `ipAddresses` * | array | IP Addresses |
| `language` | string | Language |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/ip-location-check?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `ip` | string |
| `country` | string |
| `countryCode` | string |
| `subdivision` | null |
| `city` | null |
| `postalCode` | null |
| `latitude` | float |
| `longitude` | float |
| `timezone` | string |
| `accuracyRadius` | integer |
| `success` | boolean |
| `error` | null |

---

[← All scrapers](../../README.md)
