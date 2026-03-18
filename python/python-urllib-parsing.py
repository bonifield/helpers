#!/usr/bin/env python3


#===========================
# https://docs.python.org/3/library/html.html
# https://docs.python.org/3/library/urllib.parse.html
#===========================


import os
from html import escape
from html import unescape
from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import quote_plus
from urllib.parse import unquote_plus
from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import urlparse


#=============
# interesting strings
#=============


s = "'<script>alert(1);</script>"
e = "%27%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E"


#=============
# quote / unquote / quote_plus / unquote_plus
#=============


q = quote(s)
print("quote\n\t", q) # %27%3Cscript%3Ealert%281%29%3B%3C/script%3E

q = quote(s, safe='')
print("quote nosafe\n\t", q) # %27%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E

q = unquote(q)
print("unquote\n\t", q) # '<script>alert(1);</script>

q = quote_plus(s)
print("quote_plus\n\t", q) # %27%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E

q = unquote_plus(q)
print("unquote_plus\n\t", q) # '<script>alert(1);</script>


#=============
# escape / unescape
#=============


print("escape\n\t", escape(s, quote=True)) # &lt;script&gt;alert(1);&lt;/script&gt;
print("unescape\n\t", unescape(e)) # %3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E


#=============
# urlencode / url "decode" (qs/qsl)
#=============


vars = {"key1":"val1", "key2":"val2"}
n = urlencode(vars)
print("urlencode\n\t", n) # key1=val1&key2=val2

x = quote_plus(n)
print("urlencode with quote_plus\n\t", x) # key1%3Dval1%26key2%3Dval2

dd = parse_qs(n) # {'key1': ['val1'], 'key2': ['val2']}
print("qs\n\t", dd)

ddd = parse_qsl(n) # [('key1', 'val1'), ('key2', 'val2')]
# qsl is reversible, can urlencode() directly from this object
print("qsl\n\t", ddd)


#=============
# urlparse
#=============


u = urlparse("https://myusername:mypassword@www.mywebsite.local:443/search?client=firefox-b-1-d&q=reddit&%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E")

print("full url\n\t", u.geturl())
print("filename\n\t", os.path.basename(u.path))
print("result tuple\n\t", u)
print("scheme\n\t", u.scheme)
# the full portion between the schema and path
print("netloc\n\t", u.netloc)
# just the domain, excluding username, password, and port
print("hostname\n\t", u.hostname)
print("path\n\t", u.path)
print("params\n\t", u.params)
print("query\n\t", u.query)
print("fragment\n\t", u.fragment)
print("username\n\t", u.username)
print("password\n\t", u.password)
print("port\n\t", u.port)


#=============
# function to decode punycode
#=============


def convert_punycode(ioc):
	"""International punycode checks; searches each character individually and decodes the IOC if needed."""
	is_it_punycode = False
	for char in ioc:
		#if not re.search("[A-Za-z0-9.-]", char):
		if ord(char) > 127:
			is_it_punycode = True
	if is_it_punycode:
		try:
			ioc = ioc.encode("idna").decode().strip()
		except Exception as e:
			#print(str(e))
			pass
	return ioc


# example domain, just a copy paste of text from NHK with .com appended
intl_domain = "NHKやさしいことばニュース.com"
puny_domain = convert_punycode(intl_domain)
print(puny_domain) # xn--nhk-u63b1cko2lyc6jrwxgom6k.com
