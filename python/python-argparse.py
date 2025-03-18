#!/usr/bin/env python3

import argparse

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
args = vars(parser.parse_args())

# create variables from the args object
fn = args["fn"].title()
ln = args["ln"].title()
age = args["age"]
col = args["col"]
simple = args["simple"]

if simple:
	print(f"{fn} {ln} {age} {col}")
else:
	print(f"Name: {fn} {ln}\nAge: {age}\nFavorite Color: {col}")
