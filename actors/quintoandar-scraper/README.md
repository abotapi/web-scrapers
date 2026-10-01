# QuintoAndar Scraper

Scrape QuintoAndar property listings across Brazil with 80+ fields, including rent, sale price, condo fees, IPTU, area, rooms, parking, GPS, photos, amenities, and descriptions. Supports search, URLs, sorting, and price, area, and bedroom filters.

**[Open QuintoAndar Scraper on Apify](https://apify.com/abotapi/quintoandar-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~quintoandar-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "locations": ["São Paulo"], "operationType": "rent", "propertyType": "all", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Search mode |
| `locations` | array | Locations |
| `operationType` | string | Operation |
| `propertyType` | string | Property type |
| `minPrice` | integer | Min price |
| `maxPrice` | integer | Max price |
| `minArea` | integer | Min area (m2) |
| `maxArea` | integer | Max area (m2) |
| `minBedrooms` | integer | Min bedrooms |
| `sortBy` | string | Sort order |
| `urls` | array | Results-page URLs |
| `fetchDetails` | boolean | Fetch full detail from each property p |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings |
| `proxy` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/quintoandar-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | integer |
| `idImovel` | integer |
| `listingId` | integer |
| `url` | string |
| `from_url` | string |
| `fonte` | string |
| `source` | string |
| `propertyType` | string |
| `type` | string |
| `typology` | string |
| `tipoImovel` | string |
| `tipoOperacao` | string |
| `operation` | string |
| `modo` | string |
| `business_context` | string |
| `businessContext` | string |
| `forRent` | boolean |
| `forSale` | boolean |
| `for_rent` | boolean |
| `for_sale` | boolean |
| `is_secondary_house` | boolean |
| `isSecondaryHouse` | boolean |
| `isPrimaryMarket` | boolean |
| `is_primary_market` | boolean |
| `disponivel` | boolean |
| `availability` | string |
| `status` | string |
| `visit_status` | string |
| `visitStatus` | string |
| `currency` | string |
| `rent` | integer |
| `rent_price` | integer |
| `rentPrice` | integer |
| `precoAluguel` | integer |
| `salePrice` | integer |
| `sale_price` | integer |
| `precoVenda` | integer |
| `totalCost` | integer |
| `total_cost` | integer |
| `precoTotalMensal` | integer |

---

[← All scrapers](../../README.md)
