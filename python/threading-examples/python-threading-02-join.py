#!/usr/bin/python3

import threading
import time
import random

def executeThread(i):
	print("Thread {} started".format(i))
	sleepTime = random.randint(1,3)
	time.sleep(sleepTime)
	print("Thread {} finished".format(i))

thread1 = threading.Thread(target=executeThread, args=(1,))
thread1.start()
print("this will likely print before thread1 exits")

# join locks the main process until the thread is finished
thread2 = threading.Thread(target=executeThread, args=(2,))
thread2.start()
thread2.join()
print("this definitely prints after thread2 exits")
