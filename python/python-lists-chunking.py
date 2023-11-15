#!/usr/bin/env python3

# 17 items, so we expect two 5-item lists, and one 7-item list
large_list = [r+1 for r in range(17)]
chunk_size = 5

def chunk_list(l, n) -> list:
	""" split a large list into smaller lists of n items, with one list of remainders """
	for i in range(0, len(l), n):
		yield l[i:i+n]

# convert generator to list
list_of_smaller_lists = list(chunk_list(large_list, chunk_size))

print(list_of_smaller_lists)
# output
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17]]
