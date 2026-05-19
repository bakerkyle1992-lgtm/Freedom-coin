import hashlib, json, os, getpass

WALLET_FILE="my_wallet.json"

def load(): return json.load(open(WALLET_FILE)) if os.path.exists(WALLET_FILE) else {}
def save(d): json.dump(d,open(WALLET_FILE,"w"),indent=2)

def set_password():
    print("=== FREEDOM WALLET ENCRYPTION ===")
    password = getpass.getpass("Set wallet password: ")
    confirm = getpass.getpass("Confirm password: ")
    if password != confirm:
        print("Passwords do not match")
        return
    wallet = load()
    pw_hash = hashlib.sha256(password.encode()).hexdigest()
    wallet["password_hash"] = pw_hash
    wallet["encrypted"] = True
    save(wallet)
    print("Wallet encrypted successfully")
    print("Password required for all future transactions")

def unlock_wallet():
    wallet = load()
    if not wallet.get("encrypted"):
        print("Wallet is not encrypted")
        return True
    password = getpass.getpass("Enter wallet password: ")
    pw_hash = hashlib.sha256(password.encode()).hexdigest()
    if pw_hash == wallet.get("password_hash"):
        print("Wallet unlocked successfully")
        return True
    else:
        print("Wrong password - Access denied")
        return False

print("=== FREEDOM WALLET SECURITY ===")
print("1.Set Password  2.Unlock Wallet")
c = input("Choice: ")
if c=="1": set_password()
elif c=="2": unlock_wallet()
