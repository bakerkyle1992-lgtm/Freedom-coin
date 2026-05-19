import hashlib
import os
import time

def generate_keypair():
    priv = os.urandom(32).hex()
    pub = hashlib.sha256(priv.encode()).hexdigest()
    return priv, pub

balances = {}
history = []

def create_wallet(name):
    priv, pub = generate_keypair()
    balances[pub[:16]] = 100
    print(f"{name}: {pub[:16]} | Balance: 100 coins")
    return priv, pub, name

def send(sender_name, sender_pub, receiver_name, receiver_pub, amount):
    sid = sender_pub[:16]
    rid = receiver_pub[:16]
    if balances.get(sid, 0) < amount:
        print(f"ERROR: {sender_name} doesn't have enough coins!")
        return
    balances[sid] -= amount
    balances[rid] = balances.get(rid, 0) + amount
    tx = {
        "time": time.strftime("%H:%M:%S"),
        "from": sender_name,
        "to": receiver_name,
        "amount": amount
    }
    history.append(tx)
    print(f"Sent {amount} coins from {sender_name} to {receiver_name}")

alice_priv, alice_pub, _ = create_wallet("Alice")
bob_priv, bob_pub, _ = create_wallet("Bob")
charlie_priv, charlie_pub, _ = create_wallet("Charlie")

send("Alice", alice_pub, "Bob", bob_pub, 30)
send("Bob", bob_pub, "Charlie", charlie_pub, 50)
send("Charlie", charlie_pub, "Alice", charlie_pub, 200)

print("\n=== TRANSACTION HISTORY ===")
for tx in history:
    print(f"[{tx['time']}] {tx['from']} -> {tx['to']}: {tx['amount']} coins")

print("\n=== FINAL BALANCES ===")
for name, pub in [("Alice", alice_pub), ("Bob", bob_pub), ("Charlie", charlie_pub)]:
    print(f"{name}: {balances[pub[:16]]} coins")
