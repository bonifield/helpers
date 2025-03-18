#!/usr/bin/env python3

import glob
import os
import pathlib
import shutil
import tempfile
from datetime import datetime
# https://github.com/ahupp/python-magic
# pip3 install python-magic
# or
# python3 -m pip install python-magic
import magic

#=============

def printHeader(m):
	print("\n\n#"+"="*42)
	print("# "+str(m))
	print("#"+"="*42+"\n\n")

#=============

printHeader('Full path of the script and executing user')
# __file__ is derived from sys.argv[0] so import sys is required
thisscript = os.path.realpath(__file__)
# get current user
username = os.getlogin()
print(thisscript)
print(username)

#=============

printHeader('Temporary folder created')

ourTempDir = tempfile.mkdtemp() # create temporary folder
open(str(ourTempDir+'/myAwesomeTempFile.txt'), 'a').close() # make an empty file
print(ourTempDir) # access temporary folder path as a string

printHeader('List of items in temporary folder')
print(os.listdir(ourTempDir)) # access folder items as a list

printHeader('Individual items in temporary folder')
for i in os.listdir(ourTempDir): # access folder items individually
	print(i) # just filename
	#print(str(ourTempDir+'/'+i)) # try not to do this
	print(str(os.path.join(ourTempDir, i))) # access full path for each item

print('\nremoving temporary folder and file using: shutil.rmtree(ourTempDir)')
shutil.rmtree(ourTempDir) # remove temporary folder and contents

#=============

printHeader('Files in home directory, using os.listdir()')
hfiles = os.listdir(os.environ['HOME']) # get an environment variable if it exists
print(hfiles)

printHeader('Files in home directory, using OS environment variables and glob (note inclusion of the full path)')
homefiles = glob.glob(os.environ['HOME']+"/*") # get env variable and add a wildcard
print(homefiles)

#=============

printHeader('Combine a path and filename safely (Windows-safe as well); alternatively, safely combine folder paths')
somepath = f"/home/{username}/folder/"
somefile = "file.txt"
outname = os.path.join(somepath, somefile)
print(outname) # /home/user/folder/file.txt

#=============

printHeader('Get just the path or just the filename')
fullpath = f"/home/{username}/folder/file.txt"
justpath = os.path.dirname(fullpath)
justfilename = os.path.basename(fullpath)
print(justpath) # /home/user/folder (note the trailing slash has been removed)
print(justfilename) # file.txt

#=============

printHeader('Make a folder if it does not exist')
somepath = f"/home/{username}/folder/"
homework = "homework-temp"
mathy = "math-homework.txt"
hw = os.path.join(somepath, homework)
if not os.path.exists(hw):
	os.makedirs(hw)
	print(f"made directory: {hw}")
	pathlib.Path(os.path.join(hw, mathy)).touch()

print(f"\ncontents of {os.path.join(somepath, homework)}:")
print(os.listdir(os.path.join(somepath, homework)))

print(f'\nremoving directory: {os.path.join(somepath, homework)}')
shutil.rmtree(somepath) # remove example folder and contents

#=============

printHeader('os.stat() and magic file headers for select files in the home directory')
for h in homefiles[:10]:
	stats = os.stat(h)
	if os.path.isfile(h):
		print(f"FILE: {h}")
		#
		# magic
		#
		mff = magic.from_file(h)
		mffm = magic.from_file(h, mime=True)
		mfb = magic.from_buffer(open(h, "rb").read(2048))
		mfbm = magic.from_buffer(open(h, "rb").read(2048), mime=True)
		print(f"\tmagic name: {mff}\tmime type: {mffm}")
		print(f"\tmagic (buffer of first 2048 bytes) name: {mfb}\tmime type: {mfbm}")
	elif os.path.isdir(h):
		print(f"DIRECTORY: {h}")
	else:
		print(f"OTHER: {h}")
	#
	# os.stat() variables
	# mac epoch times are in UTC
	#
	mtime = stats.st_mtime
	mtimeutc = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
	atime = stats.st_atime
	atimeutc = datetime.fromtimestamp(atime).strftime('%Y-%m-%d %H:%M:%S')
	ctime = stats.st_mtime
	ctimeutc = datetime.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')
	#
	print(f"\tfilesize using os.path.getsize(filename): {os.path.getsize(h)}")
	print(f"\tfilesize using os.stat(filename).st_size: {stats.st_size}")
	print(f"\tuid: {stats.st_uid}")
	print(f"\tgid: {stats.st_gid}")
	print(f"\tinode: {stats.st_ino}")
	print(f"\tinode links: {stats.st_nlink}")
	print(f"\tinode device: {stats.st_dev}")
	print(f"\tlast modification time:\t\tepoch: {mtime}\tutc: {mtimeutc}")
	print(f"\tlast access time:\t\tepoch: {atime}\tutc: {atimeutc}")
	print(f"\tlast created/changed time:\tepoch: {ctime}\tutc: {ctimeutc}") # unix-like: last metadata change; windows: creation time
	print(f"\tpermissions: {stats.st_mode}")
	print(f"\tpermissions (octal): {oct(stats.st_mode)}") # note last 4 digits
	#print(f"\tall stats with os.stat(filename): {stats}")
	print()
