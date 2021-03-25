#!/usr/bin/python3

l = [[1,2],[3,4],[555,666],[7777,8888],[99999,100000]]
for x in l:
	print("%-20s" % x[0], "%-20s" % x[1])

# displays:
#
#	1                    2
#	3                    4
#	555                  666
#	7777                 8888
#	99999                100000



# https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
ipa = "192.168.1.1"
b = ["{0:08b}".format(int(x)) for x in ipa.split(".")] # ['11000000', '10101001', '00000001', '00000001']



#
# examples below from
#	https://docs.python.org/3/library/string.html#format-specification-mini-language
#	https://docs.python.org/3/library/string.html#format-examples
#

n1 = '{:+f} / {:+f}'.format(3.14, -3.14) # show pos/neg signs always
n2 = '{: f} / {: f}'.format(3.14, -3.14) # show a space for positive numbers
n3 = '{:-f} / {:-f}'.format(3.14, -3.14) # show only the minus -- same as '{:f}; {:f}'
print(n1) # +3.140000 / -3.140000
print(n2) #  3.140000 / -3.140000 # note leading space
print(n3) # 3.140000 / -3.140000



n4 = '{:,}'.format(1234567890)
print(n4) # '1,234,567,890'



points = 19
total = 22
correct = 'grade: {:.2%}'.format(points/total)
print(correct) # 'grade: 86.36%'



import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d)) # '2010-07-04 12:15:58'



for align, text in zip('<^>', ['left', 'center', 'right']):
	print('{0:{fill}{align}16}'.format(text, fill=align, align=align))
# displays
#	left<<<<<<<<<<<<
#	^^^^^center^^^^^
#	>>>>>>>>>>>right
