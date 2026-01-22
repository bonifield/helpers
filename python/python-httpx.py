#!/usr/bin/env python3


# uv add httpx
import asyncio
import json
import os
import httpx
from httpx import BasicAuth


# local Flask app for testing
#url = "https://www.google.com"
url = "https://127.0.0.1:5000"
json_url = "https://127.0.0.1:5000/json"
post_url = "https://127.0.0.1:5000/validate"
# simulate a large file download
cloudflare_url = "https://speed.cloudflare.com/__down?bytes=10000000"
headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0"
}
data = {"api_key":"my_value"}


# simple GET request without the client
# default timeout is 5 seconds, use a float or None for the
#   timeout value
print(" GET output ".center(50, "="))
resp = httpx.get(url, verify=False, timeout=10.0)
print(" status code and headers ".center(50, "="))
print(resp.status_code)
print(resp.headers)
if resp.headers.get("server"):
	print(resp.headers["server"])
print(" response body content ".center(50, "="))
print(resp.content)
print(" response body text ".center(50, "="))
print(resp.text)
# can also resp.raise_for_status()


# POST (can also PUT, DELETE, etc)
print(" POST (JSON upload) output ".center(50, "="))
#data_post_resp = httpx.post(post_url, data=data, verify=False)
json_post_resp = httpx.post(post_url, json=data, verify=False)
print(json_post_resp.text)


# using the client
print(" using Client() ".center(50, "="))
with httpx.Client(verify=False) as client:
	# get the JSON URL
	resp = client.get(
		json_url,
		headers=headers,
		follow_redirects=True
	)
	print(type(resp.text), resp.text)
	# load into dict
	print(type(resp.json()), resp.json())


# async
print(" using AsyncClient() ".center(50, "="))
async def areq():
	async with httpx.AsyncClient(verify=False) as client:
		resp = await client.get(url)
		print("async function output:", resp.text)

asyncio.run(areq())


# download a large file
# iter_bytes() lets RAM usage stay consistently
# https://www.python-httpx.org/advanced/clients/
print(" download a large file ".center(50, "="))
print(f"downloading {cloudflare_url}")
with httpx.stream("GET", cloudflare_url) as resp:
	with open("large_file.dat", "wb") as f:
		for chunk in resp.iter_bytes():
			f.write(chunk)
			#print("downloaded and wrote a chunk")

print("downloaded file size is: ", os.path.getsize("large_file.dat"))
print("removing file")
os.remove("large_file.dat")


# other options
'''
# basic auth; pairs well with dotenv :)
auth = BasicAuth("my_username", "my_password")
resp = httpx.get(url+"/auth", verify=False, auth=auth)

# use a client with headers and options
client = httpx.Client(headers={"Authorization": "Bearer API_TOKEN"}, verify=False)

# proxies
# from the documentation:
# In most cases, the proxy URL for the https:// key should use
#   the http:// scheme (that's not a typo!).

proxies = {
	"http://": "http://localhost:8030",
	"https://": "http://localhost:8031",
}
client = httpx.Client(proxies=proxies)
# or
client = httpx.Client(proxies="http://localhost:8031")

# proxy mounts (copied from documentation)
proxy_mounts = {
	"http://": httpx.HTTPTransport(proxy="http://localhost:8030"),
	"https://": httpx.HTTPTransport(proxy="http://localhost:8031"),
}
with httpx.Client(mounts=proxy_mounts) as client:
	...

# proxy authentication
with httpx.Client(proxy="http://username:password@localhost:8030") as client:
	...
'''


# expected output
'''
=================== GET output ===================
============ status code and headers =============
200
Headers({'server': 'Werkzeug/3.1.5 Python/3.13.11', 'date': 'Thu, 22 Jan 2026 22:34:10 GMT', 'content-type': 'text/html; charset=utf-8', 'content-length': '37', 'connection': 'close'})
Werkzeug/3.1.5 Python/3.13.11
============= response body content ==============
b'Hello, world! This is a plain string.'
=============== response body text ===============
Hello, world! This is a plain string.
=========== POST (JSON upload) output ============
{"status": "valid"}
================= using Client() =================
<class 'str'> {"message": "Hello, world!", "message_type": "This is a JSON structure."}
<class 'dict'> {'message': 'Hello, world!', 'message_type': 'This is a JSON structure.'}
============== using AsyncClient() ===============
async function output: Hello, world! This is a plain string.
============= download a large file ==============
downloading https://speed.cloudflare.com/__down?bytes=10000000
downloaded file size is:  10000000
removing file
'''
