#!/usr/bin/env python3


# run send-alert.py a few times before using this script
# also hardcode your case number below (include the tilde)


import json
import os
import sys
import uuid
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dotenv import load_dotenv
from thehive4py import TheHiveApi
from thehive4py.query import Eq, Desc, Gte
# suppress the TLS warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


load_dotenv()
hive_url = os.getenv("hive_url")
hive_api = os.getenv("hive_api")

if not hive_url or not hive_api:
	sys.exit("'hive_url' or 'hive_api' missing from environment variables")


#==================================
# create TheHiveApi object
# https://thehive-project.github.io/TheHive4py/latest/reference/client/
#==================================

hive = TheHiveApi(
	url=hive_url,
	apikey=hive_api,
	organisation="homelab",
	verify=False,
)

# case to import into for demo
CASE_ID = "~4325528"


#==================================
# build your filters
# https://thehive-project.github.io/TheHive4py/latest/reference/query/#thehive4py.query.filters.FilterExpr
#==================================

# make a filter object using Eq and the IOCs you want, and New status (not imported, etc)
# ampersand = "and", pipe = "or"
obs_filter = (
	(Eq("dataType", "ip") & Eq("data", "8.8.8.8"))
	|
	(Eq("dataType", "domain") & Eq("data", "google.com"))
)

# calculate a lookback date of 90 days ago, in milliseconds (hive uses ms in the _createdAt field)
earliest_time_ms = int((datetime.now(timezone.utc) - timedelta(days=90)).timestamp() * 1000)
# make a filter object using Gte and the earliest timestamp you want (90 days)
alert_filter = (
	Gte("_createdAt", earliest_time_ms)
	&
	(Eq("status", "New") | Eq("status", "InProgress"))
	&
	Eq("type", "host_sensor_alert")
)

# sort arguments; newest first (for oldest first, use Asc("_createdAt") (and be sure to import it)
sort_args = Desc("_createdAt")


#==================================
# search all alerts for given observables, using the date filter
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.alert.AlertEndpoint.find
#==================================

# list of alert IDs
alerts_to_merge = []
# first pull alerts, which DO NOT include observables in the response object
print(" finding filtered alerts ".center(50, "="))
for each_alert in hive.alert.find(filters=alert_filter):
	# you have to pull observables from each alert
	observables =  hive.alert.find_observables(alert_id=each_alert["_id"], filters=obs_filter, sortby=sort_args)
	if observables:
		print(f'will merge: {each_alert["_id"]} (status: {each_alert["status"]})')
		alerts_to_merge.append(each_alert["_id"])
print(f"{alerts_to_merge=}")


#==================================
# merge found alerts into a given case
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.alert.AlertEndpoint.merge_into_case
# or bulk merge (possibly exposed you to exceptions)
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.alert.AlertEndpoint.bulk_merge_into_case
#==================================

print(" merge alerts ".center(50, "="))
for alert_id in alerts_to_merge:
	# use a try block, to avoid a race condition where an analyst may have already manually imported the alert, causing an exception
	# this will override "InProgress", "FalsePositive", "Duplicate", and other statuses if possible, and change them to "Imported"
	#### *** set your filter finds these things; the demo only looks for New or InProgress ***
	try:
		print(f"attempting to merge {alert_id}")
		resp = hive.alert.merge_into_case(alert_id=alert_id, case_id=CASE_ID)
		print(resp)
		print()
	except Exception as e:
		print(f"{e}")
		# should be something like:
		# TheHiveError('BadRequest - Alert is already imported')
		# NotFoundError - Alert not found
