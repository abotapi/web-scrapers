# ThomasNet Scraper

Scrape ThomasNet suppliers and manufacturers by keyword, category, location, certification or company type, or paste profile URLs. Get one rich record per company with contacts, certifications, products, locations, coordinates, social links, sales data and more.

**[Open ThomasNet Scraper on Apify](https://apify.com/abotapi/thomasnet-supplier-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~thomasnet-supplier-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "queries": ["valves"], "area": "NA", "sortBy": "relevance", "maxPages": 1, "maxItems": 10, "proxy": {"useApifyProxy": true, "apifyProxyGroups": []}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `queries` | array | Search terms |
| `state` | string | State / region (optional) |
| `area` | string | Area (optional) |
| `zip` | string | ZIP / postal code (optional) |
| `radius` | integer | Radius (miles, optional) |
| `certification` | string | Certification filter (optional) |
| `companyType` | string | Company type |
| `sortBy` | string | Sort by |
| `excludeIds` | array | Exclude supplier IDs (optional) |
| `urls` | array | Company or search URLs |
| `fetchDetails` | boolean | Fetch full company profiles |
| `includeWebsiteContacts` | boolean | Also read each company's own website f |
| `maxPages` | integer | Max pages per search |
| `maxItems` | integer | Max items |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/thomasnet-supplier-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `__typename` | null |
| `additionalInformation` | list |
| `address` | object |
| `ads` | null |
| `affiliatedMemberOf` | null |
| `affiliationCompanyLabel` | null |
| `affiliationContactUrl` | null |
| `affiliationFeaturedMembers` | null |
| `annualSales` | string |
| `brands` | list |
| `catalogType` | string |
| `certificationTotals` | list |
| `certifications` | list |
| `companyAd` | null |
| `description` | string |
| `descriptionByCompany` | string |
| `families` | list |
| `heading` | object |
| `headingBrands` | null |
| `headings` | null |
| `isAdvertiser` | boolean |
| `isAffiliationPage` | boolean |
| `isClaimed` | boolean |
| `isMultiLocation` | boolean |
| `isTopResponder` | boolean |
| `locationTypes` | list |
| `locations` | list |
| `logoTitle` | string |
| `logoUrl` | string |
| `mainLocationName` | string |
| `mainLocationTgramsId` | string |
| `name` | string |
| `news` | list |
| `numberEmployees` | string |
| `otherActivities` | list |
| `otherHeadings` | null |
| `personnel` | list |
| `premiums` | null |
| `primaryPhone` | string |
| `products` | list |

---

[← All scrapers](../../README.md)
