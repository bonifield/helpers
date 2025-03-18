#!/usr/bin/env python3

import sys

# saves input from stdin as a string; appends a line terminator
word = sys.stdin.readline()

# adding the size parameter (int) limits the input to x bytes
#word = sys.stdin.readline(4)

print("# not stripped")
print([hex(ord(x)) for x in word]) # each character in hex
print(word)

print("# stripped")
word = word.strip()
print([hex(ord(x)) for x in word])
print(word)

'''
echo "AAAA" | python-read-stdin.py

# not stripped
['0x41', '0x41', '0x41', '0x41', '0xa']
AAAA

# stripped
['0x41', '0x41', '0x41', '0x41']
AAAA
'''
