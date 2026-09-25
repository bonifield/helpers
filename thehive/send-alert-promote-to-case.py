#!/usr/bin/env python3


import os
import sys
import urllib3
import uuid
from datetime import datetime, timezone
from dotenv import load_dotenv
from thehive4py import TheHiveApi
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
# create observables, tags, alert type, and alert as a dictionary
#==================================

observables = [
	{"dataType":"domain", "data":"google.com"},
	{"dataType":"ip", "data":"8.8.8.8"},
	{"dataType":"mail", "data":"admin@google.com"},
]

now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

description = f'''
Alert xyz triggered at {now_utc}
---
This is an alert description body. Add useful data here. TheHive supports markdown.
---
| column 1 | column 2 |
| -- | -- |
| val 1 | val 2 |

- [Link to Incident Response Playbook]()
- [Link to Direct Action Playbooks]()
- [Link to Points of Contact]()
'''

# tlp 1=green, 2=amber
# all of these values should be constructed from sensor or SIEM data
# sourceRef could be a Splunk documentId, Elasticsearch _id, or a unique sensor value, etc
alert = {
	"title": f"{now_utc} - test alert title",
	"type": "host_sensor_alert",
	"description": description,
	"tlp": 1,
	"pap": 2,
	"sourceRef": str(uuid.uuid4()),
	"source": "sensor_type",
	"observables": observables,
	"tags": ["test", "dev"],
}
print(f"{alert=}")
print()


#==================================
# create the alert in TheHive, add file attachments
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.alert.AlertEndpoint.create
#==================================

try:
	print(" sending alert ".center(50, "="))
	alert_response = hive.alert.create(alert=alert)
	print(f"{alert_response=}")
except Exception as e:
	sys.exit(f"{e}")


# upload attachment to the alert
alert_id = None
if alert_response.get("_id", None):
	# hive.alert.add_attachment() NEEDS THE TILDE IN THE ID, SO DO NOT REMOVE IT
	alert_id = alert_response["_id"] # NO: .lstrip("~").strip()
	print(f"{alert_id=}")
	print()
	# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.alert.AlertEndpoint.add_attachment
	filenames = ["./files/test1.txt", "./files/test2.txt"]
	# don't try to send any missing files
	missing_files = [f for f in filenames if not os.path.isfile(f)]
	if missing_files:
		print(f"warning: could not find these files: {missing_files}")
	else:
		# alert_id (str), attachment_paths (list[str]), can_rename (bool)
		print(" uploading file to alert ".center(50, "="))
		upload_response = hive.alert.add_attachment(alert_id, filenames, can_rename=True)
		print(f"{upload_response=}")
		print()
else:
	sys.exit(f"{alert_response=}")


#==================================
# promote the alert to a case
# https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.alert.AlertEndpoint.promote_to_case
#==================================

print(" promoting alert to case ".center(50, "="))
promotion_response = hive.alert.promote_to_case(alert_id)
print(f"{promotion_response=}")
print()

case_id = None
case_number = None
# check response code
if getattr(promotion_response, "status_code", 200) in (200, 201):
	if promotion_response.get("_id", None):
		case_id = promotion_response["_id"] # NO: .lstrip("~").strip()
		# the number that appears to users when a case is created, ex. "1234"
		case_number = promotion_response["number"]
		print(f"created case id {case_id}, case number {case_number}")
		print()
else:
	sys.exit(f"could not promote alert {alert_id} to a case; response from TheHive: {promotion_response}")
