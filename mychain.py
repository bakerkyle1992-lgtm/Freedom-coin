import hashlib
import os
import time

def generate_keypair():
    private_key = os.urandom(32).hex()
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    return private_key, public_key

def sign(message, private_key):
    return hashlib.sha256((message + private_key).encode()).hexdigest()

def create_block(data, previous_hash, private_key):
    timestamp = str(time.time())
    content = data + previous_hash + timestamp
    hash = hashlib.sha256(content.encode()).hexdigest()
    signature = sign(hash, private_key)
    return {
        "data": data,
        "previous_hash": previous_hash,
        "hash": hash,
        "signature": signature
    }

private_key, public_key = generate_keypair()
print("Your Public Key:", public_key)

genesis = create_block("Genesis", "0000", private_key)
block2 = create_block("Alice sends 1 coin to Bob", genesis["hash"], private_key)

print("Block 1:", genesis["hash"])
print("Block 2:", block2["hash"])
print("Block 2 Signature:", block2["signature"])
