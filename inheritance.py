import json, os, time
from dilithium_py.dilithium import Dilithium2
import hashlib

INHERIT_FILE="inheritance.json"
CHAIN="freedom_chain.json"

def load(fn): return json.load(open(fn)) if os.path.exists(fn) else {}
def save(d,fn): json.dump(d,open(fn,"w"),indent=2)

def setup_inheritance():
    print("=== FREEDOM COIN INHERITANCE SYSTEM ===")
    print("Protect your family if something happens to you")
    print()
    owner = input("Your name: ")
    beneficiary = input("Beneficiary name: ")
    days = int(input("Days of inactivity before transfer: "))
    amount = float(input("Amount of FREE to protect: "))
    checkin = time.time()
    transfer_time = checkin + (days * 86400)
    record = {
        "owner": owner,
        "beneficiary": beneficiary,
        "amount": amount,
        "days": days,
        "last_checkin": checkin,
        "transfer_at": transfer_time,
        "status": "active",
        "created": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    save(record, INHERIT_FILE)
    print()
    print("Inheritance protection activated!")
    print("Owner: "+owner)
    print("Beneficiary: "+beneficiary)
    print("Amount protected: "+str(amount)+" FREE")
    print("Transfer after "+str(days)+" days of inactivity")
    print("Transfer date: "+time.strftime("%Y-%m-%d", time.localtime(transfer_time)))
    print()
    print("No lawyer needed. No bank needed. No government needed.")
    print("Your family is protected by quantum resistant cryptography.")

def checkin():
    if not os.path.exists(INHERIT_FILE):
        print("No inheritance set up yet")
        return
    record = load(INHERIT_FILE)
    record["last_checkin"] = time.time()
    record["transfer_at"] = time.time() + (record["days"] * 86400)
    save(record, INHERIT_FILE)
    print("Checkin confirmed! Timer reset.")
    print("Next transfer date: "+time.strftime("%Y-%m-%d", time.localtime(record["transfer_at"])))

def check_status():
    if not os.path.exists(INHERIT_FILE):
        print("No inheritance set up")
        return
    record = load(INHERIT_FILE)
    now = time.time()
    remaining = record["transfer_at"] - now
    days_left = int(remaining / 86400)
    if remaining <= 0:
        print("TRANSFER DUE: "+str(record["amount"])+" FREE to "+record["beneficiary"])
        record["status"] = "transferred"
        save(record, INHERIT_FILE)
    else:
        print("Status: Active")
        print("Owner: "+record["owner"])
        print("Beneficiary: "+record["beneficiary"])
        print("Amount: "+str(record["amount"])+" FREE")
        print("Days until transfer: "+str(days_left))

print("=== FREEDOM COIN INHERITANCE ===")
print("1. Setup  2. Checkin  3. Status")
c = input("Choice: ")
if c=="1": setup_inheritance()
elif c=="2": checkin()
elif c=="3": check_status()
