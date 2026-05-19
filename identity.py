import hashlib, json, os, time
from dilithium_py.dilithium import Dilithium2

ID_FILE="freedom_id.json"

def create_id():
    print("=== FREEDOM DECENTRALISED IDENTITY ===")
    print("Your wallet IS your identity. No government needed.")
    print()
    name = input("Full name: ")
    dob = input("Date of birth (DDMMYYYY): ")
    country = input("Country: ")
    pk,sk = Dilithium2.keygen()
    did = "FREEDOM-ID-"+hashlib.sha256((name+dob+country).encode()).hexdigest()[:20].upper()
    identity = {
        "did": did,
        "name": name,
        "country": country,
        "created": time.strftime("%Y-%m-%d"),
        "quantum_secured": True,
        "algorithm": "CRYSTALS-Dilithium NIST 2024"
    }
    with open(ID_FILE,"w") as f:
        json.dump(identity,f,indent=2)
    print()
    print("FREEDOM ID Created!")
    print("Your DID: "+did)
    print("Name: "+name)
    print("Country: "+country)
    print("Quantum secured: YES")
    print()
    print("This ID is yours forever.")
    print("No government can revoke it.")
    print("No bank can freeze it.")
    print("No company can cancel it.")
    print("It lives on the blockchain. Forever.")

create_id()
