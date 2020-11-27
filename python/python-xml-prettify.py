#!/usr/bin/python3

# requires BeautifulSoup an XML parser (not included with BeautifulSoup):
# pip3 install lxml

import sys
from bs4 import BeautifulSoup

bs = BeautifulSoup(open(sys.argv[1]), 'xml')
print(bs.prettify())
