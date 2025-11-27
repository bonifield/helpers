#!/usr/bin/env python


import sys
import time
import requests


print("Running. Exit with CTRL+C")
while True:
	try:
		resp = requests.get("test-server:5000")
		print(resp.text)
		time.sleep(5)
	except KeyboardInterrupt:
		print("Detected CTRL+C, goodbye!")
		sys.exit(0)
