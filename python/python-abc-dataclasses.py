#!/usr/bin/env python3


from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict, FrozenInstanceError


# You can also enforce typing with Pydantic's dataclass, which will return
# a ValidationError exception when an attribute isn't properly typed. Still
# import asdict() from dataclasses, or use Pydantic's TypeAdapter to convert
# a dataclass to dict or JSON.
#######
# from dataclasses import asdict
# from pydantic.dataclasses import dataclass


# enforce methods in all child classes
# attempting to create a child class without a method will throw a TypeError exception
class Person(ABC):
	@abstractmethod
	def full_name(self):
		pass

	@abstractmethod
	def hex_age(self):
		pass


# traditional child class
class Human_Traditional(Person):
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		print("This is a traditional class instance.")

	@property
	def full_name(self) -> str:
		return f"Hello, {self.first_name.title()} {self.last_name.title()}!"

	# commenting this would produce the following exception:
	# TypeError: Can't instantiate abstract class Human_Traditional without
	# an implementation for abstract method 'hex_age'
	@property
	def hex_age(self) -> str:
		h = hex(int(self.age))[2:]
		return f"Your age ({self.age}) in hex is {h}."


# dataclasses don't need __init__,
# can return all attributes as a dict using asdict(obj),
# can use a dedicated __post_init__() method instead of calling methods in __init__()
# pydantic's dataclass can enforce typing
#
# frozen makes the class immutable
#@dataclass(frozen=True)
@dataclass
class Human_Dataclass(Person):
	first_name: str
	last_name: str
	age: int

	def __post_init__(self):
		# this will work if the dataclass if frozen
		print("This is a dataclass instance.")
		try:
			# this won't work if the dataclass is frozen
			self._increase_age()
			print(f"Increased {self.first_name.title()}'s age by 100 years!")
		except FrozenInstanceError as err:
			print(f"Class is frozen (FrozenInstanceError), cannot increase age by 100 years.")

	# this could also use a setter pattern
	def _increase_age(self) -> None:
		self.age = int(self.age) + 100

	@property
	def full_name(self) -> str:
		return f"Hello, {self.first_name.title()} {self.last_name.title()}!"

	@property
	def hex_age(self) -> str:
		h = hex(int(self.age))[2:]
		return f"Your age ({self.age}) in hex is {h}."


# traditional instance
bob = Human_Traditional("bob", "smith", 40)
print(bob.full_name)
print(bob.hex_age)

print()

# dataclass instance
alice = Human_Dataclass("alice", "allison", 40)
print(alice.full_name)
print(alice.hex_age)
print(type(asdict(alice)), asdict(alice))


# expected output
'''
This is a traditional class instance.
Hello, Bob Smith!
Your age (40) in hex is 28.

This is a dataclass instance.
Increased Alice's age by 100 years!
Hello, Alice Allison!
Your age (140) in hex is 8c.
<class 'dict'> {'first_name': 'alice', 'last_name': 'allison', 'age': 140}
'''
