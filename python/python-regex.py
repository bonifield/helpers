#!/usr/bin/env python3

import re

stringy = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print("+"*42)
print(stringy)
print("+"*42)

# pipe multiple matches into one structure if needed:
#     - first regex - looks for "in" and anything after until a space
#     - second regex - looks for "x", then exactly 6 lowercase alphas
# multiline will search across line breaks, and dotall matches '.' as anything including newline, instead of everything except newline
# with match and search, access the object's results with group(0)

#=============
# using inline queries
#=============

# .match() returns the FIRST hit at the BEGINNING of a checked object, returns ONE item, uses .group(0)
print(re.match('Lorem|in[^\s]*|x[a-z]{6}', stringy, re.MULTILINE|re.DOTALL).group(0))

#.search() returns the FIRST hit ANYWHERE in a checked object, returns ONE item, uses .group(0)
print(re.search('Lorem|in[^\s]*|x[a-z]{6}', stringy, re.MULTILINE|re.DOTALL).group(0))

#.findall() returns ALL matches in a list structure, do not use .group(0)
print(re.findall('Lorem|in[^\s]*|x[a-z]{6}', stringy, re.MULTILINE|re.DOTALL))

print("+"*42)

#=============
# using compiled objects
#=============

# Python can pre-compile regex objects to use for comparison, which is more far efficient for large and/or repetitive tasks
compy = re.compile('Lorem|in[^\s]*|x[a-z]{6}', re.MULTILINE|re.DOTALL)

# .match() returns the FIRST hit at the BEGINNING of a checked object, returns ONE item, uses .group(0)
m = compy.match(stringy)
if m:
	print(m.group(0)) # if the matched object was not at the VERY BEGINNING of the object being checked, this would NOT print

#.search() returns the FIRST hit ANYWHERE in a checked object, returns ONE item, uses .group(0)
s = compy.search(stringy)
if s:
	print(s.group(0))

#.findall() returns ALL matches in a list structure, do not use .group(0)
f = compy.findall(stringy)
if f:
	print(f)

print("+"*42)
