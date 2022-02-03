#!/usr/bin/python3

import sys

# saves input from stdin as a string; will append a line terminator
word = sys.stdin.readline()

# size parameter (int) limits the input to 3 bytes
# hitting the limit will not include a line terminator
#word = sys.stdin.readline(3)

print("# not stripped")
print([hex(ord(x)) for x in word]) # quick hexdump
print(word)

print("# stripped")
word = word.strip()
print([hex(ord(x)) for x in word]) # quick hexdump
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
