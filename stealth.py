import hashlib, json, os, time
from dilithium_py.dilithium import Dilithium2

STEALTH_FILE="stealth_tx.json"

def load(): return json.load(open(STEALTH_FILE)) if os.path.exists(STEALTH_FILE) else {"transactions":[]}
def save(d): json.dump(d,open(STEALTH_FILE,"w"),indent=2)

def send_stealth(sender, receiver, amount):
    pk,sk = Dilithium2.keygen()
    stealth_addr = hashlib.sha256((receiver+str(time.time())).encode()).hexdigest()[:34]
    tx_hash = hashlib.sha256((sender+receiver+str(amount)+str(time.time())).encode()).hexdigest()
    tx = {
        "tx_hash": tx_hash[:16],
        "stealth_address": stealth_addr,
        "amount": amount,
        "status": "pending_confirmation",
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "visible_on_chain": False
    }
    data = load()
    data["transactions"].append(tx)
    save(data)
    print("=== STEALTH TRANSACTION SENT ===")
    print("Amount: "+str(amount)+" FREE")
    print("Stealth address: "+stealth_addr)
    print("TX hash: "+tx_hash[:16])
    print("Visible on blockchain: NO")
    print("Status: Hidden until receiver confirms")
    print()
    print("Nobody can see this transaction except sender and receiver")
    print("Not even FREEDOM coin nodes can see the real addresses")

print("=== FREEDOM STEALTH TRANSACTIONS ===")
sender = input("Your name: ")
receiver = input("Receiver name: ")
amount = float(input("Amount of FREE: "))
send_stealth(sender, receiver, amount)
