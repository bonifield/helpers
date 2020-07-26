#!/bin/bash

inputFile=$1
outputFile="snort.pcap"

echo
echo "Processing $inputFile, this may take a few seconds."
#snort -A console -r $inputFile -c /etc/snort/snort.conf -l `pwd` -L $outputFile -byqU -k none
snort -A full -r $inputFile -c /etc/snort/snort.conf -l `pwd` -L $outputFile -byqU -k none
echo

# -A console - show on console
### -A full - write log file named "alert"
# -r - read file
# -c - snort configuration file to use
# -l - log output location
# -L - log to pcap file
# -b - log in tcpdump pcap
# -y - include year in timestamp in alert and log
# -q - quiet
# -U - use UTC for timestamps
# -k none - disable checksum mode ***THIS IS REQUIRED FOR TESTING***

# may need to "sudo ~/bin/ ~/path/to/file.pcap"
