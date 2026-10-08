#!/usr/bin/env python3


# uv run download-case-and-tasklog-files.py -c 3


import argparse
import getpass
import os
import sys
from pathlib import Path
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
# make download path
#==================================

# safely make the path first
#download_path = Path(f"/home/{getpass.getuser()}/cases/{args.case_number}/downloads/")
download_path = Path(f"./downloads/{args.case_number}")
download_path.mkdir(parents=True, exist_ok=True)

def download_file(name, id):
	# download files from TheHive5
	# should pass hive and path objects if called from another file
	# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.organisation.OrganisationEndpoint.download_attachment
	print(f"downloading {name}")
	full_download_path = download_path / name.strip().replace(" ", "_")
	hive.organisation.download_attachment(id, full_download_path)
	print(f"\tsaved to: {full_download_path}")


#==================================
# get case tasks, get task logs, and download all files
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.task.TaskEndpoint.find
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.task.TaskEndpoint.find_logs
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.organisation.OrganisationEndpoint.download_attachment
#==================================

case_tasks = hive.case.find_tasks(case_id=args.case_number)

print(f" downloading tasklog-level files ".center(50, "="))
for each_task in case_tasks:
	task_logs = hive.task.find_logs(task_id=each_task["_id"])
	for each_task_log in task_logs:
		# multiple sanity checks because of edge cases
		if each_task_log.get("attachments", None):
			if len(each_task_log["attachments"]) > 0:
				for att in each_task_log["attachments"]:
					download_file(att["name"], att["_id"])
print()


#==================================
# get case attachments
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.find_attachments
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.organisation.OrganisationEndpoint.download_attachment
#==================================

# get a list of all attachments
print(f" downloading case-level files ".center(50, "="))
case_attachments = hive.case.find_attachments(case_id=args.case_number)

# download the attachments to the directory
for att in case_attachments:
	download_file(att["name"], att["_id"])
print()
