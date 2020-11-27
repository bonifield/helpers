#!/usr/bin/python3
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
# https://stackoverflow.com/questions/17439482/how-to-make-a-text-blink-in-shell-script
# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

class tcol:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	BOLD = '\033[1m'
	STRIKE = '\033[9m'
	UNDERLINE = '\033[4m'
	BGGOLD = '\033[33;7m'
	BGYELLOW = '\033[93;7m'
	BGRED = '\033[91;7m'
	BGBLUE = '\033[94;7m'
	BGGREEN = '\033[92;7m'
	RESET = '\033[0m'

print()
print(tcol.HEADER + "header" + tcol.RESET)
print(tcol.OKBLUE + "okblue" + tcol.RESET)
print(tcol.OKGREEN + "okgreen" + tcol.RESET)
print(tcol.WARNING + "warning" + tcol.RESET)
print(tcol.FAIL + "fail" + tcol.RESET)
print(tcol.BOLD + "bold" + tcol.RESET)
print(tcol.STRIKE + "strike" + tcol.RESET)
print(tcol.UNDERLINE + "underline" + tcol.RESET)
print(tcol.BGGOLD + "bggold" + tcol.RESET)
print(tcol.BGYELLOW + "bgyellow" + tcol.RESET)
print(tcol.BGRED + "bgred" + tcol.RESET)
print(tcol.BGBLUE + "bgblue" + tcol.RESET)
print(tcol.BGGREEN + "bggreen" + tcol.RESET)
print(tcol.RESET + "reset" + tcol.RESET)
print()

for i in range(1,111):
	print('\033[{}m'.format(str(i))+str(i)+'\033[0m')

print()
