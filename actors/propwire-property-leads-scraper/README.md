# Propwire Scraper

Scrape Propwire.com: 157M+ US MLS & off-market properties with owner names, mailing addresses, equity, foreclosure and auction details, mortgages, transfers, owner portfolios, tax and full MLS records. Filter by lead type, property type, value, year built, sale date and MLS status.

**[Open Propwire Scraper on Apify](https://apify.com/abotapi/propwire-property-leads-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~propwire-property-leads-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"addressMatchMode": "first", "startUrls": ["https://propwire.com/realestate/4055-Britt-Rd-Mount-Dora-FL/51608674/property-details", "https://propwire.com/search?filters=%7B%22locations%22%3A%20%5B%7B%22state%22%3A%20%22FL%22%7D%5D%7D", "https://propwire.com/realestate/4055-Britt-Rd-Mount-Dora-FL/51608674", "https://propwire.com/realestate/x/51608674/property-details", "https://propwire.com/realestate/4055-Britt-Rd-Mount-Dora-FL/51608674/property-details?foo=bar", "https://www.propwire.com/realestate/4055-Britt-Rd-Mount-Dora-FL/51608674/property-details", "http://propwire.com/realestate/4055-Britt-Rd-Mount-Dora-FL/51608674/property-details", "https://propwire.com/search?filters=%7B%22locations%22%3A%20%5B%7B%22state%22%3A%20%22FL%22%7D%5D%7D&page=2"], "searchStates": ["FL"], "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `addresses` | array | Addresses or APNs (address lookup mode |
| `addressMatchMode` | string | When several properties match one addr |
| `startUrls` | array | Links (links mode) |
| `searchStates` | array | States |
| `searchLocations` | array | Cities, ZIPs or counties (optional) |
| `searchLeadTypes` | array | Lead types |
| `searchPropertyTypes` | array | Property types |
| `searchEstimatedValueMin` | integer | Min estimated value () |
| `searchEstimatedValueMax` | integer | Max estimated value () |
| `searchYearBuiltMin` | integer | Year built from |
| `searchYearBuiltMax` | integer | Year built to |
| `searchSoldSince` | string | Last sold on or after |
| `searchOwnerType` | array | Owner type |
| `searchMlsStatus` | string | MLS status |
| `fetchDetails` | boolean | Full property records |
| `maxItems` | integer | Max records |
| `maxPages` | integer | Max pages per search |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/propwire-property-leads-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `id` | integer |
| `active` | boolean |
| `borrower_name` | string |
| `case_number` | string |
| `default_amount` | integer |
| `foreclosure_id` | integer |
| `foreclosure_type` | string |
| `lender_name` | string |
| `judgment_amount` | integer |
| `notice_type` | string |
| `notice_type_code` | string |
| `opening_bid` | integer |
| `original_loan_amount` | integer |
| `recording_date` | string |
| `trustee_address` | string |
| `trustee_name` | string |
| `trustee_phone` | string |
| `assessment_year` | integer |
| `assessed_total_value` | integer |
| `assessed_improvement_value` | integer |
| `assessed_land_value` | integer |
| `assessed_improvement_percentage` | integer |
| `previous_assessed_total_value` | integer |
| `market_total_value` | integer |
| `market_land_value` | integer |
| `market_improvement_value` | integer |
| `market_improvement_percentage` | integer |
| `tax_billed_amount` | string |
| `tax_year` | integer |
| `apn_unformatted` | string |
| `area_lot_depth` | integer |
| `area_lot_width` | integer |
| `census_block` | integer |
| `census_block_group` | integer |
| `census_tract` | integer |
| `land_use` | string |
| `legal_description` | string |
| `lot_number` | string |
| `lot_size_sf` | integer |

---

[← All scrapers](../../README.md)
