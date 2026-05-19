import json,os
FEE=1
CHAIN="freedom_chain.json"
data=json.load(open(CHAIN)) if os.path.exists(CHAIN) else {"blocks":[],"balances":{}}
b=data["balances"]
if "Alice" not in b: b["Alice"]=100
if "Bob" not in b: b["Bob"]=100
miner="kyleashleydalebaker"
print("BEFORE:","Alice:",b.get("Alice",0),"Bob:",b.get("Bob",0),"Miner:",b.get(miner,0))
if b.get("Alice",0)>=11:
    b["Alice"]-=11
    b["Bob"]=b.get("Bob",0)+10
    b[miner]=b.get(miner,0)+FEE
    print("Sent 10 FREE, Fee 1 FREE to miner")
else:
    print("Insufficient funds")
print("AFTER:","Alice:",b.get("Alice",0),"Bob:",b.get("Bob",0),"Miner:",b.get(miner,0))
data["balances"]=b
json.dump(data,open(CHAIN,"w"),indent=2)
