#!/usr/bin/env python3


import argparse


#####################


def get_arguments():
	"""Retrieves argparse values."""
	# instantiate parser
	parser = argparse.ArgumentParser(description="argparse makes it easy to assign variables via command line arguments")
	# optional switches
	parser.add_argument("-f", "--firstname", dest="first_name", default="Bob", type=str, help="your first name as a string")
	parser.add_argument("-l", "--lastname", dest="last_name", default="Robertson", type=str, help="your last name as a string")
	parser.add_argument("-a", "--age", dest="age", default=999, type=int, help="your age as an int")
	# single-switch / no arg booleans
	parser.add_argument("--simple", dest="simple", action="store_true", help="simplified output")
	# mandatory switches
	# make a new argument group, then set its options to required
	req = parser.add_argument_group("required arguments")
	req.add_argument("-c", "--color", dest="col", type=str, help="your favorite color", required=True)
	return parser.parse_args()


def main(simple: False, first_name: str, last_name: str, age: int, col: str) -> str:
	"""Main processing."""
	if simple:
		print(f"{first_name.title()} {last_name.title()} {age} {col}")
	else:
		print(f"Name: {first_name.title()} {last_name.title()}\nAge: {age}\nFavorite Color: {col}")


#####################


if __name__ == "__main__":
	# get arguments
	args = get_arguments()
	# instead of creating variables from args objects, just pass the iterable to main()
	main(**args.__dict__)
