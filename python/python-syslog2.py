#!/usr/bin/env python3

# test a single server, or a comma-delimited string of servers
# syslog-tester.py server1 514
# syslog-tester.py server1,server2,server3 514

import logging
import sys
import time
from datetime import datetime, timezone
import logging.handlers

try:
	serverstring = sys.argv[1]
	port = int(sys.argv[2])
except:
	print()
	print("USAGE:")
	print(f"\t{sys.argv[0]} server1[,server2,server3,etc] portnumber")
	print()
	sys.exit(1)

servers = serverstring.split(",")
my_logger = logging.getLogger("SyslogLogger")
for server in servers:
	handler = logging.handlers.SysLogHandler(address=(server,port))
	my_logger.addHandler(handler)

while True:
	d = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"
	my_logger.critical(d)
#	my_logger.error(d)
#	my_logger.warning(d)
#	my_logger.info(d)
#	my_logger.debug(d)
	time.sleep(1)
