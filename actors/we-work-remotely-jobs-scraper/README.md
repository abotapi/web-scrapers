# We Work Remotely Scraper

Extract current remote job listings from weworkremotely.com. Use keyword search or WWR feed, category, and remote-jobs URLs. Returns clean job rows with title, company, category, region, tags, salary text, description matches, and filtered structured output.

**[Open We Work Remotely Scraper on Apify](https://apify.com/abotapi/we-work-remotely-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~we-work-remotely-jobs-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "keyword", "searchTerms": ["python"], "categories": ["all"], "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Input mode |
| `startUrls` | array | We Work Remotely URLs |
| `searchTerms` | array | Keyword search terms |
| `categories` | array | Categories |
| `regions` | array | Region filters |
| `includeDetails` | boolean | Include full description fields |
| `maxItems` | integer | Max items |
| `postedWithinDays` | integer | Posted within days |
| `requireSalary` | boolean | Require salary |
| `requireCompanyWebsite` | boolean | Require company website |
| `requireApplyUrl` | boolean | Require apply URL |
| `minDescriptionLength` | integer | Minimum description length |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/we-work-remotely-jobs-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `rowType` | string |
| `jobId` | string |
| `jobSlug` | string |
| `rawTitle` | string |
| `title` | string |
| `companyName` | string |
| `url` | string |
| `canonicalUrl` | string |
| `listingDomain` | string |
| `applyUrl` | string |
| `applicationUrl` | string |
| `externalApplyUrl` | null |
| `applyUrlIsExternal` | boolean |
| `applyUrlDomain` | string |
| `companyWebsiteUrl` | string |
| `companyWebsiteDomain` | string |
| `companyLogoUrl` | null |
| `headquarters` | string |
| `locationText` | string |
| `region` | string |
| `regionSlug` | string |
| `country` | null |
| `state` | null |
| `isRemote` | boolean |
| `isWorldwide` | boolean |
| `jobType` | null |
| `employmentType` | null |
| `category` | string |
| `categorySlug` | string |
| `skills` | list |
| `skillsRaw` | null |
| `skillsSource` | null |
| `skillsCount` | integer |
| `technologies` | list |
| `tags` | list |
| `seniorityLevel` | string |
| `postedAt` | string |
| `postedAtText` | string |
| `postedAgeDays` | integer |
| `expiresAt` | null |

---

[← All scrapers](../../README.md)
