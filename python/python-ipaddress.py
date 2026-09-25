#!/usr/bin/env python3


# see docs for teredo, sixtofour, and more
# https://docs.python.org/3/library/ipaddress.html
import ipaddress


ip = ipaddress.ip_address("192.168.1.1")
ip2 = ipaddress.ip_address("10.10.10.10")


print(f"{ip.compressed=}")
print(f"{ip.exploded=}")
print(f"{ip.is_global=}")
print(f"{ip.is_link_local=}")
print(f"{ip.is_loopback=}")
print(f"{ip.is_multicast=}")
print(f"{ip.is_private=}")
print(f"{ip.is_reserved=}")
print(f"{ip.is_unspecified=}")
print(f"{ip.max_prefixlen=}")
print(f"{ip.packed=}")
print(f"{ip.reverse_pointer=}")
print(f"{ip.version=}")
print()


net = ipaddress.IPv4Network("10.0.0.0/8")
# also has above is_* attributes


print(f"{str(net.network_address)=}")
print(f"{str(net.broadcast_address)=}")
print(f"{str(net.hostmask)=}")
print(f"{str(net.netmask)=}")
print(f"{net.with_prefixlen=}")
print(f"{net.compressed=}")
print(f"{net.exploded=}")
print(f"{net.with_netmask=}")
print(f"{net.with_hostmask=}")
print(f"{net.num_addresses=}")
print(f"{net.prefixlen=}")
print(f"{net.hosts()=}")
print()


net2 = ipaddress.IPv4Network("10.10.0.0/16")


print(f"{net=}, {net2=}")
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
ip.compressed='192.168.1.1'
ip.exploded='192.168.1.1'
ip.is_global=False
ip.is_link_local=False
ip.is_loopback=False
ip.is_multicast=False
ip.is_private=True
ip.is_reserved=False
ip.is_unspecified=False
ip.max_prefixlen=32
ip.packed=b'\xc0\xa8\x01\x01'
ip.reverse_pointer='1.1.168.192.in-addr.arpa'
ip.version=4

str(net.network_address)='10.0.0.0'
str(net.broadcast_address)='10.255.255.255'
str(net.hostmask)='0.255.255.255'
str(net.netmask)='255.0.0.0'
net.with_prefixlen='10.0.0.0/8'
net.compressed='10.0.0.0/8'
net.exploded='10.0.0.0/8'
net.with_netmask='10.0.0.0/255.0.0.0'
net.with_hostmask='10.0.0.0/0.255.255.255'
net.num_addresses=16777216
net.prefixlen=8
net.hosts()=<generator object _BaseNetwork.hosts at 0x7e24c1189700>

net=IPv4Network('10.0.0.0/8'), net2=IPv4Network('10.10.0.0/16')
net overlaps with net2 True
net2 overlaps with net True
net is a subnet of net2 False
net2 is a subnet of net True
net is a supernet of net2 True
net2 is a supernet of net False

True
'''
