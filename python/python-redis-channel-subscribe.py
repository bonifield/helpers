#!/usr/bin/env python3

# subscribe to Redis channel and convert bytes containing JSON to dictionary

import json
import sys
import time
# python3 -m pip install redis
import redis

r = redis.Redis(host="localhost", port=6379, db=0, password="myredispassword", decode_responses=True)
s = r.pubsub()
s.subscribe("mychannel")

print("Press CTRL+C to exit...")
while True:
	try:
		m = s.get_message()
		if m:
			#print(m) # dict
			data = m["data"] # str decoded from bytes
			if isinstance(data, str):
				data_dict = json.loads(data)
				print(data_dict)
	except KeyboardInterrupt:
		print()
		print("CTRL+C detected. Goodbye!")
		sys.exit(0)
