#!/usr/bin/env python3


# see also: Pydantic dataclass and TypeAdapter to enforce typing via ValidationError


from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict, field, FrozenInstanceError
from random import randint
from typing import Optional


# enforces methods in all child classes
# attempting to create a child class without a method will throw a TypeError exception
class Person(ABC):
	"""Abstract Base Class parent class.
	Children must implement the full_name(self) and hex_age(self) methods.
	"""
	# optional attribute typing
	first_name: str
	age: int
	last_name: Optional[str] = None

	@abstractmethod
	def full_name(self) -> str:
		"""Returns the object's full name attribute as a formatted string."""
		pass

	@abstractmethod
	def hex_age(self) -> str:
		"""Returns the object's age attribute in hex as a formatted string."""
		pass


# traditional child class
class Human_Traditional(Person):
	"""Traditional (non-dataclass) child of the Person(ABC) class.
	Implements the full_name(self) and hex_age(self) methods.
	"""
	def __init__(self, first_name, last_name=None, age=0):
		"""Initializes class attributes first_name, last_name, and age."""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		print("This is the traditional class instance running the __init__ method.")

	@property
	def full_name(self) -> str:
		"""Returns the object's full name attribute as a formatted string."""
		if self.last_name:
			return f"Hello, {self.first_name.title()} {self.last_name.title()}!"
		else:
			return f"Hello, {self.first_name.title()}!"

	# commenting this would produce the following exception:
	# TypeError: Can't instantiate abstract class Human_Traditional without
	# an implementation for abstract method 'hex_age'
	@property
	def hex_age(self) -> str:
		"""Returns the object's age attribute in hex as a formatted string."""
		h = hex(int(self.age))[2:]
		return f"Your age ({self.age}) in hex is {h}."


# dataclasses don't need __init__,
# can return all attributes as a dict using asdict(obj),
# can use a dedicated __post_init__() method instead of calling methods in __init__()
# pydantic's dataclass can enforce typing
@dataclass
class Human_Dataclass(Person):
	"""Dataclass child of the Person(ABC) class.
	Implements the full_name(self), hex_age(self), __post_init__(self), and _increase_age(self) methods.
	"""
	first_name: str
	age: int
	last_name: Optional[str] = None
	# instantiate this optional attribute as 0
	calculated_number: Optional[int] = field(default_factory=int, init=False)
	# instantiate optional attribute this as None
	#calculated_number: Optional[int] = None

	def __post_init__(self):
		"""Runs post-initialization methods."""
		# this will work if the dataclass if frozen
		print("This is a dataclass instance running the __post_init__ method.")
		try:
			# this won't work if the dataclass is frozen
			self._increase_age()
			print(f"Increased {self.first_name.title()}'s age by 100 years!")
			# this sets an attribute not provided during instantiation
			self.calculated_number = randint(1,999999)
			print("Calculated a random number!")
		except FrozenInstanceError as err:
			print(f"Class is frozen (FrozenInstanceError), cannot increase age by 100 years nor calculate a random number.")

	# this could also use a setter pattern
	def _increase_age(self) -> None:
		"""Increments the object's age attribute by 100."""
		self.age = int(self.age) + 100

	@property
	def full_name(self) -> str:
		"""Returns the object's full name attribute as a formatted string."""
		if self.last_name:
			return f"Hello, {self.first_name.title()} {self.last_name.title()}!"
		else:
			return f"Hello, {self.first_name.title()}!"

	@property
	def hex_age(self) -> str:
		"""Returns the object's age attribute in hex as a formatted string."""
		h = hex(int(self.age))[2:]
		return f"Your age ({self.age}) in hex is {h}."


# frozen makes the class immutable
# operations that change attributes won't run and will return FrozenInstanceError
# you cannot create a frozen dataclass from a non-frozen one
@dataclass(frozen=True)
class Human_Dataclass_Frozen(Person):
	"""Frozen Dataclass child of the Person(ABC) class.
	Implements the full_name(self), hex_age(self), __post_init__(self), and _increase_age(self) methods.
	"""
	first_name: str
	age: int
	last_name: Optional[str] = None
	# a frozen class will instantiate this optional attribute as 0
	calculated_number: Optional[int] = field(default_factory=int, init=False)
	# a frozen class will instantiate this optional attribute as None
	#calculated_number: Optional[int] = None

	def __post_init__(self):
		"""Runs post-initialization methods."""
		# this will work if the dataclass if frozen
		print("This is the frozen dataclass instance running the __post_init__ method.")
		try:
			# this won't work if the dataclass is frozen
			self._increase_age()
			print(f"Increased {self.first_name.title()}'s age by 100 years!")
			# this sets an attribute not provided during instantiation
			self.calculated_number = randint(1,999999)
			print("Calculated a random number!")
		except FrozenInstanceError as err:
			print(f"Class is frozen (FrozenInstanceError), cannot increase age by 100 years nor calculate a random number.")

	# this could also use a setter pattern
	def _increase_age(self) -> None:
		"""Increments the object's age attribute by 100."""
		self.age = int(self.age) + 100

	@property
	def full_name(self) -> str:
		"""Returns the object's full name attribute as a formatted string."""
		if self.last_name:
			return f"Hello, {self.first_name.title()} {self.last_name.title()}!"
		else:
			return f"Hello, {self.first_name.title()}!"

	@property
	def hex_age(self) -> str:
		"""Returns the object's age attribute in hex as a formatted string."""
		h = hex(int(self.age))[2:]
		return f"Your age ({self.age}) in hex is {h}."


if __name__ == "__main__":
	
	print("\n"+" Traditional Class ".center(50, "*"))
	# traditional instance
	bob = Human_Traditional(first_name="bob", last_name="smith", age=40)
	print(bob.full_name)
	print(bob.hex_age)
	# can't use asdict() on non-dataclasses
	try:
		print(type(asdict(bob)), asdict(bob))
	except TypeError as e:
		print(str(e))
	
	print("\n"+" Dataclass (mutable) ".center(50, "*"))
		# dataclass instance
	alice = Human_Dataclass(first_name="alice", last_name="allison", age=40)
	print(alice.full_name)
	print(alice.hex_age)
	print(type(asdict(alice)), asdict(alice))
	
	print("\n"+" Frozen Dataclass (immutable) ".center(50, "*"))
	# frozen dataclass instance without last_name
	# age will be unaffected by __post_init__, and calculated_number will be 0
	john = Human_Dataclass_Frozen(first_name="john", last_name="smith", age=40)
	print(john.full_name)
	print(john.hex_age)
	print(type(asdict(john)), asdict(john))

	print()


# expected output
'''

*************** Traditional Class ****************
This is the traditional class instance running the __init__ method.
Hello, Bob Smith!
Your age (40) in hex is 28.
asdict() should be called on dataclass instances

************** Dataclass (mutable) ***************
This is a dataclass instance running the __post_init__ method.
Increased Alice's age by 100 years!
Calculated a random number!
Hello, Alice Allison!
Your age (140) in hex is 8c.
<class 'dict'> {'first_name': 'alice', 'age': 140, 'last_name': 'allison', 'calculated_number': 927870}

********** Frozen Dataclass (immutable) **********
This is the frozen dataclass instance running the __post_init__ method.
Class is frozen (FrozenInstanceError), cannot increase age by 100 years nor calculate a random number.
Hello, John Smith!
Your age (40) in hex is 28.
<class 'dict'> {'first_name': 'john', 'age': 40, 'last_name': 'smith', 'calculated_number': 0}

'''
