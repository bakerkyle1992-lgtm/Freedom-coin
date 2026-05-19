
import json, os
CHAIN_FILE = "freedom_chain.json"
INITIAL_REWARD = 50
HALVING_INTERVAL = 10
def get_reward(h):
    n = h // HALVING_INTERVAL
    return 0 if n >= 64 else INITIAL_REWARD / (2**n)
data = json.load(open(CHAIN_FILE)) if os.path.exists(CHAIN_FILE) else {"blocks":[]}
height = len(data["blocks"])
print("=== FREEDOM COIN HALVING ===")
print(f"Block height: {height}")
print(f"Current reward: {get_reward(height)} FREE")
print(f"Next halving at block: {(height//HALVING_INTERVAL+1)*HALVING_INTERVAL}")
for i in range(6):
    print(f"Block {i*HALVING_INTERVAL}: {get_reward(i*HALVING_INTERVAL)} FREE")
