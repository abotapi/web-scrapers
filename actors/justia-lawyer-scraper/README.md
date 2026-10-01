# Justia Lawyer Profiles Scraper

Scrape attorney profiles from the Justia Lawyer Directory. Extract names, contacts, office locations, practice areas, education, experience, awards, bar admissions, peer endorsements and Justia Lawyer Ratings. Search by state, city, practice area or scrape profile URLs.

**[Open Justia Lawyer Profiles Scraper on Apify](https://apify.com/abotapi/justia-lawyer-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~justia-lawyer-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "states": ["California"], "practiceAreas": ["Personal Injury"], "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `states` | array | State(s) |
| `practiceAreas` | array | Practice area(s) |
| `cities` | array | City(s) |
| `startUrls` | array | Justia directory or profile URLs |
| `fetchDetails` | boolean | Fetch full profile details (richer rec |
| `fetchVcard` | boolean | Fetch vCard (structured contact data) |
| `minRating` | number | Min Justia rating |
| `freeConsultationOnly` | boolean | Free consultation only |
| `topRatedOnly` | boolean | Top-rated only |
| `maxPages` | integer | Max pages per list |
| `maxItems` | integer | Max results |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/justia-lawyer-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `type` | string |
| `id` | integer |
| `url` | string |
| `profileUrl` | string |
| `slug` | string |
| `name` | string |
| `telephones` | list |
| `freeConsultation` | boolean |
| `topRated` | boolean |
| `profileImage` | string |
| `servingLocationText` | null |
| `scrapedAt` | string |
| `jobTitle` | string |
| `jobTitles` | list |
| `yearsOfExperience` | integer |
| `headerFacts` | list |
| `primaryPhone` | string |
| `emailContactUrl` | string |
| `vcardUrl` | null |
| `badges` | list |
| `claimedProfile` | boolean |
| `offersVideoConferencing` | boolean |
| `connectPro` | boolean |
| `liiPlatinum` | boolean |
| `hasSocialMedia` | boolean |
| `biography` | string |
| `practiceAreas` | null |
| `additionalPracticeAreas` | list |
| `videoConferencing` | null |
| `fees` | null |
| `contingentFees` | boolean |
| `jurisdictions` | null |
| `languages` | null |
| `experience` | null |
| `education` | null |
| `awards` | null |
| `associations` | null |
| `speakingEngagements` | null |
| `certifications` | null |
| `publications` | null |

---

[← All scrapers](../../README.md)
