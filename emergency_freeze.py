import json, os, time

FREEZE_FILE="freeze.json"
CHAIN="freedom_chain.json"

def load(fn): return json.load(open(fn)) if os.path.exists(fn) else {}
def save(d,fn): json.dump(d,open(fn,"w"),indent=2)

def freeze_wallet():
    print("=== EMERGENCY WALLET FREEZE ===")
    name = input("Your wallet name: ")
    reason = input("Reason (stolen/lost/compromised): ")
    freeze = {
        "wallet": name,
        "frozen": True,
        "reason": reason,
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "FROZEN"
    }
    save(freeze, FREEZE_FILE)
    print()
    print("WALLET FROZEN IMMEDIATELY")
    print("Wallet: "+name)
    print("Reason: "+reason)
    print("Time: "+freeze["time"])
    print()
    print("No transactions can be made from this wallet")
    print("Use your recovery phrase to restore access")

def unfreeze_wallet():
    if not os.path.exists(FREEZE_FILE):
        print("No frozen wallet found")
        return
    phrase = input("Enter recovery phrase to unfreeze: ")
    freeze = load(FREEZE_FILE)
    freeze["frozen"] = False
    freeze["status"] = "ACTIVE"
    save(freeze, FREEZE_FILE)
    print("Wallet unfrozen and restored")

print("=== EMERGENCY FREEZE ===")
print("1.Freeze Wallet  2.Unfreeze Wallet")
c = input("Choice: ")
if c=="1": freeze_wallet()
elif c=="2": unfreeze_wallet()
