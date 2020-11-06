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
		print("{} removed {} from the queue, current size is {}".format(threading.current_thread().name, item, queue.qsize()))
		time.sleep(0.1)
		# tell the queue the current task is done, so .join() knows the work is done
		queue.task_done()

# create a queue object and fill it with 10 items
myQueue = queue.Queue()
for i in range(10):
	myQueue.put(i)

# start a worker threads that will process items in the queue
thread = threading.Thread(target=consumeQueueItems, args=(myQueue,))
# daemonize the thread, which only completes if the main thread is still active (or locked)
#thread.daemon = True
thread.start()

# ensure the thread has finished by checking that the queue is empty
print("script will not finish until the queue is empty")
myQueue.join()
print("queue is empty")
