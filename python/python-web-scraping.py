#!/usr/bin/python3

# sudo apt install chromium-chromedriver
# pip3 install selenium selenium-wire beautifulsoup4 lxml html5lib

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#	lxml = very fast, lenient; use bs(content, 'lxml') for html parsing or 'lxml-xml'/'xml' for xml parsing
#	html5lib = very slow, extremely lenient, parses like a browser; use bs(content, 'html5lib')
# https://pypi.org/project/selenium-wire/
#	request.headers and response.headers are both case-insensitive "dictionary-like object(s) of headers"




#from selenium import webdriver
from seleniumwire import webdriver # allows header inspection
from bs4 import BeautifulSoup as bs
import json, requests
from urllib.parse import urlparse




#================================================
# using Selenium-Wire and Chromium
#================================================

#-------------
# set URL and User-Agent
#-------------
URL = "https://www.google.com/"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"

#-------------
# set Chromium options
#-------------
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--user-agent="{}"'.format(UA))

#-------------
# fetch content and store page data in "source_code"
#-------------
driver = webdriver.Chrome(chrome_options=options)
source = driver.get(URL)
source_code = driver.page_source

#-------------
# get headers for each captured item in chronological order, and first 50 bytes of the body
#-------------
for request in driver.requests:
	print("\n"+"="*100+"\n")
	req = {**request.headers} # headers are "dictionary-like"
	res = {**request.response.headers} # headers are "dictionary-like"
	print("REQUESTED URL", request.url)
	print("\t\tPARSED VIA urllib.parse", urlparse(request.url))
	print()
	print("\t\tREQUEST HEADERS",)
	for k,v in req.items():
		print("\t\t\t"+k+": "+v)
	print()
	print("\t\tSTATUS CODE", request.response.status_code, "REASON", request.response.reason)
	print()
	print("\t\tRESPONSE HEADERS",)
	for k,v in res.items():
		print("\t\t\t"+k+": "+v)
	print()
	lenb = len(request.response.body)
	print("\t\tBODY LENGTH", str(lenb)+" bytes")
	print()
	if lenb >= 50:
		print("\t\tFIRST 50 BODY BYTES")
		s = request.response.body.decode("ISO-8859-1")[:50]
		print("\t\t\t"+s)
	print()

#-------------
# parse with Beautiful Soup
#-------------
soup = bs(source_code,'lxml')
#print(soup.prettify())
# extract all "href" attributes from <a> tags and make a unique list
a_links = soup.find_all('a')
a_list = []
for a in a_links:
	a_list.append(a.get("href"))
a_list = list(set(a_list))
print(len(a_list), a_list)

print("\n"*4)




#================================================
# using Python
#================================================

#-------------
# set URL and header options via dictionary
#-------------
URL = "https://www.uber.com/"
heady={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
	'Accept': 'text/html'
}

#-------------
# fetch content and store page data in "c"
#-------------
r = requests.get(URL, headers=heady, allow_redirects=True)
c = r.content

#-------------
# get headers
#-------------
for k,v in r.request.headers.items():
	print(k+": "+v)
print()
print(r.status_code)
for k,v in r.headers.items():
	print(k+": "+v)
print()

#-------------
# request history
#-------------

if r.history:
	for h in r.history:
		print(h)

#-------------
# parse with Beautiful Soup
#-------------
soup = bs(c, "html5lib")
#print(soup.prettify())



'''
#================================================
# extras for selenium-wire
#================================================

#-------------
# intercept and spoof a referrer (note - "Referer" is the proper, albeit incorrect, usage
#-------------
def interceptor(request):
	del request.headers['Referer'] # delete the header first
	request.headers['Referer'] = 'https://www.google.com' # spoof a new referer

#-------------
# intercept and add a response header for a specific URL (takes two arguments)
#-------------
def interceptor_resp(request, response):
	if request.url == 'https://www.google.com':
		response.headers["X-New-Header"] = "Some Value"

#-------------
# intercept and add a parameter
#-------------
def interceptor_param(request):
	params = request.params
	params["foo"] = "bar"
	request.params = params

driver = webdriver.Chrome(chrome_options=options)
# if spoofing the Referer
#	driver.request_interceptor = interceptor
# if adding headers to a response from a specific URL
#	driver.response_interceptor = interceptor_resp
# if adding parameters to the request
#	driver.request_interceptor = interceptor_params
source = driver.get(URL)
source_code = driver.page_source
'''
