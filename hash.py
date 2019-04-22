from hashlib import sha256

hi = 'Hi'.encode('utf-8')
Hi = 'hi'.encode('utf-8')
hello = 'Hello'.encode('utf-8')

print(sha256(hi).hexdigest())
print(sha256(Hi).hexdigest())
print(sha256(hello).hexdigest())
