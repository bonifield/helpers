#!/usr/bin/python3


#
# Note using queues to shuffle lines between files is VERY slow.
#
# This is just an example of how to use a queue to handle multiple threads that
# need to write into the same output file, via dedicated writer thread.
#


import hashlib, queue, sys, threading, time


try:
	inputFile = sys.argv[1]
	outputFile = inputFile + ".processed"
except Exception as e:
	print("Usage: script.py inputFile")
	sys.exit(1)


# this object, once spawned in its own thread, will read lines from an input file and push them into a queue
class ReadInputFile(threading.Thread):
	def __init__(self, queue, inputFile):
		threading.Thread.__init__(self)
		self.queue = queue
		self.inputFile = inputFile

	def run(self):
		with open(self.inputFile) as inFile:
			while True:
				for line in inFile:
					self.queue.put(line)
		inFile.close()


# this object, once spawned in its own thread, will read lines from the queue and write to an output file
class WriteOutputFile(threading.Thread):
	def __init__(self, queue, outputFile):
		threading.Thread.__init__(self)
		self.queue = queue
		self.outputFile = outputFile

	def run(self):
		# https://docs.python.org/3/library/queue.html#queue.Queue.get
		# https://stackoverflow.com/questions/38545832/python-multithreading-queues-not-running-or-exiting-cleanly
		with open(self.outputFile, "w") as outFile:
			c = 0
			try:
				while True:
					#item = self.queue.get()
					# consume items without blocking queue until a new item is available
					item = self.queue.get_nowait()
					c += 1
					if item is None:
						break
					i = self.processLine(item)
					outFile.write(i)
					# for troubleshooting purposes
					#if c >= 1999960:
					#	print(c, item, i)
					self.queue.task_done()
			except self.queue.Empty:
				pass
		outFile.close()

	def processLine(self, line):
		h = hashlib.md5(line.encode('utf-8')).hexdigest() + "\n"
		return h


if __name__ == '__main__':
	starttime = time.time()
	qq = queue.Queue()
	# spawn input thread
	i = ReadInputFile(qq, inputFile)
	i.setDaemon(True)
	i.start()
	# spawn output thread
	o = WriteOutputFile(qq, outputFile)
	o.setDaemon(True)
	o.start()
	qq.join()
	print("queue is empty, made {}".format(outputFile))
	endtime = time.time()
	fintime = str(int(endtime-starttime))
	print("script finished in {} seconds".format(fintime))
