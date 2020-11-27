#!/usr/bin/python3

import requests
from requests import Request, Session

#
# UN-COMMENT ONE BLOCK AT A TIME TO SEE IT IN ACTION
# http://docs.python-requests.org/en/master/user/quickstart/
# http://docs.python-requests.org/en/master/user/advanced/
# ALWAYS HAVE A TIMEOUT FOR YOUR REQUESTS
#

#=============
# set custom headers
#=============
heady={
	'User-Agent': 'python_requests_test_ua'
}
## or in-line
## r = requests.get('https://www.google.com', headers={'User-Agent':'CustomUA'}, timeout=1.0)

#=============
# basic GET request/response
#=============
## simple request (won't print on screen but it will generate req/resp traffic)
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
