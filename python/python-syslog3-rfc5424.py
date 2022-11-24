#!/usr/bin/python3

# basic rfc5424 formatter
# https://www.ietf.org/rfc/rfc5424.txt
#
# manual testing with https://github.com/bonifield/helpers/raw/master/logstash/conf.d/syslog-rfc5424-input.conf
#	sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/syslog-rfc5424-input.conf --config.test_and_exit
#	sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/syslog-rfc5424-input.conf --config.reload.automatic
#	python3 python-syslog3-rfc5424.py 127.0.0.1 514
#
# test a single server, or a comma-delimited string of servers
# syslog-tester.py server1 514
# syslog-tester.py server1,server2,server3 514

import logging
import os
import socket
import sys
import time
import uuid
from datetime import datetime
import logging.handlers

try:
	serverstring = sys.argv[1]
	port = int(sys.argv[2])
	servers = serverstring.split(",")
except:
	print()
	print("USAGE:")
	print(f"\t{sys.argv[0]} server1[,server2,server3,etc] portnumber")
	print()
	sys.exit(1)

my_logger = logging.getLogger("LoggerName")
for server in servers:
	handler = logging.handlers.SysLogHandler(address=(server,port))
	my_logger.addHandler(handler)

try:
	user = str(os.environ.get('USER'))
except:
	user = "-"

try:
	hostname = socket.gethostname()
except:
	hostname = "-"

# loop over various severities for testing on the remote server
while True:
	now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"
	appname = "someapp"
	try:
		procid = os.getpid()
	except:
		procid = "-"
	msgid = str(uuid.uuid4())
	structured_data = "[sip=a.b.c.d dip=e.f.g.h]"
	msg = "this is the message contents"
	d = f"{now} {hostname} {appname}: {procid} {msgid} {structured_data} {msg}"
	print(d)
	#
	my_logger.critical(d) # 50
	time.sleep(0.25)
	my_logger.error(d) # 40
	time.sleep(0.25)
	my_logger.warning(d) # 30
	time.sleep(0.25)
	my_logger.info(d) # 20
	time.sleep(0.25)
	my_logger.debug(d) # 10
	time.sleep(0.25)
