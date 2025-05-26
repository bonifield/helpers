#!/usr/bin/env python3


import argparse


def main(simple: False, fn: str, ln: str, age: int, col: str) -> str:
	if simple:
		print(f"{fn.title()} {ln.title()} {age} {col}")
	else:
		print(f"Name: {fn.title()} {ln.title()}\nAge: {age}\nFavorite Color: {col}")


if __name__ == "__main__":
	# instantiate parser
	parser = argparse.ArgumentParser(description="argparse makes it easy to assign variables via command line arguments")

	# optional switches
	# short arg, long arg, variable name to be used (accessed as dict), a default value (optional), variable type, help message when using -h
	parser.add_argument("-f", "--firstname", dest="fn", default="defaultfn", type=str, help="your first name as a string")
	parser.add_argument("-l", "--lastname", dest="ln", default="defaultln", type=str, help="your last name as a string")
	parser.add_argument("-a", "--age", dest="age", default=999, type=int, help="your age as an int")
	# single-switch / no arg booleans (do not specify type=boolean with these)
	# store_true implies false (becomes true when specified on the command line); store_false implies true
	parser.add_argument("--simple", dest="simple", action="store_true", help="simplified output")

	# mandatory switches
	# make a new argument group then set it to required
	req = parser.add_argument_group("required arguments")
	req.add_argument("-c", "--color", dest="col", type=str, help="your favorite color", required=True)

	# treat parser as dictionary
	opts = parser.parse_args()

	# instead of creating variables from args objects, just pass the iterable to main()
	main(**opts.__dict__)
	#print(opts)
	#print(opts.__dict__)
	'''
	# create variables from the args object
	args = vars(parser.parse_args())
	fn = args["fn"].title()
	ln = args["ln"].title()
	age = args["age"]
	col = args["col"]
	simple = args["simple"]
	'''


'''
$ python3 python-argparse-2.py -f bob -l smith -a 50 -c red
Name: Bob Smith
Age: 50
Favorite Color: red

$ python3 python-argparse-2.py -f bob -l smith -a 50 -c red --simple
Bob Smith 50 red
'''
