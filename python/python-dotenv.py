#!/usr/bin/env python3

# pip install python-dotenv

import os
from dotenv import load_dotenv

load_dotenv()

my_var = os.getenv("MY_VAR")

print(my_var)
# abcd1234
