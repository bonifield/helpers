#!/usr/bin/env python3


# uv run get-case.py -c 3


import argparse
import json
import os
import sys
from dotenv import load_dotenv
from thehive4py import TheHiveApi
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
	return parser.parse_args()


args = get_arguments()


#==================================
# get a case
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.get
#==================================

the_case =  hive.case.get(case_id=args.case_number)
print(json.dumps(the_case, indent=4))