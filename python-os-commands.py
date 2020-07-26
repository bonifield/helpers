#!/usr/bin/python3

# different ways to execute system commands with python3
# subprocess returns bytes, which need to be decoded if strings are expected

import os, subprocess

o = os.popen('uname -a').read().strip()
p = subprocess.Popen('uname -a'.split(), stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
s = subprocess.Popen('ss -ptuan'.split(), stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()

print("\n\n\n#=============\n# os.popen('uname -a').read().strip()\n#=============\n")
print(o)
print("\n\n\n#=============\n# subprocess.Popen('uname -a'.split(), stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()\n#=============\n")
print(p)
print("\n\n\n#=============\n# subprocess.Popen('ss -ptuan'.split(), stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()\n#=============\n")
print(s)
print("\n\n\n")
