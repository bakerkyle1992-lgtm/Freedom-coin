import hashlib
import time
import json
import os
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

CHAIN_FILE = "blockchain_data.json"

def load_chain():
    if os.path.exists(CHAIN_FILE):
        with open(CHAIN_FILE, "r") as f:
            return json.load(f)
    return {"blocks": [], "balances": {}}

def save_chain(data):
    with open(CHAIN_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("Blockchain saved!")

def mine(data, prev):
    nonce = 0
    while True:
        h = hashlib.sha256((data+prev+str(nonce)).encode()).hexdigest()
        if h.startswith("0000"):
            return h, nonce
        nonce += 1

# Load existing chain
chain_data = load_chain()
blocks = chain_data["blocks"]
balances = chain_data["balances"]

# Add starting balances if new
if not balances:
    balances["Alice"] = 100
    balances["Bob"] = 100
    print("New blockchain started!")
else:
    print(f"Loaded existing blockchain with {len(blocks)} blocks!")

# Show current balances
print("\n=== CURRENT BALANCES ===")
for name, bal in balances.items():
    print(f"{name}: {bal} FREE")

# Make a transaction
if balances.get("Alice", 0) >= 10:
    balances["Alice"] -= 10
    balances["Bob"] = balances.get("Bob", 0) + 10
    tx = f"Alice sends 10 FREE to Bob at {time.strftime('%H:%M:%S')}"
    print(f"\nTransaction: {tx}")

    # Mine block
    print("Mining...")
    prev_hash = blocks[-1]["hash"] if blocks else "0000"
    h, nonce = mine(tx, prev_hash)
    
    block = {
        "index": len(blocks) + 1,
        "transaction": tx,
        "hash": h,
        "nonce": nonce,
        "time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    blocks.append(block)
    print(f"Block {block['index']} mined!")
    print(f"Hash: {h}")

# Save everything
chain_data = {"blocks": blocks, "balances": balances}
save_chain(chain_data)

print("\n=== UPDATED BALANCES ===")
for name, bal in balances.items():
    print(f"{name}: {bal} FREE")

print(f"\nTotal blocks in chain: {len(blocks)}")
