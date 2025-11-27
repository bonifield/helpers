#!/usr/bin/env python3


# see docs for teredo, sixtofour, and more
# https://docs.python.org/3/library/ipaddress.html
import ipaddress


ip = ipaddress.ip_address("192.168.1.1")
ip2 = ipaddress.ip_address("10.10.10.10")


print("compressed", ip.compressed)
print("exploded", ip.exploded)
print("is_global", ip.is_global)
print("is_link_local", ip.is_link_local)
print("is_loopback", ip.is_loopback)
print("is_multicast", ip.is_multicast)
print("is_private", ip.is_private)
print("is_reserved", ip.is_reserved)
print("is_unspecified", ip.is_unspecified)
print("max_prefixlen", ip.max_prefixlen)
print("packed", ip.packed)
print("reverse_pointer", ip.reverse_pointer)
print("version", ip.version)
print()


net = ipaddress.IPv4Network("10.0.0.0/8")
# also has above is_* attributes


print("network_address", net.network_address)
print("broadcast_address", net.broadcast_address)
print("hostmask", net.hostmask)
print("netmask", net.netmask)
print("with_prefixlen", net.with_prefixlen)
print("compressed", net.compressed)
print("exploded", net.exploded)
print("with_netmask", net.with_netmask)
print("with_hostmask", net.with_hostmask)
print("num_addresses", net.num_addresses)
print("prefixlen", net.prefixlen)
print("hosts() generator", net.hosts())
print()


net2 = ipaddress.IPv4Network("10.10.0.0/16")


print(f"net: {net}, net2: {net2}")
print("net overlaps with net2", net.overlaps(net2))
print("net2 overlaps with net", net2.overlaps(net))
print("net is a subnet of net2", net.subnet_of(net2))
print("net2 is a subnet of net", net2.subnet_of(net))
print("net is a supernet of net2", net.supernet_of(net2))
print("net2 is a supernet of net", net2.supernet_of(net))
print()


def check_cidr(ip: str, cidr: str) -> bool:
	"""Returns True if an IP address is within a given CIDR netblock."""
	return ipaddress.ip_address(ip) in ipaddress.ip_network(cidr)


print(check_cidr(ip2, net2))


'''
compressed 192.168.1.1
exploded 192.168.1.1
is_global False
is_link_local False
is_loopback False
is_multicast False
is_private True
is_reserved False
is_unspecified False
max_prefixlen 32
packed b'\xc0\xa8\x01\x01'
reverse_pointer 1.1.168.192.in-addr.arpa
version 4

network_address 10.0.0.0
broadcast_address 10.255.255.255
hostmask 0.255.255.255
netmask 255.0.0.0
with_prefixlen 10.0.0.0/8
compressed 10.0.0.0/8
exploded 10.0.0.0/8
with_netmask 10.0.0.0/255.0.0.0
with_hostmask 10.0.0.0/0.255.255.255
num_addresses 16777216
prefixlen 8
hosts() generator <generator object _BaseNetwork.hosts at 0x71fea9cb2c70>

net: 10.0.0.0/8, net2: 10.10.0.0/16
net overlaps with net2 True
net2 overlaps with net True
net is a subnet of net2 False
net2 is a subnet of net True
net is a supernet of net2 True
net2 is a supernet of net False

True
'''
