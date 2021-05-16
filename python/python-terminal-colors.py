#!/usr/bin/python3
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
# https://stackoverflow.com/questions/17439482/how-to-make-a-text-blink-in-shell-script
# https://en.wikipedia.org/wiki/ANSI_escape_code#Colors

class tcol:
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	GOLD = '\033[33m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	STRIKE = '\033[9m'
	UNDERLINE = '\033[4m'
	BGPURPLE = '\033[95;7m'
	BGBLUE = '\033[94;7m'
	BGGREEN = '\033[92;7m'
	BGYELLOW = '\033[93;7m'
	BGGOLD = '\033[33;7m'
	BGRED = '\033[91;7m'
	RESET = '\033[0m'

print()
print(tcol.PURPLE + "purple" + tcol.RESET)
print(tcol.BLUE + "blue" + tcol.RESET)
print(tcol.GREEN + "green" + tcol.RESET)
print(tcol.YELLOW + "yellow" + tcol.RESET)
print(tcol.GOLD + "gold" + tcol.RESET)
print(tcol.RED + "red" + tcol.RESET)
print(tcol.BOLD + "bold" + tcol.RESET)
print(tcol.STRIKE + "strike" + tcol.RESET)
print(tcol.UNDERLINE + "underline" + tcol.RESET)
print(tcol.BGPURPLE + "bgpurple" + tcol.RESET)
print(tcol.BGBLUE + "bgblue" + tcol.RESET)
print(tcol.BGGREEN + "bggreen" + tcol.RESET)
print(tcol.BGYELLOW + "bgyellow" + tcol.RESET)
print(tcol.BGGOLD + "bggold" + tcol.RESET)
print(tcol.BGRED + "bgred" + tcol.RESET)
print(tcol.RESET + "reset" + tcol.RESET)
print()

for i in range(1,111):
	print('\033[{}m'.format(str(i))+str(i)+'\033[0m')

print()
