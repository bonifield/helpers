#!/usr/bin/env python3


import json


# load() the entire file (not for NDJSON) as a dict
print("read an entire JSON file")
with open("data.json", "r", encoding="utf-8") as f:
	d = json.load(f)
print(type(d))
print(d)
print()

# dump dict as JSON string with indentation
j = json.dumps(d, indent=4)
print(type(j))
print(j)
print()

# loads() from a JSON string to dict
d2 = json.loads(j)
print(type(d2))
print(d2)
print()

# dump() to file "output.json" with indentation
#with open("output.json", "w", encoding="utf-8") as output_file:
#	json.dump(d2, output_file, indent=4, ensure_ascii=False)

# process NDJSON one line at a time
print("read NDJSON one line at a time")
with open("data.ndjson", "r", encoding="utf-8") as f2:
	for line in f2:
		l = json.loads(line)
		print(type(l), l)
print()
