import json,os,hashlib,time
from dilithium_py.dilithium import Dilithium2
CHAIN="freedom_chain.json"
WALLET="my_wallet.json"
REWARD=50
HALVING=10
FEE=1
def load(f): return json.load(open(f)) if os.path.exists(f) else {}
def save(d): json.dump(d,open(CHAIN,"w"),indent=2)
def reward(h): n=h//HALVING; return 0 if n>=64 else REWARD/(2**n)
def mine(d,p):
    n=0
    while True:
        h=hashlib.sha256(f"{d}{p}{n}".encode()).hexdigest()
        if h.startswith("0000"): return h,n
        n+=1
wallet=load(WALLET)
if not wallet: print("Run wallet.py first"); exit()
name=wallet["name"]
data=load(CHAIN) or {"blocks":[],"balances":{},"total_mined":0}
blocks=data["blocks"]
balances=data["balances"]
if name not in balances: balances[name]=0
while True:
    print("=== FREEDOM COIN ===")
    print(f"User: {name}")
    print(f"Balance: {balances.get(name,0)} FREE")
    print(f"Blocks: {len(blocks)}")
    print(f"Reward: {reward(len(blocks))} FREE")
    print("1.Mine 2.Send 3.Balances 4.Chain 5.Exit")
    c=input("Choice: ")
    if c=="1":
        print("Mining...")
        prev=blocks[-1]["hash"] if blocks else "0000"
        h,n=mine(f"reward to {name}",prev)
        r=reward(len(blocks))
        balances[name]=balances.get(name,0)+r
        blocks.append({"index":len(blocks)+1,"hash":h,"miner":name,"reward":r})
        save({"blocks":blocks,"balances":balances,"total_mined":data.get("total_mined",0)+r})
        print(f"Mined! +{r} FREE")
    elif c=="2":
        r=input("Send to: ")
        a=float(input("Amount: "))
        if balances.get(name,0)<a+FEE:
            print("Insufficient funds!")
        else:
            balances[name]-=a+FEE
            balances[r]=balances.get(r,0)+a
            balances[name]+=FEE
            save({"blocks":blocks,"balances":balances,"total_mined":data.get("total_mined",0)})
            print(f"Sent {a} FREE to {r}!")
    elif c=="3":
        [print(f"{k}: {v} FREE") for k,v in balances.items()]
    elif c=="4":
        [print(f"Block {b[chr(105)+(chr(110)+chr(100)+chr(101)+chr(120))]}:{b[chr(104)+chr(97)+chr(115)+chr(104)][:16]}...") for b in blocks[-5:]]
    elif c=="5":
        print("Goodbye!")
        break
