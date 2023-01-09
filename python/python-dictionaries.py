#!/usr/bin/python3

# dictionaries are comprised of key-value pairs
# keys are unique, values are not

import collections
import json

dicta = {"key1":"value1","key2":"value2","key3":[3,"threethree"],4:[44, 444],5:"five"}

print('\nwhole dictionary in raw form')
print(dicta)

print('\nprint all keys in a dict')
for k in dicta.keys():
	print(k)

print('\nprint all values in a dict')
for v in dicta.values():
	print(v)

print('\nprint all items (key-value pairs) in a dict')
for k,v in dicta.items():
	print(k,v)

print('\naccess key3\'s value directly')
print(dicta["key3"])

print('\nuse a generator to print a key\'s value (which is a list)')
print(' '.join(str(x) for x in dicta["key3"]))

print('\nchange an existing key\'s value')
dicta["key3"]="value3"

print('\nadd a new key to the dict and assign it a value')
dicta['key6']='value6'
print(dicta['key6'])

print('\nuse a function that works with either\n\texisting keys that have values which are lists, or\n\tmake a new key with a value which is a list')
def dgen(d,k,v):
	if k not in d.keys():
		d.setdefault(k,[])
		d[k].append(v)
	elif k in d.keys():
		d[k].append(v)
dgen(dicta,4,'new_value4')
print(dicta[4])

print('\nremove a key by name (key2) and it\'s value from a dict')
dicta.pop('key2', None)
print(dicta)

print('\nmerge two dictionaries')
dictb = {"key10":"value10", "key11":11, 12:"k12", 13:131313}
print('dicta - '+str(dicta))
print('dictb - '+str(dictb))
# dictc = {**dicta, **dictb} # uncomment if Python 3.5 or greater and ignore function below
def merger(x,y):
	z = x.copy()
	z.update(y)
	return(z)
dictc = merger(dicta, dictb)
print('dictc - '+str(dictc))	

print('\npretty-print dicta using json.dumps()')
j = json.loads(json.dumps(dicta))
print(json.dumps(j, indent=4))
#print(json.dumps(dicta, indent=4)) # this works too, if you do not want a json object at all

# create a deeply-nested dictionary or create a deeply-nested key in an existing dictionary
# https://stackoverflow.com/questions/67930334/create-a-nested-dictionary-of-arbitrary-depth-in-python/67930462#67930462
def recursive_dict():
	return collections.defaultdict(recursive_dict)
xyz = recursive_dict()
xyz['a']['b']['c'] = 3
xyz['a']['b']['d']['e'] = 4
print(json.dumps(xyz))

print()
