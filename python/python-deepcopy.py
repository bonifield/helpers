#!/usr/bin/env python3


import copy


def process(d):
	for k,v in d.items():
		c = 0
		for i in v:
			v[c] = i*2
			c += 1
	return(d)


dd = {"key1":[1, 2, 3]}


print("-"*100)
print("dd pre-function:\t", dd)
p = process(dd)
print("p function output:\t", p)
print("dd post-function:\t", dd, "<-- Huh!?")
print('\tnotice that the global dictionary "dd" changes; the dict sent to the function is a shallow copy, meaning')
print('\tit refers to the same object in memory and is not a true "full copy"; depth actions (modifying values, etc)')
print('\twill affect *both* dictionaries (again, because they are actually the same thing)')




print("-"*100)




def process2(d):
	ddd = copy.deepcopy(d)
	for k,v in ddd.items():
		c = 0
		for i in v:
			v[c] = i*2
			c += 1
	return(ddd)


dd = {"key1":[1, 2, 3]}


print("dd pre-function:\t", dd)
p = process2(dd)
print("p function output:\t", p)
print("dd post-function:\t", dd)
print("\tby using copy.deepcopy(obj), a new object is created in memory, and the original is left intact")
print("-"*100)




'''
----------------------------------------------------------------------------------------------------
dd pre-function:         {'key1': [1, 2, 3]}
p function output:       {'key1': [2, 4, 6]}
dd post-function:        {'key1': [2, 4, 6]} <-- Huh!?
        notice that the global dictionary "dd" changes; the dict sent to the function is a shallow copy, meaning
        it refers to the same object in memory and is not a true "full copy"; depth actions (modifying values, etc)
        will affect *both* dictionaries (again, because they are actually the same thing)
----------------------------------------------------------------------------------------------------
dd pre-function:         {'key1': [1, 2, 3]}
p function output:       {'key1': [2, 4, 6]}
dd post-function:        {'key1': [1, 2, 3]}
        by using copy.deepcopy(obj), a new object is created in memory, and the original is left intact
----------------------------------------------------------------------------------------------------
'''
