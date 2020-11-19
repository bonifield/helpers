#!/usr/bin/python3

# Usage: python-syslog.py [ip] [port]
# https://en.wikipedia.org/wiki/Syslog
# https://docs.python.org/3/library/logging.html
# https://stackoverflow.com/questions/38907637/quick-remote-logging-system

import logging, sys, time
import logging.handlers

# define destination info
target_address = sys.argv[1]
target_port = int(sys.argv[2])

# create a logger object
my_logger = logging.getLogger('SyslogLogger')
# ignore everything below "DEBUG" level
#my_logger.setLevel(logging.DEBUG)

# create a "handler" for sending logs
handler = logging.handlers.SysLogHandler(address = (target_address,target_port))
# add the handler created above to the logger object
my_logger.addHandler(handler)

# various severity levels
my_logger.critical('test critical')
time.sleep(1)
my_logger.error('test error')
time.sleep(1)
my_logger.warning('test warning')
time.sleep(1)
my_logger.info('test info')
time.sleep(1)
my_logger.debug('test debug')
