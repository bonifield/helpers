#!/usr/bin/python

##############
#
# Python 2.7.x
# sets up a parent class and child class that inherits from the parent
# defines variables the reference the classes
# prints or calls methods from the classes
#
##############

##############
# Parent Class
##############

class Human(object):
	""" simple class tester """
	def __init__(self, name, age, power):
		""" initialize variables and attributes """
		self.name = name
		self.age = age
		self.power = power
	
	def printName(self):
		return self.name
	
	def nameAge(self):
		print '%s is %d years old and has %s powers.' % (self.name, self.age, self.power)
		
	def updatePowers(self, pow):
		""" creates an attribute that can be updated """
		self.power = pow
		print '%s actually has the power of %s!' % (self.name, self.power)
		
##############
# Child Class
##############

class Superhuman(Human):
	def __init__(self, name, age, power):
		""" initializes child class inheriting from the parent class """
		# use super to link the child class and self to the parent class
		super(Superhuman, self).__init__(name, age, power)
		# initialize a variable unique to the child class
		self.powerLevel = 9001
		
	def wowPowerLevel(self):
		""" define a child class method """
		print '%s has a power level of %d!' % (self.name, self.powerLevel)
		
##############
# Parent Class Examples
##############

# create a variable to reference the parent class
clark = Human('Clark Kent', 29, 'zero')

# print Clark's name using a method in the parent class that gets returned
print clark.printName()

# display Clark's name, age, and powers using a method in the parent class that gets printed
clark.nameAge()

# give Clark a superpower by updating his power by using a method in the parent class
clark.updatePowers('flight')

##############
# Child Class Examples
##############

# create a variable to reference the child class
superman = Superhuman('Superman', 29, 'flight')

# print Clark's name using a method in the parent class that gets returned
print superman.printName()

# display Superman's name, age, and powers using a method in the parent class that gets printed
superman.nameAge()

# print Superman's power level using a method in the child class
superman.wowPowerLevel()

##############
# Results
##############
#
# Clark Kent
# Clark Kent is 29 years old and has zero powers.
# Clark Kent actually has the power of flight!
# Superman
# Superman is 29 years old and has flight powers.
# Superman has a power level of 9001!
