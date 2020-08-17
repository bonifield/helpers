#!/usr/bin/python3
# August 2020
#
# TODO: creates and visualizes a strange last bucket; identify and remove
# 
# basic example of using Pandas to generate a multi-line graph, with a legend, based on CSV data
# uses subgroup iteration to generate legend names
#
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
# https://stackoverflow.com/questions/19555525/saving-plots-axessubplot-generated-from-python-pandas-with-matplotlibs-savefi
# https://stackoverflow.com/questions/29233283/plotting-multiple-lines-with-pandas-dataframe
# https://stackoverflow.com/questions/21920233/matplotlib-log-scale-tick-label-number-formatting
# https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend
# https://stackoverflow.com/questions/43374920/how-to-automatically-annotate-maximum-value-in-pyplot
# https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
#

import csv, os, sys, time
# IMPORT PANDAS BEFORE MATPLOTLIB
import pandas as pd
import matplotlib.pyplot as plt
# long numbers for logarithmic y-axis
from matplotlib.ticker import ScalarFormatter

try:
	inputFile = sys.argv[1]
	epoch = str(int(time.time()))
	outputFile = "out."+epoch+".png"
except Exception as e:
	print(e)
	print('needs an input path where CSV files are located')

class tcol:
	OKGREEN = '\033[92m'
	OKBLUE = '\033[94m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'

def print_okgreen(x):
	return(tcol.OKGREEN + str(x) + tcol.RESET)

def print_okblue(x):
	return(tcol.OKBLUE + str(x) + tcol.RESET)

def print_warning(x):
	return(tcol.WARNING + str(x) + tcol.RESET)

def print_fail(x):
	return(tcol.FAIL + str(x) + tcol.RESET)

print(print_okblue("WORKING") +" "+ inputFile)

def graphMaker(inputFile):
	# ingest CSV in Pandas-native format (df means dataframe by convention)
	df = pd.read_csv(inputFile, header=0, index_col="Datestamp", parse_dates=True, infer_datetime_format=True)

	# get a sorted unique list of all Message values (will use for making individual graphs)
	#um = sorted(list(df['Message'].unique()))
	#print(um)

	# drop columns (or make new dataframe with df1=df[["Datestamp", "Message", "Count"]] )
	df.drop(["Type", "Nice"], axis=1, inplace=True)

	# convert Count to integer
	df.Count = pd.to_numeric(df.Count)

	# holder list for legend labels, to be filled by loop below with key names
	legendLabels = []

	# make figure and set of subplots
	f, ax = plt.subplots()

	# make one graph with each line representing the "Message" field
	# key = Message, the groupby field
	# grp = all values by each grouped key
	for key, grp in df.groupby(['Message']):
		# append each key (Message) to a holding list which will then fuel the legend
		legendLabels.append(key)
	#	print(key)
	#	print(grp)
		# get min/max values on y-axis
		ymin = min(grp['Count'])
		ymax = max(grp['Count'])

	#	print(grp.index)
	#	print(grp.values)

		# iterate over the subgroup to find the index values for the min and max using a counter, and each Message value
		yminindex = 0
		ymaxindex = 0
		counter = -1
		for vv in grp.values:
			counter += 1
			for v in vv:
				if v == ymin:
					yminindex = counter
				elif v == ymax:
					ymaxindex = counter

		# use the min/max index values to find the associated x-value (date)
		yminxpos = grp.index[yminindex]
		ymaxxpos = grp.index[ymaxindex]

	#	print(key)
	#	print("\tymin: {}\t yminindex: {}\tyminxpos: {}".format(ymin, yminindex, yminxpos))
	#	print("\tymax: {}\t ymaxindex: {}\tymaxxpos: {}".format(ymax, ymaxindex, ymaxxpos))

		# create axis and define line graph
		ax = grp.plot(logy=True, ax=ax, kind='line')
		# use Scalar format for axis numbers (aka not the logarithmic 10^n format on y-axis etc)
		for axis in [ax.xaxis, ax.yaxis]:
			axis.set_major_formatter(ScalarFormatter())

		# label for peak on graph
		#annotationLabel = str("{} {}".format(str(ymaxxpos).split()[0], ymax))
		annotationLabel = str(ymax)
		# add peak annotations to graph
		#ax.annotate(annotationLabel, xy=(ymaxxpos, ymax), xytext=(ymaxxpos, ymax+5), arrowprops=dict(facecolor='black', shrink=0.01))
		# no arror for peak annotations
		ax.annotate(annotationLabel, xy=(ymaxxpos, ymax), xytext=(ymaxxpos, ymax+5))

	# generate one graph with many subplots
	# legend labels read from the keys added to the list "legendLabels" in the loop above
	plt.legend(bbox_to_anchor=(1.01,1), loc="upper left", labels=legendLabels)
	plt.subplots_adjust(right=0.7)
	#plt.show()
	fig = plt.gcf()
	fig.set_size_inches(10, 5)
	try:
		fig.savefig(outputFile, dpi=300)
		print(print_okgreen("SUCCESS") +" generated {}".format(outputFile))
	except Exception as e:
		print(e)
		print(print_fail("ERROR") +" could not generate output file")
		sys.exit(1)

if __name__ == "__main__":
	graphMaker(inputFile)
