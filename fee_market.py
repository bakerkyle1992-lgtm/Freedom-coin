import json, os, time

CHAIN="freedom_chain.json"

def load(): return json.load(open(CHAIN)) if os.path.exists(CHAIN) else {"blocks":[]}

def calculate_fee():
    print("=== FREEDOM FEE MARKET ===")
    data = load()
    blocks = data.get("blocks",[])
    if len(blocks) < 5:
        base_fee = 1.0
    elif len(blocks) < 10:
        base_fee = 0.5
    else:
        base_fee = 0.1
    print("Current network blocks: "+str(len(blocks)))
    print("Current base fee: "+str(base_fee)+" FREE")
    print()
    amount = float(input("Transaction amount: "))
    priority = input("Priority (low/medium/high): ")
    if priority=="high":
        fee = base_fee * 3
        speed = "Next block"
    elif priority=="medium":
        fee = base_fee * 2
        speed = "Within 3 blocks"
    else:
        fee = base_fee
        speed = "Within 10 blocks"
    total = amount + fee
    print()
    print("=== TRANSACTION ESTIMATE ===")
    print("Amount: "+str(amount)+" FREE")
    print("Fee: "+str(fee)+" FREE")
    print("Total: "+str(total)+" FREE")
    print("Speed: "+speed)
    print("Fee goes to miner as reward")

calculate_fee()
