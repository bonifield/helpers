#!/usr/bin/env python3


# TO DUMP TOML, USE toml.dumps(data) OR tomli_w.dumps(data)
# tomllib is "read only" (will NOT create TOML)


import json
import sys
import tomllib


try:
	inputFile = sys.argv[1]
except:
	print(f"USAGE: {sys.argv[0]} somefile.toml")
	sys.exit(1)


# load() without an "s" - store the loaded TOML config file as a dictionary
# must use "rb"
with open(inputFile, "rb") as f:
	t = tomllib.load(f)

print(type(t))
print(t)
print()

j = json.dumps(t, indent=4)
print(type(j))
print(j)


# loads() with an "s" = store a TOML-formatted string directly (see d above, or if provided as a multi-line string directly in a script)
#r = tomllib.loads("a large TOML-formatted string")


# expected output
'''
$ uv run python-toml-usage.py data.toml

<class 'dict'>
{'title': 'Weather Project Title', 'description': "another top-level key's value", 'weather': {'temperature': 70.0, 'marker': 'farenheit', 'sunshine': True, 'keywords': ['nice', 'pleasant', 'ideal']}, 'location': {'continent': {'north_america': True, 'south_america': True, 'antarctica': False}, 'country': {'united_states_of_america': True, 'canada': True, 'uruguay': True, 'antarctica': False}}, 'planet': {'galaxy': {'name': 'milky way'}}}

<class 'str'>
{
    "title": "Weather Project Title",
    "description": "another top-level key's value",
    "weather": {
        "temperature": 70.0,
        "marker": "farenheit",
        "sunshine": true,
        "keywords": [
            "nice",
            "pleasant",
            "ideal"
        ]
    },
    "location": {
        "continent": {
            "north_america": true,
            "south_america": true,
            "antarctica": false
        },
        "country": {
            "united_states_of_america": true,
            "canada": true,
            "uruguay": true,
            "antarctica": false
        }
    },
    "planet": {
        "galaxy": {
            "name": "milky way"
        }
    }
}
'''
