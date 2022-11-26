#!/usr/bin/python3

#================================================
#
# simulates acquiring a JSON object and inserting it into the SQLite3 database
#
# python3 python-sqlite3-12-write-json.py ~/testalerts.db
#
#================================================

import uuid
import json
import sqlite3
import sys
import time
from datetime import datetime
from random import randint

try:
	dbName = str(sys.argv[1])
except Exception as e:
	print(str(e))
	print(f"Usage: {sys.argv[0]} /path/to/registryDatabase.db")
	sys.exit(1)

conn = sqlite3.connect(dbName)
print(f"opened connection to {dbName}")
# https://en.wikipedia.org/wiki/Cursor_%28databases%29
#	"...a database cursor is a control structure that enables traversal over the records in a database.
#	Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval,
#	addition and removal of database records."
c = conn.cursor()
tableName = "ALERTS"

def generateJsonLog():
	# simulates fetching a JSON document from another source
	# create a timestamp
	d = datetime.utcnow().timestamp()
	# provided epoch is already in utc time, hence not using datetime.utcfromtimestamp()
	# create nonsense IPs for added effect
	j = {
		"time": datetime.fromtimestamp(d).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
		"epoch": d,
		"rulename": "generic malware inbound test alert",
		"hostname": "nycdc01",
		"username": "bobdomainadmin",
		"transport": "tcp",
		"protocol": "tls",
		"sip": str(randint(256, 999))+"."+str(randint(256, 999))+"."+str(randint(256, 999))+"."+str(randint(256, 999)),
		"dip": str(randint(256, 999))+"."+str(randint(256, 999))+"."+str(randint(256, 999))+"."+str(randint(256, 999)),
		"sport": 443,
		"dport": randint(1025, 65535),
		"guid": str(uuid.uuid4())
	}
	jj = json.dumps(j)
	return(jj)

def insertRecords(c, j):
	q = ("INSERT INTO ALERTS (time, epoch, rulename, hostname, username, transport, protocol, sip, dip, sport, dport, guid, sent) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)")
	c.execute(q, (j["time"], j["epoch"], j["rulename"], j["hostname"], j["username"], j["transport"], j["protocol"], j["sip"], j["dip"], j["sport"], j["dport"], j["guid"], 0))
	print(f"inserted record with guid {j['guid']} into {dbName}")

# insert 10 test logs
for i in range(10):
	simLog = generateJsonLog() # JSON object returned as str
	j = json.loads(simLog) # convert to dict
	insertRecords(c, j)

conn.commit()
print(f"commited changes to {dbName}")
conn.close()
print(f"closed connection to {dbName}")
