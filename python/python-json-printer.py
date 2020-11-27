#!/usr/bin/python

import json,sys

try:
	with open(sys.argv[1], 'r') as f:
		data = json.load(f)
		print json.dumps(data, indent=4, sort_keys="True")
except Exception as e:
	print "Usage:  json-printer.py somefile.json\n%s" % (str(e))
