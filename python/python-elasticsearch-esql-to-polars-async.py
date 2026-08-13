#!/usr/bin/env python3


# ES|QL references
# https://www.elastic.co/docs/reference/query-languages/esql
# https://www.elastic.co/docs/reference/query-languages/esql/esql-syntax-reference
# https://www.elastic.co/docs/reference/query-languages/esql/esql-rest
# https://www.elastic.co/docs/explore-analyze/query-filter/languages/esql-kibana
# https://www.elastic.co/docs/solutions/security/esql-for-security/esql-threat-hunting-tutorial


import asyncio
import os
import polars as pl
from dotenv import load_dotenv
from elasticsearch import AsyncElasticsearch, ApiError, TransportError


load_dotenv()


query = """
FROM logs-*
| WHERE (`event.module`=="network_traffic" AND @timestamp >= (NOW() - 24 hours))
  AND (destination.domain IN ("ubuntu.com") OR destination.domain LIKE "*.ubuntu.*")
| STATS count = count(*) BY destination.domain
| SORT count DESC
| LIMIT 1000
| KEEP destination.domain, count
"""


async def query_elasticsearch(cluster: AsyncElasticsearch, query: str, semaphore: asyncio.Semaphore) -> pl.DataFrame | None:
	# use the semaphore as a context manager
	async with semaphore:
		try:
			# Elasticsearch can return the Apache Arrow format, which Polars can zero-copy read into a dataframe
			resp = await cluster.esql.query(query=query, format="arrow")
			df = pl.from_arrow(resp.body)
			return df if not df.is_empty() else None
		except (ApiError, TransportError) as e:
			print(str(e))
			return None


async def query_handler(clusters: list, queries: list[str], max_concurrency: int = 10) -> list[pl.DataFrame]:
	# will hold a list of polars dataframes
	results: list[pl.DataFrame | None] = []
	# https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore
	semaphore = asyncio.Semaphore(max_concurrency)
	# Python 3.11+ uses a TaskGroup context manager to "hold a group of tasks"
	# https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup
	# Changed in version 3.14: Passes on all kwargs to loop.create_task()
	async with asyncio.TaskGroup() as tg:
		# this is a list comprehension instead of building a list in nested for loops
		tasks = [
			tg.create_task(query_elasticsearch(cluster, query, semaphore))
			for cluster in clusters
			for query in queries
		]
		print(f"sending {len(tasks)} queries")
	# ensure no None objects in the returned "results" list
	valid_dfs = [t.result() for t in tasks if t.result() is not None]
	return valid_dfs


async def main():

	elastic_api_encoded = os.environ["ELASTIC_API_ENCODED"]

	async with AsyncElasticsearch(
		"https://elasticsearch01.local:9200",
		api_key = elastic_api_encoded,
		ca_certs = "certs/ca-chain.pem",
		client_cert = "certs/public.pem",
		client_key = "certs/private.key",
		max_retries=3,
		request_timeout=120.0,
	) as es:
		# create a list of clusters (in case you need to query multiple at once)
		clusters = [es]
		# create a list of queries (to be read from an external provider or config)
		queries = [query]
		# send asynchronous queries and get back a list of polars dataframes
		result_dataframes = await query_handler(clusters, queries)
		if not result_dataframes:
			print(f"no dataframes returned: {result_dataframes=}")
			return
		# combine into one single result
		combined = pl.concat(result_dataframes, how="diagonal")
		# print all rows for the sake of demonstration
		with pl.Config(tbl_rows=-1, set_fmt_str_lengths=150):
			print(combined)


if __name__ == "__main__":
	asyncio.run(main())
