#!/usr/bin/env python3

# https://pypi.org/project/python-whois/
# uv add python-whois (import "whois")

import json
import whois

# sadly, python-whois does not support IPs; use MaxMind instead
#ip = "8.8.8.8"
domain = "google.com"

d = whois.whois(domain)
print(d.__dict__)
