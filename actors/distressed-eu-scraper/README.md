# Europe Distressed Property Scraper

Distressed-property leads across Europe: German ZVG foreclosure auctions, Polish KRZ restructuring proceedings, and Spanish BOE judicial auctions in one run, with detail enrichment, resume, and incremental change tracking.

**[Open Europe Distressed Property Scraper on Apify](https://apify.com/abotapi/distressed-eu-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~distressed-eu-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "country": ["de"], "deLand": "be", "deSort": "2", "esAuctionStatus": "EJ", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `country` | array | Country lanes |
| `deLand` | string | DE State (required) |
| `deLands` | array | DE States (multi-select, optional) |
| `deCourt` | string | DE Court / place (optional) |
| `deObjectType` | string | DE Object type (optional) |
| `deStreet` | string | DE Street (optional) |
| `dePostalCode` | string | DE Postal code (optional) |
| `deCity` | string | DE City (optional) |
| `deAuctionType` | string | DE Auction type (optional) |
| `deAuctionDateFrom` | string | DE Auction date from (optional) |
| `deAuctionDateTo` | string | DE Auction date to (optional) |
| `deSort` | string | DE Sort order |
| `plEntityName` | string | PL Entity name |
| `plIdentifier` | string | PL Identifier (KRS/NIP/PESEL) |
| `plCaseSignature` | string | PL Case signature (optional) |
| `plSoleTraderName` | string | PL Sole trader business name (optional |
| `plFirstName` | string | PL First name (optional) |
| `plLastName` | string | PL Last name (optional) |
| `esAuctionStatus` | string | ES Auction status |
| `esDeadlineFrom` | string | ES Deadline from (optional) |
| `esDeadlineTo` | string | ES Deadline to (optional) |
| `esStartFrom` | string | ES Start from (optional) |
| `esStartTo` | string | ES Start to (optional) |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch detail pages |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search (0  unlimited) |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/distressed-eu-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `court` | string |
| `stateName` | string |
| `objectType` | string |
| `propertyType` | string |
| `areaSqm` | float |
| `areaBasis` | string |
| `pricePerSqmEur` | float |
| `daysUntilAuction` | integer |
| `isNewSinceLastRun` | null |
| `recordId` | string |
| `country` | string |
| `source` | string |
| `title` | string |
| `distressType` | string |
| `url` | string |
| `caseNumber` | string |
| `publishedAt` | string |
| `auctionDate` | string |
| `location` | object |
| `valueAmount` | integer |
| `valueCurrency` | string |
| `valueText` | string |
| `status` | string |
| `description` | string |
| `parties` | list |
| `attachments` | list |
| `raw` | object |
| `details` | object |

---

[← All scrapers](../../README.md)
