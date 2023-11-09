#!/usr/bin/python3

import json

# only for terminal colorization, this is not part of the flattening/un-flattening process
def printGreen(input) -> str:
	""" newline + green terminal color character + provided text + terminal color reset character """
	print(f"\n\033[92m{input}\033[0m")

# example dictionary
d = {"toplevel1":{"layer2":"val1"}, "toplevel2":{"nested2":{"nested3":"val2"}}}

#====================
# flatten traditional nested keys into a single dotted string key
# ex. "toplevel2":{"nested2":{"nested3":... --> "toplevel2.nested2.nested3"
#====================
def flatten_dict(y) -> dict:
	""" convert nested dictionaries into flattened dotted keys: see https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10 """
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

#print("\n"+tcol.GREEN+"original"+tcol.RESET)
printGreen("original")
print(json.dumps(d, indent=4))

#original
#{
#    "toplevel1": {
#        "layer2": "val1"
#    },
#    "toplevel2": {
#        "nested2": {
#            "nested3": "val2"
#        }
#    }
#}

#print("\n"+tcol.GREEN+"flattened"+tcol.RESET)
printGreen("flattened")
dd = flatten_dict(d)
print(json.dumps(dd, indent=4))

#flattened
#{
#    "toplevel1.layer2": "val1",
#    "toplevel2.nested2.nested3": "val2"
#}

#====================
# un-flatten dotted string keys into traditional nested keys
# ex. "toplevel2.nested2.nested3" -> "toplevel2":{"nested2":{"nested3":...
#====================
def unflatten_dict(dictionary) -> dict:
	""" convert dotted keys into nested dictionaries: see https://stackoverflow.com/questions/6037503/python-unflatten-dict """
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

#print("\n"+tcol.GREEN+"un-flattened / back to original"+tcol.RESET)
printGreen("un-flattened / back to original")
u = unflatten_dict(dd)
print(json.dumps(u, indent=4))

#un-flattened / back to original
#{
#    "toplevel1": {
#        "layer2": "val1"
#    },
#    "toplevel2": {
#        "nested2": {
#            "nested3": "val2"
#        }
#    }
#}

#print("\n"+tcol.GREEN+"example flattening for config file dump or backup"+tcol.RESET)
printGreen("example flattening for config file dump or backup")
for k,v in dd.items():
	print(str(k)+" = "+str(v))

#example flattening for config file dump or backup
#toplevel1.layer2 = val1
#toplevel2.nested2.nested3 = val2

print()
