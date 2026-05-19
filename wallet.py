import json, os
from dilithium_py.dilithium import Dilithium2
import hashlib

WALLET_FILE = "my_wallet.json"

def create_wallet(name):
    pk, sk = Dilithium2.keygen()
    address = hashlib.sha256(pk).hexdigest()[:34]
    wallet = {
        "name": name,
        "address": address,
        "public_key": pk.hex(),
        "secret_key": sk.hex()
    }
    with open(WALLET_FILE, "w") as f:
        json.dump(wallet, f, indent=2)
    print(f"Wallet created for {name}!")
    print(f"Address: {address}")
    return wallet

def load_wallet():
    if os.path.exists(WALLET_FILE):
        with open(WALLET_FILE) as f:
            return json.load(f)
    return None

wallet = load_wallet()
if wallet:
    print(f"Wallet loaded: {wallet['name']}")
    print(f"Address: {wallet['address']}")
else:
    name = input("Enter your name: ")
    wallet = create_wallet(name)
