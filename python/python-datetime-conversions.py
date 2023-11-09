#!/usr/bin/python3

from datetime import date, datetime, timedelta, timezone

# start a timer
start = datetime.utcnow().timestamp()

print()
print("#--------------------")
print("# use a given epoch")
print("#--------------------")
print()

# generate a local epoch timestamp with datetime.now().timestamp()
# or generate a UTC epoch timestamp with datetime.now(timezone.utc).timestamp()
EPOCHEXAMPLE = 1699557515.080355 # float

print(f"{EPOCHEXAMPLE = }")

print()
print("convert given epoch to local timestamp")
print("datetime.fromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S')")
a = datetime.fromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S') # 2023-11-09 13:18:35
print(f"\t{a}")

print()
print("convert given epoch to UTC timestamp")
print("datetime.utcfromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S')")
b = datetime.utcfromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S') # 2023-11-09 19:18:35
print(f"\t{b}")

print()
print("#--------------------")
print("# use a given string")
print("#--------------------")
print()

STRINGEXAMPLE = "2023-11-09 13:08:30.123"

# ensure the given string is in UTC before proceding
print(f"{STRINGEXAMPLE = }")

print()
print("convert given timestamp string to UTC epoch")
print("datetime.strptime(STRINGEXAMPLE, '%Y-%m-%d %H:%M:%S.%f').astimezone(timezone.utc).strftime('%s')")
aa = datetime.strptime(STRINGEXAMPLE, '%Y-%m-%d %H:%M:%S.%f').astimezone(timezone.utc).strftime('%s') # 1699578510
print(f"\t{aa}")

print()
print("#--------------------")
print("# local timestamps")
print("#--------------------")

print()
print("datetime.now()")
c = datetime.now() # 2023-11-09 13:18:35.181241
print(f"\t{c}")

print()
print("datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]")
d = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # 2023-11-09 13:18:35.181
print(f"\t{d}")

print()
print("datetime.now().timestamp()")
e = datetime.now().timestamp() # 1699557515.181285
print(f"\t{e}")

print()
print("datetime.now().timestamp()*1000 (milliseconds)")
f = datetime.now().timestamp()*1000 # 1699557515181.2961
print(f"\t{f}")

print()
print("datetime.now().astimezone()")
g = datetime.now().astimezone() # 2023-11-09 13:18:35.181300-06:00
print(f"\t{g}")

print()
print("datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')")
h = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z') # 2023-11-09 13:18:35.181316 CST -0600
print(f"\t{h}")

print()
print("datetime.now().astimezone(timezone.utc)")
i = datetime.now().astimezone(timezone.utc) # 2023-11-09 19:18:35.181332+00:00
print(f"\t{i}")

print()
print("datetime.now().astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')")
j = datetime.now().astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f %Z %z') # 2023-11-09 19:18:35.181338 UTC +0000
print(f"\t{j}")

print()
print("#--------------------")
print("# UTC timestamps")
print("# further reading - https://medium.com/@life-is-short-so-enjoy-it/python-datetime-utcnow-maybe-no-more-for-me-221795e8ddbf")
print("# note - DO use datetime.now(timezone.utc).timestamp()")
print("# note - DO NOT USE datetime.utcnow().timestamp()")
print("#--------------------")

print()
print("datetime.utcnow()")
k = datetime.utcnow() # 2023-11-09 19:18:35.181349
print(f"\t{k}")

print()
print("datetime.now(timezone.utc)")
k = datetime.now(timezone.utc) # 2023-11-09 19:18:35.181353+00:00
print(f"\t{k}")

print()
print("DO NOT DO THIS: datetime.utcnow().timestamp()")
l = datetime.utcnow().timestamp() # 1699579115.181357
print(f"\t{l}")

print()
print("datetime.now(timezone.utc).timestamp()")
l = datetime.now(timezone.utc).timestamp() # 1699557515.181361
print(f"\t{l}")

print()
print("DO NOT DO THIS: datetime.utcnow().timestamp()*1000 (milliseconds)")
m = datetime.utcnow().timestamp()*1000 # 1699579115181.365
print(f"\t{m}")

print()
print("datetime.now(timezone.utc).timestamp()*1000 (milliseconds)")
m = datetime.now(timezone.utc).timestamp()*1000 # 1699557515181.367
print(f"\t{m}")

print()
print("datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')")
n = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f') # 2023-11-09 19:18:35.181370
print(f"\t{n}")

print()
print("datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]")
o = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] # 2023-11-09 19:18:35.181
print(f"\t{o}")

print()
print("str(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3])+'Z'")
p = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+"Z" # 2023-11-09T19:18:35.181Z
print(f"\t{p}")

print()
print("DO NOT DO THIS: datetime.utcnow().astimezone()")
q = datetime.utcnow().astimezone() # VERY BAD - 2022-12-14 16:39:48.350550-06:00
print(f"\t{q}")

print()
print("DO NOT DO THIS: datetime.utcnow().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')")
r = datetime.utcnow().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z') # VERY BAD - 2023-11-09 19:18:35.181394-06:00
print(f"\t{r}")

print()
print("#--------------------")
print("# calculate future dates")
print("#--------------------")

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
print(f"\t{present} --> {future} --> {wayfuture}") # 2023-11-09 --> 2024-02-07 --> 2024-11-07
print(f"\tusing strftime:\t{ppp} --> {fff} --> {www}") # using strftime: 20231109 --> 20240207 --> 20241107

print()
# end a timer
end = datetime.utcnow().timestamp()
complete = end-start
print(f"script took {complete} seconds to execute")
print()

"""

#--------------------
# use a given epoch
#--------------------

EPOCHEXAMPLE = 1699557515.080355

convert given epoch to local timestamp
datetime.fromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S')
	2023-11-09 13:18:35

convert given epoch to UTC timestamp
datetime.utcfromtimestamp(EPOCHEXAMPLE).strftime('%Y-%m-%d %H:%M:%S')
	2023-11-09 19:18:35

#--------------------
# use a given string
#--------------------

STRINGEXAMPLE = '2023-11-09 13:08:30.123'

convert given timestamp string to UTC epoch
datetime.strptime(STRINGEXAMPLE, '%Y-%m-%d %H:%M:%S.%f').astimezone(timezone.utc).strftime('%s')
	1699578510

#--------------------
# local timestamps
#--------------------

datetime.now()
	2023-11-09 13:18:35.181241

datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
	2023-11-09 13:18:35.181

datetime.now().timestamp()
	1699557515.181285

datetime.now().timestamp()*1000 (milliseconds)
	1699557515181.2961

datetime.now().astimezone()
	2023-11-09 13:18:35.181300-06:00

datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')
	2023-11-09 13:18:35.181316 CST -0600

datetime.now().astimezone(timezone.utc)
	2023-11-09 19:18:35.181332+00:00

datetime.now().astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')
	2023-11-09 19:18:35.181338 UTC +0000

#--------------------
# UTC timestamps
# further reading - https://medium.com/@life-is-short-so-enjoy-it/python-datetime-utcnow-maybe-no-more-for-me-221795e8ddbf
# note - DO use datetime.now(timezone.utc).timestamp()
# note - DO NOT USE datetime.utcnow().timestamp()
#--------------------

datetime.utcnow()
	2023-11-09 19:18:35.181349

datetime.now(timezone.utc)
	2023-11-09 19:18:35.181353+00:00

DO NOT DO THIS: datetime.utcnow().timestamp()
	1699579115.181357

datetime.now(timezone.utc).timestamp()
	1699557515.181361

DO NOT DO THIS: datetime.utcnow().timestamp()*1000 (milliseconds)
	1699579115181.365

datetime.now(timezone.utc).timestamp()*1000 (milliseconds)
	1699557515181.367

datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
	2023-11-09 19:18:35.181370

datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
	2023-11-09 19:18:35.181

str(datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3])+'Z'
	2023-11-09T19:18:35.181Z

DO NOT DO THIS: datetime.utcnow().astimezone()
	2023-11-09 19:18:35.181394-06:00

DO NOT DO THIS: datetime.utcnow().astimezone().strftime('%Y-%m-%d %H:%M:%S.%f %Z %z')
	2023-11-09 19:18:35.181403 CST -0600

#--------------------
# calculate future dates
#--------------------

future = date.today() + timedelta(days=90)
wayfuture = date.today() + timedelta(weeks=52)
	2023-11-09 --> 2024-02-07 --> 2024-11-07
	using strftime:	20231109 --> 20240207 --> 20241107

script took 0.011044979095458984 seconds to execute

"""
