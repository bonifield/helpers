#!/usr/bin/python3

#
# add key/value pairs to every entry in a JSON file, for project tracking or adding timestamps etc
#
# example usage:
# 	cat food.json
#		{"apples": "red"}
# 	python-json-enrich.py food.json lemon=yellow grape=purple fake=False floaty=1.02 number=7 truth=True fruit="very delicious"
#	cat food.json
#		{"apples": "red", "lemon": "yellow", "grape": "purple", "fake": false, "floaty": 1.02, "number": 7, "truth": true, "fruit": "very delicious"}
#	all of the values are corrected to int, bool, or float if able
#
# optionally un-comment the datetime components in the function to add a timestamp during enrichment
#

from datetime import datetime
import hashlib
import json
import os
import shutil
import sys

try:
	INPUTFILE = sys.argv[1]
	NEW_VALUES = sys.argv[2:]
except:
	print()
	print("USAGE")
	print("python-json-enrich.py /path/to/file.json key1=value1 key2=value2")
	print('ex.')
	print("enrich-json.py /path/to/file.json apple=red lemon=yellow")
	print()
	sys.exit(1)

def enrich_json_file(inputFile, *args):
	"""add key/value pairs to every entry in a JSON file, for project tracking or adding timestamps etc"""
	#
	#
	# create a timestamp
#	now = datetime.utcnow()
#	epoch = str(now.timestamp())
#	timestamp = str(now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')[:-3])
	# process args and instantiate the dictionary with timestamps
#	d = {"@timestamp":timestamp, "epoch":epoch} # Elasticsearch time field
#	d = {"_time":timestamp, "epoch":epoch} # Splunk time field
	#
	#
	# process args
	d = {}
	for arg in args:
		a = arg.split("=") # split each argument
		k = a[0] # set the key
		v = a[1] # set the value
		# check if booleans were presented
		try:
			if v.lower() == "true":
				v = True
		except:
			pass # explicitly silence
		try:
			if v.lower() == "false":
				v = False
		except:
			pass # explicitly silence
		# check if v is an integer
		try:
			if v.isdigit():
				v = int(v)
		except:
			pass # explicitly silence
		# check if v is a float
		try:
			if not isinstance(v, int):
				v = float(v)
		except:
			pass # explicitly silence
		# load the dictionary with the key and processed value
		d[k] = v
	#
	#
	# process files
	p = os.path.dirname(inputFile) # just path
	f = os.path.basename(inputFile) # just file
	mf = hashlib.md5(f.encode('utf-8')).hexdigest() # md5 hash string of the file, to serve as a temporary name for the output file
	outputFile = os.path.join(p, mf) # the full path to the new output file
	# begin writing the new file
	with open(inputFile, "r", encoding="utf-8") as infile:
		with open(outputFile, "w") as outfile:
			for line in infile:
				l = json.loads(line) # l is now a dict
				l = {**l, **d} # merge all of the custom keys
				outfile.write(json.dumps(l)+"\n") # add a newline character for proper application/x-ndjson handling if needed, and readability
		outfile.close()
	infile.close()
	shutil.move(outputFile, inputFile) # overwrite the original file with the newly-enriched file

if __name__ == "__main__":
	enrich_json_file(INPUTFILE, *NEW_VALUES)
