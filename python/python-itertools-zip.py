#!/usr/bin/python3

#
# goal: for each index in multiple lists, get that index in all of the lists at once, and create a new object with those peer items
# use itertools zip/zip_longest to walk multiple lists at once
#

import itertools

l1 = ["A", "B", "C", "1", "2"]
l2 = ["a", "b", "c", "6", "7", "qqq"]
l3 = ["F", "G", "H", "1", "2", "qqq", "rrr"]
l4 = ["f", "g", "h", "6", "7", "qqq", "rrr", "sss"]

# make a combined list if desired for readability, so you can just use zip(*list_of_lists) instead of zip(*[l1, l2, l3, l4])
#list_of_lists = [l1, l2, l3, l4]
#print(list_of_lists)
# [['A', 'B', 'C', '1', '2'], ['a', 'b', 'c', '6', '7', 'qqq'], ['F', 'G', 'H', '1', '2', 'qqq', 'rrr'], ['f', 'g', 'h', '6', '7', 'qqq', 'rrr', 'sss']]

print()
print("="*100)
print()

zipped_list = []
#for (item) in zip(*list_of_lists):
for (item) in zip(*[l1, l2, l3, l4]):
	zipped_list.append(item)
print("a new list of tuples using zip(*[l1, l2, l3, l4]) which stops when the end of the shortest member is reached:")
print(zipped_list) # list of tuples
# [('A', 'a', 'F', 'f'), ('B', 'b', 'G', 'g'), ('C', 'c', 'H', 'h'), ('1', '6', '1', '6'), ('2', '7', '2', '7')]

print()
print("="*100)
print()

zipped_list_longest = []
#for (item) in itertools.zip_longest(*list_of_lists, fillvalue="filler"):
for (item) in itertools.zip_longest(*[l1, l2, l3, l4], fillvalue="filler"):
	zipped_list_longest.append(item)
print("a new list of tuples using itertools.zip_longest(*[l1, l2, l3, l4]) which adds filler terms, or None by default, when the shorter members end but the longest member is still being iterated")
print(zipped_list_longest) # list of tuples, "filler" is placed positionally as needed, when shorter lists run out of values
# [('A', 'a', 'F', 'f'), ('B', 'b', 'G', 'g'), ('C', 'c', 'H', 'h'), ('1', '6', '1', '6'), ('2', '7', '2', '7'), ('filler', 'qqq', 'qqq', 'qqq'), ('filler', 'filler', 'rrr', 'rrr'), ('filler', 'filler', 'filler', 'sss')]

print()
print("="*100)
print()


keys_to_map = ["uid", "acct", "pid", "guid"]
for v in zipped_list:
	x = [a for a in zip(keys_to_map,v)] # list of tuples, each tuple is a key and value
	print("list of tuples:\t\t\t", x)
	xx = ["=".join(a) for a in x] # list of key=value pair strings
	print("list of key=value pairs:\t", xx)
	xxx = "&".join(xx) # ex. a URL query string ready to be appended
	print("ampersand-joined string:\t", xxx)
	print()
	# list of tuples:                  [('uid', 'A'), ('acct', 'a'), ('pid', 'F'), ('guid', 'f')]
	# list of key=value pairs:         ['uid=A', 'acct=a', 'pid=F', 'guid=f']
	# ampersand-joined string:         uid=A&acct=a&pid=F&guid=f

print()
print("="*100)
print()

for v in zipped_list_longest:
	x = [a for a in zip(keys_to_map,v)] # list of tuples, each tuple is a key and value
	print("list of tuples:\t\t\t", x)
	xx = ["=".join(a) for a in x] # list of key=value pair strings
	print("list of key=value pairs:\t", xx)
	xxx = "&".join(xx) # ex. a URL query string ready to be appended
	print("ampersand-joined string:\t", xxx)
	print()
	# list of tuples:                  [('uid', 'filler'), ('acct', 'filler'), ('pid', 'rrr'), ('guid', 'rrr')]
	# list of key=value pairs:         ['uid=filler', 'acct=filler', 'pid=rrr', 'guid=rrr']
	# ampersand-joined string:         uid=filler&acct=filler&pid=rrr&guid=rrr


print()
print("="*100)
print()
