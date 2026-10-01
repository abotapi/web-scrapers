# Cars.com Scraper

Scrape cars.com listings by make, ZIP and radius. 90+ fields per car: price, MSRP, monthly payment, mileage, VIN, deal rating, price drop, photos, dealer name, rating and location. Search and URL modes, 11 sort orders, price/year/mileage filters, optional CARFAX flags and dealer phone.

**[Open Cars.com Scraper on Apify](https://apify.com/abotapi/cars-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~cars-com-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "makes": ["tesla"], "zip": "90001", "stockType": "all", "sortBy": "best_match_desc", "maxItems": 10, "maxPages": 1, "proxy": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"], "apifyProxyCountry": "US"}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `makes` | array | Makes |
| `models` | array | Models |
| `zip` | string | ZIP code |
| `maximumDistance` | integer | Search radius (miles) |
| `stockType` | string | Stock type |
| `priceMin` | integer | Minimum price (USD) |
| `priceMax` | integer | Maximum price (USD) |
| `yearMin` | integer | Minimum year |
| `yearMax` | integer | Maximum year |
| `mileageMax` | integer | Maximum mileage |
| `sortBy` | string | Sort by |
| `urls` | array | Cars.com URLs |
| `fetchDetails` | boolean | Fetch full details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per search |
| `proxy` | object | Proxy configuration |
| `maxResidentialMB` | integer | Residential traffic budget (MB) |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/cars-com-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `id` | string |
| `listingId` | string |
| `vin` | string |
| `url` | string |
| `listingUrl` | string |
| `searchUrl` | string |
| `title` | string |
| `year` | integer |
| `make` | string |
| `model` | string |
| `trim` | string |
| `model_trim` | string |
| `bodyStyle` | string |
| `mileage` | integer |
| `drivetrain` | string |
| `fuelType` | string |
| `fuel_type` | string |
| `exterior_color` | string |
| `interior_color` | null |
| `transmission` | null |
| `mpg_city` | null |
| `mpg_highway` | null |
| `stockType` | string |
| `cpoIndicator` | boolean |
| `price` | integer |
| `priceText` | null |
| `msrp` | integer |
| `monthlyPayment` | null |
| `price_drop` | null |
| `deal_rating` | null |
| `deal_badge_text` | null |
| `price_vs_market` | null |
| `shipPrice` | null |
| `shippingNote` | null |
| `isShippable` | boolean |
| `deliveryType` | null |
| `financingType` | string |
| `dealer` | object |
| `dealerName` | null |
| `dealer_name` | null |

---

[← All scrapers](../../README.md)
