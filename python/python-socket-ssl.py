#!/usr/bin/env python3

import json
import os
import socket
import ssl
import sys
from datetime import datetime, timezone

try:
	HOSTNAME = sys.argv[1]
	PORT = sys.argv[2]
except Exception as e:
	print(str(e))
	print(f"USAGE: {sys.argv[0]} DestHostname DestPort")
	sys.exit(1)

# track originating host
agentname = str(socket.gethostname())
# track script sending data
# __file__ can only be referenced in a script as it comes from sys.argv[0])
filepath = str(os.path.realpath(__file__))

payload = {
	"@timestamp": str(datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3])+"Z",
	"message": "This JSON document was sent over an SSL/TLS-wrapped Python3 Socket object.",
	"ecs": {
		"version": "1.0.0"
	},
	"agent": {
		"type": "customlogger",
		"version": "0.1.0",
		"name": agentname
	},
	"file": {
		"path": filepath
	},
	"labels": {
		"custom_message": "Labels are automatically keyword fields. Do not use nested values beyond the first level, such as labels.xyz. Refresh your Kibana tab to update field types if you are viewing brand new fields as they stream in."
	}
}

# convert dict to str
payload = json.dumps(payload)
# cleanup
payload = payload.replace("\r","").replace("\n","").strip()
# newline for NDJSON parser
payload = payload + "\n"
# convert str to bytes
payload = payload.encode()

context = ssl.create_default_context()
#context.load_verify_locations("ca-chain.cert.pem")
#context.check_hostname = True
# below is unsafe but useful for testing
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

# convert "with" statements into variables if sending documents using for-loops
with socket.create_connection((HOSTNAME, PORT)) as sock:
	with context.wrap_socket(sock, server_hostname=HOSTNAME) as tlssock:
		print(tlssock.version())
		tlssock.send(payload)
	tlssock.close()
