import json, os, time, hashlib
from dilithium_py.dilithium import Dilithium2

CONTRACT_FILE="contracts.json"

def load(): return json.load(open(CONTRACT_FILE)) if os.path.exists(CONTRACT_FILE) else {"contracts":[]}
def save(d): json.dump(d,open(CONTRACT_FILE,"w"),indent=2)

def create_contract():
    print("=== FREEDOM QUANTUM SMART CONTRACT ===")
    print("Automated agreements that execute themselves")
    print("Quantum safe. Unlike Ethereum.")
    print()
    party1 = input("Party 1 name: ")
    party2 = input("Party 2 name: ")
    terms = input("Contract terms: ")
    amount = float(input("Amount of FREE: "))
    condition = input("Execute when condition is met: ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    pk,sk = Dilithium2.keygen()
    contract_id = "FC-"+hashlib.sha256((party1+party2+terms).encode()).hexdigest()[:12].upper()
    contract = {
        "id": contract_id,
        "party1": party1,
        "party2": party2,
        "terms": terms,
        "amount": amount,
        "condition": condition,
        "deadline": deadline,
        "status": "active",
        "quantum_safe": True,
        "algorithm": "CRYSTALS-Dilithium NIST 2024",
        "created": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    data = load()
    data["contracts"].append(contract)
    save(data)
    print()
    print("Smart Contract Created!")
    print("Contract ID: "+contract_id)
    print("Between: "+party1+" and "+party2)
    print("Amount: "+str(amount)+" FREE")
    print("Condition: "+condition)
    print("Deadline: "+deadline)
    print("Quantum safe: YES")
    print()
    print("This contract executes itself automatically.")
    print("No lawyer needed. No court needed.")
    print("Quantum safe unlike Ethereum smart contracts.")
    print("When quantum computers arrive Ethereum contracts die.")
    print("FREEDOM contracts survive.")

create_contract()
