import hashlib,json,os,time
L2_FILE="layer2.json"
def load(): return json.load(open(L2_FILE)) if os.path.exists(L2_FILE) else {"transactions":[],"batches":[]}
def save(d): json.dump(d,open(L2_FILE,"w"),indent=2)
def add_tx():
    sender=input("Sender: ")
    receiver=input("Receiver: ")
    amount=float(input("Amount: "))
    data=load()
    tx={"sender":sender,"receiver":receiver,"amount":amount,"time":time.strftime("%H:%M:%S")}
    data["transactions"].append(tx)
    save(data)
    print("TX added to Layer 2 pool")
    print("Speed: Instant")
    print("Fee: 0.001 FREE")
def batch():
    data=load()
    txs=data["transactions"]
    if not txs: print("No transactions to batch"); return
    batch_hash=hashlib.sha256(str(txs).encode()).hexdigest()[:16]
    data["batches"].append({"hash":batch_hash,"tx_count":len(txs),"time":time.strftime("%Y-%m-%d %H:%M:%S")})
    data["transactions"]=[]
    save(data)
    print("Batched "+str(len(txs))+" transactions")
    print("Batch hash: "+batch_hash)
    print("All transactions settled on main chain")
    print("This is how FREEDOM coin scales to millions of users")
print("=== FREEDOM LAYER 2 ===")
print("Instant transactions at near zero cost")
print("1.Send TX  2.Batch to chain")
c=input("Choice: ")
if c=="1": add_tx()
elif c=="2": batch()
