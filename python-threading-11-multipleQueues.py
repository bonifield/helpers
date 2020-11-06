#!/usr/bin/python3


import threading
import queue
import time


# time script execution
startTime = time.time()


# this object fills queue1
class Filler(threading.Thread):
	def __init__(self, queue1, num):
		threading.Thread.__init__(self)
		self.queue1 = queue1
		self.num = num

	def run(self):
		for i in range(self.num):
			# fill queue with numbers starting at 1, instead of 0
			self.queue1.put(i+1)
			print("Filler placed {} into queue1".format(str(i)))


# this object reads data from queue1, manipulates it, and puts it in queue2
class Shuffler(threading.Thread):
	def __init__(self, queue1, queue2):
		threading.Thread.__init__(self)
		self.queue1 = queue1
		self.queue2 = queue2

	def run(self):
		while True:
			# get item to work on from first queue
			item = self.queue1.get()
			# process that item
			result = self.process(item)
			# put the result in the second queue
			self.queue2.put(result)
			print("Shuffler got {} from queue1 and placed {} into queue2".format(str(item), str(result)))
			# tell queue1 the task is finished (for the queue.join() at the end)
			self.queue1.task_done()

	# map numbers to letters to see what is happening easier
	def process(self, item):
		l = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
		if item >= 1 and item <= 26:
			return l[item]
		else:
			return item**2


# this object drains queue2
class Drainer(threading.Thread):
	def __init__(self, queue2):
		threading.Thread.__init__(self)
		self.queue2 = queue2

	def run(self):
		while True:
			item = self.queue2.get()
			if item is None:
				break
			print("Drainer removed {} from queue2".format(str(item)))
			# tell queue2 the task is finished (for the queue.join() at the end)
			self.queue2.task_done()


# this queue gets filled with numbers
queue1 = queue.Queue()
# this queue gets filled with the calculated numbers
queue2 = queue.Queue()


# daemonize the threads so they run in the background
# thread to fill queue1
f = Filler(queue1, 10)
f.setDaemon(True)
f.start()
# thread to shuffle from queue1 to queue2
s = Shuffler(queue1, queue2)
s.setDaemon(True)
s.start()
# thread to drain queue2
d = Drainer(queue2)
d.setDaemon(True)
d.start()


# ensure the daemon threads have finished by checking that the queues are empty
queue1.join()
print("queue1 is empty")
queue2.join()
print("queue2 is empty")


# time script execution
endTime = time.time()
totalTime = endTime - startTime
print("took {} seconds".format(totalTime))
