#!/usr/bin/python3

import argparse
#import json
import time

# instantiate parser
parser = argparse.ArgumentParser(description="script description")

# optional switches
# short arg, long arg, variable name to be used (accessed as dict), a default value (optional), variable type, help message when using -h
parser.add_argument("-f", "--file", dest="file", default="test_file.txt", type=str, help="input file")
parser.add_argument("-i", "--input", dest="input", default="test_in.txt", type=str, help="input filename")
parser.add_argument("-o", "--output", dest="output", default="test_out.txt", type=str, help="output filename")
parser.add_argument("-u", "--url", dest="url", default="google.com", type=str, help="target url")
#parser.add_argument("-a", "--number", dest="number", default=999, type=int, help="some int")
# single-switch / no arg booleans (do not specify type=boolean with these)
# store_true implies false (becomes true when specified on the command line); store_false implies true
#parser.add_argument("--simple", dest="simple", action="store_true", help="some boolean")

# mandatory switches
# make a new argument group then set it to required
#req = parser.add_argument_group("required arguments")
#req.add_argument("-m", "--mandatory", dest="mand", type=str, help="some mandatory argument", required=True)

# treat parser as dictionary
args = vars(parser.parse_args())

# create variables from the args object
input_file_single = args["file"]
input_file = args["input"]
output_file = args["output"]
url = args["url"]


def process_input_file(i):
	""" comment """
	with open(i, "r") as in_file:
		pass
		#j = json.load(in_file) # j is now dict of the file content
		#pass
		#for line in in_file:
			#l = json.loads(line) # l is now a dict
			#pass
	in_file.close()


if __name__ == '__main__':
	starttime = time.time()
	process_input_file(input_file)
	endtime = time.time()
	fintime = str(int(endtime-starttime))
	print(f"script finished in {fintime} seconds")
