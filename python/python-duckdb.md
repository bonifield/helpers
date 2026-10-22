# DuckDB

## Table of Contents

[Setup](#1-setup)

[Database Connections](#2-database-connections)

[Reading Data](#3-reading-data)

[Writing Data](#4-writing-data)

[Zero-Copy and Dataframes](#5-zero-copy-and-dataframes)

[Context Manager](#6-context-manager)

[Utilities and Helpful Settings](#7-utilities-and-helpful-settings)

[Apache Hive-style Partitioning](#8-apache-hive-style-partitioning)

# 1. Setup

### `uv add duckdb psycopg2-binary xlsxwriter`
- `xlsxwriter` is for Polars integration
- also add `pyarrow` if you wish to work with heavily with Apache Arrow tables

[Python Documentation Overview](https://duckdb.org/docs/2.0/clients/python/overview)

*The official documentation uses the `con` naming convention*

## Import

### `import duckdb`

# 2. Database Connections

## **Each thread in a process must use `duckdb.connect()`, as it is not thread safe**

## Connect to the default unnamed database
- ["The `duckdb` module has a default connection to an unnamed in-memory database"](https://duckdb.org/docs/2.0/clients/python/dbapi#default-connection)
- You may also provide a name for a new in-memory database when running `duckdb.connect()`
- note this creates "my_table", with a seed column "my_column" that has a single value of 42

use the default, in-memory, temporary, **unnamed** database
```
duckdb.execute("CREATE TABLE my_table AS SELECT 42 AS my_column")
duckdb.default_connection().sql("SELECT * from my_table")
┌───────────┐
│ my_column │
│   int32   │
├───────────┤
│        42 │
└───────────┘
```

you may create a connection object to the default database to run SQL commands
```
con = duckdb.connect(":default:")
con.sql("SELECT * from my_table")
┌───────────┐
│ my_column │
│   int32   │
├───────────┤
│        42 │
└───────────┘
```

change the default connection, to another connection
```
con = (something else)
duckdb.set_default_connection(con)
```

## Connect to a non-default, in-memory database
- uses a shared cache within the same process that multiple connection objects may access

```
con = duckdb.connect("file::memory:?cache=shared")
# named in-memory database
con = duckdb.connect("ATTACH 'file::memory:?cache=shared' AS my_in_memory_db;")
```

## Create and connect to a DuckDB database file
- extensions are irrelevant; `.duckdb` is common convention

```
con = duckdb.connect("my_database.duckdb")
# read_only=True is useful for parallel reads
con = duckdb.connect("my_database.duckdb", read_only=True)
```

Use a RAM disk in `/dev/shm/my_shared_db.duckdb`
```
con_writer = duckdb.connect("/dev/shm/my_shared_db.duckdb")
con_reader = duckdb.connect("/dev/shm/my_shared_db.duckdb", read_only=True)
```

## Connect to Sqlite
```
con = duckdb.connect()
con.sql("ATTACH 'my_database.db' AS my_sqlite (TYPE sqlite);")
# then run SQL commands
```

## Connect to PostgreSQL
```
con = duckdb.connect()
con.sql("INSTALL postgres; LOAD postgres;")
pg_connection_string = "dbname=my_db user=my_user password=my_password host=localhost port=5432"
con.sql(f"ATTACH '{pg_connection_string}' AS pg_db (TYPE POSTGRES);")
# then run SQL commands
```

## Connect to S3
- examples load into memory, not a local database file

```
with duckdb.connect(config={"memory_limit": "4GB", "threads": 4}) as con:
	con.sql("INSTALL httpfs; LOAD httpfs;")
	con.sql("INSTALL aws; LOAD aws;")
	con.sql("""
		CREATE SECRET my_s3_secret (
			TYPE s3,
			PROVIDER config,
			KEY_ID 'AWS_ACCESS_KEY_ID',
			SECRET 'AWS_SECRET_ACCESS_KEY',
			REGION 'us-east-1'
		);
	""")
	df = con.sql("SELECT * FROM 's3://my-bucket-name/data/**/*.parquet'").pl()
```

load credentials from AWS SDK credential chain, external to DuckDB
```
con.sql("""
	CREATE SECRET (
		TYPE s3,
		PROVIDER credential_chain,
		REGION 'us-east-1'
	);
""")
```

# 3. Reading Data

## Read files
- you could also use a new connection object for each unique dataset, then use `con.sql()` instead of `duckdb.sql()`
- use `my_csv.fetchall()` or `.limit(1).fetchall()` to view sample results

```
# CSV
my_csv = duckdb.sql("SELECT * FROM 'data.csv'")
print(my_csv.fetchall())
# Excel - use a connection
con = duckdb.connect()
con.sql("INSTALL excel; LOAD excel;")
con.sql("SELECT * FROM read_xlsx('data.xlsx')")
# JSON
my_json = duckdb.sql("SELECT * FROM 'data.json'")
# NDJSON
my_ndjson = duckdb.sql("SELECT * FROM read_ndjson('data.ndjson')")
# Parquet
my_parquet = duckdb.sql("SELECT * FROM 'data.parquet'")
# YAML - use a connection
con = duckdb.connect()
con.sql("INSTALL yaml FROM community; LOAD yaml;")
my_yaml = con.sql("SELECT * FROM 'data.yml'")
```

# 4. Writing Data

## Writing files
- DuckDB can infer formats based on extension, but explicit is better than implicit

```
# CSV
con.sql("COPY users TO 'users.csv' (HEADER, DELIMITER ',');")
# Excel
con.sql("INSTALL excel; LOAD excel;")
con.sql("COPY my_table TO 'data.xlsx' WITH (FORMAT xlsx, HEADER true, SHEET 'my_data');")
# JSON (uses NDJSON)
con.sql("COPY users TO 'users.json' (FORMAT JSON);")
# NDJSON
con.sql("COPY users TO 'users.ndjson';")
# Parquet
con.sql("COPY users TO 'users.parquet' (FORMAT PARQUET);")
# YAML
con.sql("INSTALL yaml FROM community; LOAD yaml;")
con.sql("COPY users TO 'users.yaml' (FORMAT yaml, STYLE block);")
```

# 5. Zero-Copy and Dataframes

## Zero-copy into Polars or Pandas dataframes and Arrow tables
- "zero-copy" means convert already-in-memory structures
- Arrow, use `.to_arrow_table()`
- Arrow streaming `RecordBatchReader`, use `.arrow()`
- Polars, use `.pl()` or `.pl(lazy=True)`
- Pandas, use `.df()`

```
# Polars
df_json = duckdb.sql("SELECT * FROM 'data.json'").pl()
df_json_lazy = duckdb.sql("SELECT * FROM 'data.json'").pl(lazy=True)
# Arrow
arrow_reader = duckdb.sql("SELECT * FROM massive_dataset").arrow()
for batch in arrow_reader:
	print(batch.num_rows)
	...
```

# 6. Context Manager

## Using a context manager to zero-copy read a dataframe
- you can also do `result = con.sql(...).pl()` to immediately get a Polars dataframe
- **this example directly queries a Polars dataframe using SQL**

```
import duckdb
import polars as pl

pl_df = pl.DataFrame({
	"item": ["apple", "banana", "cherry"],
	"price": [1.00, 1.50, 2.50]
})

with duckdb.connect() as con:
	result = con.sql("SELECT item, price FROM pl_df WHERE price > 1.00")
	result_df = result.pl()
	#
	print(result)
	print(result_df)
```
expected output (first is DuckDB, second is Polars)
```
┌─────────┬────────┐
│  item   │ price  │
│ varchar │ double │
├─────────┼────────┤
│ banana  │    1.5 │
│ cherry  │    2.5 │
└─────────┴────────┘
shape: (2, 2)
┌────────┬───────┐
│ item   ┆ price │
│ ---    ┆ ---   │
│ str    ┆ f64   │
╞════════╪═══════╡
│ banana ┆ 1.5   │
│ cherry ┆ 2.5   │
└────────┴───────┘
```

## Indented SQL commands

```
with duckdb.connect() as con:
	con.sql("""
		SELECT
			ROUND(AVG(price), 3) AS avg_price,
			MIN(price) as min_price,
			MAX(price) as max_price
		FROM pl_df
	""")
#
┌───────────┬───────────┬───────────┐
│ avg_price │ min_price │ max_price │
│  double   │  double   │  double   │
├───────────┼───────────┼───────────┤
│     1.667 │       1.0 │       2.5 │
└───────────┴───────────┴───────────┘
```

# 7. Utilities and Helpful Settings

## Describe an unfamiliar file or database
```
con.sql("DESCRIBE SELECT * FROM pl_df")
#
┌─────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
│ column_name │ column_type │  null   │   key   │ default │  extra  │
│   varchar   │   varchar   │ varchar │ varchar │ varchar │ varchar │
├─────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
│ item        │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ price       │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
└─────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┘
```

## Execution plan

```
con.sql("EXPLAIN SELECT * FROM pl_df WHERE price > 1").show()
```

## Set resource limitations
```
con.sql("SET memory_limit = '4GB';")
# or
duckdb.connect("my_db.duckdb", config={"memory_limit": "4GB", "threads": 4})
```

# 8. Apache Hive-style Partitioning

## Example of yearly directories further broken down by region
- DuckDB would add `year` and `region` columns if not already present
- partitioning lets DuckDB skip directories and files it doesn't need

```
data/
├── year=2024/
│   ├── region=US/
│   │   └── part-0.parquet
│   └── region=EU/
│       └── part-0.parquet
└── year=2025/
    ├── region=US/
    │   └── part-0.parquet
    └── region=EU/
        └── part-0.parquet
```

query example for this structure
```
result = con.sql("""
	SELECT region, AVG(price) 
	FROM 'data/**/*.parquet' 
	WHERE year = 2025 AND region = 'US'
	GROUP BY region
""")
```

## Create Apache Hive-style partitioned directories - with a datetime column

```
import duckdb
import polars as pl

# sample data with a datetime column
df = pl.DataFrame({
	"order_id": [1, 2, 3, 4],
	"order_date": [
		"2026-01-15 10:00:00", 
		"2026-01-20 14:30:00", 
		"2026-02-10 09:15:00", 
		"2026-02-18 16:45:00"
	],
	"amount": [100.0, 250.0, 150.0, 300.0]
}).with_columns(pl.col("order_date").str.to_datetime())

with duckdb.connect() as con:
	# create directory structure
	result = con.sql("""
		COPY (
			SELECT 
				order_id,
				amount,
				EXTRACT('year' FROM order_date) AS year,
				EXTRACT('month' FROM order_date) AS month
			FROM df
		) TO 'partitioned_orders' (
			FORMAT PARQUET,
			PARTITION_BY (year, month)
		)
	""")
```

expected output in `./partitioned_orders/`
```
$ tree partitioned_orders/
partitioned_orders/
└── year=2026
    ├── month=1
    │   └── data_0.parquet
    └── month=2
        └── data_0.parquet
```

## Create Apache Hive-style partitioned directories - without a datetime column
- example also shows using `FILENAME_PATTERN` to give a prefix to the parquet files
	- `FILENAME_PATTERN 'employees_{i}'` adds an incrementing sequence number
		- ex. `employees_0.parquet`
	- `FILENAME_PATTERN 'employees_{uuid}'` adds a 128-bit UUID
		- ex. `employees_3163d419-4fb7-4006-8793-a1586e5b0a20.parquet`

```
import duckdb
import polars as pl

# sample data without a datetime column
df = pl.DataFrame({
	"employee_id": [101, 102, 103, 104],
	"region": ["US", "EU", "US", "APAC"],
	"department": ["Engineering", "Sales", "Sales", "Engineering"],
	"salary": [85000, 60000, 62000, 90000]
})

with duckdb.connect() as con:
	# create directory structure
	result = con.sql("""
		COPY df TO 'partitioned_employees' (
			FORMAT PARQUET,
			PARTITION_BY (region, department),
			FILENAME_PATTERN 'employees_{i}'
		)
	""")
```

expected output in `./partitioned_employees/`
```
$ tree partitioned_employees/
partitioned_employees/
├── region=APAC
│   └── department=Engineering
│       └── employees_0.parquet
├── region=EU
│   └── department=Sales
│       └── employees_0.parquet
└── region=US
    ├── department=Engineering
    │   └── employees_0.parquet
    └── department=Sales
        └── employees_0.parquet
```

## Filename collision avoidance and overwrites

example error trying to send data to a directory with parquet files already present
```
IO Error: Directory "partitioned_employees" is not empty! Enable OVERWRITE option to overwrite files
```

- use `OVERWRITE` to clear and replace an **entire directory**
- use `OVERWRITE_OR_IGNORE` to overwrite existing **individual files** if there is a name collision
- use `APPEND` to write new data into an existing directory; clashing filenames will be regenerated

```
con.sql("COPY df TO 'partitioned_employees' (..., OVERWRITE)")
```

## Recurse all files in a single directory
- if columns match, DuckDB union-merges them into a single table

```
with duckdb.connect() as con:
	combined_table = con.sql("SELECT * FROM 'my_data/*.parquet'")
```

## Recurse all files in multiple directories
- if columns match, DuckDB union-merges them into a single table

```
with duckdb.connect() as con:
	combined_table = con.sql("SELECT * FROM 'my_data/**/*.parquet'")
```
