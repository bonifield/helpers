#!/usr/bin/env python3


# python3 python-argparse.py -f bob -a 42 -c blue --required -x extra1 -x extra2


import argparse
from argparse import Namespace


def get_arguments() -> Namespace:
	"""Retrieves argparse values."""
	# instantiate parser
	parser = argparse.ArgumentParser(description="argparse makes it easy to assign variables via command line arguments")
	# optional switches
	parser.add_argument("-f", "--firstname", dest="first_name", default="Bob", type=str, help="your first name as a string")
	parser.add_argument("-a", "--age", dest="age", default=999, type=int, help="your age as an int")
	parser.add_argument("-x", "--extra", dest="extra", action="append", default=[], type=str, help="creates a list of strings containing each -x argument")
	# single-switch, no default, no-arguments boolean
	parser.add_argument("--true", dest="is_true", action="store_true", help="a boolean option")
	# required in the same argument group
	parser.add_argument("--required", dest="is_required", action="store_true", help="a required boolean option", required=True)
	# or make a new argument group, then set its options to required
	req = parser.add_argument_group("required arguments")
	req.add_argument("-c", "--color", dest="color", type=str, help="your favorite color", required=True)
	return parser.parse_args()


args: Namespace = get_arguments()


print(f"{args.first_name=}")
print(f"{args.age=}")
print(f"{args.color=}")
print(f"{args.is_true=}")
print(f"{args.is_required=}")
print(f"{args.extra=}")
for item in args.extra:
	print(f"\t{type(item)=} {item=}")


# expected output
'''
$ python3 python-argparse.py -f bob -a 42 -c blue --required -x extra1 -x extra2
args.first_name='bob'
args.age=42
args.color='blue'
args.is_true=False
args.is_required=True
args.extra=['extra1', 'extra2']
	type(item)=<class 'str'> item='extra1'
	type(item)=<class 'str'> item='extra2'
'''
