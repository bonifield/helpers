#!/usr/bin/python3

#=============
# python-class-py3.py
#=============

#------

class Parent():
	def __init__(self, stringy=None, inty=None, numby=None):
		''' initialize attributes and values '''
		self.stringy = stringy
		self.inty = inty
		self.numby = 123

	def add_num(self, num):
		''' directly modify an attribute value '''
		self.inty += num

	def change_num(self, num):
		''' directly modify an attribute value '''
		self.inty = num
	
	def printy(self):
		print(str("{} {}".format(self.stringy, self.inty)))

	def __repr__(self):
		''' default return statement '''
		return str("{} {}".format(self.stringy, self.inty))

#------

# naming variables works too
# p = Parent(inty=4444, stringy="SomeString")

p = Parent("SomeString", 4444)
print(p) # based on the default __repr__ action
p.printy()
# both return SomeString 4444

p.add_num(25)
p.printy()
# SomeString 4469

p.change_num(50)
p.printy()
# SomeString 50

print(p.stringy)
# SomeString

#------

class Child(Parent):
	def __init__(self, stringy=None, inty=None, numby=None):
		''' initialize attributes and values of parent class '''
		super().__init__(stringy, inty, numby)
		self.smallnum = 3
	
	def change_num(self, num):
		''' directly override parent method '''
		self.inty = num
	
	def mod_string(self):
		''' modify the string '''
		#return self.stringy.title()
		return str('{} {} {}'.format(self.stringy.title(), self.stringy.upper(), self.stringy.lower()))
	
	def append_data(self, s):
		''' adds data to the string '''
		self.stringy = self.stringy+str(s)

#------

c = Child("AnotherString", 8888)
print(c)
c.printy()
# both return AnotherString 8888, since Child inherits from Parent

print(c.stringy)
# AnotherString

print(c.numby)
# 123, which was set in the parent class

print(c.smallnum)
# 3

c.change_num(25)
c.printy()
# AnotherString 25

print(c.inty)
# 25
print(p.inty)
# 50
# child overrides parent in it's instance

print(c.mod_string())
# Anotherstring ANOTHERSTRING anotherstring

c.append_data("abcd1234")
print(c.mod_string())
# Anotherstringabcd1234 ANOTHERSTRINGABCD1234 anotherstringabcd1234

print(c.mod_string.__doc__)
# prints the docstring (triple-quoted help message)

print(dir(c))
# prints list of attributes and methods for any object
