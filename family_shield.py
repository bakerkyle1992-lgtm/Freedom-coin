import json, os, time, hashlib

SHIELD_FILE="family_shield.json"

def load(): return json.load(open(SHIELD_FILE)) if os.path.exists(SHIELD_FILE) else {"shield":{}}
def save(d): json.dump(d,open(SHIELD_FILE,"w"),indent=2)

def setup_shield():
    print("=== FREEDOM FAMILY SHIELD ===")
    print("Require multiple family members to approve large transactions")
    print()
    owner = input("Your name: ")
    members = []
    num = int(input("How many family members to add: "))
    for i in range(num):
        m = input("Family member "+str(i+1)+" name: ")
        members.append(m)
    threshold = int(input("How many must approve large transactions: "))
    limit = float(input("What amount triggers approval requirement: "))
    shield = {
        "owner": owner,
        "members": members,
        "threshold": threshold,
        "limit": limit,
        "created": time.strftime("%Y-%m-%d %H:%M:%S"),
        "status": "active"
    }
    save({"shield": shield})
    print()
    print("Family Shield activated!")
    print("Owner: "+owner)
    print("Protected by: "+", ".join(members))
    print("Approvals needed for large transactions: "+str(threshold))
    print("Triggers on amounts over: "+str(limit)+" FREE")
    print()
    print("No single person can drain this wallet alone.")
    print("Your family protects each other.")

setup_shield()
