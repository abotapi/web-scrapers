# Spain Property & Judicial Auctions Scraper

Scrape Spain's official BOE auction portal: judicial and public auction listings with expediente, dates, claim amounts, valuations, minimum bids, deposits, authority contact, property lots and documents. Monitoring (NEW, UPDATED, EXPIRED), incremental runs, resume, MCP export.

**[Open Spain Property & Judicial Auctions Scraper on Apify](https://apify.com/abotapi/boe-es-auction-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo)** to run it without code and export JSON, CSV or Excel.

## Run it from code

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=<your token>   # https://console.apify.com/settings/integrations
python example.py
```

[`example.py`](example.py) starts a small run and prints the results. Or use plain HTTP, which runs and returns the items in one call:

```bash
curl -s -X POST "https://api.apify.com/v2/acts/abotapi~boe-es-auction-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"mode": "search", "estados": ["EJ"], "tipoBien": "I", "sortField": "SUBASTA.FECHA_FIN", "sortOrder": "asc", "maxItems": 10, "maxPages": 1, "proxyConfiguration": {"useApifyProxy": true, "apifyProxyGroups": ["RESIDENTIAL"]}}'
```

## Inputs

| Input | Type | What it is |
| --- | --- | --- |
| `mode` * | string | Mode |
| `estados` | array | Auction statuses |
| `fechaFinDesde` | string | Conclusion date from (YYYY-MM-DD) |
| `fechaFinHasta` | string | Conclusion date to (YYYY-MM-DD) |
| `fechaInicioDesde` | string | Start date from (YYYY-MM-DD) |
| `fechaInicioHasta` | string | Start date to (YYYY-MM-DD) |
| `tipoBien` | string | Asset type |
| `sortField` | string | Sort results by |
| `sortOrder` | string | Sort order |
| `valorMinimo` | string | Min auction value (EUR, optional) |
| `valorMaximo` | string | Max auction value (EUR, optional) |
| `provincia` | string | Province (optional) |
| `idSubasta` | string | Auction id filter (optional) |
| `startUrls` | array | Auction links |
| `urls` | array | Auction links (alias) |
| `fetchDetails` | boolean | Read auction details |
| `maxItems` | integer | Max items |
| `maxPages` | integer | Max pages per status (0  no cap) |
| `proxyConfiguration` | object | Proxy configuration |

`*` required

Full details on the [scraper page](https://apify.com/abotapi/boe-es-auction-scraper?utm_source=github&utm_medium=web-scrapers&utm_campaign=monorepo).

## Sample output

[`sample.json`](sample.json) is **mock data**: the same fields and types as real output, with made-up values.

| Field | Type |
| --- | --- |
| `idSub` | string |
| `titulo` | string |
| `estado` | string |
| `estadoDetalle` | string |
| `tipoSubasta` | string |
| `cuentaExpediente` | string |
| `expediente` | string |
| `fechaInicio` | string |
| `fechaConclusion` | string |
| `fechaFin` | string |
| `fechaPublicacion` | string |
| `cantidadReclamada` | string |
| `lotes` | string |
| `anuncioBOE` | string |
| `valorSubasta` | string |
| `tasacion` | string |
| `pujaMinima` | string |
| `tramos` | string |
| `deposito` | string |
| `descripcion` | string |
| `autoridadCodigo` | string |
| `autoridadDescripcion` | string |
| `autoridadDireccion` | string |
| `autoridadTelefono` | string |
| `autoridadFax` | string |
| `autoridadEmail` | string |
| `autoridad` | object |
| `bienes` | list |
| `documentos` | list |
| `pujasEstado` | string |
| `hasBids` | boolean |
| `provincia` | string |
| `localidad` | string |
| `direccion` | string |
| `codigoPostal` | string |
| `detailUrl` | string |

---

[← All scrapers](../../README.md)
