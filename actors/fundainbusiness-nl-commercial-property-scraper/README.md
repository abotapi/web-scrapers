# Funda in Business Scraper

Scrape Funda in Business commercial listings: offices, retail, industrial, catering and more. Full detail pages, pricing, floor areas, energy labels, coordinates, images, and agent/agency contacts with ratings. Dual search and URL modes, deep filters, and forward pagination.

**[Open Funda in Business Scraper on Apify](https://apify.com/abotapi/fundainbusiness-nl-commercial-property-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~fundainbusiness-nl-commercial-property-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["Amsterdam"], "propertyType": "all", "dealType": "both", "rentPriceBasis": "per_month", "publicationDate": "any", "parking": "any", "constructionType": "any", "auctionDate": "any", "openDay": "any", "sortBy": "relevance", "language": "nl", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `locations` | array | Locations |
| `propertyType` | string | Property type |
| `dealType` | string | Buy or rent |
| `keyword` | string | Keyword |
| `minPrice` | integer | Minimum price |
| `maxPrice` | integer | Maximum price |
| `rentPriceBasis` | string | Rent price basis |
| `minArea` | integer | Minimum floor area (m2) |
| `maxArea` | integer | Maximum floor area (m2) |
| `publicationDate` | string | Published within |
| `surrounding` | array | Surrounding context |
| `amenities` | array | Property features |
| `availability` | array | Availability signals |
| `parking` | string | Parking capacity |
| `constructionType` | string | Construction type |
| `propertyAge` | array | Construction period |
| `energyLabel` | array | Energy label |
| `auctionDate` | string | Auction timing |
| `openDay` | string | Open day |
| `includeSoldRented` | boolean | Include sold or rented listings |
| `sortBy` | string | Sort by |
| `urls` | array | URLs |
| `highlighted` | boolean | Only highlighted listings |
| `language` | string | Output language |
| `fetchDetails` | boolean | Fetch full detail pages |
| `includeAgencyDetails` | boolean | Include agency profile and reviews |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/fundainbusiness-nl-commercial-property-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `record_type` | string |
| `record_id` | string |
| `source_context` | object |
| `entity` | object |
| `listing` | object |
| `pricing` | object |
| `location` | object |
| `property` | object |
| `media` | object |
| `relationships` | object |
| `availability` | object |
| `attributes` | object |

---

[← All scrapers](../../README.md)
