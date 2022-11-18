#!/usr/bin/python3

#================================================
#
# connects to a SQLite3 database and creates a new table, if the table does not already exist
#
# python3 python-sqlite3-11-makedb.py ~/testalerts.db
#
#================================================

import sqlite3
import sys
from datetime import datetime

try:
	dbName = str(sys.argv[1])
except Exception as e:
	print(str(e))
	print(f"Usage: {sys.argv[0]} /path/to/registryDatabase.db")
	sys.exit(1)

# connect to the database
conn = sqlite3.connect(dbName)
print(f"opened connection to {dbName}")
# https://en.wikipedia.org/wiki/Cursor_%28databases%29
#	"...a database cursor is a control structure that enables traversal over the records in a database.
#	Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval,
#	addition and removal of database records."
c = conn.cursor()
tableName = "ALERTS"
try:
	c.execute(f"CREATE TABLE {tableName} (time DATETIME, epoch REAL, rulename VARCHAR(999), hostname VARCHAR(999), username VARCHAR(999), transport VARCHAR(999), protocol VARCHAR(999), sip VARCHAR(999), dip VARCHAR(999), sport INT(5), dport INT(5), guid VARCHAR(999), sent INT(1));")
	print(f"created table {tableName}")
	conn.commit()
	print(f"commited changes to {dbName}")
except sqlite3.OperationalError as e:
	print(str(e))

conn.close()
print(f"closed connection to {dbName}")

'''
# alternative way to check if the table already exists, without relaying on sqlite3.OperationalError
print("checking for ALERTS table")
tableList = c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='ALERTS';").fetchall()
# returns a list of tuples
if ("ALERTS",) not in tableList:
	print(f"table {tableName} not found, creating table")
	c.execute(f"CREATE TABLE {tableName} (time DATETIME, epoch REAL, rulename VARCHAR(999), guid VARCHAR(999), sent INT(1));")
	print(f"made table {tableName}")
	conn.commit()
'''