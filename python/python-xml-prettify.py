#!/usr/bin/python3

# requires BeautifulSoup and an XML parser (not included with BeautifulSoup):
# pip3 install bs4 lxml

import sys
from bs4 import BeautifulSoup

bs = BeautifulSoup(open(sys.argv[1]), 'xml')
print(bs.prettify())
