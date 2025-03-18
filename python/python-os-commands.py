#!/usr/bin/env python3

# different ways to execute system commands with python3
# subprocess returns bytes, which need to be decoded if strings are expected

import os
import subprocess

o = os.popen('uname -a').read().strip()
p = subprocess.Popen('uname -a'.split(), stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()

print()

print(" os.popen() ".center(50, "="))
print(o)
print()

print(" subprocess.Popen() ".center(50, "="))
print(p)
print()
