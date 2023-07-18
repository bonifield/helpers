#!/usr/bin/python3



from datetime import date, datetime, timedelta, timezone



# start a timer
start = datetime.utcnow().timestamp()



print()
print()
print("#--------------------")
print("# use a given epoch")
print("#--------------------")
print()



# generate a local epoch timestamp with datetime.now().timestamp() or UTC with datetime.utcnow().timestamp()
EPOCHEXAMPLE = 1671033931.080355 # float

print(f"EPOCHEXAMPLE = 1671033931.080355")

print()
print("convert given epoch to local timestamp: datetime.fromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S')")
a = datetime.fromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S') # 2022-12-14 10:05:31
print(f"\t{a}")

print()
print("convert given epoch to UTC timestamp: datetime.utcfromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S')")
b = datetime.utcfromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S') # 2022-12-14 16:05:31
print(f"\t{b}")



print()
print()
print("#--------------------")
print("# use a given string")
print("#--------------------")
print()



STRINGEXAMPLE = "2022-12-14 22:07:57.000"

# ensure the given string is in UTC before proceding
print(f"STRINGEXAMPLE = 2022-12-14 22:07:57.000")

print()
print("convert given timestamp string to UTC epoch: datetime.strptime(STRINGEXAMPLE, '%Y-%m-%d %H:%M:%S.%f').astimezone(timezone.utc).strftime('%s')")
aa = datetime.strptime(STRINGEXAMPLE, '%Y-%m-%d %H:%M:%S.%f').astimezone(timezone.utc).strftime('%s') # 1671098877
print(f"\t{aa}")



print()
print()
print("#--------------------")
print("# local timestamps")
print("#--------------------")
print()



print()
print("datetime.now()")
c = datetime.now() # 2022-12-14 10:39:48.349885
print(f"\t{c}")

print()
print("datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]")
d = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # 2022-12-14 10:39:48.350
print(f"\t{d}")

print()
print("datetime.now().timestamp()")
e = datetime.now().timestamp() # 1671035988.349939
print(f"\t{e}")

print()
print("datetime.now().timestamp()*1000 (milliseconds)")
f = datetime.now().timestamp()*1000 # 1671035988349.977
print(f"\t{f}")

print()
print("datetime.now().astimezone()")
g = datetime.now().astimezone() # 2022-12-14 10:39:48.350018-06:00
print(f"\t{g}")

print()
print("datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')")
h = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z') # 2022-12-14 10:39:48.350018 CST -0600
print(f"\t{h}")

print()
print("datetime.now().astimezone(timezone.utc)")
i = datetime.now().astimezone(timezone.utc) # 2022-12-14 16:39:48.350018+00:00
print(f"\t{i}")

print()
print("datetime.now().astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')")
j = datetime.now().astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f %Z %z') # 2022-12-14 16:39:48.350018 UTC +0000
print(f"\t{j}")



print()
print()
print("#--------------------")
print("# UTC timestamps")
print("# note - DO NOT use astimezone() (with or without strftime and %Z/%z) here because they return the machine-local timezone info")
print("#--------------------")
print()



print()
print("datetime.utcnow()")
k = datetime.utcnow() # 2022-12-14 16:39:48.350286
print(f"\t{k}")

print()
print("datetime.utcnow().timestamp()")
l = datetime.utcnow().timestamp() # 1671057588.350316
print(f"\t{l}")

print()
print("datetime.utcnow().timestamp()*1000 (milliseconds)")
m = datetime.utcnow().timestamp()*1000 # 1671057588350.361
print(f"\t{m}")

print()
print("datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')")
n = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f') # 2022-12-14 16:39:48.350400
print(f"\t{n}")

print()
print("datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]")
o = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # 2022-12-14 16:39:48.350
print(f"\t{o}")

print()
print("str(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3])+'Z'")
p = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+"Z" # 2022-12-14T16:39:48.350Z
print(f"\t{p}")

print()
print("DO NOT DO THIS: datetime.utcnow().astimezone()")
q = datetime.utcnow().astimezone() # VERY BAD - 2022-12-14 16:39:48.350550-06:00
print(f"\t{q}")

print()
print("DO NOT DO THIS: datetime.utcnow().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')")
r = datetime.utcnow().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z') # VERY BAD - 2022-12-14 16:39:48.350604 CST -0600
print(f"\t{r}")



print()
print()
print("#--------------------")
print("# Calculate Future Dates")
print("#--------------------")
print()



print()
print("future = date.today() + timedelta(days=90)")
print("wayfuture = date.today() + timedelta(weeks=52)")
present = date.today()
future = present + timedelta(days=90)
# weeks is the largest supported argument
wayfuture = present + timedelta(weeks=52)
ppp = present.strftime('%Y%m%d')
fff = future.strftime('%Y%m%d')
www = wayfuture.strftime('%Y%m%d')
print(f"\t{present} --> {future} --> {wayfuture}")
print(f"\tusing strftime:\t{ppp} --> {fff} --> {www}")




print()
print()
# end a timer
end = datetime.utcnow().timestamp()
complete = end-start
print(f"script took {complete} seconds to execute")
print()
print()



"""


#--------------------
# use a given epoch
#--------------------

EPOCHEXAMPLE = 1671033931.080355

convert given epoch to local timestamp: datetime.fromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S')
	2022-12-14 10:05:31

convert given epoch to UTC timestamp: datetime.utcfromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S')
	2022-12-14 16:05:31


#--------------------
# use a given string
#--------------------

STRINGEXAMPLE = 2022-12-14 22:07:57.000

convert given timestamp string to UTC epoch: datetime.strptime(STRINGEXAMPLE, '%Y-%m-%d %H:%M:%S.%f').astimezone(timezone.utc).strftime('%s')
	1671098877


#--------------------
# local timestamps
#--------------------


datetime.now()
	2022-12-14 12:33:55.381492

datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
	2022-12-14 12:33:55.381

datetime.now().timestamp()
	1671042835.383091

datetime.now().timestamp()*1000 (milliseconds)
	1671042835383.363

datetime.now().astimezone()
	2022-12-14 12:33:55.383625-06:00

datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')
	2022-12-14 12:33:55.383913 CST -0600

datetime.now().astimezone(timezone.utc)
	2022-12-14 18:33:55.384236+00:00

datetime.now().astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')
	2022-12-14 18:33:55.384512 UTC +0000


#--------------------
# UTC timestamps
# note - DO NOT use astimezone() (with or without strftime and %Z/%z) here because they return the machine-local timezone info
#--------------------


datetime.utcnow()
	2022-12-14 18:33:55.385303

datetime.utcnow().timestamp()
	1671064435.385567

datetime.utcnow().timestamp()*1000 (milliseconds)
	1671064435385.8298

datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
	2022-12-14 18:33:55.386157

datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
	2022-12-14 18:33:55.386

str(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3])+'Z'
	2022-12-14T18:33:55.386Z

DO NOT DO THIS: datetime.utcnow().astimezone()
	2022-12-14 18:33:55.387008-06:00

DO NOT DO THIS: datetime.utcnow().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')
	2022-12-14 18:33:55.387287 CST -0600


#--------------------
# Calculate Future Dates
#--------------------


futre = date.today() + timedelta(days=90)
wayfuture = date.today() + timedelta(weeks=52)
	2023-07-18 --> 2023-10-16 --> 2024-07-16
	using strftime:	20230718 --> 20231016 --> 20240716

script took 0.00855398178100586 seconds to execute


"""
