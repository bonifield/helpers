#!/usr/bin/python3

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
	print('slice attempt error message:\n\t'+str(e)+'\n\tyou cannot slice deques directly, instead use itertools.islice(object,start,end)')

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
