import hashlib, time
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

def generate_keypair():
    priv = Ed25519PrivateKey.generate()
    return priv, priv.public_key()

def sign(msg, priv):
    return priv.sign(msg.encode())

def verify(msg, sig, pub):
    try:
        pub.verify(sig, msg.encode())
        return True
    except:
        return False

def mine(data, prev):
    nonce = 0
    while True:
        h = hashlib.sha256((data+prev+str(nonce)).encode()).hexdigest()
        if h.startswith("0000"):
            return h, nonce
        nonce += 1

balances = {}

def wallet(name):
    priv, pub = generate_keypair()
    balances[name] = 100
    print(f"{name}: 100 FREE")
    return priv, pub

def send(s, r, amt, priv):
    if balances.get(s,0) < amt:
        print("ERROR: insufficient funds")
        return
    balances[s] -= amt
    balances[r] = balances.get(r,0) + amt
    print(f"{s} -> {r}: {amt} FREE")

ap, _ = wallet("Alice")
bp, _ = wallet("Bob")
send("Alice","Bob",30,ap)
send("Bob","Alice",10,bp)
print("\nMining...")
h,n = mine("Alice Bob transactions","0000")
print(f"Done! Nonce:{n}")
print(f"Hash:{h}")
print("\nBalances:")
for k,v in balances.items():
    print(f"{k}: {v} FREE")
