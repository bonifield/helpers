#!/usr/bin/env python3


import sys


#====================
# precendence of operators in a function: standard operators, *args, **kwargs
# ex. somefunc(a, b, *args, **kwargs)
#====================
# *args is the "unpacking operator" for an iterable object
#====================
# **kwargs is the "unpacking operator" for iterable key=value pairs
# in a nutshell, **kwargs converts key:value to key=value
#====================


#====================
# using "*"
#====================


# iterate over a list directly
print()
listy = [1, 2, 3, 4, 5, 6]
print(*listy)

# strings are iterable, so using "*" will unpack them
print()
ss = "string to unpack"
print(ss)
print(*ss)

# unpack a string to a list, but this is pretty unreadable and non-Pythonic
# the "*" expects an iterable, and the comma treats the following string as a tuple, which then outputs to a list "tt"
print()
*tt, = "string to unpack again"
print(type(tt))
print(tt)

# a is first item, c is last item, everything in between is b
print()
a, *b, c = listy
print(a)
print(b)
print(c)


#====================
# merging lists and dictionaries
#====================


# merge two lists using "*"
print()
listA = [1, 2, 3]
listB = [4, 5, 6]
listC = [*listA, *listB]
print(listC)

# merge two dictionaries using "**"
print()
dictA = {"keyOne":"valueOne", "keyTwo":"valueTwo"}
dictB = {"keyThree":"valueThree", "keyFour":"valueFour"}
dictC = {**dictA, **dictB}
print(dictC)


#====================
# example function using "*args"
#====================


# this function takes a variable number of arguments, so use "*args" to capture them all at once
def add_numbers(*args):
	result = 0
	for x in args:
		try:
			result += x
		except:
			print("skipping item (non-int found): {}".format(x))
	return("the result is {}".format(result))

print()
print("using *args to process multiple arguments at once")
n = add_numbers(1, 2, "a", 3, 4)
print(n) # outputs: the result is 10


#====================
# example function using "**kwargs"
#====================


# this is why merging dictionaries A and B is (typically) expressed as C = {**A, **B}
def print_dict(**kwargs):
	for k,v in kwargs.items():
		print("key: {}\tvalue: {}".format(k, v))

print()
print("using **kwargs as the function input")
d = {"apple":"red", "orange":"orange", "cherry":"red", "watermelon":"green", "lemon":"yellow"}
print_dict(**d)

print()
# same as calling key=value inside the function directly
print("using key=value format for each pair in the function input")
print_dict(apple="red", orange="orange", cherry="red", watermelon="green", lemon="yellow")


#====================
# load a dictionary with command line arguments
#====================


def get_cli_arguments(*args):
	d = {}
	for arg in args:
		a = arg.split("=") # split each argument
		k = a[0] # set the key
		v = a[1] # set the value
		d[k] = v # load the dict
		print(k, v) # just for show
	print(d) # do something with d

# get_cli_arguments(*sys.argv[1:]) # commented because this script does not otherwise expect inputs like this
# usage:
#	script.py a=b c=d
# outputs:
#	a b
#	c d
#	{'a': 'b', 'c': 'd'}



print()
