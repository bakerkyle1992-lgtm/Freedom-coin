import hashlib, json, os, time
from dilithium_py.dilithium import Dilithium2

CHAIN_FILE = "freedom_chain.json"
BLOCK_REWARD = 50

def load():
    if os.path.exists(CHAIN_FILE):
        with open(CHAIN_FILE) as f:
            return json.load(f)
    return {"blocks":[],"balances":{},"total_mined":0}

def save(data):
    with open(CHAIN_FILE,"w") as f:
        json.dump(data,f,indent=2)

def mine(data, prev):
    nonce = 0
    while True:
        h = hashlib.sha256(f"{data}{prev}{nonce}".encode()).hexdigest()
        if h.startswith("0000"):
            return h, nonce
        nonce += 1

data = load()
blocks = data["blocks"]
balances = data["balances"]
total_mined = data.get("total_mined", 0)

if not balances:
    balances["Alice"] = 100
    balances["Bob"] = 100

pk, sk = Dilithium2.keygen()
msg = f"Alice sends 10 FREE to Bob at {time.strftime('%H:%M:%S')}".encode()
sig = Dilithium2.sign(sk, msg)
verified = Dilithium2.verify(pk, msg, sig)

print("=== FREEDOM COIN v2 ===")
print(f"Quantum signature verified: {verified}")

if verified and balances.get("Alice",0) >= 10:
    balances["Alice"] -= 10
    balances["Bob"] = balances.get("Bob",0) + 10
    print("Transaction accepted!")

prev = blocks[-1]["hash"] if blocks else "0000"
print("Mining block...")
h, n = mine(msg.decode(), prev)
balances["Alice"] = balances.get("Alice",0) + BLOCK_REWARD
total_mined += BLOCK_REWARD

blocks.append({
    "index": len(blocks)+1,
    "hash": h,
    "nonce": n,
    "verified": verified,
    "reward": BLOCK_REWARD,
    "time": time.strftime("%Y-%m-%d %H:%M:%S")
})

save({"blocks":blocks,"balances":balances,"total_mined":total_mined})

print(f"Block {len(blocks)} mined!")
for k,v in balances.items():
    print(f"{k}: {v} FREE")
print(f"Total mined: {total_mined}")
