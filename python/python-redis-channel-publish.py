#!/usr/bin/env python3

# publish dictionary as JSON to Redis channel, will be stored as bytes

import json
import sys
import time
from random import randint
# python3 -m pip install redis
import redis

r = redis.Redis(host="localhost", port=6379, db=0, password="myredispassword")
p = r.pubsub()

print("Press CTRL+C to exit...")
while True:
	try:
		num = randint(2,254)
		msg = {	"message":{"ip":f"192.168.1.{num}"}}
		msg = json.dumps(msg)
		r.publish("mychannel", msg)
		time.sleep(0.25)
	except KeyboardInterrupt:
		print()
		print("CTRL+C detected. Goodbye!")
		sys.exit(0)
