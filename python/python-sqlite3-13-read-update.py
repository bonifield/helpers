#!/usr/bin/python3

#================================================
#
# simulates reading from the SQLite3 database, sending row data elsewhere, and updating the row to indicate it sent successfully
#
# python3 python-sqlite3-13-read-update.py ~/testalerts.db
#
#================================================

import sqlite3
import sys

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

def updateRecord(c, r):
	# update the row based on GUID to change "sent" from 0 to 1
	guid = r[11]
	print(f"called updateRecord() for record with guid {guid}")
	q = ("UPDATE ALERTS SET sent=? WHERE guid=?")
	c.execute(q, (1, guid))
	return

def sendSimulation(c, r):
	# simulate sending to an external system successfully
	guid = r[11]
	print(f"sent record with guid {guid} to the external system, updating sent value")
	updateRecord(c, r)
	return

print("< before >".center(50, "="))
rows = c.execute("SELECT * FROM ALERTS WHERE sent = '0';")
for row in rows:
	print(type(row).__name__, row)

print("< during >".center(50, "="))
rows = c.execute("SELECT * FROM ALERTS WHERE sent = '0';").fetchall()
# https://stackoverflow.com/questions/10404988/python-sqlite3-for-loop-update
#	"Using .fetchall() returns a list of results so that you have them stored locally before you re-use the cursor."
for row in rows:
	sendSimulation(c, row)
	conn.commit()
	print(f"commited changes to {dbName}")

print("< after >".center(50, "="))
rows = c.execute("SELECT * FROM ALERTS")
for row in rows:
	print(type(row).__name__, row)

conn.commit()
print(f"commited changes to {dbName}")
conn.close()
print(f"closed connection to {dbName}")