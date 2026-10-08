# TheHive API Examples

`send-alert.py`
- send an alert with observables
- attach files to that alert

`send-alert-promote-to-case.py`
- send an alert with observables
- attach files to that alert
- promote the alert to a case
	- the files become case-level attachments

`case-actions.py`
- add observables to a case using multiple methods
- get case observables
- upload and download case attachments

`merge-alerts-into-case.py`
- use filters to locate relevant alerts by status, time, observable
- merge alerts into a case

`find-alerts-cases-observables.py`
- use filters to locate relevant alerts and cases by status, time, observable
- find alerts with desired observables
- find cases with desired observables

`case-and-tasklog-comments.py`
- add case comments
- create a new task, if it doesn't exist already
- add tasklog comments to the new task
- attach files to the tasklog comment

`add-observables-to-case.py`
- add observables from a list or file to a given case

`tasklog-file-upload-only.py`
- upload one or more files to a case task log, with an optional message

`download-case-and-tasklog-files.py`
- download case and task-level files from a given case

`get-case-observables.py`
- get observables for a given case

`get-alert.py` and `get-case.py`
- get a single alert or case, respectively

---

These scripts require you to have:
- TheHive5 running
- An organisation (note "s" not "z") named `homelab`
- A user (that isn't the default admin) with an API key
- create a `.env` file containing `hive_api` and `hive_url`
- TODO: add Docker quickstart notes

*This process, using the Docker version, takes ~5 minutes or less to get configured.*

[Installation Methods](https://docs.strangebee.com/thehive/installation/installation-methods/)

[API Docs](https://docs.strangebee.com/thehive/api-docs/)

[thehive4py Python Docs](https://thehive-project.github.io/TheHive4py/latest/reference/client/)

[thehive4py Offical Examples](https://github.com/TheHive-Project/TheHive4py/tree/main/examples)

---

### Anywhere you use [case_id](https://thehive-project.github.io/TheHive4py/latest/reference/endpoints/#thehive4py.endpoints.case.CaseId) you may use the case ID, such as "~1234" (with tilde), or the number displayed in the web view, such as "42" (as a string).

```
hive.case.get(case_id="~1234")
hive.case.get(case_id="42")
```

---

### Default Observable Types

```
autonomous-system
domain
file
filename
fqdn
hash
hostname
ip
mail
mail-subject
other
regexp
registry
uri_path
url
user-agent
```

### Default Case `status` and `stage` Options

- all statuses and stages are displayed by default in the web GUI
- note the trailing `d` in `Duplicated` for cases
- `uv run get-case.py -c 1234 | jq '{stage, status}'`

| status | stage |
| -- | -- |
| `New` | `New` |
| `InProgress` | `InProgress` |
| `Duplicated` | `Closed` |
| `FalsePositive` | `Closed` |
| `Indeterminate` | `Closed` |
| `Other` | `Closed` |
| `TruePositive` | `Closed` |

### Default Alert `status` and `stage` Options

- all statuses and stages are displayed by default in the web GUI
- note the lack of trailing `d` in `Duplicate` for alerts
- `uv run get-alert.py -a ~567890 | jq '{stage, status}'`

| status | stage |
| -- | -- |
| `New` | `New` |
| `InProgress` | `InProgress` |
| `Pending` | `InProgress` |
| `Imported` | `Imported` |
| `Duplicate` | `Closed` |
| `FalsePositive` | `Closed` |
| `Ignored` | `Closed` |

### Traffic Light Protocol (TLP) - how information may be **shared**
- used when creating alerts or managing cases
- see full descriptions in the [MISP TLP Taxonomy](https://github.com/MISP/misp-taxonomies/blob/main/tlp/machinetag.json)

| Number | Value | TLP Meaning |
| -- | -- | -- |
| 0 | clear | formerly "white"; Recipients can spread this to the world, there is no limit on disclosure. |
| 1 | green | Limited disclosure, recipients can spread this within their community. |
| 2 | amber | Limited disclosure, recipients can only spread this on a need-to-know basis within their organization and its clients. |
| 3 | amber+strict | Limited disclosure, recipients can only spread this on a need-to-know basis within their organization. |
| 4 | red | For the eyes and ears of individual recipients only, no further disclosure. |

### Permissable Actions Protocol (PAP) - how information may be **used**
- used when creating alerts or managing cases
- see full descriptions in the [MISP PAP Taxonomy](https://github.com/MISP/misp-taxonomies/blob/main/PAP/machinetag.json)

| Number | Value | PAP Meaning |
| -- | -- | -- |
| 0 | clear | No restrictions in using this information. |
| 1 | green | Active actions allowed. Recipients may use PAP:GREEN information to ping the target, block incoming/outgoing traffic from/to the target or specifically configure honeypots to interact with the target. |
| 2 | amber | Passive cross check. Recipients may use PAP:AMBER information for conducting online checks, like using services provided by third parties (e.g. ripe whois), or set up a monitoring honeypot. |
| 3 | red | Non-detectable actions only. Recipients may not use PAP:RED information on the network. Only passive actions on logs, that are not detectable from the outside. |

### Misc Imports

[main client](https://thehive-project.github.io/TheHive4py/latest/reference/client/): `from thehive4py import TheHiveApi`
[observable creation](https://thehive-project.github.io/TheHive4py/latest/reference/types/#thehive4py.types.observable.InputObservable): `from thehive4py.types.observable import InputObservable`
[query filters](https://thehive-project.github.io/TheHive4py/latest/reference/query/): `from thehive4py.query import Eq, Asc, Desc, Gte` (etc)

---

## Examples

### `uv run send-alert-promote-to-case.py`
- or run `send-alert.py` to generate test alerts, without promoting them to a case

new alert with `imported` status (promoted to case)

![new alert with `imported` status (promoted to case)](images/alert_imported_status.png)

alert observables

![alert observables](images/alert_observables.png)

alert attachments

![alert attachments](images/alert_attachments.png)

### `uv run case-actions.py`

**hardcode the demo case ID and case number at the top of the script**

the new case

![the new case](images/case_new.png)

case description body

![case description body](images/case_description.png)

case file attachments

![case file attachments](images/case_attachments.png)

### `uv run case-and-tasklog-comments.py -c <id|number>`

case comment

![case comment](images/case_comment.png)

new task

![new task](images/case_task.png)

task tasklogs (comments) with markdown and file attachment

![task tasklog](images/case_task_tasklog.png)
