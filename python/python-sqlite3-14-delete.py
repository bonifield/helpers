#!/usr/bin/python3

#================================================
#
# simulates reading from the SQLite3 database and deleting rows that match a condition
#
# python3 python-sqlite3-14-delete.py ~/testalerts.db
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

print("< existing records before deletion >".center(50, "="))
s = c.execute(f"SELECT * FROM {tableName};").fetchall()
# https://stackoverflow.com/questions/10404988/python-sqlite3-for-loop-update
#	"Using .fetchall() returns a list of results so that you have them stored locally before you re-use the cursor."
for row in s:
	print(row)
	# alternatively send the GUID to a function for additional checks or modifications

print("< removing old records >".center(50, "="))
c.execute(f"DELETE FROM {tableName} WHERE sent = '1';")
# commit the DELETE statement
conn.commit()

print("< checking for any remaining records >".center(50, "="))
s = c.execute(f"SELECT * FROM {tableName};").fetchall()
for row in s:
	print(row)
	# alternatively send the GUID to a function for targeted deletion

conn.close()
print(f"closed connection to {dbName}")
