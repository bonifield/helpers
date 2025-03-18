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

# create a Priority queue object and fill it twice with tuples items to process, where 0 is highest priority
myQueue = queue.PriorityQueue()
for i in range(5):
	myQueue.put(i, i)
# a second batch will be appended to the queue, but it will not matter since the queue is prioritized
for i in range(5):
	myQueue.put(i, i)

# start 2 worker threads that will process items in the queue
threads = []
for i in range(2):
	thread = threading.Thread(target=consumeQueueItems, args=(myQueue,))
	print("starting thread", i)
	thread.start()
	threads.append(thread)

# ensure all threads have finished
for thread in threads:
	thread.join()
