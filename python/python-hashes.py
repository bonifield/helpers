#!/usr/bin/python3

import hashlib

s = "this is a string with no line terminators"

# hexdigest() returns a string object of double length, containing only hexadecimal digits
# md5() may be blocked if using a FIPS-compliant build of Python
s_md5 = hashlib.md5(s.encode('utf-8')).hexdigest()
s_sha1 = hashlib.sha1(s.encode('utf-8')).hexdigest()
s_sha224 = hashlib.sha224(s.encode('utf-8')).hexdigest()
s_sha256 = hashlib.sha256(s.encode('utf-8')).hexdigest()
s_sha384 = hashlib.sha384(s.encode('utf-8')).hexdigest()
s_sha512 = hashlib.sha512(s.encode('utf-8')).hexdigest()
s_sha3_224 = hashlib.sha3_224(s.encode('utf-8')).hexdigest()
s_sha3_256 = hashlib.sha3_256(s.encode('utf-8')).hexdigest()
s_sha3_384 = hashlib.sha3_384(s.encode('utf-8')).hexdigest()
s_sha3_512 = hashlib.sha3_512(s.encode('utf-8')).hexdigest()

print()
print("md5", "("+str(len(s_md5))+" bytes)", s_md5)
print("sha1", "("+str(len(s_sha1))+" bytes)", s_sha1)
print("sha224", "("+str(len(s_sha224))+" bytes)", s_sha224)
print("sha256", "("+str(len(s_sha256))+" bytes)", s_sha256)
print("sha384", "("+str(len(s_sha384))+" bytes)", s_sha384)
print("sha512", "("+str(len(s_sha512))+" bytes)", s_sha512)
print()
print("sha3_224", "("+str(len(s_sha3_224))+" bytes)", s_sha3_224)
print("sha3_256", "("+str(len(s_sha3_256))+" bytes)", s_sha3_256)
print("sha3_384", "("+str(len(s_sha3_384))+" bytes)", s_sha3_384)
print("sha3_512", "("+str(len(s_sha3_512))+" bytes)", s_sha3_512)
print()
