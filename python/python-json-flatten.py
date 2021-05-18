#!/usr/bin/python3

import json

# only for colorization, this is not part of the JSON flattening/un-flattening process
class tcol:
	GREEN = '\033[92m'
	RESET = '\033[0m'

d = {"toplevel1":{"layer2":"val1"}, "toplevel2":{"nested2":{"nested3":"val2"}}}

def flatten_json(y):
	# https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10
	out = {}
	def flatten(x, name=""):
		if type(x) is dict:
			for a in x:
				flatten(x[a], name + a + ".")
		elif type(x) is list:
			i = 0
			for a in x:
				flatten(a, name + str(i) + ".")
				i += 1
		else:
			out[name[:-1]] = x
	flatten(y)
	return(out)

print("\n"+tcol.GREEN+"original"+tcol.RESET)
print(json.dumps(d, indent=4))

print("\n"+tcol.GREEN+"flattened"+tcol.RESET)
dd = flatten_json(d)
print(json.dumps(dd, indent=4))

print("\n"+tcol.GREEN+"for flat config file dump"+tcol.RESET)
for k,v in dd.items():
	print(str(k)+" = "+str(v))

# un-flatten from a config
# read all dot-keys back into a flat dictionary as the keys, and values as each value (similar to "dd" above)

def unflatten_json(dictionary):
	# https://stackoverflow.com/questions/6037503/python-unflatten-dict
	resultDict = dict()
	for key, value in dictionary.items():
		parts = key.split(".")
		d = resultDict
		for part in parts[:-1]:
			if part not in d:
				d[part] = dict()
			d = d[part]
		d[parts[-1]] = value
	return(resultDict)

print("\n"+tcol.GREEN+"un-flattened"+tcol.RESET)
u = unflatten_json(dd)
print(json.dumps(u, indent=4))
