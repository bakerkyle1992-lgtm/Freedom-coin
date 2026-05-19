import hashlib
import os

def generate_keypair():
    private_key = os.urandom(32).hex()
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    return private_key, public_key

def sign(message, private_key):
    return hashlib.sha256((message + private_key).encode()).hexdigest()

def create_transaction(sender, receiver, amount, private_key):
    data = f"{sender[:8]} sends {amount} coins to {receiver[:8]}"
    signature = sign(data, private_key)
    return {"sender": sender[:8], "receiver": receiver[:8], "amount": amount, "signature": signature}

alice_priv, alice_pub = generate_keypair()
bob_priv, bob_pub = generate_keypair()
charlie_priv, charlie_pub = generate_keypair()

print("=== WALLETS ===")
print(f"Alice:   {alice_pub[:16]}...")
print(f"Bob:     {bob_pub[:16]}...")
print(f"Charlie: {charlie_pub[:16]}...")

tx1 = create_transaction(alice_pub, bob_pub, 10, alice_priv)
print(f"\nTX1: {tx1['sender']} -> {tx1['receiver']} : {tx1['amount']} coins")

tx2 = create_transaction(bob_pub, charlie_pub, 5, bob_priv)
print(f"TX2: {tx2['sender']} -> {tx2['receiver']} : {tx2['amount']} coins")
