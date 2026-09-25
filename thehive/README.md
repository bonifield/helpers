# TheHive API Examples

`send-alert.py`
- sending an alert with observables
- attaching files to that alert

`send-alert-promote-to-case.py`
- sending an alert with observables
- attaching files to that alert
- promoting the alert to a case

`case-actions.py`
- getting case ID and number
- adding observables to a case using multiple methods
- getting case observables
- uploading and downloading case attachments

`merge-alerts-into-cases.py`
- using filters to locate relevant alerts by status, time, observable
- merging alerts into a case

`find-alerts-cases-observables.py`
- using filters to locate relevant alerts and cases by status, time, observable
- finding alerts with desired observables
- finding cases with desired observables

---

These scripts require you to have:
- TheHive5 running
- An organisation (note "s" not "z") named `homelab`
- A user (that isn't the default admin) with an API key
- create a `.env` file containing `hive_api` and `hive_url`

*This process, using the Docker version, takes ~3 minutes or less to get configured.*

[Installation Methods](https://docs.strangebee.com/thehive/installation/installation-methods/)

[API Docs](https://docs.strangebee.com/thehive/api-docs/)

[thehive4py Python Docs](https://thehive-project.github.io/TheHive4py/latest/reference/client/)

[thehive4py Offical Examples](https://github.com/TheHive-Project/TheHive4py/tree/main/examples)

---

### `uv run send-alert.py`

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
