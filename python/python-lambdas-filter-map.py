#!/usr/bin/python3

m = 1
n = 2

# this function just adds a number to itself; because it's a named def-function, it can be called multiple times
def exampleAdd(x):
	return(x+x)

# this lambda also adds a number to itself; "x" (left of the colon) is the function's input, "x+x" is the function body, "n" is the provided argument
# lambdas are one-shot only; use a named def-function if repeat use is needed
lam1 = (lambda x: x+x)(n)

# this lambda takes "x,y" as inputs, "x+y" is the function body, and "m,n" are the variables provided as input
lam2 = (lambda x,y: x+y)(m,n)

print("lambda with one argument added to itself (2+2)")
print(lam1) # 4
print("lambda with two arguments added to each other (1+2):")
print(lam2) # 3
print()

# this is a base list we will work with
l = [1,2,3,4,5,6,7,8,9,10]
print("base list:")
print(l)
print()

# filter returns an object containing only specified criteria from the provided interable; filter(lambdafunction, iterable)
# this looks for only even numbers via modulo
f = filter(lambda x: x%2==0, l)
print("filter for only even numbers:")
print(list(f)) # the filter object is an iterable, so cast as a list
print()

# map returns an altered instance of the original iterable, where modifications are made according to specified criteria; map(lambdafunction, iterable)
# this adds 10 to every number in the list
p = map(lambda x: x+10, l)
print("map to add 10 to every number:")
print(list(p)) # the map object is an iterable, so cast as a list
print()

# lambdas only support if/else, so nest additional if/else statements inside the else block to acts as "elif"
# this returns members as "even" or "odd" (or "uhoh" for example only)
ff = map(lambda x: "even" if x%2==0 else ("odd" if x%2!=0 else "uhoh"), l)
print("map to display even or odd:")
print(list(ff)) # the map object is an iterable, so cast as a list
print()
