#!/usr/bin/env python3

import json
import sys

try:
	with open(sys.argv[1], 'r') as infile:
		for line in infile:
			data = json.loads(line)
			print(json.dumps(data, indent=4, sort_keys="True"))
	infile.close()
except Exception as e:
	print(str(e))
	print()
	print("USAGE:")
	print(f"{sys.argv[0]} somefile.ndjson")
	print()
