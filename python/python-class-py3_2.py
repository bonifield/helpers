#!/usr/bin/python3

#=============
#
# sets up a parent class and child class that inherits from the parent
# defines variables the reference the classes
# prints or calls methods from the classes
#
#=============

#=============
# Parent Class
#=============

class Human:
	""" simple class tester """
	def __init__(self, name, age, power):
		""" initialize variables and attributes, which will later be passed to the child class via inheritance """
		self.name = name
		self.age = age
		self.power = power
	
	def nameAge(self):
		print('%s is %d years old and has %s powers.' % (self.name, self.age, self.power))
		
	def updatePowers(self, pow):
		""" creates an attribute that can be updated """
		self.power = pow
		print('%s has the power of %s.' % (self.name, self.power))
		
	def addPowers(self, pow):
		""" creates an attribute that can be updated """
		self.power = self.power + " and " + pow
		print('%s has the power of %s.' % (self.name, self.power))
		
#=============
# Child Class
#=============

class Superhuman(Human):
	def __init__(self, name, age, power):
		""" initializes child class inheriting from the parent class """
		# use super(parent) to inherit from the parent class
		super(Superhuman, self).__init__(name, age, power)
		# initialize a variable unique to the child class
		self.powerLevel = 9001

	def wowPowerLevel(self):
		""" define a child class method """
		print('%s has a power level of %d!' % (self.name, self.powerLevel))
		
#=============
# Parent Class Examples
#=============

# create a variable to reference the parent class
clark = Human('Clark Kent', 29, 'zero')

# display Clark's name, age, and powers using a method in the parent class
clark.nameAge()

# give Clark a superpower by updating his powers using a method in the parent class
clark.updatePowers('flight')

#=============
# Child Class Examples
#=============

# create a variable to reference the child class
superman = Superhuman('Superman', 29, 'flight')

# display Superman's name, age, and powers using a method in the parent class
superman.nameAge()

# give Superman another superpower by updating his powers using a method in the parent class
superman.addPowers('heat vision')

# print Superman's power level using a method in the child class
superman.wowPowerLevel()

#=============
# Results
#=============
#
# Clark Kent is 29 years old and has zero powers.
# Clark Kent has the power of flight.
# Superman is 29 years old and has flight powers.
# Superman has the power of flight and heat vision.
# Superman has a power level of 9001!
