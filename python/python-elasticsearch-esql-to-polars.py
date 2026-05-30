#!/usr/bin/env python3

# ES|QL references
# https://www.elastic.co/docs/reference/query-languages/esql
# https://www.elastic.co/docs/reference/query-languages/esql/esql-syntax-reference
# https://www.elastic.co/docs/reference/query-languages/esql/esql-rest
# https://www.elastic.co/docs/explore-analyze/query-filter/languages/esql-kibana
# https://www.elastic.co/docs/solutions/security/esql-for-security/esql-threat-hunting-tutorial

import os
import polars as pl
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

elastic_api_encoded = os.environ["ELASTIC_API_ENCODED"]

es = Elasticsearch(
	"https://elasticsearch01.local:9200",
	api_key = elastic_api_encoded,
	ca_certs = "certs/ca-chain.pem",
	client_cert = "certs/public.pem",
	client_key = "certs/private.key"
)

query = """
FROM logs-*
| WHERE (`event.module`=="network_traffic" AND @timestamp >= (NOW() - 24 hours))
  AND (destination.domain IN ("ubuntu.com") OR destination.domain LIKE "*.ubuntu.*")
| STATS count = count(*) BY destination.domain
| SORT count DESC
| LIMIT 1000
| KEEP destination.domain, count
"""

# ES|QL can return the binary Arrow IPC stream format, which Polars supports natively
resp = es.esql.query(query=query, format="arrow")

# zero-copy consume the binary response from the existing memory buffer, no de/re-serialization needed
df = pl.from_arrow(resp.body)

print(df)

# expected output
```
shape: (6, 2)
┌────────────────────────────────┬───────┐
│ destination.domain             ┆ count │
│ ---                            ┆ ---   │
│ str                            ┆ i64   │
╞════════════════════════════════╪═══════╡
│ connectivity-check.ubuntu.com. ┆ 95    │
│ us.archive.ubuntu.com          ┆ 16    │
│ security.ubuntu.com            ┆ 2     │
│ motd.ubuntu.com                ┆ 1     │
│ esm.ubuntu.com                 ┆ 1     │
│ changelogs.ubuntu.com          ┆ 1     │
└────────────────────────────────┴───────┘
```
