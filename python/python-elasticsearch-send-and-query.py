#!/usr/bin/env python3

import gc
import json
import time
# Elasticsearch
from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
# Pandas
import pandas as pd

# client object
es = Elasticsearch(
	"https://elasticsearch.local:9200",
	ca_certs="/path/to/ca-chain.cert.pem",
	basic_auth=("elastic", "abcd1234")
)

# check connection
es.ping
if es.ping():
	print("connection successful")
else:
	print("connection failed")

# sample document to upload, as a dictionary
doc = {
	"source":{ "ip":"192.168.10.10" },
	"destination":{ "ip":"192.168.30.30" }
}

# upload to specific index
index_name = "static_index_test"
# you can specify an ID if you need to update records based on some known value
es.index(index=index_name, document=doc, id="aaaa")

# give elasticsearch time to ingest the sample document
time.sleep(2)
# search for documents
search_result = es.search(index=index_name, query={"match_all": {}})
print(" search results ".center(50, "="))
print(search_result)

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

for_pandas = []

# use scan to paginate results; first argument is the client object; returns iterator
# note query argument uses top-level "query" parameter
scan_result = scan(es, index=index_name, query={"query":{"match_all": {}}})
print(" scan results ".center(50, "="))
for result in scan_result:
	print(result["_source"])
	# flatten for simpler dataframe conversions
	r = flatten_dict(result["_source"])
	print(r)
	# add to massive list-of-dictionaries for dataframe conversion
	for_pandas.append(r)

# convert to dataframe
df = pd.DataFrame(for_pandas)
print(" DataFrame ".center(50, "="))
print(df.head())

# empty the old list if massive
for_pandas = []
gc.collect()
