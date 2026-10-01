# JobTeaser Scraper

Scrape early-career jobs and internships from JobTeaser across Europe. Search with 15 filters or use JobTeaser URLs. Returns title, company, employer profile, locations with coordinates, contract, salary, real external apply link, dates, and full description.

**[Open JobTeaser Scraper on Apify](https://apify.com/abotapi/jobteaser-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~jobteaser-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["data analyst"], "locale": "en", "radius": "30", "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "FR"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Keywords |
| `locale` | string | Site language |
| `location` | string | Location |
| `radius` | string | Radius (km) |
| `contract` | array | Contract types |
| `contractDuration` | array | Contract duration |
| `remoteTypes` | array | Remote work |
| `candidacyType` | string | Application flow |
| `studyLevels` | array | Level of study |
| `workExperience` | array | Experience |
| `companyBusinessType` | array | Company type |
| `companySectors` | array | Industries |
| `jobCategories` | array | Job categories |
| `languages` | array | Listing languages |
| `startDate` | array | Start dates |
| `jobWithImpact` | boolean | Companies with impact only |
| `startUrls` | array | URLs |
| `fetchDetails` | boolean | Fetch full job details |
| `includeCompanyDetails` | boolean | Include employer profiles |
| `maximizeCoverage` | boolean | Maximize coverage |
| `maxItems` | integer | Max results |
| `proxy` | object | Proxy |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/jobteaser-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `title` | string |
| `url` | string |
| `company` | object |
| `company_profile` | object |
| `company_taxonomy` | object |
| `primary_location` | object |
| `locations` | list |
| `google_locations` | list |
| `location_count` | integer |
| `has_multiple_locations` | boolean |
| `contract` | object |
| `classification` | object |
| `requirements` | object |
| `work_arrangement` | object |
| `compensation` | object |
| `application` | object |
| `application_flags` | object |
| `dates` | object |
| `status` | object |
| `search_metadata` | object |
| `listing_flags` | object |
| `content` | object |
| `media` | list |
| `platform_metadata` | object |
| `source_context` | object |

---

[← All scrapers](../../README.md)
