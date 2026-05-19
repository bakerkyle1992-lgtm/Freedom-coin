import hashlib

message = "Hello Quantum World"
hash = hashlib.sha256(message.encode()).hexdigest()
print("SHA256 Hash:", hash)
