#!/usr/bin/env python3


import gc
import json
import sys
import time
# Elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
# Pandas
# python3 -m pip install pandas
import pandas as pd
# Polars
# python3 -m pip install polars
import polars as pl


# client object
es = Elasticsearch(
	"https://elasticsearch.local:9200",
	ca_certs="/path/to/certs/ca-chain.cert.pem",
	basic_auth=("elastic", "abcd1234")
)


# check connection
es.ping
if es.ping():
	#print("connection successful")
	pass
else:
	print("connection failed")
	sys.exit(1)


# index to search
index_name = "packetbeat-*"


# query to search for documents
query = {
	"aggs": {
		"agg_dns": {
			"terms": {
				"field": "dns.question.name",
				"order": {
					"agg_mintime": "desc"
				},
				"size": 500
			},
			"aggs": {
				"agg_mintime": {
					"min": {
						"field": "@timestamp"
					}
				},
				"agg_maxtime": {
					"max": {
						"field": "@timestamp"
					}
				}
			}
		}
	},
	"size": 0,
	"_source": {
		"excludes": []
	},
	"query": {
		"bool": {
			"must": [],
			"filter": [
				{
					"range": {
						"@timestamp": {
							"format": "strict_date_optional_time",
							"gte": "now-1y",
							"lte": "now"
						}
					}
				}
			],
			"should": [],
			"must_not": []
		}
	},
	"stored_fields": [
		"*"
	],
	"runtime_mappings": {},
	"script_fields": {},
	"fields": [
		{
			"field": "@timestamp",
			"format": "date_time"
		}
	]
}


# send the query to Elasticsearch
search_result = es.search(index=index_name, body=query)
print(" Search Results ".center(50, "="))
#print(type(search_result)) # <class 'elastic_transport.ObjectApiResponse'>
# cast as dictionary
result = dict(search_result)
#print(json.dumps(result, indent=4))


# function that flattens nested dictionaries into dotted keys
# d[key1][key2] --> d.key1.key2
def flatten_dict(y) -> dict:
	""" convert nested dictionaries into flattened dotted keys: see https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10 """
	out = {}
	def flatten(x, name=""):
		if type(x) is dict:
			for a in x:
				flatten(x[a], name + a + ".")
		elif type(x) is list:
			i = 0
			for a in x:
				flatten(a, name + str(i) + ".")
				i += 1
		else:
			out[name[:-1]] = x
	flatten(y)
	return(out)


# list to hold flattened results, to be used for dataframes
for_dataframes = []


print()
# convert results to a flattened structure and append to the for_dataframes list
for result in search_result["aggregations"]["agg_dns"]["buckets"]:
	#print(result["_source"])
	# flatten for simpler dataframe conversions
	r = flatten_dict(result)
	print(r)
	# add to massive list-of-dictionaries for dataframe conversion
	for_dataframes.append(r)
print()


# convert to Pandas dataframe
df_pandas = pd.DataFrame(for_dataframes)
print(" Pandas DataFrame ".center(50, "="))
print(df_pandas)
print()


# convert to Polars dataframe
df_polars = pl.DataFrame(for_dataframes)
print(" Polars DataFrame ".center(50, "="))
print(df_polars)
print()


# empty the old list if massive
for_pandas = []
gc.collect()
