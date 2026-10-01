# StepStone.de Scraper

Scrape StepStone.de jobs by keyword, location, filters, or URL. Extract 35+ fields including employer, logo, location, posting date, home-office status, and optional full descriptions, GPS, employment type, and company profiles.

**[Open StepStone.de Scraper on Apify](https://apify.com/abotapi/stepstone-de?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~stepstone-de/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Berlin"], "workType": "any", "contractType": "any", "datePosted": "0", "workFromHome": "any", "jobLanguage": "any", "experienceLevel": "any", "applyMethod": "any", "sortBy": "relevance", "maxListings": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "DE"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `keywords` | string | Keywords |
| `workType` | string | Working hours (Arbeitszeit) |
| `contractType` | string | Contract type (Vertragsart) |
| `datePosted` | string | Posted within (days) |
| `workFromHome` | string | Home office |
| `jobLanguage` | string | Job ad language |
| `experienceLevel` | string | Experience level |
| `applyMethod` | string | How you apply |
| `sortBy` | string | Sort by |
| `urls` | array | Search URLs |
| `fetchDetails` | boolean | Fetch full job details |
| `maxListings` | integer | Max jobs |
| `maxPages` | integer | Max pages per search |
| `maxResidentialRequests` | integer | Residential request cap |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/stepstone-de?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
| `brand` | string |
| `backend` | string |
| `sourceSearchUrl` | string |
| `jobId` | integer |
| `harmonisedId` | string |
| `jobUrl` | string |
| `applyUrl` | string |
| `sourceSite` | string |
| `title` | string |
| `datePosted` | string |
| `publishFromDate` | null |
| `publishToDate` | null |
| `employer` | object |
| `location` | object |
| `salary` | object |
| `workFromHome` | string |
| `labels` | list |
| `skills` | list |
| `textSnippet` | string |
| `crossPostedCount` | null |
| `isSponsored` | boolean |
| `isHighlighted` | boolean |
| `isTopJob` | boolean |
| `isTrafficFromPartner` | boolean |
| `partnership` | object |
| `travelTime` | null |
| `description` | null |
| `descriptionText` | null |
| `validThrough` | null |
| `employmentType` | null |
| `industry` | null |
| `directApply` | null |
| `applyType` | null |
| `jobLocationType` | null |
| `applicantLocationRequirements` | null |
| `externalId` | string |
| `contractType` | null |
| `workType` | null |
| `company` | null |

---

[← All scrapers](../../README.md)
