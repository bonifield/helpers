### Files
- splunk-analyst-annotation-maker-dashboard.txt
	- A method of using text inputs to capture analyst annotations into lookup tables (a workaround for Splunk's lack of built-in knowledge management tools); use with the Annotation Viewer dashboard
- splunk-analyst-annotation-viewer-dashboard.txt
	- View analyst annotations; use with the Annotation Maker dashboard
- splunk-byte-and-packet-summary-dashboard.txt
	- Examples of input/output monitoring, with drilldown examples based on loadjob. Includes commented-out queries in case an IP-to-hostname lookup is in place
- splunk-dashboard-example-features.txt
	- Several examples of input types in Splunk's Simple XML, and other features like colorization, drilldowns, and token usage
- splunk-host-last-seen-dashboard.txt
	- Check if any hosts fell off the network, if new hosts appeared, and check for gaps in logs. Can also be used for sensor troubleshooting.

### Helpful Commands
```
# make an HTTP input+token, and use it in a header with cURL/etc to send events
# plain message, will appear in the field "_raw"
curl -k -H "Authorization: Splunk TOKEN-HERE" https://splunk.local:8088/services/collector/event -d '{"sourcetype": "beats", "event": "test event 1234 AAAA"}'
# use JSON to make named field+value pairs
curl -k -H "Authorization: Splunk TOKEN-HERE" https://splunk.local:8088/services/collector/event -d '{"sourcetype": "beats", "event": {"key1":"val1", "key2":"val2"}}'

sudo /opt/splunk/bin/splunk start
sudo /opt/splunk/bin/splunk stop
sudo /opt/splunk/bin/splunk restart
sudo ./splunk stop
sudo ./splunk list index
sudo ./splunk clean eventdata -index _thefishbucket
sudo ./splunk clean eventdata -index [index]
sudo ./splunk start

# force Splunk to recognize new changes to props.conf and/or transforms.conf (try these things IN THIS ORDER)
# Search Bar --> type (yes with a leading pipe)    | extract reload=T
sudo /opt/splunk/bin/splunk restart

# Windows Universal Forwarder helpers
msiexec.exe /i [yoursplunkforwarder].msi RECEIVING_INDEXER="INDEXER_IP_ADDRESS:9997" SERVICESTARTTYPE=manual AGREETOLICENSE=Yes /quiet
# make changes to configs etc then change the service to auto start
sc config SplunkForwarder start=auto
"C:\Program Files\SplunkUniversalForwarder\bin\splunk.exe" start
"C:\Program Files\SplunkUniversalForwarder\bin\splunk.exe" stop
"C:\Program Files\SplunkUniversalForwarder\bin\splunk.exe" restart
```
