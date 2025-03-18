#!/usr/bin/python3

import threading
import queue
import time

# each thread calls this function to consume queued items, if available
def consumeQueueItems(queue):
	while not queue.empty():
		item = queue.get()
		if item is None:
			break
		print("{} removed {} from the queue".format(threading.current_thread().name, item))
		time.sleep(0.1)
		# tell the queue the current task is done, so .join() knows the work is done
		queue.task_done()

# create a Last-In-First-Out (LIFO) queue object and fill it with 10 items to process
myQueue = queue.LifoQueue()
for i in range(20):
	myQueue.put(i)

# start 4 worker threads that will process items in the queue
threads = []
for i in range(4):
	thread = threading.Thread(target=consumeQueueItems, args=(myQueue,))
	print("starting thread", i)
	thread.start()
	threads.append(thread)

# ensure all threads have finished
for thread in threads:
	thread.join()
