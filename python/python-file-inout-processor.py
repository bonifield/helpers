#!/usr/bin/python3


import hashlib, sys, time


try:
	inputFile = sys.argv[1]
	outputFile = inputFile + ".processed.2"
except Exception as e:
	print("Usage: script.py inputFile")
	sys.exit(1)


def processLine(line):
	h = hashlib.md5(line.encode('utf-8')).hexdigest() + "\n"
	return h


# opens the input file for reading, opens the output file for writing, and performs transform actions on each line
def processFile(i, o):
	with open(i, "r") as inFile:
		with open(o, "w") as outFile:
			for line in inFile:
				p = processLine(line)
				outFile.write(p)
		outFile.close()
	inFile.close()


if __name__ == '__main__':
	starttime = time.time()
	processFile(inputFile, outputFile)
	endtime = time.time()
	fintime = str(int(endtime-starttime))
	print("script finished in {} seconds".format(fintime))
