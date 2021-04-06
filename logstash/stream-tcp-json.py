#!/usr/bin/python3

#
# stream a JSON file to Logstash via TCP socket (use with tcp9088-json-streaming.conf)
#

import json, socket, sys

try:
	INPUTJSONFILE = sys.argv[1]
	HOST = str(sys.argv[2])
	PORT = int(sys.argv[3])
except:
	print()
	print("stream-tcp-json.py file.json LogstashHost LogstashPort")
	print()
	sys.exit(1)

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
	m = "[ERROR1] {}\n".format(msg)
	sys.stderr.write(m)
	sys.exit(1)

try:
	sock.connect((HOST, PORT))
except socket.error as msg:
	m = "[ERROR2] {}\n".format(msg)
	sys.stderr.write(m)
	sys.exit(2)

with open(INPUTJSONFILE, "r") as o:
	c = 0
	for line in o:
		c += 1
		if len(line) > 2:
			msg = line.encode('utf-8')
			sock.send(msg)
	print("streamed {} lines".format(c))
o.close()
