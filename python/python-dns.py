#!/usr/bin/python3

# looks up name servers, gets A records, and can attempt zone transfers
# python3 -m pip install dnspython

import sys
import dns.query
import dns.zone
import dns.resolver

try:
	domain = str(sys.argv[1]).strip()
except:
	print("USAGE:\tpython3 dns-azt.py DOMAIN [zt]")
	print("\tpython3 dns-azt.py megacorpone.com")
	print("\tpython3 dns-azt.py megacorpone.com zt")
	sys.exit(1)

# (quick and dirty) add "zt" to the command line to attempt zone transfer
try:
	do_zt = str(sys.argv[2]).strip()
	if do_zt == "zt":
		do_zt = True
except:
	do_zt = False
	pass

def getARecord(domain) -> str:
	# returns a string, that may be comma-separated, of network addresses
	resolver = dns.resolver.Resolver()
	resolved = resolver.resolve(domain, "A")
	x = ""
	for r in resolved:
		x += ','.join([str(r)])
	#return(resolved)
	return(x)

def getNameservers(domain) -> dict:
	# returns a dictionary of nameservers and their IPs
	try:
		# dns.resolver.resolve() returns a list-like iterable
		n = [str(i).rstrip(".").strip() for i in dns.resolver.resolve(domain, 'NS')]
		d = {}
		# iterate over the hosts "n", add them to the dict as keys, and set their values to the resolved IPs
		for x in n:
			d[x] = getARecord(x)
		return(d)
	except Exception as e:
		print(str(e))
		return(None)

def zoneTransfer(nameserver, domain) -> dict:
	# returns a dictionary of nameservers and the hosts they reveal
	d = {}
	try:
		zone = dns.zone.from_xfr(dns.query.xfr(nameserver, domain))
	except Exception as e:
		print(str(e))
		return(None)
	for subdomain in zone:
		if str(subdomain) != '@':
			# combine subdomain back into full domain format
			h = str(subdomain)+"."+domain
			# add host as a key and resolved IPs as values
			d[h] = getARecord(h)
	return(d)

if __name__ == "__main__":
	nameservers = getNameservers(domain) # dict of name servers and their IPs
	print(nameservers)
	if do_zt:
		for nsrv in nameservers:
			print(f"TRYING {nsrv}")
			# future examples: nest found items under the nameserver as key
			z = zoneTransfer(nameservers[nsrv], domain)
			if z:
				if len(z) > 0:
					print(z)
