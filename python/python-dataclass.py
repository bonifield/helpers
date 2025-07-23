#!/usr/bin/env python3


from dataclasses import dataclass, field, fields
#from typing import List


# mutable dataclass
#@dataclass
# immutable dataclass
@dataclass(frozen=True)
class Human:
	# parameters WITHOUT default arguments must go BEFORE those with defaults
	first_name: str
	# parameters WITH default arguments must go AFTER those without defaults
	# use field() to store the default argument safely, and metadata accessible with fields(obj)
	# absurd defaults make it easier to identify where users didn't input data
	age: int = field(default=999, metadata={"unit": "years"})

	# implement string representation (not __repr__) for printing
	def __str__(self):
		return f"First Name: {self.first_name.title()}, Age: {self.age}"


# hello bob
bob = Human(first_name="bob")
print(bob)
print()
# tuple of Field objects describing the contents of the dataclass
print(fields(bob))
print()
# access metadata values set for the age parameter
print(fields(bob)[1].metadata)
print()
# attempting to change the frozen dataclass triggers dataclasses.FrozenInstanceError
# omitting frozen=True in the @dataclass decorator will let you change it like any other class
bob.first_name = "Sentry"


'''
First Name: Bob, Age: 999

(Field(name='first_name',type=<class 'str'>,default=<dataclasses._MISSING_TYPE object at 0x7b4dd29d38b0>,default_factory=<dataclasses._MISSING_TYPE object at 0x7b4dd29d38b0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), Field(name='age',type=<class 'int'>,default=999,default_factory=<dataclasses._MISSING_TYPE object at 0x7b4dd29d38b0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({'unit': 'years'}),kw_only=False,_field_type=_FIELD))

{'unit': 'years'}

Traceback (most recent call last):
  File "python-dataclass.py", line 33, in <module>
    bob.first_name = "Sentry"
  File "<string>", line 4, in __setattr__
dataclasses.FrozenInstanceError: cannot assign to field 'first_name'
'''
