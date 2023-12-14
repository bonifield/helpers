#!/usr/bin/python3



import json
import queue
import sys
import threading
import time



class Worker(threading.Thread):
	"""simulate a web request and send the response into queueout"""
	def __init__(self, queueout):
		threading.Thread.__init__(self)
		#self.setDaemon(True) # deprecated
		self.daemon = True
		self.queueout = queueout
		self.name = threading.current_thread().name

	def processItem(self, item):
		"""process a queue item"""
		item = json.dumps(item)
		#print(f"\033[94m{self.name}\033[0m processed item: {item}") # blue
		return(item)

	def run(self):
		"""simulate receiving a large JSON response from a web request"""
		print(f"\033[94m{self.name}\033[0m sending web request") # blue
		time.sleep(2)
		print(f"\033[94m{self.name}\033[0m received web response") # blue
		item = {f"{str(self.name)}":[x for x in range(1,101)]}
		# processing actions
		result = self.processItem(item)
		# place the processed item into the output queue
		self.queueout.put(result)
		#print(f"\033[94m{self.name}\033[0m put item into queueout: {result}") # blue



class Drainer(threading.Thread):
	"""provides output management"""
	def __init__(self, queueout):
		threading.Thread.__init__(self)
		#self.setDaemon(True) # deprecated
		self.daemon = True
		self.queueout = queueout
		self.name = threading.current_thread().name

	def run(self):
		"""this emulates output handling"""
		while True:
			item = self.queueout.get()
			if item is None:
				break
			print(f"\033[33m{self.name}\033[0m removed item from queueout:\t{item}") # gold
			self.queueout.task_done()



# this is not a thread object
class ThreadHandler:
	"""main handler to dispatch threaded objects"""
	def __init__(self, threads, delay=0):
		self.threads = threads
		self.delay = delay
		self.name = threading.current_thread().name

	def run(self):
		# worker threads fill this queue with the processed results
		queueout = queue.Queue()
		# worker threads make a web request, process the results, and send results to queueout
		for i in range(self.threads):
			w = Worker(queueout)
			w.name = f"Worker-{i}"
			w.start()
		# thread to handle output
		d = Drainer(queueout)
		d.name = "Drainer"
		d.start()
		# do not join daemon threads, but do check queue sizes
		# ensure the daemon threads have finished by checking that the queues are empty
		# give time for the queue to fill, otherwise main will exit
		time.sleep(self.delay)
		queueout.join()
		print("\033[33;7mqueueout is empty\033[0m") # gold background



def tool_entrypoint():
	"""this function handles arguments (to include argparse if provided) and serves as the entry_points reference in setup.py"""
	th = ThreadHandler(threads=4, delay=3)
	th.name = "ThreadHandler"
	th.run()



#=========================================



# this allows the script to be invoked directly
if __name__ == "__main__":

	# time script execution
	startTime = time.time()

	tool_entrypoint()

	# time script execution
	endTime = time.time()
	totalTime = endTime - startTime
	sys.stderr.write(f"took {totalTime} seconds\n")
	sys.exit(0)
