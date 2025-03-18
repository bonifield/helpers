#!/usr/bin/python3

import threading
import time
import random

def executeThread(i):
	print("Thread {} started".format(i))
	sleepTime = random.randint(1,3)
#	sleepTime = 0.01
	time.sleep(sleepTime)
	print("Thread {} finished".format(i))

for i in range(10):
	# creates a thread object which sends the looping values through the executeThread function
	thread = threading.Thread(target=executeThread, args=(i,))
	# daemonize the thread, which terminates threads when the main thread ends
	# if False (default) script will hang until all threads are finished
	thread.daemon = True
	# start a new thread on every loop
	thread.start()
	# view a list of threads currently being processed
	print("\tActive Threads:", len(threading.enumerate()))
