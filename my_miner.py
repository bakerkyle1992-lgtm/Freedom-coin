import hashlib, json, os

CHAIN_FILE = "freedom_chain.json"
WALLET_FILE = "my_wallet.json"
BLOCK_REWARD = 50

wallet = json.load(open(WALLET_FILE))
miner = wallet["name"]

data = json.load(open(CHAIN_FILE)) if os.path.exists(CHAIN_FILE) else {"blocks":[],"balances":{},"total_mined":0}
blocks = data["blocks"]
balances = data["balances"]
total_mined = data.get("total_mined", 0)

prev = blocks[-1]["hash"] if blocks else "0000"
nonce = 0
print(f"Mining for {miner}...")
while True:
    h = hashlib.sha256(f"reward{prev}{nonce}".encode()).hexdigest()
    if h.startswith("0000"):
        break
    nonce += 1

balances[miner] = balances.get(miner, 0) + BLOCK_REWARD
total_mined += BLOCK_REWARD
blocks.append({"index":len(blocks)+1,"hash":h,"miner":miner,"reward":BLOCK_REWARD})
json.dump({"blocks":blocks,"balances":balances,"total_mined":total_mined}, open(CHAIN_FILE,"w"))
print(f"Mined! +{BLOCK_REWARD} FREE to {miner}")
print(f"Balance: {balances[miner]} FREE")
