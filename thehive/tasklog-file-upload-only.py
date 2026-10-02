#!/usr/bin/env python3


# provide a case number
#	 uv run tasklog-file-upload-only.py -c 3 -t "Block Files" -f file1.txt [-f file2.txt, ...] [-m <message>]
# or provide a case ID
#	 uv run tasklog-file-upload-only.py -c ~135384 -t "Block Files" -f file1.txt [-f file2.txt, ...] [-m <message>]



import argparse
import os
import sys
import urllib3
from datetime import datetime, timezone
from dotenv import load_dotenv
from thehive4py import TheHiveApi
from thehive4py.types.comment import InputComment
from thehive4py.types.task import InputTask
from thehive4py.types.task_log import InputTaskLog
from thehive4py.query import Eq
# suppress the TLS warning
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
	parser.add_argument("-t", "--task-name", dest="task_name", default="Block Files", type=str, help="task name")
	parser.add_argument("-m", "--message", dest="message", default="attached block files", type=str, help="task log text for the file upload")
	# -f creates a list of files, used by hive.task_log.add_attachment()
	# and make default argument into a list
	parser.add_argument("-f", "--file", dest="upload_filename", action="append", default=[], type=str, help="filename (path) for file to upload")
	return parser.parse_args()


args = get_arguments()


#==================================
# send a tasklog message, use its task_log_id to attach files
# attach a file to a task
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.task_log.TaskLogEndpoint.add_attachment
#==================================

print(" case tasks ".center(50, "="))
tasks = hive.case.find_tasks(case_id=args.case_number)
print(f"{tasks=}")
print()

# check if the task exists
task_id = None
for task in tasks:
	if task["title"] == args.task_name:
		task_id = task["_id"]
		break
		# may want to access or keep
		# task["_id"], task["status"], task["title"]

# create the task if it doesn't exist
if not task_id:
	task = InputTask(title=args.task_name)
	print(f" creating task {args.task_name} ".center(50, "="))
	resp = hive.case.create_task(case_id=args.case_number, task=task)
	task_id = resp["_id"]
	print(f'{resp["_id"]=}')
	print(resp)
	print()

# should provide a dynamic value here
message = args.message

print(f" sending message and getting task_log_id ".center(50, "="))
task_log = InputTaskLog(message=message)
resp = hive.task_log.create(task_id=task_id, task_log=task_log)
# we'll attach a file to this task further below
task_log_id = resp["_id"]
print(resp)
print()

print(f" adding attachment to {task_log_id=} ".center(50, "="))
resp = hive.task_log.add_attachment(task_log_id=task_log_id, attachment_paths=args.upload_filename)
print(resp)
print()


