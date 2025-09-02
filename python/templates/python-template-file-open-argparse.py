#!/usr/bin/env python3


import argparse
import json
import time


def get_arguments():
	"""Retrieves argparse values."""
	# instantiate parser
	parser = argparse.ArgumentParser(description="script description")

	# optional switches
	parser.add_argument("-i", "--infile", dest="input_filename", default="test_in.txt", type=str, help="input filename")
	parser.add_argument("-o", "--outfile", dest="output_filename", default="test_out.txt", type=str, help="output filename")
	parser.add_argument("-a", "--number", dest="number", default=999, type=int, help="some number value")
	parser.add_argument("--simple", dest="simple", action="store_true", help="some boolean value that is False unless specified, then it becomes True")

	# mandatory switches - make a new argument group then make its arguments required
	#req = parser.add_argument_group("required arguments")
	#req.add_argument("-m", "--mandatory", dest="mand", type=str, help="some mandatory argument", required=True)

	return parser.parse_args()


def process_input_file(i):
	"""Load the input file's contents."""
	with open(i, "r") as in_file:
		pass
		#j = json.load(in_file)
		# or
		#for line in in_file:
			#l = json.loads(line)


def main():
	"""Main execution comments go here."""
	pass


if __name__ == '__main__':
	start = time.time()
	# get arguments
	args = get_arguments()
	main()
	end = time.time()
	print(f"script finished in {end - start} seconds")

