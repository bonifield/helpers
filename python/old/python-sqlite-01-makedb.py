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

try:
	# make a table with 4 columns
	c.execute('CREATE TABLE people (time DATETIME, fname VARCHAR(99), lname VARCHAR(99), age INT(5));')
	print('made database named {}'.format(dbName))
	conn.commit()
	conn.close()
except Exception as e:
	print(str(e))

sys.exit()
