#!/usr/bin/env python3

# get (LPOP) a value from a Redis list

import json
import sys
import time
# python3 -m pip install redis
import redis

r = redis.Redis(host="localhost", port=6379, db=0, password="myredispassword", decode_responses=True)

print("Press CTRL+C to exit...")
while True:
	try:
		m = r.lpop("mylist")
		if m:
			#print(m) # str decoded from bytes
			if isinstance(m, str):
				mm = json.loads(m)
				print(mm)
		time.sleep(0.001)
	except KeyboardInterrupt:
		print()
		print("CTRL+C detected. Goodbye!")
		sys.exit(0)
