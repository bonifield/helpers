#!/usr/bin/env python3


# uv run case-actions.py -c 3
# uv run case-actions.py -c 3 -f file1.txt [-f file2.txt ...]


import argparse
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


#==================================
# get arguments
#==================================

def get_arguments():
	"""Retrieves argparse values."""
	parser = argparse.ArgumentParser(description="script description")
	parser.add_argument("-c", "--case-number", dest="case_number", default="1", type=str, help="case number", required=True)
	# use this to upload multiple files, each with -f, such as "-f file1.txt -f file2.txt ..."
	parser.add_argument("-f", "--file", dest="upload_filename", action="append", default=[], type=str, help="filename (path) for file to upload")
	return parser.parse_args()


args = get_arguments()


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
print(" add observables ".center(50, "="))
print(f"adding observable: {new_obs1=}")
print(f"adding observable: {new_obs2=}")
print()
#
# method 1 using hive.case.create_observable()
# hive.case.create_observable() NEEDS THE TILDE IN THE ID, SO DO NOT REMOVE IT
obs_response_one = hive.case.create_observable(case_id=args.case_number, observable=new_obs1)
print(obs_response_one)
#
# method 2 using hive.observable.create_in_case()
obs_response_two = hive.observable.create_in_case(case_id=args.case_number, observable=new_obs2)
print(obs_response_two)
#
# add these to a list then loop over it, using either method
print()


#==================================
# get case observables
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.find_observables
#==================================

print(" case observables ".center(50, "="))
case_obs = hive.case.find_observables(case_id=args.case_number)
print(f"{case_obs=}")
print()


#==================================
# add case-level attachments
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.add_attachment
#==================================

args.upload_filename.extend(["./files/test3.txt", "./files/test4.txt"])
# don't try to send any missing files
missing_files = [f for f in args.upload_filename if not os.path.isfile(f)]
if missing_files:
	print(f"warning: could not find these files: {missing_files}")
else:
	for f in args.upload_filename:
		# hive.case.add_attachment() is NOT graceful!
		# if a file exists, it will not attempt to upload subsequent files, so loop over them instead
		try:
			print(f" upload {f} to case ".center(50, "="))
			# case_id (str), attachment_paths (list[str])
			f = [f]
			case_upload_response = hive.case.add_attachment(args.case_number, f)
			print(f"{case_upload_response=}")
			print()
		except Exception as e:
			print(f"{e}")
print()

#==================================
# get case attachments
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.find_attachments
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.organisation.OrganisationEndpoint.download_attachment
#==================================

# safely make the path first
download_path = Path(f"./downloads/{args.case_number}")
download_path.mkdir(parents=True, exist_ok=True)

# get a list of all attachments
print(f" case attachments to be downloaded ".center(50, "="))
case_attachments = hive.case.find_attachments(case_id=args.case_number)
print(f"{case_attachments=}")
print()

# download the attachments to the directory
print(" downloading files ".center(50, "="))
for att in case_attachments:
	print(f'ID: {att["_id"]}, FILENAME: {att["name"]}')
	full_download_path = download_path / att["name"]
	hive.organisation.download_attachment(att["_id"], full_download_path)
	print(full_download_path)
print()