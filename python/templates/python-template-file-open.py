#!/usr/bin/env python3

import sys
import time

try:
	input_file = sys.argv[1]
except Exception as e:
	print(f"Usage: {sys.argv[0]} input_file")
	sys.exit(1)

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
