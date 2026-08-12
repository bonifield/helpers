#!/usr/bin/env python3


# https://loguru.readthedocs.io/en/latest/resources/migration.html
# https://realpython.com/python-loguru/


import os
import socket
import sys
from loguru import logger


hostname = socket.gethostname()
app_name = "loguru_demo_app"
proc_id = os.getpid()


#====================
# use the default logger immediately
#====================

logger.trace("trace message - severity level 5")
# trace won't show, need to use: logger.add(sys.stderr, level="TRACE")
logger.debug("debug message - severity level 10")
logger.info("info message - severity level 20")
logger.success("success message - severity level 25")
logger.warning("warning message - severity level 30")
logger.error("error message - severity level 40")
logger.critical("critical message - severity level 50")

# expected output (this is colorized)
'''
2026-08-09 15:14:43.022 | DEBUG    | __main__:<module>:23 - debug message - severity level 10
2026-08-09 15:14:43.022 | INFO     | __main__:<module>:24 - info message - severity level 20
2026-08-09 15:14:43.023 | SUCCESS  | __main__:<module>:25 - success message - severity level 25
2026-08-09 15:14:43.023 | WARNING  | __main__:<module>:26 - warning message - severity level 30
2026-08-09 15:14:43.023 | ERROR    | __main__:<module>:27 - error message - severity level 40
2026-08-09 15:14:43.023 | CRITICAL | __main__:<module>:28 - critical message - severity level 50
'''

# remove the default logger
logger.remove()


#====================
# add a custom logger that only prints INFO level or above
# - DEBUG and TRACE-level messages won't show anymore
# - level parameter values are capitalized
# - format lets you add custom messages
#====================

logger.add(
	sys.stderr,
	level="INFO",
	format="{time:YYYY-MM-DD HH:mm:ss.SSS!UTC}Z {extra[hostname]} {name}:{level}:{line} {message} {extra}",
)

# bind "extra" key/value information ("pins" the information to the logger, creates permanent context)
# can also make a new logger instead
logger = logger.bind(hostname=hostname)
# add extra info as key=value
logger.info("just informational")

# use a temporay context[ualize] to group logs together using "extra" data
with logger.contextualize(request_id="demo1234"):
	logger.info("info message 1")
	logger.info("info message 2")
	logger.info("info message 3")

logger.info("info message 4 unrelated to the previous 3 events")

# expected output
'''
2026-08-09 20:02:58.680Z demohost01 __main__:INFO:55 just informational {'hostname': 'demohost01'}
2026-08-09 20:02:58.681Z demohost01 __main__:INFO:59 info message 1 {'request_id': 'demo1234', 'hostname': 'demohost01'}
2026-08-09 20:02:58.681Z demohost01 __main__:INFO:60 info message 2 {'request_id': 'demo1234', 'hostname': 'demohost01'}
2026-08-09 20:02:58.681Z demohost01 __main__:INFO:61 info message 3 {'request_id': 'demo1234', 'hostname': 'demohost01'}
2026-08-09 20:02:58.681Z demohost01 __main__:INFO:63 info message 4 unrelated to the previous 3 events {'hostname': 'demohost01'}
'''

# remove the example logger
logger.remove()


#====================
# use a format based on RFC 5424
# <14> = priority: (user-level facility 1 * 8) + (informational severity 6)
# 1 = RFC 5424 version number
# <pri>version iso8601timestampZ hostname appname procid msgid [structureddata] message
# double-escape the less-than symbol, otherwise loguru will think it's a color markup (or use colorize=False in the logger.add() statement); single backslash will trigger a SyntaxWarning
#====================

# include Z for adherence to RFC 5424
syslog_format = (
    "\\<14>1 {time:YYYY-MM-DDTHH:mm:ss.SSS!UTC}Z {extra[hostname]} "
    f"{app_name} {proc_id} - - {{message}}"
)

logger.add(sys.stderr, level="INFO", format=syslog_format)

logger = logger.bind(hostname=hostname)
logger.info("this is an RFC 5424 formatted syslog entry")

# expected output
'''
2026-08-09 20:06:36.370Z demohost01 __main__:INFO:59 just informational {'hostname': 'demohost01'}
2026-08-09 20:06:36.370Z demohost01 __main__:INFO:63 info message 1 {'request_id': 'demo1234', 'hostname': 'demohost01'}
2026-08-09 20:06:36.370Z demohost01 __main__:INFO:64 info message 2 {'request_id': 'demo1234', 'hostname': 'demohost01'}
2026-08-09 20:06:36.370Z demohost01 __main__:INFO:65 info message 3 {'request_id': 'demo1234', 'hostname': 'demohost01'}
2026-08-09 20:06:36.371Z demohost01 __main__:INFO:67 info message 4 unrelated to the previous 3 events {'hostname': 'demohost01'}
'''


#====================
# decorator to catch exceptions and then continue the script
# uses RFC 5424 syslog logger created above
# from realpython
#====================
@logger.catch
def divide(a, b):
	return a / b

divide(10, 0)

logger.info("this log is after the divide() exception")

# expected output
'''
<14>1 2026-08-09T20:06:36.377Z demohost01 loguru_demo_app 310594 - - An error has been caught in function '<module>', process 'MainProcess' (310594), thread 'MainThread' (131678872811328):
Traceback (most recent call last):

> File "/home/user/demo/python-loguru.py", line 117, in <module>
    divide(10, 0)
    └ <function divide at 0x77c2df63e7a0>

  File "/home/user/demo/python-loguru.py", line 115, in divide
    return a / b
           │   └ 0
           └ 10

ZeroDivisionError: division by zero
<14>1 2026-08-09T20:06:36.378Z demohost01 loguru_demo_app 310594 - - this log is after the divide() exception
'''

# catch can also have messages, could set a custom string here for downstream multiline parsing
@logger.catch(message="oops, bad math")
def divide(a, b):
	return a / b

divide(10, 0)

# expected output
'''
<14>1 2026-08-09T20:06:36.378Z demohost01 loguru_demo_app 310594 - - oops, bad math
Traceback (most recent call last):

> File "/home/user/demo/python-loguru.py", line 130, in <module>
    divide(10, 0)
    └ <function divide at 0x77c2df63d4e0>

  File "/home/user/demo/python-loguru.py", line 128, in divide
    return a / b
           │   └ 0
           └ 10

ZeroDivisionError: division by zero
'''

# remove the example logger
logger.remove()


#====================
# serialize into JSON
#====================

logger.add(
	sys.stderr,
	serialize=True
)

logger.info("User logged in", user_id=123)

# expected output
'''
{"text": "2026-08-09 15:06:36.384 | INFO     | __main__:<module>:152 - User logged in\n", "record": {"elapsed": {"repr": "0:00:00.026870", "seconds": 0.02687}, "exception": null, "extra": {"hostname": "demohost01", "user_id": 123}, "file": {"name": "python-loguru.py", "path": "/home/user/demo/python-loguru.py"}, "function": "<module>", "level": {"icon": "ℹ️", "name": "INFO", "no": 20}, "line": 152, "message": "User logged in", "module": "python-loguru", "name": "__main__", "process": {"id": 310594, "name": "MainProcess"}, "thread": {"id": 131678872811328, "name": "MainThread"}, "time": {"repr": "2026-08-09 15:06:36.384341-05:00", "timestamp": 1786304396.384341}}}
'''

# remove the example logger
logger.remove()
