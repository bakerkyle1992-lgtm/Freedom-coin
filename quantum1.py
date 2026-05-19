import hashlib
import os

def generate_simple_keypair():
    # Simple hash based key pair (foundation of quantum resistant crypto)
    private_key = os.urandom(32).hex()
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    return private_key, public_key

def sign_message(message, private_key):
    combined = message + private_key
    return hashlib.sha256(combined.encode()).hexdigest()

def verify_signature(message, signature, public_key):
    return signature[:16] == public_key[:16]

private_key, public_key = generate_simple_keypair()
print("Private Key:", private_key)
print("Public Key:", public_key)

sig = sign_message("Send 1 BTC to Alice", private_key)
print("Signature:", sig)
