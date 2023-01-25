#!/usr/bin/python3

import glob
import magic # sudo pip3 install python-magic
import os
import shutil
import tempfile


def printy(m):
	print("\n\n#"+"="*42)
	print("# "+str(m))
	print("#"+"="*42+"\n\n")

#=============

ourTempDir = tempfile.mkdtemp() # create temporary folder
open(str(ourTempDir+'/myAwesomeTempFile.txt'), 'a').close() # make an empty file

#=============

printy('Temporary folder created at:')
print(ourTempDir) # access temporary folder path as a string

printy('List of items in temporary folder')
print(os.listdir(ourTempDir)) # access folder items as a list

printy('Individual items in temporary folder')
for i in os.listdir(ourTempDir): # access folder items individually
	#print(i)
	print(str(ourTempDir+'/'+i)) # access full path for each item

print('\n(now removing temporary folder and file)')
shutil.rmtree(ourTempDir) # remove temporary folder and contents

#=============

printy('Files in home directory, using os.listdir()')
hfiles = os.listdir(os.environ['HOME']) # get an environment variable if it exists
print(hfiles)

#=============

printy('Files in home directory, using OS environment variables and glob (note inclusion of the full path)')
homefiles = glob.glob(os.environ['HOME']+"/*") # get env variable and add a wildcard
print(homefiles)

#=============

printy('Magic file headers for some items in the home directory')
for h in homefiles[:10]:
	if os.path.isfile(h):
		m = magic.from_file(h)
		fs = str(os.path.getsize(h)) 
		st = os.stat(h) # stat has permissions (convert to octal), inode, uid/gid, MAC times, size, and more
#		st = os.stat(h).st_size
		oct_perms = str(oct(st.st_mode)) # note the last few bytes
		print(h+"\t"+m+"\t"+fs+"\t"+oct_perms)
#		print("\t",st)
	elif os.path.isdir(h):
		print(h+"\tdirectory")
	else:
		print(h+"\tsomething else")

#=============

# combine a path and filename safely (Windows-safe as well); alternatively, safely combine folder paths
somepath = "/home/user/folder/"
somefile = "file.txt"
outname = os.path.join(somepath, somefile)
print(outname) # /home/user/folder/file.txt

#=============

# get just the path or just the filename
fullpath = "/home/user/folder/file.txt"
justpath = os.path.dirname(fullpath)
justfilename = os.path.basename(fullpath)
print(justpath) # /home/user/folder (note the trailing slash has been removed)
print(justfilename) # file.txt

#=============

# make a folder if it does not exist
somepath = "/home/user/folder/"
homework = "homework"
h = os.path.join(somepath, homework)
if not os.path.exists(h):
	os.makedirs(h)

#=============

# print the full path of the script being executed
# __file__ is derived from sys.argv[0] so import sys is required
thisscript = os.path.realpath(__file__)
print(thisscript)

