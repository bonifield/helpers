#!/usr/bin/env python3

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

'''
md5 (32 bytes) dd69dfac527ec54b4d6c3368c77930a0
sha1 (40 bytes) 004187bcb32c571675b9b1a5078872abbc86642a
sha224 (56 bytes) fdb4fb5ba6d29b8da2e4368386bd55cfe6ee2e39d070488d97ab89d6
sha256 (64 bytes) f0af8a03aa33f73d20235680e9f39fb31e3bbb38252ae938314c2cd41ff5ff9e
sha384 (96 bytes) 279d3d73e3f7f0e160f44690c1e26ffeb0001d974d756532dc630f9d345b3c894b4ed01979252119f5bb18cfcece5f95
sha512 (128 bytes) ae686987c0885d688d878e6c99b30097f9bcf4f450c1ee496ce2e08c0d2894b5f689d9eb44b93d44648a26d84fecd25b5009df396a5c2f88f9f6f22027510cd2

sha3_224 (56 bytes) 72208c1cc1fe784c461d2e3528c3d1834fc6b6577d6517dd90a00071
sha3_256 (64 bytes) 06eaa93f4c4f7ca517e4cca7fb3d1aa716620dbcc0a935f33a159b7dd9c5fcb4
sha3_384 (96 bytes) 3e7a9a500e236f5e241428a13adb80cfa5443368a9c251279cab152d2bd49c46e57cd67371fe908f5686b0a1a7c47ef5
sha3_512 (128 bytes) cb26c38eead65d244fa2436f769497181810e473d4ebe35b799842cdb54ce056cce210e24b96c8e58b7f588b94ce75b626b1dd0343cfa3e9a6d589e4fcd14972
'''
