# AU & NZ Real Estate Agent OSINT Scraper

Build OSINT intelligence reports on real estate agents across Australia and New Zealand. Extract profiles, contacts, agency details, active listings, sales history, reviews and media mentions. Each report includes an evidence-backed 0–100 decision score. Structured JSON for AI agents, APIs and MCP.

**[Open AU & NZ Real Estate Agent OSINT Scraper on Apify](https://apify.com/abotapi/realestate-agent-osint?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~realestate-agent-osint/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "realestate", "suburbs": ["Applecross WA"], "country": "au", "maxItems": 10, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "AU"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` | string | Mode |
| `urls` | array | URLs |
| `agentQueries` | array | Agents by name (name  suburb) |
| `agentUrls` | array | Agent profile URLs (optional) |
| `suburbs` | array | Suburbs to sweep (optional) |
| `maxAgentsPerSuburb` | integer | Max agents per suburb |
| `country` | string | Country |
| `includeSoldHistory` | boolean | Full sold history |
| `includeReviews` | boolean | Reviews (agent level) |
| `includeLicenceCheck` | boolean | Licence & disciplinary check |
| `includeNetwork` | boolean | Co-listing network |
| `includeAgencyData` | boolean | Agency profile block |
| `includeCurrentListings` | boolean | Current listings |
| `includeAgentWebsites` | boolean | Agency website profiles |
| `includeMedia` | boolean | Media mentions |
| `includeAgencyEntity` | boolean | Agency business entity (Australia) |
| `aiAnalysis` | boolean | Deprecated option |
| `suburbLeaderboard` | boolean | Suburb leaderboard |
| `maxItems` | integer | Max results per run |
| `proxyConfiguration` | object | Proxy configuration |
| `maxRequestsPerMin` | integer | Max requests per minute |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/realestate-agent-osint?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `recordType` | string |
| `source` | list |
| `sourceUrl` | string |
| `fetchedAt` | string |
| `agentId` | string |
| `name` | string |
| `title` | string |
| `phones` | list |
| `phoneDetails` | list |
| `emails` | list |
| `emailDetails` | list |
| `agencyName` | string |
| `agencyGroup` | null |
| `officeAddress` | string |
| `socialLinks` | object |
| `socialLinkDetails` | list |
| `website` | null |
| `agencyProfileUrl` | string |
| `bio` | null |
| `bioSource` | null |
| `yearsExperienceStated` | null |
| `yearsExperienceEvidence` | null |
| `languages` | list |
| `specialities` | list |
| `agency` | object |
| `currentListings` | object |
| `nzStats` | list |
| `servicedSuburbs` | list |
| `nzRecentSales` | list |
| `mediaMentions` | list |
| `mentionLeads` | list |
| `memberships` | list |
| `suburbs` | list |
| `region` | string |
| `profileUrls` | list |
| `sourceIds` | object |
| `soldSummary` | object |
| `soldAnalysis` | object |
| `statistics` | object |
| `photo` | string |

---

[← All scrapers](../../README.md)
