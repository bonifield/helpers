#!/usr/bin/env python3


import ipaddress
import polars as pl


# two dataframes for testing
# df with IPs and hostnames
ips = [
	{"ip":"10.1.2.3", "hostname":"bob-pc"},
	{"ip":"192.168.1.2", "hostname":"alice-pc"},
	{"ip":"99.99.99.99", "hostname":"unknown-pc"},
]
# df with CIDRs and descriptions to be used in the IP dataframe
net = [
	{"network":"10.0.0.0/8", "description":"east-coast"},
	{"network":"192.168.0.0/16", "description":"west-coast"},
	{"network":"172.16.0.0/12", "description":"private-space"},
]


# create the dataframes
dfips = pl.DataFrame(ips)
dfnet = pl.DataFrame(net)
# show the new dataframes
print(dfips)
print(dfnet)


# True if the IP is within the network, otherwise False
# THIS IS THE SLOWEST PART OF THE SCRIPT
def check_cidr(ip: str, cidr: str) -> bool:
	"""Returns True if an IP address is within a given CIDR netblock."""
	return ipaddress.ip_address(ip) in ipaddress.ip_network(cidr)


# list comprehension to create a new list of descriptions
#   this will exactly match the "dfips" dataframe length
# iter_rows() is faster than rows() in larger datasets, but rows() may be
#   faster for smaller datasets
# named=True means return a dictionary so we can access values by name,
#   but returning a dict is more expensive than just calling positional values
# next() lets us get the first match from the inner generator
#   the outer loop maintains the same number of rows as the IP dataframe
#   and the default None prevents the loop from breaking
descriptions = [
	next((
		row["description"] for row in dfnet.iter_rows(named=True)
		if check_cidr(ip, row["network"])
	), None) for ip in dfips["ip"]
]


# the order and length of "descriptions" matches exactly the IP dataframe,
#   so with_columns just adds the list directly as a new column
dfx = dfips.with_columns(pl.Series("description", descriptions)).fill_null("no-match")
print(dfx)


'''
$ python3 dataframe-cidr-test.py
shape: (3, 2)
┌─────────────┬────────────┐
│ ip          ┆ hostname   │
│ ---         ┆ ---        │
│ str         ┆ str        │
╞═════════════╪════════════╡
│ 10.1.2.3    ┆ bob-pc     │
│ 192.168.1.2 ┆ alice-pc   │
│ 99.99.99.99 ┆ unknown-pc │
└─────────────┴────────────┘
shape: (3, 2)
┌────────────────┬───────────────┐
│ network        ┆ description   │
│ ---            ┆ ---           │
│ str            ┆ str           │
╞════════════════╪═══════════════╡
│ 10.0.0.0/8     ┆ east-coast    │
│ 192.168.0.0/16 ┆ west-coast    │
│ 172.16.0.0/12  ┆ private-space │
└────────────────┴───────────────┘
shape: (3, 3)
┌─────────────┬────────────┬─────────────┐
│ ip          ┆ hostname   ┆ description │
│ ---         ┆ ---        ┆ ---         │
│ str         ┆ str        ┆ str         │
╞═════════════╪════════════╪═════════════╡
│ 10.1.2.3    ┆ bob-pc     ┆ east-coast  │
│ 192.168.1.2 ┆ alice-pc   ┆ west-coast  │
│ 99.99.99.99 ┆ unknown-pc ┆ no-match    │
└─────────────┴────────────┴─────────────┘
'''
