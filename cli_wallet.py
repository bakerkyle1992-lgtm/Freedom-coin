import json, os
WALLET_FILE = "my_wallet.json"
CHAIN_FILE = "freedom_chain.json"

def load_wallet():
    if os.path.exists(WALLET_FILE):
        with open(WALLET_FILE) as f:
            return json.load(f)
    return None

def load_chain():
    if os.path.exists(CHAIN_FILE):
        with open(CHAIN_FILE) as f:
            return json.load(f)
    return {"blocks":[],"balances":{},"total_mined":0}

def save_chain(data):
    with open(CHAIN_FILE,"w") as f:
        json.dump(data, f, indent=2)

wallet = load_wallet()
if not wallet:
    print("Run wallet.py first!")
    exit()

data = load_chain()
balances = data["balances"]
name = wallet["name"]
if name not in balances:
    balances[name] = 0
while True:
    print(f"\n=== FREEDOM WALLET ===")
    print(f"User: {name}")
    print(f"Balance: {balances.get(name,0)} FREE")
    print("1. Send  2. Balance  3. Exit")
    choice = input("Choice: ")
    if choice == "1":
        r = input("Send to: ")
        a = int(input("Amount: "))
        if balances.get(name,0) < a:
            print("Insufficient funds!")
        else:
            balances[name] -= a
            balances[r] = balances.get(r,0) + a
            data["balances"] = balances
            save_chain(data)
            print(f"Sent {a} FREE to {r}!")
    elif choice == "2":
        print(f"Balance: {balances.get(name,0)} FREE")
    elif choice == "3":
        print("Goodbye!")
        break
