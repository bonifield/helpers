# helpers
Skeleton scripts and sample data to help jog the memory.

TODO: fix naming conventions, clean up code examples

- 2020-11-06
	- added lots of Python threading examples
- 2020-07-25
	- rebuilt the repo, which was originally created in 2016

### Files
- bash-array-comparison.sh
	- How to compare two arrays in Bash
- bash-array-usage.sh
	- Examples of working with Bash arrays
- bash-getopts.sh
	- Uses Bash cases to add switch functionality to scripts
- bash-if-while-for-functions.sh
	- Examples of Bash if/elif/else, while, and for statements in both functions and one-liners
- bash-yesno.sh
	- Simple Yes/No comparison check, accounting for case
- c-loops.c
	- Various loops in C
- c-structs.c
	- Using C structures to create complex objects
- esp.c / exe
	- Estimate the location of the ESP register
- javascript-bookmarklet-hide-element
	- A bookmarklet for Firefox that, when clicked, allows the user to hover over elements on a webpage and click to remove them from view. ESC to cancel.
	- Make a new bookmark, name it "hideElement", and paste the code into the Location field
- powershell-examples.ps1
	- Many examples of PowerShell variables, string manipulation, functions, custom objects, arrays, hashtables, output colorization, and more
- python-argparse.py
	- Basic way to add switches to a Python script (better than getopt)
- python-class-py2.py
	- Outlines the creation and usage of parent and child classes, with output examples
- python-class-py3.py
	- Outlines the creation and usage of parent and child classes, with output examples
- python-collections-deque.py
	- How to use deque to handle list-like objects, but with better options like left appends, extends, and pops
- python-csv-worker_01_combine.py
	- Combine only desired CSV files in a given path into a single working file (usage: script path)
	- use with the dated sample CSVs in the sampledata folder
- python-csv-worker_02_pandas_graph.py
	- Use Pandas to create a multi-line graph from a given CSV (ex. as processed by python-csv-worker_01_combine.py) (usage: script file.csv)
- python-dictionaries.py
	- How to use dictionaries in Python
- python-file-inout-processor.py
	- How to read from one file, manipulate the content, and write to a separate output file.
- python-files-folders.py
	- Working with both regular and temporary files and folders
- python-json-printer.py
	- Ingest then dump a JSON file for review
- python-lists.py
	- How to use lists in Python
- python-generators-comprehensions-yield.py
	- How to use generator expressions, list comprehensions, and an example of yield generator expressions in a function
- python-os-commands.py
	- Basic execution of OS commands with os and subprocess modules
- python-regex.py
	- Using in-line regex and compiled regex objects
- python-sqlite-01-makedb.py
	- Make a SQLite database (usage: ./python-sqlite-01-writer.py mydb)
- python-sqlite-02-writer.py
	- Write records to a SQLite database (usage: ./python-sqlite-02-writer.py mydb)
- python-sqlite-03-reader.py
	- Read records from a SQLite database (usage: ./python-sqlite-03-reader.py -i mydb -f Alice -a 42)
- python-terminal-colors.py
	- ANSI terminal color usage in Python
- python-threading-01-randomSleep.py
	- Basic thread creation; threads sleep then exit
- python-threading-02-join.py
	- Use a join() to lock the main process until threads have finished
- python-threading-03-daemon.py
	- Daemonizing threads; the threads terminate when the main thread exits
- python-threading-04-FIFOqueue.py
	- A first-in-first-out queue
- python-threading-05-LIFOqueue.py
	- A last-in-first-out queue
- python-threading-06-priorityQueue.py
	- A queue which empties based on prioritized values (0 = highest priority)
- python-threading-07-fillQueue.py
	- Using threads to fill a queue which has a maximum size
- python-threading-08-joinWithQueue.py
	- Use daemonized threads to process items in a queue, then use join() to ensure the queue is empty
- python-threading-09-executorBasic.py
	- Use ThreadPoolExecutor to create worker threads, define max_worker cap
- python-threading-10-fillAndConsumeFromQueue.py
	- Use one thread to fill a queue, while another thread consumes from the same queue
- python-threading-11-multipleQueues.py
	- Uses multiple threads to process multiple queues; the first thread fills queue1, the second thread shuffles queue1 items to queue2, and the third thread drains queue2
- python-threading-12-processFiles.py
	- Uses one thread to read from a file and push to a queue, and another thread to read the queue, transform items, and push to an output file.
	- Note: using queues to process files line-by-line is VERY slow; this is just an example of converging multiple threads into a queue for a single output thread to safely write files.
- python-tkinter-gui-basics.py
	- How to make a simple GUI in Python
- python-web-requests.py
	- Usage of Python 3's Requests library to interact with network/web objects
- python-wifi-sniffing.py
	- Use Scapy to sniff basic WiFi information, such as base station IDs and transmitting device addresses
- python-xml-prettify
	- Example of using BeautifulSoup and lxml to "pretty print" XML data
- sampleCsv.csv
	- Four lines of test data
- shell_address.c / exe
	- Estimate the address of the SHELL environment variable
- splitHashCombiner.py
	- Identifies and matches sessions where data fields are potentially reversed using hash keys
- splunk-analyst-annotation-maker-dashboard.txt
	- A method of using text inputs to capture analyst annotations into lookup tables (a workaround for Splunk's lack of built-in knowledge management tools); use with the Annotation Viewer dashboard
- splunk-analyst-annotation-viewer-dashboard.txt
	- View analyst annotations; use with the Annotation Maker dashboard
- splunk-byte-and-packet-summary-dashboard.txt
	- Examples of input/output monitoring, with drilldown examples based on loadjob. Includes commented-out queries in case an IP-to-hostname lookup is in place
- splunk-dashboard-example-features.txt
	- Several examples of input types in Splunk's Simple XML, and other features like colorization, drilldowns, and token usage
- splunk-host-last-seen-dashboard.txt
	- Check if any hosts fell off the network, if new hosts appeared, and check for gaps in logs. Can also be used for sensor troubleshooting.
- terminator.desktop
	- Desktop launcher and icon for the Terminator terminal emulator; also a basic outline of how to make desktop launchers

### Sample Data
- sampleCSV.csv
	- very small CSV with quoted fields
- sample_2020-06-0x.csv
	- dated CSVs for testing with Pandas or similar
- testdata-2M.txt.gz
	- text file with 2 million lines (newline-separated), each with 13 digits; approximately 27 MB decompressed
