# AutoTrader UK Scraper

Pull structured vehicle listings from autotrader.co.uk at scale. Search by filters or use AutoTrader URLs. Returns price, make, model, year, mileage, full specs, finance, vehicle history check, photo gallery, and dealer contact details.

**[Open AutoTrader UK Scraper on Apify](https://apify.com/abotapi/autotrader?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~autotrader/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "channel": "cars", "postcode": "SW1A 1AA", "make": "BMW", "sellerType": "any", "writeoffStatus": "include", "priceSearchType": "total", "sortBy": "relevance", "maxPages": 1, "maxListings": 10, "proxy": {"useApifyProxy": true}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `channel` | string | Vehicle type |
| `postcode` | string | Postcode |
| `make` | string | Make |
| `model` | string | Model |
| `minPrice` | integer | Min price () |
| `maxPrice` | integer | Max price () |
| `minYear` | integer | Min year |
| `maxYear` | integer | Max year |
| `minMileage` | integer | Min mileage |
| `maxMileage` | integer | Max mileage |
| `fuelType` | string | Fuel type |
| `bodyType` | string | Body type |
| `transmission` | string | Transmission |
| `colour` | string | Colour |
| `drivetrain` | string | Drivetrain |
| `sellerType` | string | Seller type |
| `minEngineSize` | string | Min engine size (litres) |
| `maxEngineSize` | string | Max engine size (litres) |
| `doors` | integer | Doors |
| `seats` | integer | Seats |
| `radius` | integer | Search radius (miles) |
| `writeoffStatus` | string | Write-off status |
| `priceSearchType` | string | Price basis |
| `sortBy` | string | Sort order |
| `urls` | array | URLs |
| `fetchDetails` | boolean | Fetch full advert details |
| `includeFinanceGuides` | boolean | Include finance guide text |
| `maxPages` | integer | Max pages per search |
| `maxListings` | integer | Max listings (0  unlimited) |
| `proxy` | object | Proxy |
| `maxResidentialRequests` | integer | Residential usage cap |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/autotrader?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `advertId` | string |
| `url` | string |
| `channel` | string |
| `title` | string |
| `subTitle` | string |
| `attentionGrabber` | string |
| `make` | string |
| `model` | string |
| `vehicleCategory` | string |
| `year` | integer |
| `condition` | string |
| `mileage` | integer |
| `price` | integer |
| `priceFormatted` | string |
| `priceIndicator` | string |
| `priceIndicatorLabel` | null |
| `rrp` | null |
| `discount` | null |
| `hasFinance` | boolean |
| `monthlyPrice` | null |
| `financeProvider` | null |
| `financeInitialPayment` | null |
| `financeTermMonths` | null |
| `sellerType` | string |
| `dealerId` | string |
| `dealerName` | string |
| `dealerReviewRating` | float |
| `dealerReviewCount` | integer |
| `dealerLink` | string |
| `isManufacturerApproved` | boolean |
| `isFranchiseApproved` | boolean |
| `preReg` | boolean |
| `hasDigitalRetailing` | boolean |
| `vehicleLocation` | string |
| `distanceMiles` | integer |
| `latitude` | float |
| `longitude` | float |
| `images` | list |
| `numberOfImages` | integer |
| `badges` | list |

---

[← All scrapers](../../README.md)
