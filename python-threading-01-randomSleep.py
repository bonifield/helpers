#!/usr/bin/python3

import threading
import time
import random

def executeThread(i):
	print("Thread {} started".format(i))
	sleepTime = random.randint(1,3)
	#sleepTime = 0.01
	time.sleep(sleepTime)
	print("Thread {} finished".format(i))

for i in range(10):
	# creates a thread object which sends the looping values through the executeThread function
	thread = threading.Thread(target=executeThread, args=(i,))
	# start a new thread on every loop
	thread.start()
	# view a list of threads currently being processed
	print("\tActive Threads:", len(threading.enumerate()))
