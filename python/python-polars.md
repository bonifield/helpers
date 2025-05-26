# Polars

[Installation](https://docs.pola.rs/user-guide/installation/)

[Python API Documentation](https://docs.pola.rs/api/python/stable/reference/index.html)

## Create Dataframes

Create dataframes from a dictionary of column names as keys, with values containing column data
- will error if column lengths mismatch
```
df1 = pl.DataFrame(
	{
		"source":["nips", "nips", "meta", "hips", "nips", "meta"],
		"count": [2, 2, 1, 1, 1, 3],
		"indicator": ["bad1", "bad2", "ok1", "bad3", "ok2", "ok3"]
	}
)

print(df1)
#
shape: (6, 3)
┌────────┬───────┬───────────┐
│ source ┆ count ┆ indicator │
│ ---    ┆ ---   ┆ ---       │
│ str    ┆ i64   ┆ str       │
╞════════╪═══════╪═══════════╡
│ nips   ┆ 2     ┆ bad1      │
│ nips   ┆ 2     ┆ bad2      │
│ meta   ┆ 1     ┆ ok1       │
│ hips   ┆ 1     ┆ bad3      │
│ nips   ┆ 1     ┆ ok2       │
│ meta   ┆ 3     ┆ ok3       │
└────────┴───────┴───────────┘
```

```
df2 = pl.DataFrame(
	{
		"action": ["block", "block", "observe", "block", "allow"],
		"indicator": ["bad1", "bad2", "ok1", "bad3", "ok2"],
		"case_number": [123, 123, 234, 456, 345]
	}
)

print(df2)
#
shape: (5, 3)
┌─────────┬───────────┬─────────────┐
│ action  ┆ indicator ┆ case_number │
│ ---     ┆ ---       ┆ ---         │
│ str     ┆ str       ┆ i64         │
╞═════════╪═══════════╪═════════════╡
│ block   ┆ bad1      ┆ 123         │
│ block   ┆ bad2      ┆ 123         │
│ observe ┆ ok1       ┆ 234         │
│ block   ┆ bad3      ┆ 456         │
│ allow   ┆ ok2       ┆ 345         │
└─────────┴───────────┴─────────────┘
```

Create a dataframe from a list-of-lists containing COLUMN values, and a list of column headers
```
case_values = [
	[123, 456, 789],
	["case1", "case2", "case3"],
]

case_value_headers = ["case_number", "case_name"]

df3 = pl.DataFrame(
	case_values,
	schema=case_value_headers,
	orient=None
)
print(df3)
#
shape: (3, 2)
┌─────────────┬───────────┐
│ case_number ┆ case_name │
│ ---         ┆ ---       │
│ i64         ┆ str       │
╞═════════════╪═══════════╡
│ 123         ┆ case1     │
│ 456         ┆ case2     │
│ 789         ┆ case3     │
└─────────────┴───────────┘
```

Create a dataframe from a list-of-lists containing ROW values, and a list of column headers
```
more_case_values = [
	["case2", "medium"],
	["case3", "low"],
]

more_case_value_headers = ["case_name", "case_severity"]

df4 = pl.DataFrame(
	more_case_values,
	schema=more_case_value_headers,
	orient="row"
)

print(df4)
#
shape: (2, 2)
┌───────────┬───────────────┐
│ case_name ┆ case_severity │
│ ---       ┆ ---           │
│ str       ┆ str           │
╞═══════════╪═══════════════╡
│ case2     ┆ medium        │
│ case3     ┆ low           │
└───────────┴───────────────┘
```

## View Schema

```
df1.collect_schema()
#
Schema([('source', String), ('count', Int64), ('indicator', String)])
```

## select, functions, group_by, sort

`select` one column
```
df1.select("indicator")
#
shape: (6, 1)
┌───────────┐
│ indicator │
│ ---       │
│ str       │
╞═══════════╡
│ bad1      │
│ bad2      │
│ ok1       │
│ bad3      │
│ ok2       │
│ ok3       │
└───────────┘
```

`select` multiple columns
```
df1.select(["indicator", "count"])
#
shape: (6, 2)
┌───────────┬───────┐
│ indicator ┆ count │
│ ---       ┆ ---   │
│ str       ┆ i64   │
╞═══════════╪═══════╡
│ bad1      ┆ 2     │
│ bad2      ┆ 2     │
│ ok1       ┆ 1     │
│ bad3      ┆ 1     │
│ ok2       ┆ 1     │
│ ok3       ┆ 3     │
└───────────┴───────┘
```

`sum` aggregation on column
```
df1.select(
	pl.sum("count")
)
#
shape: (1, 1)
┌───────┐
│ count │
│ ---   │
│ i64   │
╞═══════╡
│ 10    │
└───────┘
```

`sum` the "count" column for each "source" (`group_by`), and `sort` highest to lowest
```
df1.group_by("source").agg(
	pl.sum("count")
).sort("count", descending=True)
#
shape: (3, 2)
┌────────┬───────┐
│ source ┆ count │
│ ---    ┆ ---   │
│ str    ┆ i64   │
╞════════╪═══════╡
│ nips   ┆ 5     │
│ meta   ┆ 4     │
│ hips   ┆ 1     │
└────────┴───────┘
```

## Conversions to Python `dict` or `list` or Polars `series`

Python dict - all columns
```
d1 = df1.to_dict(as_series=False)
print(d1)
#
{'source': ['nips', 'nips', 'meta', 'hips', 'nips', 'meta'], 'count': [2, 2, 1, 1, 1, 3], 'indicator': ['bad1', 'bad2', 'ok1', 'bad3', 'ok2', 'ok3']}
```

Polars key/value series - all columns (as_series=True)
```
d2 = df1.to_dict()
print(d2)
#
{'source': shape: (6,)
Series: 'source' [str]
[
	"nips"
	"nips"
	"meta"
	"hips"
	"nips"
	"meta"
], 'count': shape: (6,)
Series: 'count' [i64]
[
	2
	2
	1
	1
	1
	3
], 'indicator': shape: (6,)
Series: 'indicator' [str]
[
	"bad1"
	"bad2"
	"ok1"
	"bad3"
	"ok2"
	"ok3"
]}
```

Python dict - from single df column
```
d3 = df1.select("indicator").to_dict(as_series=False)
print(d3)
#
{'indicator': ['bad1', 'bad2', 'ok1', 'bad3', 'ok2', 'ok3']}
```

Polars key/value series - from single df column (as_series=True)
```
d4 = df1.select("indicator").to_dict()
print(d4)
#
{'indicator': shape: (6,)
Series: 'indicator' [str]
[
	"bad1"
	"bad2"
	"ok1"
	"bad3"
	"ok2"
	"ok3"
]}
```

List - access column as a series using df[col] syntax
```
l1 = df1["count"].to_list()
print(l1)
#
[2, 2, 1, 1, 1, 3]
```

List - unique column values
```
l2 = df1["count"].unique().to_list()
print(l2)
#
[1, 2, 3]
```

## Joins

`inner`: Returns rows that have matching values in both tables
```
df1.join(
	df2, on="indicator", how="inner"
)
#
shape: (5, 5)
┌────────┬───────┬───────────┬─────────┬─────────────┐
│ source ┆ count ┆ indicator ┆ action  ┆ case_number │
│ ---    ┆ ---   ┆ ---       ┆ ---     ┆ ---         │
│ str    ┆ i64   ┆ str       ┆ str     ┆ i64         │
╞════════╪═══════╪═══════════╪═════════╪═════════════╡
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ 123         │
│ nips   ┆ 2     ┆ bad2      ┆ block   ┆ 123         │
│ meta   ┆ 1     ┆ ok1       ┆ observe ┆ 234         │
│ hips   ┆ 1     ┆ bad3      ┆ block   ┆ 456         │
│ nips   ┆ 1     ┆ ok2       ┆ allow   ┆ 345         │
└────────┴───────┴───────────┴─────────┴─────────────┘
```

`left`: Returns all rows from the left table, and the matched rows from the right table
```
df1.join(
	df2, on="indicator", how="left"
)
#
shape: (6, 5)
┌────────┬───────┬───────────┬─────────┬─────────────┐
│ source ┆ count ┆ indicator ┆ action  ┆ case_number │
│ ---    ┆ ---   ┆ ---       ┆ ---     ┆ ---         │
│ str    ┆ i64   ┆ str       ┆ str     ┆ i64         │
╞════════╪═══════╪═══════════╪═════════╪═════════════╡
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ 123         │
│ nips   ┆ 2     ┆ bad2      ┆ block   ┆ 123         │
│ meta   ┆ 1     ┆ ok1       ┆ observe ┆ 234         │
│ hips   ┆ 1     ┆ bad3      ┆ block   ┆ 456         │
│ nips   ┆ 1     ┆ ok2       ┆ allow   ┆ 345         │
│ meta   ┆ 3     ┆ ok3       ┆ null    ┆ null        │
└────────┴───────┴───────────┴─────────┴─────────────┘
```

`right`: Returns all rows from the right table, and the matched rows from the left table
```
df1.join(
	df2, on="indicator", how="right"
)
#
shape: (5, 5)
┌────────┬───────┬─────────┬───────────┬─────────────┐
│ source ┆ count ┆ action  ┆ indicator ┆ case_number │
│ ---    ┆ ---   ┆ ---     ┆ ---       ┆ ---         │
│ str    ┆ i64   ┆ str     ┆ str       ┆ i64         │
╞════════╪═══════╪═════════╪═══════════╪═════════════╡
│ nips   ┆ 2     ┆ block   ┆ bad1      ┆ 123         │
│ nips   ┆ 2     ┆ block   ┆ bad2      ┆ 123         │
│ meta   ┆ 1     ┆ observe ┆ ok1       ┆ 234         │
│ hips   ┆ 1     ┆ block   ┆ bad3      ┆ 456         │
│ nips   ┆ 1     ┆ allow   ┆ ok2       ┆ 345         │
└────────┴───────┴─────────┴───────────┴─────────────┘
```

`full`: Returns all rows when there is a match in either left or right table
```
df1.join(
	df2, on="indicator", how="full"
)
#
shape: (6, 6)
┌────────┬───────┬───────────┬─────────┬─────────────────┬─────────────┐
│ source ┆ count ┆ indicator ┆ action  ┆ indicator_right ┆ case_number │
│ ---    ┆ ---   ┆ ---       ┆ ---     ┆ ---             ┆ ---         │
│ str    ┆ i64   ┆ str       ┆ str     ┆ str             ┆ i64         │
╞════════╪═══════╪═══════════╪═════════╪═════════════════╪═════════════╡
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ bad1            ┆ 123         │
│ nips   ┆ 2     ┆ bad2      ┆ block   ┆ bad2            ┆ 123         │
│ meta   ┆ 1     ┆ ok1       ┆ observe ┆ ok1             ┆ 234         │
│ hips   ┆ 1     ┆ bad3      ┆ block   ┆ bad3            ┆ 456         │
│ nips   ┆ 1     ┆ ok2       ┆ allow   ┆ ok2             ┆ 345         │
│ meta   ┆ 3     ┆ ok3       ┆ null    ┆ null            ┆ null        │
└────────┴───────┴───────────┴─────────┴─────────────────┴─────────────┘
```

`full` with `coalesce=True`
```
df1.join(
	df2, on="indicator", how="full", coalesce=True
)
#
shape: (6, 5)
┌────────┬───────┬───────────┬─────────┬─────────────┐
│ source ┆ count ┆ indicator ┆ action  ┆ case_number │
│ ---    ┆ ---   ┆ ---       ┆ ---     ┆ ---         │
│ str    ┆ i64   ┆ str       ┆ str     ┆ i64         │
╞════════╪═══════╪═══════════╪═════════╪═════════════╡
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ 123         │
│ nips   ┆ 2     ┆ bad2      ┆ block   ┆ 123         │
│ meta   ┆ 1     ┆ ok1       ┆ observe ┆ 234         │
│ hips   ┆ 1     ┆ bad3      ┆ block   ┆ 456         │
│ nips   ┆ 1     ┆ ok2       ┆ allow   ┆ 345         │
│ meta   ┆ 3     ┆ ok3       ┆ null    ┆ null        │
└────────┴───────┴───────────┴─────────┴─────────────┘
```

`full` with print `nulls_equal=True`
```
df1.join(
	df2, on="indicator", how="full", nulls_equal=True
)
#
shape: (6, 6)
┌────────┬───────┬───────────┬─────────┬─────────────────┬─────────────┐
│ source ┆ count ┆ indicator ┆ action  ┆ indicator_right ┆ case_number │
│ ---    ┆ ---   ┆ ---       ┆ ---     ┆ ---             ┆ ---         │
│ str    ┆ i64   ┆ str       ┆ str     ┆ str             ┆ i64         │
╞════════╪═══════╪═══════════╪═════════╪═════════════════╪═════════════╡
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ bad1            ┆ 123         │
│ nips   ┆ 2     ┆ bad2      ┆ block   ┆ bad2            ┆ 123         │
│ meta   ┆ 1     ┆ ok1       ┆ observe ┆ ok1             ┆ 234         │
│ hips   ┆ 1     ┆ bad3      ┆ block   ┆ bad3            ┆ 456         │
│ nips   ┆ 1     ┆ ok2       ┆ allow   ┆ ok2             ┆ 345         │
│ meta   ┆ 3     ┆ ok3       ┆ null    ┆ null            ┆ null        │
└────────┴───────┴───────────┴─────────┴─────────────────┴─────────────┘
```

`full` with `coalesce=True` and `nulls_equal=True`
```
df1.join(
	df2, on="indicator", how="full", coalesce=True, nulls_equal=True
)
#
shape: (6, 5)
┌────────┬───────┬───────────┬─────────┬─────────────┐
│ source ┆ count ┆ indicator ┆ action  ┆ case_number │
│ ---    ┆ ---   ┆ ---       ┆ ---     ┆ ---         │
│ str    ┆ i64   ┆ str       ┆ str     ┆ i64         │
╞════════╪═══════╪═══════════╪═════════╪═════════════╡
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ 123         │
│ nips   ┆ 2     ┆ bad2      ┆ block   ┆ 123         │
│ meta   ┆ 1     ┆ ok1       ┆ observe ┆ 234         │
│ hips   ┆ 1     ┆ bad3      ┆ block   ┆ 456         │
│ nips   ┆ 1     ┆ ok2       ┆ allow   ┆ 345         │
│ meta   ┆ 3     ┆ ok3       ┆ null    ┆ null        │
└────────┴───────┴───────────┴─────────┴─────────────┘
```

`full` with `coalesce=True` and `nulls_equal=True` and null values filled using `action`
```
df1.join(
	df2, on="indicator", how="full", coalesce=True, nulls_equal=True
).with_columns(
	pl.col("action").fill_null("NOT_BLOCKED")
)
#
shape: (6, 5)
┌────────┬───────┬───────────┬─────────────┬─────────────┐
│ source ┆ count ┆ indicator ┆ action      ┆ case_number │
│ ---    ┆ ---   ┆ ---       ┆ ---         ┆ ---         │
│ str    ┆ i64   ┆ str       ┆ str         ┆ i64         │
╞════════╪═══════╪═══════════╪═════════════╪═════════════╡
│ nips   ┆ 2     ┆ bad1      ┆ block       ┆ 123         │
│ nips   ┆ 2     ┆ bad2      ┆ block       ┆ 123         │
│ meta   ┆ 1     ┆ ok1       ┆ observe     ┆ 234         │
│ hips   ┆ 1     ┆ bad3      ┆ block       ┆ 456         │
│ nips   ┆ 1     ┆ ok2       ┆ allow       ┆ 345         │
│ meta   ┆ 3     ┆ ok3       ┆ NOT_BLOCKED ┆ null        │
└────────┴───────┴───────────┴─────────────┴─────────────┘
```

`cross` (no join key): Returns the Cartesian product of rows from both tables
```
df1.join(
	df2, how="cross"
)
#
shape: (30, 6)
┌────────┬───────┬───────────┬─────────┬─────────────────┬─────────────┐
│ source ┆ count ┆ indicator ┆ action  ┆ indicator_right ┆ case_number │
│ ---    ┆ ---   ┆ ---       ┆ ---     ┆ ---             ┆ ---         │
│ str    ┆ i64   ┆ str       ┆ str     ┆ str             ┆ i64         │
╞════════╪═══════╪═══════════╪═════════╪═════════════════╪═════════════╡
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ bad1            ┆ 123         │
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ bad2            ┆ 123         │
│ nips   ┆ 2     ┆ bad1      ┆ allow   ┆ ok2             ┆ 345         │
│ …      ┆ …     ┆ …         ┆ …       ┆ …               ┆ …           │
│ meta   ┆ 3     ┆ ok3       ┆ block   ┆ bad1            ┆ 123         │
│ meta   ┆ 3     ┆ ok3       ┆ block   ┆ bad3            ┆ 456         │
│ meta   ┆ 3     ┆ ok3       ┆ allow   ┆ ok2             ┆ 345         │
└────────┴───────┴───────────┴─────────┴─────────────────┴─────────────┘
```

`semi`: Returns rows from the left table that have a match in the right table
```
df1.join(
	df2, on="indicator", how="semi"
)
#
shape: (30, 6)
┌────────┬───────┬───────────┬─────────┬─────────────────┬─────────────┐
│ source ┆ count ┆ indicator ┆ action  ┆ indicator_right ┆ case_number │
│ ---    ┆ ---   ┆ ---       ┆ ---     ┆ ---             ┆ ---         │
│ str    ┆ i64   ┆ str       ┆ str     ┆ str             ┆ i64         │
╞════════╪═══════╪═══════════╪═════════╪═════════════════╪═════════════╡
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ bad1            ┆ 123         │
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ bad2            ┆ 123         │
│ nips   ┆ 2     ┆ bad1      ┆ observe ┆ ok1             ┆ 234         │
│ nips   ┆ 2     ┆ bad1      ┆ block   ┆ bad3            ┆ 456         │
│ nips   ┆ 2     ┆ bad1      ┆ allow   ┆ ok2             ┆ 345         │
│ …      ┆ …     ┆ …         ┆ …       ┆ …               ┆ …           │
│ meta   ┆ 3     ┆ ok3       ┆ block   ┆ bad1            ┆ 123         │
│ meta   ┆ 3     ┆ ok3       ┆ block   ┆ bad2            ┆ 123         │
│ meta   ┆ 3     ┆ ok3       ┆ observe ┆ ok1             ┆ 234         │
│ meta   ┆ 3     ┆ ok3       ┆ block   ┆ bad3            ┆ 456         │
│ meta   ┆ 3     ┆ ok3       ┆ allow   ┆ ok2             ┆ 345         │
└────────┴───────┴───────────┴─────────┴─────────────────┴─────────────┘
```

`anti`: Returns rows from the left table that have no match in the right table
```
df1.join(
	df2, on="indicator", how="anti"
)
#
shape: (1, 3)
┌────────┬───────┬───────────┐
│ source ┆ count ┆ indicator │
│ ---    ┆ ---   ┆ ---       │
│ str    ┆ i64   ┆ str       │
╞════════╪═══════╪═══════════╡
│ meta   ┆ 3     ┆ ok3       │
└────────┴───────┴───────────┘
```

create new dataframe from `join`
- cast `count` as `Int64` that won't error on strings
- mutiple-dataframe `full` with `coalesce=True` and `nulls_equal=True` and null values filled using `action`
- can also just do `dataframe.fill_null(value)` or use a fill_null `strategy`
```
df5 = df1.join(
	df2, on="indicator", how="full", coalesce=True, nulls_equal=True
).join(
	df3, on="case_number", how="full", coalesce=True, nulls_equal=True
).join(
	df4, on="case_name", how="full", coalesce=True, nulls_equal=True
).with_columns(
	pl.col("action").fill_null("NOT_BLOCKED"),
	pl.col("case_name").fill_null("NO_CASE_NAME"),
	pl.col("case_number").fill_null("NO_CASE_NUMBER"),
	pl.col("case_severity").fill_null("NO_CASE_SEVERITY"),
	pl.col("count").fill_null("NO_COUNT"),
	pl.col("indicator").fill_null("NO_INDICATOR"),
	pl.col("source").fill_null("NO_SOURCE"),
).with_columns(
	pl.col("count").cast(pl.Int64, strict=False)
)

print(df5)
#
shape: (7, 7)
┌───────────┬───────┬──────────────┬─────────────┬────────────────┬──────────────┬──────────────────┐
│ source    ┆ count ┆ indicator    ┆ action      ┆ case_number    ┆ case_name    ┆ case_severity    │
│ ---       ┆ ---   ┆ ---          ┆ ---         ┆ ---            ┆ ---          ┆ ---              │
│ str       ┆ i64   ┆ str          ┆ str         ┆ str            ┆ str          ┆ str              │
╞═══════════╪═══════╪══════════════╪═════════════╪════════════════╪══════════════╪══════════════════╡
│ nips      ┆ 2     ┆ bad1         ┆ block       ┆ 123            ┆ case1        ┆ NO_CASE_SEVERITY │
│ nips      ┆ 2     ┆ bad2         ┆ block       ┆ 123            ┆ case1        ┆ NO_CASE_SEVERITY │
│ meta      ┆ 1     ┆ ok1          ┆ observe     ┆ 234            ┆ NO_CASE_NAME ┆ NO_CASE_SEVERITY │
│ hips      ┆ 1     ┆ bad3         ┆ block       ┆ 456            ┆ case2        ┆ medium           │
│ nips      ┆ 1     ┆ ok2          ┆ allow       ┆ 345            ┆ NO_CASE_NAME ┆ NO_CASE_SEVERITY │
│ meta      ┆ 3     ┆ ok3          ┆ NOT_BLOCKED ┆ NO_CASE_NUMBER ┆ NO_CASE_NAME ┆ NO_CASE_SEVERITY │
│ NO_SOURCE ┆ null  ┆ NO_INDICATOR ┆ NOT_BLOCKED ┆ 789            ┆ case3        ┆ low              │
└───────────┴───────┴──────────────┴─────────────┴────────────────┴──────────────┴──────────────────┘
```

## Filters

```
df6 = df5.filter(
	(pl.col("action") == "block") & (pl.col("source") == "nips")
)

print(df6)
#
shape: (2, 7)
┌────────┬───────┬───────────┬────────┬─────────────┬───────────┬──────────────────┐
│ source ┆ count ┆ indicator ┆ action ┆ case_number ┆ case_name ┆ case_severity    │
│ ---    ┆ ---   ┆ ---       ┆ ---    ┆ ---         ┆ ---       ┆ ---              │
│ str    ┆ i64   ┆ str       ┆ str    ┆ str         ┆ str       ┆ str              │
╞════════╪═══════╪═══════════╪════════╪═════════════╪═══════════╪══════════════════╡
│ nips   ┆ 2     ┆ bad1      ┆ block  ┆ 123         ┆ case1     ┆ NO_CASE_SEVERITY │
│ nips   ┆ 2     ┆ bad2      ┆ block  ┆ 123         ┆ case1     ┆ NO_CASE_SEVERITY │
└────────┴───────┴───────────┴────────┴─────────────┴───────────┴──────────────────┘
```

## Combining Dataframes

create two dataframes with the same column names, for `concat`
```
df9 = pl.DataFrame(
	{
		"a":["A", "B", "C", "D"],
		"b": [1, 2, None, None],
		"c": ["one", "two", "three", "four"]
	}
)
df10 = pl.DataFrame(
	{
		"a":["E", "F", "G", "H"],
		"b": [5, 6, 7, 8],
		"c": ["five", "six", None, None]
	}
)
```

Concatenate (`concat`) dataframes
```
df11 = pl.concat([df9, df10])

print(df11)
#
shape: (8, 3)
┌─────┬──────┬───────┐
│ a   ┆ b    ┆ c     │
│ --- ┆ ---  ┆ ---   │
│ str ┆ i64  ┆ str   │
╞═════╪══════╪═══════╡
│ A   ┆ 1    ┆ one   │
│ B   ┆ 2    ┆ two   │
│ C   ┆ null ┆ three │
│ D   ┆ null ┆ four  │
│ E   ┆ 5    ┆ five  │
│ F   ┆ 6    ┆ six   │
│ G   ┆ 7    ┆ null  │
│ H   ┆ 8    ┆ null  │
└─────┴──────┴───────┘
```

## Create new column, based on other columns

```
df55 = df5.select(
	[
		pl.format("SENSOR:{}|ACTION:{}", pl.col("source"), pl.col("action")).alias("my_formatted_column")
	]
)

print(df55)
#
shape: (7, 1)
┌─────────────────────────────────┐
│ my_formatted_column             │
│ ---                             │
│ str                             │
╞═════════════════════════════════╡
│ SENSOR:nips|ACTION:block        │
│ SENSOR:nips|ACTION:block        │
│ SENSOR:meta|ACTION:observe      │
│ SENSOR:hips|ACTION:block        │
│ SENSOR:nips|ACTION:allow        │
│ SENSOR:meta|ACTION:NOT_BLOCKED  │
│ SENSOR:NO_SOURCE|ACTION:NOT_BL… │
└─────────────────────────────────┘
```
note truncated output; next section fixes that
- column values are unaffected

## Increase characters used to print strings

Only affects displayed output; column values are unaffected
- `tbl_rows=-1` means print all rows
- `set_fmt_str_lengths=100` means use up to 100 characters for printing strings
```
with pl.Config(tbl_rows=-1, set_fmt_str_lengths=100):
	print(df55)
#
shape: (7, 1)
┌─────────────────────────────────────┐
│ my_formatted_column                 │
│ ---                                 │
│ str                                 │
╞═════════════════════════════════════╡
│ SENSOR:nips|ACTION:block            │
│ SENSOR:nips|ACTION:block            │
│ SENSOR:meta|ACTION:observe          │
│ SENSOR:hips|ACTION:block            │
│ SENSOR:nips|ACTION:allow            │
│ SENSOR:meta|ACTION:NOT_BLOCKED      │
│ SENSOR:NO_SOURCE|ACTION:NOT_BLOCKED │
└─────────────────────────────────────┘
```

## Write Files

Must have write access; recommend also using `pathlib`

Parquet and CSV
```
df5.write_parquet("df5.parquet")
df5.write_csv("df5.csv")
```

## Ingest - Lazy Frames

Uses `scan_` functions

Gathers metadata, creates optimized execution plan before running `.collect()` to "materialize" and run operations
- use `low_memory=True` which trades memory utilization for slower ingest

Lazy ingest a Parquet
```
df6_parquet_lazy = pl.scan_parquet("df5.parquet")
type(df6_parquet_lazy)
# <class 'polars.lazyframe.frame.LazyFrame'>
```

Perform several operations, then execute with `.collect()`
- allows Polars to optimize operations instead of running them sequentially
- recall we cast `count` as `Int64` when creating `df5`
- can use `.collect(streaming=True)` for processing files too big to fit in RAM
```
(
	df6_parquet_lazy
	.group_by("source")
	.agg(pl.sum("count"))
	.with_columns(
		pl.col("count")
		.alias("total_by_source")
	)
	.sort("total_by_source")
).collect()
#
shape: (4, 3)
┌───────────┬───────┬─────────────────┐
│ source    ┆ count ┆ total_by_source │
│ ---       ┆ ---   ┆ ---             │
│ str       ┆ i64   ┆ i64             │
╞═══════════╪═══════╪═════════════════╡
│ NO_SOURCE ┆ 0     ┆ 0               │
│ hips      ┆ 1     ┆ 1               │
│ meta      ┆ 4     ┆ 4               │
│ nips      ┆ 5     ┆ 5               │
└───────────┴───────┴─────────────────┘

# or as one line
df6_parquet_lazy.group_by("source").agg(pl.sum("count")).with_columns(pl.col("count").alias("total_by_source")).sort("count").collect()
# or as one line, no alias
df6_parquet_lazy.group_by("source").agg(pl.sum("count")).sort("count").collect()
#
shape: (4, 2)
┌───────────┬───────┐
│ source    ┆ count │
│ ---       ┆ ---   │
│ str       ┆ i64   │
╞═══════════╪═══════╡
│ NO_SOURCE ┆ 0     │
│ hips      ┆ 1     │
│ meta      ┆ 4     │
│ nips      ┆ 5     │
└───────────┴───────┘
```

Lazy ingest a CSV
```
df6_csv_lazy = pl.scan_csv("df5.csv")
type(df6_csv_lazy)
# <class 'polars.lazyframe.frame.LazyFrame'>
df6_csv_lazy.group_by("source").agg(pl.sum("count")).sort("count").collect()
#
shape: (4, 2)
┌───────────┬───────┐
│ source    ┆ count │
│ ---       ┆ ---   │
│ str       ┆ i64   │
╞═══════════╪═══════╡
│ NO_SOURCE ┆ 0     │
│ hips      ┆ 1     │
│ meta      ┆ 4     │
│ nips      ┆ 5     │
└───────────┴───────┘
```

View the optimization plan
- can pass `.explain(optimized=False)` for sub-optimal / pre-optimalized plan
- use print since `explain()` returns a string with newline characters
```
print(
	(
		df6_parquet_lazy
		.group_by("source")
		.agg(pl.sum("count"))
		.with_columns(
			pl.col("count")
			.alias("total_by_source")
		)
		.sort("total_by_source")
	).explain()
)
#
SORT BY [col("total_by_source")]
   WITH_COLUMNS:
   [col("count").alias("total_by_source")] 
    AGGREGATE
    	[col("count").sum()] BY [col("source")] FROM
      Parquet SCAN [df5.parquet]
      PROJECT 2/7 COLUMNS
```

## Sink (Write) Lazy Frames

Sinks only work with lazy frames

Sink to a Parquet
```
df6_parquet_lazy.sink_parquet("df6.parquet")
```

Sink multiple lazy frames; copied directly from the official [documentation](https://docs.pola.rs/user-guide/lazy/sources_sinks/#multiplexing-sinks)
```
q1 = df6_parquet_lazy.sink_parquet("lazy_sink_1.parquet", lazy=True)
q2 = df6_parquet_lazy.sink_parquet("lazy_sink_2.parquet", lazy=True)
pl.collect_all([q1, q2])
```

## Ingest - Read Into Memory

Uses `read_` functions

Read a whole Parquet into memory
```
df6_parquet_read = pl.read_parquet("df5.parquet")
type(df6_parquet_read)
# <class 'polars.dataframe.frame.DataFrame'>
print(df6_parquet_read)
#
shape: (7, 7)
┌───────────┬───────┬──────────────┬─────────────┬────────────────┬──────────────┬──────────────────┐
│ source    ┆ count ┆ indicator    ┆ action      ┆ case_number    ┆ case_name    ┆ case_severity    │
│ ---       ┆ ---   ┆ ---          ┆ ---         ┆ ---            ┆ ---          ┆ ---              │
│ str       ┆ i64   ┆ str          ┆ str         ┆ str            ┆ str          ┆ str              │
╞═══════════╪═══════╪══════════════╪═════════════╪════════════════╪══════════════╪══════════════════╡
│ nips      ┆ 2     ┆ bad1         ┆ block       ┆ 123            ┆ case1        ┆ NO_CASE_SEVERITY │
│ nips      ┆ 2     ┆ bad2         ┆ block       ┆ 123            ┆ case1        ┆ NO_CASE_SEVERITY │
│ meta      ┆ 1     ┆ ok1          ┆ observe     ┆ 234            ┆ NO_CASE_NAME ┆ NO_CASE_SEVERITY │
│ hips      ┆ 1     ┆ bad3         ┆ block       ┆ 456            ┆ case2        ┆ medium           │
│ nips      ┆ 1     ┆ ok2          ┆ allow       ┆ 345            ┆ NO_CASE_NAME ┆ NO_CASE_SEVERITY │
│ meta      ┆ 3     ┆ ok3          ┆ NOT_BLOCKED ┆ NO_CASE_NUMBER ┆ NO_CASE_NAME ┆ NO_CASE_SEVERITY │
│ NO_SOURCE ┆ null  ┆ NO_INDICATOR ┆ NOT_BLOCKED ┆ 789            ┆ case3        ┆ low              │
└───────────┴───────┴──────────────┴─────────────┴────────────────┴──────────────┴──────────────────┘
```

Read a whole CSV into memory
```
df6_csv_read = pl.read_csv("df5.csv")
type(df6_csv_read)
# <class 'polars.dataframe.frame.DataFrame'>
```

```
```
