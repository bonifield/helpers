#!/usr/bin/env python3


# https://docs.python.org/3/library/configparser.html
#
# this script is meant to be stored locally with config.ini


from configparser import ConfigParser, BasicInterpolation, ExtendedInterpolation


config = ConfigParser(interpolation=ExtendedInterpolation())
config.read("config.ini")


# DEFAULT is the expected default section name, change if needed in ConfigParser()
print(config["DEFAULT"])
for key in config['DEFAULT']:
	print(key, "=", config['DEFAULT'][key])


# all sections have the default section's keys available, so they'll print here for each section
for sec in config.sections():
	print()
	print(f" {sec} ".center(50, "="))
	for key in config[sec]:
		print(key, "=", config[sec][key])


# expected output
'''
<Section: DEFAULT>
name = Alice Allison
age = 99
nickname = alice

============== some_key.with_a_dot ===============
hello = hi hi hi
world = %(hello)s
name = Alice Allison
age = 99
nickname = alice

============== some key with spaces ==============
strange = yes
name = Alice Allison
age = 99
nickname = alice

===================== files ======================
home_path = /home
user_name = alice
user_path = /home/alice
user_bin = /home/alice/bin
test_path = Alice Allison/99
name = Alice Allison
age = 99
nickname = alice

==================== allison =====================
full_path = /home/alice/bin
name = Alice Allison
age = 99
nickname = alice
'''
