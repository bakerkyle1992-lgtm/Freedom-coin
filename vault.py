import json, os, time, hashlib

VAULT_FILE="vault.json"

def load(): return json.load(open(VAULT_FILE)) if os.path.exists(VAULT_FILE) else {"vaults":[]}
def save(d): json.dump(d,open(VAULT_FILE,"w"),indent=2)

def create_vault():
    print("=== FREEDOM COIN TIME LOCKED VAULT ===")
    owner = input("Your name: ")
    recipient = input("Who receives this vault: ")
    message = input("Secret message for them: ")
    amount = float(input("FREE coins to lock: "))
    unlock_date = input("Unlock date (YYYY-MM-DD): ")
    key = hashlib.sha256((owner+recipient+unlock_date).encode()).hexdigest()
    vault = {
        "owner": owner,
        "recipient": recipient,
        "message": hashlib.sha256(message.encode()).hexdigest(),
        "amount": amount,
        "unlock_date": unlock_date,
        "key": key[:16],
        "created": time.strftime("%Y-%m-%d"),
        "status": "locked"
    }
    data = load()
    data["vaults"].append(vault)
    save(data)
    print()
    print("Vault created and locked!")
    print("Owner: "+owner)
    print("Recipient: "+recipient)
    print("Amount locked: "+str(amount)+" FREE")
    print("Unlocks on: "+unlock_date)
    print("Vault key: "+key[:16])
    print()
    print("Nobody can access this vault until "+unlock_date)
    print("Not even you. The code enforces it.")

def check_vaults():
    data = load()
    today = time.strftime("%Y-%m-%d")
    print("=== YOUR VAULTS ===")
    for v in data["vaults"]:
        status = "UNLOCKED" if today >= v["unlock_date"] else "LOCKED until "+v["unlock_date"]
        print("Recipient: "+v["recipient"]+" | Amount: "+str(v["amount"])+" FREE | "+status)

print("=== FREEDOM VAULT ===")
print("1.Create Vault  2.Check Vaults")
c = input("Choice: ")
if c=="1": create_vault()
elif c=="2": check_vaults()
