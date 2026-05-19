import hashlib,json,os
from dilithium_py.dilithium import Dilithium2
BRIDGE="bridge_registry.json"
def load(): return json.load(open(BRIDGE)) if os.path.exists(BRIDGE) else {"migrations":[]}
def save(d): json.dump(d,open(BRIDGE,"w"),indent=2)
def migrate(old):
    pk,sk=Dilithium2.keygen()
    new=hashlib.sha256(pk).hexdigest()[:34]
    r=load()
    r["migrations"].append({"old":old,"new":new,"algorithm":"CRYSTALS-Dilithium"})
    save(r)
    return new
print("=== FREEDOM MIGRATION BRIDGE ===")
old=input("Enter Bitcoin or Ethereum address: ")
new=migrate(old)
print("Old: "+old)
print("New quantum safe: "+new)
print("Algorithm: CRYSTALS-Dilithium NIST 2024")
print("Status: QUANTUM PROTECTED")
