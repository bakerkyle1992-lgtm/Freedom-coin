import hashlib
import os

def generate_keypair():
    priv = os.urandom(32).hex()
    pub = hashlib.sha256(priv.encode()).hexdigest()
    return priv, pub

balances = {}

def create_wallet(name):
    priv, pub = generate_keypair()
    balances[pub[:16]] = 100
    print(f"{name}: {pub[:16]} | Balance: 100 coins")
    return priv, pub

def send(sender_pub, receiver_pub, amount, sender_priv):
    sid = sender_pub[:16]
    rid = receiver_pub[:16]
    if balances.get(sid, 0) < amount:
        print("ERROR: Not enough coins!")
        return False
    balances[sid] -= amount
    balances[rid] = balances.get(rid, 0) + amount
    print(f"Sent {amount} coins | {sid} -> {rid}")
    print(f"Balances: {sid}={balances[sid]} | {rid}={balances[rid]}")
    return True

alice_priv, alice_pub = create_wallet("Alice")
bob_priv, bob_pub = create_wallet("Bob")

send(alice_pub, bob_pub, 30, alice_priv)
send(bob_pub, alice_pub, 200, bob_priv)
