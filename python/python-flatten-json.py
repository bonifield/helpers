#!/usr/bin/python3

d = {"toplevel1":{"layer2":"val1"}, "toplevel2":{"nested2":{"nested3":"val2"}}}

def flatten_json(y):
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

print("\noriginal")
print(d)

print("\nflattened")
dd = flatten_json(d)
print(dd)

print("\nfor flat config file dump")
for k,v in dd.items():
	print(str(k)+" = "+str(v))
print()
