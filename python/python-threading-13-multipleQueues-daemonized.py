#!/usr/bin/python3



import queue
import sys
import threading
import time



class Filler(threading.Thread):
	"""fills a queue with words from the provided wordlist"""
	def __init__(self, queue, wordlist):
		threading.Thread.__init__(self)
		#self.setDaemon(True) # deprecated
		self.daemon = True
		self.name = threading.current_thread().name
		self.queue = queue
		self.wordlist = wordlist

	def run(self):
		for item in self.wordlist:
			item = str(item).strip()
			self.queue.put(item)
			print(f"\033[95m{self.name}\033[0m placed item into queuein: {item}") # purple



class Worker(threading.Thread):
	"""take an item from queuein, process it, and place it into queueout"""
	def __init__(self, queuein, queueout):
		threading.Thread.__init__(self)
		#self.setDaemon(True) # deprecated
		self.daemon = True
		self.queuein = queuein
		self.queueout = queueout
		self.name = threading.current_thread().name

	def processItem(self, item):
		"""process a queue item"""
		item = str(item)+"-processed"
		print(f"\033[94m{self.name}\033[0m processed item from queuein: {item}") # blue
		return(item)

	def run(self):
		"""handle processing on the current queue item"""
		while True:
			# get item to work on from first queue
			item = self.queuein.get()
			if item is None:
				break
			print(f"\033[94m{self.name}\033[0m got item from queuein: {item}") # blue
			# processing actions
			result = self.processItem(item)
			# place the processed item into the output queue
			self.queueout.put(result)
			print(f"\033[94m{self.name}\033[0m put item into queueout: {result}") # blue
			# tell queuein the task is finished (for the queue.join() at the end)
			self.queuein.task_done()



class Drainer(threading.Thread):
	"""provides output management"""
	def __init__(self, queue):
		threading.Thread.__init__(self)
		#self.setDaemon(True) # deprecated
		self.daemon = True
		self.queue = queue
		self.name = threading.current_thread().name

	def run(self):
		"""this emulates output handling"""
		while True:
			item = self.queue.get()
			if item is None:
				break
			print(f"\033[33m{self.name}\033[0m removed item from queueout:\t{item}") # gold
			self.queue.task_done()



class ThreadHandler:
	"""main handler to dispatch threaded objects"""
	def __init__(self, wordlist, threads):
		self.wordlist = wordlist
		self.threads = threads

	def run(self):
		# this queue gets filled with words from the wordlist
		queuein = queue.Queue()
		# this queue gets filled with the processed results
		queueout = queue.Queue()
		# hold thread objects here to be joined
		threads = []
		# begin loading words into queuein
		f = Filler(queuein, self.wordlist)
		f.name = "Filler"
		f.start()
		threads.append(f)
		# worker threads read from queuein, process the current item, and send results to queueout
		for i in range(self.threads):
			w = Worker(queuein, queueout)
			w.name = f"Worker-{i}"
			w.start()
			threads.append(w)
		# thread to handle output
		d = Drainer(queueout)
		d.name = "Drainer"
		d.start()
		threads.append(d)
		# do not join daemon threads, but do check queue sizes
		# ensure the daemon threads have finished by checking that the queues are empty
		queuein.join()
		print("\033[33;7mqueuein is empty\033[0m") # gold background
		queueout.join()
		print("\033[33;7mqueueout is empty\033[0m") # gold background



def tool_entrypoint():
	"""this function handles arguments (to include argparse if provided) and serves as the entry_points reference in setup.py"""
	wordlist = []
	for i in range(1, 51):
		wordlist.append(f"entry{i}")
	x = ThreadHandler(wordlist=wordlist, threads=4)
	x.run()



#=========================================



# this allows the script to be invoked directly (if the repo was cloned, if just this file was downloaded and placed in some bin path, etc)
if __name__ == "__main__":

	# time script execution
	startTime = time.time()

	tool_entrypoint()

	# time script execution
	endTime = time.time()
	totalTime = endTime - startTime
	sys.stderr.write(f"took {totalTime} seconds\n")
	sys.exit(0)
