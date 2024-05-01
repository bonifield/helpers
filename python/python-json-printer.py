#!/usr/bin/env python3

import json
import sys

try:
	with open(sys.argv[1], 'r') as f:
		data = json.load(f)
	f.close()
	print(json.dumps(data, indent=4, sort_keys="True"))
except Exception as e:
	print(str(e))
	print()
	print("USAGE:")
	print(f"{sys.argv[0]} somefile.json")
	print()
