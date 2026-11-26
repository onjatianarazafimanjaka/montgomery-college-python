import hashlib

prompt = input(str("Enter String: "))

print("MD5:", hashlib.md5(prompt.encode('utf-8')).hexdigest(), "\n")

print("SHA-1:", hashlib.sha1(prompt.encode('utf-8')).hexdigest(), "\n")

print("SHA-2-256:", hashlib.sha256(prompt.encode('utf-8')).hexdigest(), "\n")

print("SHA-2-512:", hashlib.sha512(prompt.encode('utf-8')).hexdigest(), "\n")

print("SHA-3-256:", hashlib.sha3_256(prompt.encode('utf-8')).hexdigest(), "\n")

print("SHA-3-512:", hashlib.sha3_512(prompt.encode('utf-8')).hexdigest(), "\n")

print("BLAKE-2-256:", hashlib.blake2s(prompt.encode('utf-8')).hexdigest(), "\n")

print("BLAKE-2-512:", hashlib.blake2b(prompt.encode('utf-8')).hexdigest(), "\n")
