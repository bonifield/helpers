#!/usr/bin/python3

##############
# Matches forward and reverse hashes
# of potentially reversed strings
# into one object dictionary
#
# random/choice is used to provide a
# unique string (of any desired length)
# to serve as the key for a future dict
#
# IN PRACTICE, USE MD5 OR SHA256
#
##############

from random import choice
from string import digits

##############

string1 = "12345"
string2 = "54321"
string3 = "67890"
string4 = "09876"
string5 = "ABCDE"
string6 = "EDCBA"
string7 = "FGHIJ"
string8 = "JIHGF"
string9 = "12345"
string0 = "TACOS"

worker = str("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}".format(string1, string2, string3, string4, string5, string6, string7, string8, string9, string0)).split()

##############

dict1 = {}
def method1(): # extends all values into one list
	for i in worker:
		randval = str(''.join(choice(digits) for i in range(8)))
		vals = str("{0} {1}".format(i, randval)).split()
		h = str(hash(i))
		r = str(hash(i[::-1]))
		try:
			if h not in dict1.keys() and r not in dict1.keys():
				dict1[h]=vals
			elif h in dict1.keys() and r not in dict1.keys():
				dict1[h].extend(vals)
			elif h not in dict1.keys() and r in dict1.keys():
				dict1[r].extend(vals)
		except:
			pass
# it is possible to extend multiple values at once with double parentheses
# dictionary[key].extend((val1, val2, val3))

dict2 = {}
def method2(): # appends all items into their own lists
	for i in worker:
		randval = str(''.join(choice(digits) for i in range(8)))
		vals = [i, randval]
		h = str(hash(i))
		r = str(hash(i[::-1]))
		try:
			if h not in dict2.keys() and r not in dict2.keys():
				dict2.setdefault(h,[])
				dict2[h].append(vals)
			elif h in dict2.keys() and r not in dict2.keys():
				dict2[h].append(vals)
			elif h not in dict2.keys() and r in dict2.keys():
				dict2[r].append(vals)
		except:
			pass



def printer():
	print()
	print("method 1")
	for k,v in dict1.items():
		print("len(v): {0}\t {1} {2}".format(len(v),k,v))

	print()
	print("method 2")
	for k,v in dict2.items():
		print("len(v): {0}\t {1} {2}".format(len(v),k,v))

##############

method1()
method2()
printer()
