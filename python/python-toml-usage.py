#!/usr/bin/python3

# install the Python TOML module:
#	sudo apt install python3-toml
#	or
#	pip3 install toml
# see also https://github.com/uiri/toml

import json
import sys
import toml

try:
	inputFile = sys.argv[1]
except:
	print(f"USAGE: {sys.argv[0]} somefile.toml")
	sys.exit(1)

# toml.load() = store the loaded TOML config file as a dictionary
t = toml.load(inputFile)
print(t)

# toml.dumps() = dump the dict as a TOML-formatted string object, for writing to a file
d = toml.dumps(t)
print(d)

# toml.loads() = store a TOML-formatted string directly (see d above, or if provided as a multi-line string directly in a script)
r = toml.loads(d)
print(r)

# dump the dict as a JSON string object
j = json.dumps(t, indent=4)
print(j)