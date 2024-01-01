#!/usr/bin/env python3

# https://docs.python.org/3/library/uuid.html
# python -m uuid [-h] [-u {uuid1,uuid3,uuid4,uuid5}] [-n NAMESPACE] [-N NAME]
# -n and -N only required for uuid3 and uuid5

import uuid

# make a UUID based on the host ID and current time
u1 = uuid.uuid1()

# make a UUID using an MD5 hash of a namespace UUID and a name
u3 = uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')

# make a random UUID
u4 = uuid.uuid4()

# make a UUID using a SHA-1 hash of a namespace UUID and a name
u5 = uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')

print(f"u1\t{u1}")
print(f"u3\t{u3}")
print(f"u4\t{u4}")
print(f"u5\t{u5}")

# output
# u1	e4724802-a8de-11ee-a376-c91ecafa4429
# u3	6fa459ea-ee8a-3ca4-894e-db77e160355e
# u4	d11023e2-fcdd-4a39-b8b4-771251e68394
# u5	886313e1-3b8a-5372-9b90-0c9aee199e5d
