#!/usr/bin/python3
# August 2020
#
# basic example of combining all CSVs of a desired format into one working file,
# optionally specifying columns to keep or discard
#
# https://docs.python.org/3/library/os.html
# https://stackoverflow.com/questions/8625991/use-python-os-walk-to-identify-a-list-of-files
# https://stackoverflow.com/questions/16953842/using-os-walk-to-recursively-traverse-directories-in-python
# https://docs.python.org/3/howto/sorting.html
#

import csv, os, re, sys, time

try:
	inputPath = sys.argv[1]
	epoch = str(int(time.time()))
	tempCsv = "working."+epoch+".csv"
except Exception as e:
	print(e)
	print('needs an input path where CSV files are located')

class tcol:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'

# change this line if the naming convention ever changes
fileNameFormat = re.compile('.*sample_[0-9]{4}-[0-9]{2}-[0-9]{2}.csv')

def makeWorkingFile(inputPath):
	# list of files to be worked on
	workingFiles = []

	# walk a folder, look for CSVs, add to working list or skip
	for root, dirs, files in os.walk(inputPath):
		path = root.split(os.sep)
		for file in files:
			fname = os.path.join(root, file)
			#if fname.endswith((".csv", ".CSV")):
			if fname.lower().endswith(".csv"):
				# generate processing worklog here?
				# if the filename matches the fileNameFormat defined above
				if fileNameFormat.findall(file):
					# append to the list of files to be worked on
					workingFiles.append(fname)
					# print a green status message
					print(tcol.OKGREEN + 'OK' + tcol.RESET + '\tPROCESSING {}'.format(file))
				else:
					# note - change the re.compile() statement above if the naming convention ever changes
					# print a red status message
					print(tcol.FAIL + 'ERROR' + tcol.RESET + '\tNOT PROCESSING {} due to naming convention error: expected sample_YYYY-MM-DD.csv format'.format(file))

	# sort and unique the list
	workingFiles = sorted(list(set(workingFiles)))

	# make the combined working CSV
	with open(tempCsv, 'w') as t:
		# end lines with Windows CRLF
		cw = csv.writer(t, delimiter=",", lineterminator="\r\n", quoting=csv.QUOTE_NONNUMERIC)
		cw.writerow(["Datestamp", "Type", "Nice", "Message", "Count"])
		for workingFile in workingFiles:
			# ensure this date extraction matches the filename format and re.compile() statement above
			try:
				datestamp = workingFile.split('_')[-1].split('.')[0]
			except Exception as e:
				print("{} this filename does not appear to follow the naming convention, and a date could not be extracted".format(workingFile))
			cc = csv.DictReader(open(workingFile, 'r'))
			# specify columns to write into the new working CSV
			for row in cc:
				type = row['Type']
				nice = row['Nice']
				message = row['Message']
				count = row['Count']
				cw.writerow([datestamp, type, nice, message, count])
	t.close()

if __name__ == "__main__":
	makeWorkingFile(inputPath)
