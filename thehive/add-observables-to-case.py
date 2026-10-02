#!/usr/bin/env python3


# uv run upload-observables-to-case.py -c 3
# uv run upload-observables-to-case.py -c 3 -f demo-iocs.txt

import argparse
import json
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from thehive4py import TheHiveApi
from thehive4py.types.observable import InputObservable
# parse IOCs
from parse_ioc import ParseIOC
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
# get arguments
#==================================

def get_arguments():
	"""Retrieves argparse values."""
	parser = argparse.ArgumentParser(description="script description")
	parser.add_argument("-c", "--case-number", dest="case_number", default="1", type=str, help="case number", required=True)
	parser.add_argument("-f", "--file", dest="upload_filename", default="", type=str, help="filename (path) for file to upload")
	return parser.parse_args()


args = get_arguments()


#==================================
# add case observables, one at a time, unlike alerts which just take a dict
# https://docs.strangebee.com/thehive/api-docs/#tag/Observable/operation/Create%20Observable%20in%20Case
# note for multiple observables, it may be faster to create an alert,
#	then use hive.alert.import_in_case(alert_id, case_id)
#	then delete the "helper" alert
#==================================

# please modify this if you use it beyond this demonstration
def add_observables_to_case(raw_ioc, hive_obj, case_id=args.case_number, sighted=False, tlp=2, pap=2, tags=["test-ioc"], message="just a test ioc"):
	"""Upload observables to TheHive5."""
	ioc = raw_ioc.strip()
	# avoid BadRequest exceptions due to blank lines
	if not ioc:
		return
	data_type = ParseIOC(ioc).ioc_type
	#print(ioc, "->", data_type)
	if "ipv" in data_type:
		data_type = "ip"
	if "email" in data_type:
		data_type = "mail"
	obs = InputObservable(
		dataType=data_type,
		data=ioc,
		sighted=sighted,
		ioc=True,
		tlp=tlp,
		pap=pap,
		tags=tags,
		message=message
	)
	try:
		resp = hive.case.create_observable(case_id, observable=obs)
		# or
		# resp = hive.observable.create_in_case(case_id=args.case_number, observable=obs)
		print(ioc, "->", resp)
		return resp
	except Exception as e:
		print(f"{e}")
		return None


#-------------
# using a list sourced from other interactions
#-------------

print(f" add observables to case {args.case_number} ".center(50, "="))

for ioc in ["google.com", "8.8.8.8", "bob@local", "bob@domain.local"]:
	add_observables_to_case(ioc, hive_obj=hive, case_id=args.case_number)
print()


#-------------
# using a file
#-------------

try:
	if args.upload_filename:
		if len(args.upload_filename) > 0:
			print(f" add observables from a file to case {args.case_number} ".center(50, "="))
			with Path(args.upload_filename).open(mode="r", encoding="utf-8") as infile:
				for ioc in infile:
					add_observables_to_case(ioc, hive_obj=hive, case_id=args.case_number)
except Exception as e:
	print(f"{e}")
print()


#==================================
# get case observables
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.find_observables
#==================================

print(f" case {args.case_number} observables ".center(50, "="))
case_obs = hive.case.find_observables(case_id=args.case_number)
print(f"{case_obs=}")
#print(json.dumps(case_obs, indent=4))
print()