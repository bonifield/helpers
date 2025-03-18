#!/usr/bin/env python3

import json
import time
from elasticsearch import Elasticsearch

#=============
# client object
#=============

es = Elasticsearch(
	"https://elasticsearch.local:9200",
	ca_certs="/path/to/ca-chain.cert.pem",
	basic_auth=("elastic", "abcd1234")
)

#=============
# check connection
#=============

es.ping
if es.ping():
	print("connection successful")
else:
	print("connection failed")

query = {
	"query": 'SELECT "@timestamp","source.ip","destination.ip","source.port","destination.port" FROM "packetbeat-*" WHERE "source.ip"=\'127.0.0.1\' ORDER BY "@timestamp" DESC'
}
# add LIMIT 20 after DESC if needed

#=============
# query Elasticsearch
#=============

def get_results(resp, page):
	""" prints paginated results """
	print("="*10, "START OF PAGE", page, "="*10)
	if resp.get("columns"):
		print("COLUMNS:", resp["columns"])
	print(resp["rows"])
	print("="*10, "END OF PAGE", page, "="*10)
	if resp.get("cursor"):
		body = {"cursor":resp["cursor"]}
		next_resp = es.sql.query(body=body)
		page += 1
		get_results(next_resp, page)

search_result = es.sql.query(body=query)

if search_result:
	get_results(search_result, page=1)
