#!/usr/bin/python3

# usage:
#	thread-dispatcher.py && tail -n 1 ~/test-tool-output.txt
#
# purpose:
#	use a reliable parent thread to start a long-running OS command daemon thread, to ensure the OS command executes successfully
#

import os, shutil, threading
from random import randint
import subprocess

#------
uploadPath = os.getenv("HOME")
outputFilename = "TEST-TOOL-OUTPUT.txt"
outputCombined = os.path.join(uploadPath, outputFilename)
#
outputFilenameLower = outputFilename.lower()
#------

def printGreen(s):
	''' prints a green string to the terminal '''
	print('\033[92m'+s+'\033[0m')

def printPurple(s):
	''' prints a purple string to the terminal '''
	print('\033[95m'+s+'\033[0m')

def executeSubDaemonThread(cmd):
	''' performs an OS-related task in the background, allowing the main process to continue unhindered by run time '''
	printGreen("subdaemon thread started")
	subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate() # run an OS command
	shutil.move(outputCombined, outputFilenameLower) # perform an additional move operation; can also use os.rename(old, new) or os.replace(old, new)
	#subprocess.Popen("sleep 1", shell=True, stdout=subprocess.PIPE).communicate()
	printGreen("subdaemon thread finished")

def executeParentThread(cmd):
	''' starts a daemon thread which runs independent of this thread, so the calling function prepareThread() can return instantly  '''
	printPurple("parent thread started")
	thread = threading.Thread(target=executeSubDaemonThread, args=(cmd,))
	thread.Daemon = True
	thread.start() # do not join a daemon thread
	printPurple("parent thread finished")

def prepareThread(i, o):
	''' sets up a parent thread, which subsequently starts a daemon thread, so that the function calling prepareThread() can return instantly and the daemon can run in the background until completion '''
	print("expect {}".format(i))
	s = 'echo "{}" >> {}'.format(i, o)
	thread = threading.Thread(target=executeParentThread, args=(s,))
	thread.start()
	thread.join()

if __name__ == "__main__":
	i = str(randint(1,100))
	prepareThread(i, outputCombined)
