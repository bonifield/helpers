#!/usr/bin/env python3

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

	def name_age(self):
		print(f"{self.name} is {self.age} years old and has {self.power} powers.")

	def update_powers(self, pow):
		""" creates an attribute that can be updated """
		self.power = pow
		print(f"{self.name} has the power of {self.power}.")

	def add_powers(self, pow):
		""" creates an attribute that can be updated """
		self.power = self.power + " and " + pow
		print(f"{self.name} has the power of {self.power}.")

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

	def wow_power_level(self):
		""" define a child class method """
		print(f"{self.name} has a power level of {self.powerLevel}!")

#=============
# Parent Class Examples
#=============

# create a variable to reference the parent class
clark = Human('Clark Kent', 29, 'zero')

# display Clark's name, age, and powers using a method in the parent class
clark.name_age()

# give Clark a superpower by updating his powers using a method in the parent class
clark.update_powers('flight')

#=============
# Child Class Examples
#=============

# create a variable to reference the child class
superman = Superhuman('Superman', 29, 'flight')

# display Superman's name, age, and powers using a method in the parent class
superman.name_age()

# give Superman another superpower by updating his powers using a method in the parent class
superman.add_powers('heat vision')

# print Superman's power level using a method in the child class
superman.wow_power_level()

#=============
# Results
#=============
#
# Clark Kent is 29 years old and has zero powers.
# Clark Kent has the power of flight.
# Superman is 29 years old and has flight powers.
# Superman has the power of flight and heat vision.
# Superman has a power level of 9001!
