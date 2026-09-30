#!/usr/bin/env python3


# provide a case number
#     uv run case-and-tasklog-comments.py -c 1
# or provide a case ID
#     uv run case-and-tasklog-comments.py -c ~1234



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
	# instantiate parser
	parser = argparse.ArgumentParser(description="script description")
	# optional switches
	parser.add_argument("-c", "--case-number", dest="case_number", default="1", type=str, help="case number", required=True)
	parser.add_argument("-f", "--file", dest="upload_filename", default="files/tasklog_file.txt", type=str, help="filename (path) for file to upload")
	return parser.parse_args()


args = get_arguments()


#==================================
# make a case filter then pull the actual case _id value (~1234), if provided a number like 5678
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.get
#==================================

# look for _id (~1234) or number value (1)
if args.case_number.isdigit():
	case_id = hive.case.get(case_id=str(args.case_number))["_id"]
else:
	case_id = args.case_number

print(f"{case_id=}")

case_filter = Eq("_id", case_id)


#==================================
# create a case-level comment (displayed on the sidebar within a case)
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.comment.CommentEndpoint.create_in_case
#==================================

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

comment = InputComment(message=f"Hello, world! The current time is {now_utc}")

resp = hive.comment.create_in_case(case_id=case_id, comment=comment)
print(resp)
print()


#==================================
# create a task-level comment within a case
# assumes you have a task named "observable sweep"
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.find_tasks
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseEndpoint.create_task
# https://thehive-project.github.io/TheHive4py/latest/reference/types/#thehive4py.types.task.InputTask
# https://thehive-project.github.io/TheHive4py/latest/reference/types/#thehive4py.types.task_log.InputTaskLog
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.task_log.TaskLogEndpoint.create
#==================================

# we want to make an "Observable Sweep" task, if:
# - the task wasn't in a case template, when the case was created or imported from an alert
# - the task wasn't otherwise created by an analyst
# - the task got deleted

tasks = hive.case.find_tasks(case_id=case_id)
print(f"{tasks=}")
print()

task_id = None
for task in tasks:
	if task["title"] == "Observable Sweep":
		task_id = task["_id"]
		break
		# may want to access or keep
		# task["_id"], task["status"], task["title"]

if not task_id:
	task = InputTask(title="Observable Sweep")
	resp = hive.case.create_task(case_id=case_id, task=task)
	task_id = resp["_id"]
	print(f'{resp["_id"]=}')
	print(resp)
	print()

# add a new comment to that task
# note now we use InputTaskLog instead of InputComment
task_log = InputTaskLog(message="Hello, world!")
# applied to the task, not the case, hence task_id
resp = hive.task_log.create(task_id=task_id, task_log=task_log)
print(resp)
print()


#==================================
# sending a formatted message
#==================================

message = f"""
this is a formatted task log comment sent at {now_utc}

there won't be a line break between this and the above line,

nor this; use triple-hyphen markdown separators

---

`wrapped single code line`

```
multiline
code block
```

markdown table

| h1 | h2 |
| --- | --- |
| v11 | v21 |
| v12 | v22 |

---

bulleted list
- one
- two

"""

task_log = InputTaskLog(message=message)
resp = hive.task_log.create(task_id=task_id, task_log=task_log)
# we'll attach a file to this task further below
task_log_id = resp["_id"]
print(resp)
print()


#==================================
# attach a file to a task
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.task_log.TaskLogEndpoint.add_attachment
#==================================

the_file = "files/tasklog_file.txt"
# wrap all files in a list
files_to_attach = [the_file]
resp = hive.task_log.add_attachment(task_log_id=task_log_id, attachment_paths=files_to_attach)
print(resp)
print()


