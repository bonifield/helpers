#!/usr/bin/env python3

import json
import sys
import time


try:
	input_file = sys.argv[1]
except Exception as e:
	print(f"Usage: {sys.argv[0]} input_file")
	sys.exit(1)


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
	# get args
	args = get_arguments()
	main()
	end = time.time()
	print(f"script finished in {end - start} seconds")
