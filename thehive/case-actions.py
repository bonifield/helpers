#!/usr/bin/env python3


import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from thehive4py import TheHiveApi
from thehive4py.types.observable import InputObservable
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

# for demonstration, hardcode these values
# KEEP THE TILDE!
CASE_ID = "~4325528"
CASE_NUMBER = 5


#==================================
# convert user-visible case number, to case ID
# ex. 1234 --> "~8638672"
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.get
#==================================

some_case = hive.case.get(case_id=str(CASE_NUMBER))
real_case_id = some_case["_id"]
print(f"{real_case_id=}")
# note these variables aren't used below, since the case ID is hardcoded above
print()


#==================================
# add case observables, one at a time, unlike alerts which just take a dict
# https://docs.strangebee.com/thehive/api-docs/#tag/Observable/operation/Create%20Observable%20in%20Case
# note for multiple observables, it may be faster to create an alert,
#    then use hive.alert.import_in_case(alert_id, case_id)
#    then delete the helper alert
#==================================

new_obs1 = InputObservable(
	dataType="domain",
	data="yahoo.com",
	sighted=False,
	ioc=True,
	tags=["test-ioc"],
	tlp=2,
	pap=2,
	message="just a test ioc"
)
new_obs2 = InputObservable(
	dataType="domain",
	data="bing.com",
	sighted=False,
	ioc=True,
	tags=["test-ioc"],
	tlp=2,
	pap=2,
	message="just a test ioc"
)
print(f"uploading observable: {new_obs1=}")
print(f"uploading observable: {new_obs2=}")
print()
#
# method 1 using hive.case.create_observable()
# hive.case.create_observable() NEEDS THE TILDE IN THE ID, SO DO NOT REMOVE IT
obs_response_one = hive.case.create_observable(case_id=CASE_ID, observable=new_obs1)
print(obs_response_one)
#
# method 2 using hive.observable.create_in_case()
obs_response_two = hive.observable.create_in_case(case_id=CASE_ID, observable=new_obs2)
print(obs_response_two)
#
# add these to a list then loop over it, using either method
print()


#==================================
# get case observables
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.find_observables
#==================================

case_obs = hive.case.find_observables(case_id=CASE_ID)
print(f"{case_obs=}")
print()


#==================================
# add case attachments
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.add_attachment
#==================================

filenames_for_case = ["./test3.txt", "./test4.txt"]
# don't try to send any missing files
missing_files = [f for f in filenames_for_case if not os.path.isfile(f)]
if missing_files:
	print(f"warning: could not find these files: {missing_files}")
else:
	try:
		# case_id (str), attachment_paths (list[str])
		# not graceful - will throw errors if a file already exists
		case_upload_response = hive.case.add_attachment(CASE_ID, filenames_for_case)
		print(f"{case_upload_response=}")
		print()
	except Exception as e:
		print(f"{e}")


#==================================
# get case attachments
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.find_attachments
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.organisation.OrganisationEndpoint.download_attachment
#==================================

# safely make the path first
download_path = Path(f"./downloads/{CASE_NUMBER}")
download_path.mkdir(parents=True, exist_ok=True)

case_attachments = hive.case.find_attachments(case_id=CASE_ID)
print(f"{case_attachments=}")

for att in case_attachments:
	print(att["_id"], att["name"])
	#hive.organisation.download_attachment(att["_id"], f"./downloads/{CASE_NUMBER}/{att['name']}")
	full_download_path = download_path / att["name"]
	hive.organisation.download_attachment(att["_id"], full_download_path)


