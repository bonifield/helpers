#!/usr/bin/python3

import threading
import queue
import time

# each thread calls this function to publish to the queue
def publishQueueItems(queue):
	while not queue.full():
		queue.put(1)
		print("{} appended an item to the queue, current size is {}".format(threading.current_thread().name, queue.qsize()))
#		time.sleep(0.1)
		# tell the queue the current task is done, so .join() knows the work is done
		queue.task_done()

# create a queue with a max size of 25
myQueue = queue.Queue(maxsize=25)

# start 10 worker threads that will race to fill the queue, and will terminate when the queue is full
# the queue will likely be full by the time the threads are finished spawning, thus the unnecessary threads terminate immediately because of the "while not queue.full()" check in the above function
threads = []
for i in range(10):
	thread = threading.Thread(target=publishQueueItems, args=(myQueue,))
	print("starting thread", i)
	thread.start()
	threads.append(thread)

# ensure all threads have finished (block main thread's execution until threads have finished and queue is empty)
for thread in threads:
	thread.join()
