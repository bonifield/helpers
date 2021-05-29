#!/usr/bin/python3

from datetime import datetime

#
#
#

EPOCHEXAMPLE = 1622299682.128648 # float

print()
print("convert epoch to local timestamp")
lt = datetime.fromtimestamp(EPOCHEXAMPLE).strftime("%Y-%m-%d %H:%M:%S")
print("\t"+str(EPOCHEXAMPLE), "-->", lt)

print()
print("convert epoch to UTC timestamp")
ut = datetime.utcfromtimestamp(EPOCHEXAMPLE).strftime("%Y-%m-%d %H:%M:%S")
print("\t"+str(EPOCHEXAMPLE), "-->", ut)

#
#
#

print()
print("local timestamps")
print("\tdatetime.now()", "-->", datetime.now())
print("\tdatetime.now().timestamp()", "-->", datetime.now().timestamp())
print("\tdatetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')", "-->", datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z'), "(machine-local timezone info)")
print("\tdatetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]", "-->", datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

#
#
#

print()
print("UTC timestamps (note do not use astimezone() and %Z/%z here because they return the machine-local timezone info)")
print("\tdatetime.utcnow()", "-->", datetime.utcnow())
print("\tdatetime.utcnow().timestamp()", "-->", datetime.utcnow().timestamp())
print("\tdatetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')", "-->", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'))
print("\tdatetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]", "-->", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
print("\tstr(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3])+'Z'", "-->", str(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3])+"Z")

print()
