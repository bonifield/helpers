#!/usr/bin/python3

import requests
from requests import Request, Session
# suppress InsecureRequestWarning from urllib3 if using verify=False to access websites using self-signed certs
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#
# UN-COMMENT ONE BLOCK AT A TIME TO SEE IT IN ACTION
# http://docs.python-requests.org/en/master/user/quickstart/
# http://docs.python-requests.org/en/master/user/advanced/
# ALWAYS HAVE A TIMEOUT FOR YOUR REQUESTS
#

#=============
# set custom headers
#=============
# as a best practice, use legit User-Agent and Accept strings, and any other "recommended" headers your customer has documented
heady = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
	'Accept': 'text/html'
}
proxy = {
	'http': 'http://127.0.0.1:8080',
	'https': 'https://127.0.0.1:8080'
}
## or in-line
## r = requests.get('https://www.google.com', headers={'User-Agent':'CustomUA'}, timeout=1.0)

#=============
# basic GET request/response
#=============
## simple request (won't print on screen but it will generate req/resp traffic)
#r = requests.get('https://www.google.com', headers=heady, proxies=proxy, timeout=1.0) # using a proxy
r = requests.get('https://www.google.com', headers=heady, timeout=1.0)

print('\n---=== Request Headers ===---')
print(r.request.headers)
print('\n---=== Response Headers ===---')
print(r.headers)
print('\n---=== Response Status Code ===---')
print(r.status_code)
print('\n---=== Response Content Type ===---')
print(r.headers['content-type'])
print('\n')
#print(r.content)
print('='*50)

#=============
# basic GET request/response using streaming data to control response body access (response body is not downloaded until .content attribute is called, also preserves raw socket information)
#	https://docs.python-requests.org/en/master/user/advanced/#body-content-workflow
# access redirect/history objects (stream does not impact this)
# use no TLS/SSL validation (just an example, Google most definitely uses signed certificates)
# get the IP address (ONLY works with stream=True due to preserving socket info)
#=============
# will be redirected from http://google.com --> http://www.google.com --> https://www.google.com/?gws_rd=ssl
r = requests.get('http://google.com', headers=heady, timeout=1.0, stream=True, allow_redirects=True, verify=False)
# access raw socket information BEFORE any calls to .content
#	ONLY works with stream=True because the connection is held open until .content is called, hence the socket information is still available, but then once .content is called the socket info gets dumped
# returns an IP/port tuple
# note if using proxies, the IP/port will be the proxy info, not the true remote IP address
ip = r.raw._fp.fp.raw._sock.getpeername()
# if the history iterable exists, access each item individually (note this does not include the most recent website / final landing page)
if r.history:
	for h in r.history:
		print(h.status_code, h.url)
print(r.status_code, ip, r.url)
r.close()
# ALWAYS close a streaming connection
# or wrap it in a "with" statement, such as
# with requests.get('http://google.com', stream=True) as r: ...

#=============
# prepared requests
#=============
#s = Session()
#r = requests.Request('GET', 'https://www.google.com', headers=heady)
#p = r.prepare()
#resp = s.send(p, timeout=1.0)
#print(resp.request.headers)
#print(resp.status_code)

#=============
# headers
#=============
#r = requests.get('https://www.google.com', headers=heady, timeout=1.0)
## request headers
#print(r.request.headers)
## response headers
#print(r.headers)

#=============
# redirects
#=============
## no redirects
#r = requests.get('http://github.com', allow_redirects=False, headers=heady, timeout=1.0)
#print r.status_code
#print r.history
## with redirects
#r = requests.get('http://github.com', allow_redirects=True, headers=heady, timeout=1.0)
#print(r.url)
#print(r.status_code)
#print(r.history)

#=============
# check content encoding (if expecting text)
#=============
## use r.content to find encoding
## r.encoding = 'UTF-8'

#=============
# binary response data (images etc)
#=============
#from PIL import Image
#from io import BytesIO
#r = requests.get('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')
#i = Image.open(BytesIO(r.content))
#i.save('/home/user/googlelogo_color_272x92dp.png')

#=============
# json response content
#=============
## use r.status_code to check for a proper response code and r.raise_for_status() (None means it isn't returing json)
#r = requests.get('http://api.github.com/events', headers=heady, timeout=1.0)
#print(r.status_code)
#print(r.raise_for_status())
#print(r.json())

#=============
# raw response content
#=============
## must set stream=True
## use a with open...  file.write() block for effective use of this
#r = requests.get('http://api.github.com/events', headers=heady, stream=True, timeout=1.0)
#for chunk in r.iter_content(chunk_size=128):
#	print(chunk)
#	print()

#=============
# pass parameters in url
#=============
#payload = {'key1':'val1', 'key2':'val2', 'key3':['val33', 'val44']}
#r = requests.get('http://httpbin.org/get', params=payload, headers=heady, timeout=1.0)
#print(r.url)
#print(r.headers)
#print(r.content)

#=============
# POST requests
#=============
## data instead of params - data can pass tuples, if a form has multiple elements using the same key
#payload = {'key1':'val1', 'key2':'val2', 'key3':['val33', 'val44']} # DICT WITH DIFFERENT KEYS
#payload = (('key1','value1'), ('key1', 'value2')) # TUPLE WITH SAME KEY
#r = requests.post('http://httpbin.org/post', data=payload, headers=heady, timeout=1.0)
#print(r.text)
#print(r.json())

#=============
# JSON as URL payload 
#=============
## requires import json
#url = 'https://www.google.com'
#payload = {'some':'data'}
#r = requests.post(url, data=json.dumps(payload), headers=heady, timeout=1.0)
#print(r.text)
