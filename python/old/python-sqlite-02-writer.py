#!/usr/bin/env python3

import sys
import sqlite3 as s3
from datetime import datetime, timezone

try:
	dbName = str(sys.argv[1])
except Exception as e:
	print("Usage: script.py newDatabaseName")
	sys.exit(1)

now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

# connect to the database
conn = s3.connect(dbName)
# https://en.wikipedia.org/wiki/Cursor_%28databases%29
#	"...a database cursor is a control structure that enables traversal over the records in a database.
#	Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval,
#	addition and removal of database records."
c = conn.cursor()

def insert_records(x):
	for entry in x:
		t = entry[0]
		f = entry[1]
		l = entry[2]
		a = entry[3]
		try:
			# insert into table (column names) values (values to insert)
			q = ('INSERT INTO people (time, fname, lname, age) VALUES (?,?,?,?)')
			c.execute(q, (t, f, l, a))
		except Exception as e:
			print(str(e))
	# always commit after inserting records
	conn.commit()

peopleList = [
	[now, "John", "Smith", "42"],
	[now, "Alice", "Allison", "50"],
	[now, "Bob", "Robertson", "60"]
]

if __name__ == "__main__":
	insert_records(peopleList)
	conn.close()
