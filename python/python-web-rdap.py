#!/usr/bin/env python3

# python3 -m pip install whoisit

import json
import whoisit
# query IANA for RDAP servers
whoisit.bootstrap()

ip = "8.8.8.8"
domain = "google.com"

i = whoisit.ip("8.8.8.8")
print(type(i))
print(i)

print()
print()

d = whoisit.domain("google.com")
print(type(d))
print(d)

'''
whois.asn
whois.domain
whois.ip (single, CIDR, IPv6)
whois.entity
'''
