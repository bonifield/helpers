#!/usr/bin/python3

#
# test with this query
# ./python-sqlite-03-reader.py -i tacodb -f Alice -a 42
#

import argparse, sys
import sqlite3 as s3
from datetime import datetime, timezone

#now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
#now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

#
#
# DO NOT ALLOW USERS TO SPECIFY THEIR OWN SQL QUERIES AT ANY TIME, FOR ANY REASON, EVER
#
#

# instantiate parser
parser = argparse.ArgumentParser(description="arguments")
# mandatory switches
# make a new argument group then set it to required
requiredArgs = parser.add_argument_group("required arguments")
requiredArgs.add_argument("-i", "--database", dest="dbArgs", default="", type=str, help="database name", required=True)
# optional switches
# short arg, long arg, variable name to be used (accessed as dict), a default value (optional), variable type, help message when using -h
parser.add_argument
parser.add_argument("-t", "--time", dest="timeArgs", default="", type=str, help="timestamp, format YYYY-mm-ddTHH:MM:SSZ (UTC)")
parser.add_argument("-f", "--fname", dest="fnameArgs", default="", type=str, help="first name as a string")
parser.add_argument("-l", "--lname", dest="lnameArgs", default="", type=str, help="first name as a string")
parser.add_argument("-a", "--age", dest="ageArgs", default=9999, type=int, help="age as an integer")
parser.add_argument("-q", "--query", dest="queryArgs", default="", type=str, help="SQLite query wrapped in double-quotes")
# treat args as a dictionarty
args = vars(parser.parse_args())
# create variables from the args object, and string representations of the arguments for Elasticsearch queries
dbName = args["dbArgs"]
timestamp = args["timeArgs"]
fname = args["fnameArgs"]
lname = args["lnameArgs"]
age = args["ageArgs"]
query = args["queryArgs"]

# connect to the database
conn = s3.connect(dbName)
# https://en.wikipedia.org/wiki/Cursor_%28databases%29
#	"...a database cursor is a control structure that enables traversal over the records in a database.
#	Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval,
#	addition and removal of database records."
c = conn.cursor()

# query for fname
if len(fname) > 0:
	print("\nlooking for first name: {}".format(fname))
	q = ('SELECT fname FROM people WHERE ? IN(fname);')
	# execute expects a tuple, include the comma
	for i in c.execute(q, (fname,)):
		print("\t", i)

# query for given arguments
print("\ndumping records matching any provided arguments")
q = ('SELECT * FROM people WHERE ? IN (time) OR ? IN(fname) OR ? IN(lname) OR ? IN(age);')
# remember we are using "timestamp" not "time"
for i in c.execute(q, (timestamp, fname, lname, age)):
	print("\t", i)

# select all records
print('\ndumping all records in table "people"')
x = c.execute("SELECT * FROM people")
for p in x:
	print("\t", p)

# count all records
print('\ncount of all records in table "people"')
x = c.execute("SELECT COUNT(time) FROM people")
for n in x:
	# get first item from tuple
	t = n[0]
	print("\t", t)

print()
conn.close()
