#!/usr/bin/python3

# yes, this code and script are very messy

# generator expressions create items on the fly
#	- uses ()
#	- useful for one iteration, and large or infinite sequences
#	- gens don't support indexing or slicing
#	- gens cannot be added to lists
# list comprehensions will create an entire list in memory first
#	- uses []
#	- useful for multiple iterations and/or storing results
#	- lists are iterables (can use for x in y statements, etc.)
#
# https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

listy = ['one', 'two', 'three', 'four', 'five']

#gene = (i for i in listy)
#comp = [i for i in listy]
gene = (i*i for i in range(5))
comp = [i*2 for i in range(5)]

def printer(msg, x):
	print(' {} '.format(msg).center(50,'='))
	print(' type '.center(30,'-'))
	print(type(x))
	try:
		print(' length '.center(30,'-'))
		print(len(x))
	except:
		print('cannot determine length of object')
		pass
	print(' object '.center(30,'-'))
	print(x)
	print(' iterating over object '.center(30,'-'))
	for i in x:
		print(i)
	print()
	print()

print()
printer('Generator Expression', gene)
printer('Iterable List Comprehension', comp)

#######

print(' Yield statement usage '.center(50,'='))
# this function only returns the generator object
# subsequent "for" calls on an instantiated generator object will run the code in the function
def createGen():
	l = range(5)
	for x in l:
		yield x*x

mygen = createGen() # creates a generator
print(mygen) # mygen is an object
for i in mygen: # iterate over the object, which is generated on the fly
	print(i)
