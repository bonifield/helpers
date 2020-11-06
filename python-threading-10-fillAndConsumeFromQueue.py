#!/usr/bin/python3

import threading
import queue
import time

# create a queue object and fill it with 10 items
myQueue = queue.Queue()
def fillQueue(q):
	for i in range(10):
		myQueue.put(i)
		print("{} added {} to the queue, current size is {}".format(threading.current_thread().name, i, myQueue.qsize()))

# each thread calls this function to consume queued items, if available
def consumeQueueItems(queue):
	while not queue.empty():
		item = queue.get()
		if item is None:
			break
		print("{} removed {} from the queue, current size is {}".format(threading.current_thread().name, item, myQueue.qsize()))
#		time.sleep(0.1)
		# tell the queue the current task is done, so .join() knows the work is done
		queue.task_done()


threadFill = threading.Thread(target=fillQueue, args=(myQueue,))
threadRead = threading.Thread(target=consumeQueueItems, args=(myQueue,))

threadFill.start()
threadRead.start()

# ensure the thread has finished by checking that the queue is empty
myQueue.join()
print("queue is empty")

