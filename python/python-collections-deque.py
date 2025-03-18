#!/usr/bin/env python3

from collections import deque
import itertools

#=============

letters = "abc"

dq = deque(letters)

print(dq)

dq.append('d')
dq.appendleft('z')

print(dq)

dq.extend('efg')
dq.extendleft('yxw')

print(dq)

dq.rotate(4)
print(dq)

dq.rotate(-9)
print(dq)

print(dq.pop())
print(dq.popleft())

try:
	print(dq[0:5])
except Exception as e:
	print("slice attempt error message below; you cannot slice deques directly, instead use itertools.islice(object,start,end)")
	print(str(e))

print(list(itertools.islice(dq,3,8)))

#=============

# make a deque that processes values but has a max size and consumes oldest values first
dq2 = deque([], maxlen=3)
for i in range(6):
	dq2.append(i)
	print(dq2)

dq3 = deque([], maxlen=3)
for i in range(6):
	dq3.appendleft(i)
	print(dq3)

#=============
# output
#=============

'''
deque(['a', 'b', 'c'])
deque(['z', 'a', 'b', 'c', 'd'])
deque(['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
deque(['d', 'e', 'f', 'g', 'w', 'x', 'y', 'z', 'a', 'b', 'c'])
deque(['b', 'c', 'd', 'e', 'f', 'g', 'w', 'x', 'y', 'z', 'a'])
a
b
slice attempt error message:
	sequence index must be integer, not 'slice'
	you cannot slice deques directly, instead use itertools.islice(object,start,end)
['f', 'g', 'w', 'x', 'y']
deque([0], maxlen=3)
deque([0, 1], maxlen=3)
deque([0, 1, 2], maxlen=3)
deque([1, 2, 3], maxlen=3)
deque([2, 3, 4], maxlen=3)
deque([3, 4, 5], maxlen=3)
deque([0], maxlen=3)
deque([1, 0], maxlen=3)
deque([2, 1, 0], maxlen=3)
deque([3, 2, 1], maxlen=3)
deque([4, 3, 2], maxlen=3)
deque([5, 4, 3], maxlen=3)
'''
