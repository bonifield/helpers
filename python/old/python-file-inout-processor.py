#!/usr/bin/env python3


# reads a file, processes it, and writes the output to a new file


import hashlib
import sys
import time


try:
	inputFile = sys.argv[1]
	outputFile = inputFile + ".processed.2"
except Exception as e:
	print("Usage: script.py inputFile")
	sys.exit(1)


def process_line(line):
	""" simulates processing a line from the input file """
	h = hashlib.md5(line.encode('utf-8')).hexdigest() + "\n"
	return h


def process_file(i, o):
	""" opens the input file for reading, opens the output file for writing, and performs transform actions on each line """
	with open(i, "r") as inFile:
		with open(o, "w") as outFile:
			for line in inFile:
				p = process_line(line)
				outFile.write(p)
		outFile.close()
	inFile.close()


if __name__ == '__main__':
	start_time = time.time()
	process_file(inputFile, outputFile)
	end_time = time.time()
	fintime = str(int(end_time-start_time))
	print("script finished in {} seconds".format(fintime))
