#!/usr/bin/env python3


import json
import os
import sys
import uuid
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dotenv import load_dotenv
from thehive4py import TheHiveApi
from thehive4py.query import Eq, Asc, Desc, Gte
#from thehive4py.types.observable import InputObservable
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


#==================================
# build your filters
# https://thehive-project.github.io/TheHive4py/latest/reference/query/#thehive4py.query.filters.FilterExpr
#==================================

# make a filter object using Eq and the IOCs you want
# ampersand = "and", pipe = "or"
obs_filter = (
	(Eq("dataType", "ip") & Eq("data", "8.8.8.8"))
	|
	(Eq("dataType", "domain") & Eq("data", "google.com"))
)

# calculate a lookback date of 90 days ago, in milliseconds (hive uses ms in the _createdAt field)
earliest_time_ms = int((datetime.now(timezone.utc) - timedelta(days=90)).timestamp() * 1000)
# make a filter object using Gte and the earliest timestamp you want (90 days)
alert_filter = Gte("_createdAt", earliest_time_ms)

# sort arguments; newest first (for oldest first, use Asc("_createdAt") (and be sure to import it)
sort_args = Desc("_createdAt")


#==================================
# search all ALERTS for given observables, using the date filter
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.alert.AlertEndpoint.find
#==================================

# list-of-dicts; will hold all alerts, and their observables, also as a list-of-dicts
alerts_with_obs = []
# first pull alerts, which DO NOT include observables in the response object
for each_alert in hive.alert.find(filters=alert_filter):
	# you have to pull observables from each alert
	observables =  hive.alert.find_observables(alert_id=each_alert["_id"], filters=obs_filter, sortby=sort_args)
	if observables:
		alerts_with_obs.append({"alert":each_alert, "observables":observables})
print(" matching alerts ".center(50, "="))
print(json.dumps(alerts_with_obs, indent=4))


#==================================
# search all CASES for given observables, using the date filter
# just change hive.alert.(...) to hive.case.(...)
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.find
#==================================

# list-of-dicts; will hold all alerts, and their observables, also as a list-of-dicts
cases_with_obs = []
# first pull alerts, which DO NOT include observables in the response object
for each_case in hive.case.find(filters=alert_filter):
	# you have to pull observables from each alert
	observables =  hive.case.find_observables(case_id=each_case["_id"], filters=obs_filter, sortby=sort_args)
	if observables:
		cases_with_obs.append({"alert":each_case, "observables":observables})
print(" matching cases ".center(50, "="))
print(json.dumps(cases_with_obs, indent=4))
