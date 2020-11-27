#! /usr/bin/python3


#
# get interface and put that interface into monitor mode
#	sudo airmon-ng
#	sudo airmon-ng check kill
#	sudo airmon-ng start INTERFACE
#
# note the airmon-ng suite is much better suited for
# wifi tasks than custom python/scapy solutions
#


import json, logging, sys, time
# disable the Scapy IPv6 warning, must go above Scapy import
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


interface = "INTERFACE-GOES-HERE"
types = {"00":{"description":"management", "subtype": {"0000": {"description": "Association Request"},"0001": {"description": "Association Response"},"0010": {"description": "Reassociation Request"},"0011": {"description": "Reassociation Response"},"0100": {"description": "Probe Request"},"0101": {"description": "Probe Response"},"0110": {"description": "Timing Advertisement"},"0111": {"description": "Reserved"},"1000": {"description": "Beacon"},"1001": {"description": "ATIM"},"1010": {"description": "Disassociation"},"1011": {"description": "Authentication"},"1100": {"description": "Deauthentication"},"1101": {"description": "Action"},"1110": {"description": "Action No Ack (NACK)"},"1111": {"description": "Reserved"}}},"01":{"description":"control", "subtype": {"0000": {"description": "Reserved"},"0001": {"description": "Reserved"},"0010": {"description": "Trigger"},"0011": {"description": "TACK"},"0100": {"description": "Beamforming Report Poll"},"0101": {"description": "VHT/HE NDP Announcement"},"0110": {"description": "Control Frame Extension"},"0111": {"description": "Control Wrapper"},"1000": {"description": "Block Ack Request (BAR)"},"1001": {"description": "Block Ack (BA)"},"1010": {"description": "PS-Poll"},"1011": {"description": "RTS"},"1100": {"description": "CTS"},"1101": {"description": "ACK"},"1110": {"description": "CF-End"},"1111": {"description": "CF-End + CF-ACK"}}},"10":{"description":"data", "subtype": {"0000": {"description": "Data"},"0001": {"description": "Data + CF-ACK"},"0010": {"description": "Data + CF-Poll"},"0011": {"description": "Data + CF-ACK + CF-Poll"},"0100": {"description": "Null (no data)"},"0101": {"description": "CF-ACK (no data)"},"0110": {"description": "CF-Poll (no data)"},"0111": {"description": "CF-ACK + CF-Poll (no data)"},"1000": {"description": "QoS Data"},"1001": {"description": "QoS Data + CF-ACK"},"1010": {"description": "QoS Data + CF-Poll"},"1011": {"description": "QoS Data + CF-ACK + CF-Poll"},"1100": {"description": "QoS Null (no data)"},"1101": {"description": "Reserved"},"1110": {"description": "QoS CF-Poll (no data)"},"1111": {"description": "QoS CF-ACK + CF-Poll (no data)"}}},"11":{"description":"extension", "subtype": {"0000": {"description": "DMG Beacon"},"0001": {"description": "S1G Beacon"},"0010": {"description": "Reserved"},"0011": {"description": "Reserved"},"0100": {"description": "Reserved"},"0101": {"description": "Reserved"},"0110": {"description": "Reserved"},"0111": {"description": "Reserved"},"1000": {"description": "Reserved"},"1001": {"description": "Reserved"},"1010": {"description": "Reserved"},"1011": {"description": "Reserved"},"1100": {"description": "Reserved"},"1101": {"description": "Reserved"},"1110": {"description": "Reserved"},"1111": {"description": "Reserved"}}}}
clientOnlySubTypes = ["0000", "0010", "0100"] # these are only sent by clients; 0000=Association Request, 0010=Reassociation Request, 0100=Probe Request


def basicInfo(pkt):
	try:
		# make a holding dictionary
		d = {
			"time":"",
			"type":"",
			"typeName":"",
			"subType":"",
			"subTypeName":"",
			"rx": "",
			"tx": "",
			"bssid": "",
			"ssid": ""
		}
		# get packet information
		ptime = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.localtime(pkt.time))
		type = str(bin(pkt.type)[2:].zfill(2))
		typeName = types[type]["description"]
		subType = str(bin(pkt.subtype)[2:].zfill(4))
		subTypeName = types[type]["subtype"][subType]["description"]
		a1 = pkt.addr1 # destination/receiving address
		a2 = pkt.addr2 # source/transmitting address
		a3 = pkt.addr3 # base station ID (BSSID)
		ssid = str(pkt.info.decode("utf-8"))
		# assign to the dictionary
		d["time"] = ptime
		d["type"] = type
		d["typeName"] = typeName
		d["subType"] = subType
		d["subTypeName"] = subTypeName
		d["rx"] = a1
		d["tx"] = a2
		d["bssid"] = a3
		d["ssid"] = ssid
		# dump dictionary as JSON
#		j = json.dumps(d)
		j = json.dumps(d, indent=4, sort_keys="True")
		print(j)
		# below is from SANS
		# https://www.sans.org/blog/special-request-wireless-client-sniffing-with-scapy/
#		if type == "00": # management
#			if subType in clientOnlySubTypes:
#				j = json.dumps(d, indent=4, sort_keys="True")
#				print(j)
	except Exception as e:
#		print(e)
		# skip over any packets that do not have the fields we want
		# in practice, ascertain what you fully want and do not use a try/except+pass statement
		pass


if __name__ == "__main__":
	sniff(iface=interface, prn=basicInfo)
