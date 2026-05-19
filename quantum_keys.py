from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

def generate_keypair():
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def sign(message, private_key):
    return private_key.sign(message.encode())

def verify(message, signature, public_key):
    try:
        public_key.verify(signature, message.encode())
        return True
    except:
        return False

private_key, public_key = generate_keypair()
print("=== FREEDOM COIN QUANTUM KEYS ===")

sig = sign("Alice sends 10 FREE to Bob", private_key)
print(f"Signature size: {len(sig)} bytes")

valid = verify("Alice sends 10 FREE to Bob", sig, public_key)
print(f"Signature valid: {valid}")

tampered = verify("Alice sends 999 FREE to Bob", sig, public_key)
print(f"Tampered valid: {tampered}")
