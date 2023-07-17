#!/usr/bin/env python3

# python3 -m pip install python-whois

import json
from whois import whois

ip = "8.8.8.8"
domain = "google.com"

i = whois(ip)
print(i.country)
print(i)

d = whois(domain)
print(d.country)
print(d)
