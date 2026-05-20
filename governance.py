import json,os,time
GOVERN_FILE="governance.json"
CHAIN="freedom_chain.json"
def load(fn): return json.load(open(fn)) if os.path.exists(fn) else {}
def save(d,fn): json.dump(d,open(fn,"w"),indent=2)
def create_proposal():
    print("=== FREEDOM GOVERNANCE ===")
    title=input("Proposal title: ")
    desc=input("Description: ")
    days=int(input("Voting days: "))
    data=load(GOVERN_FILE)
    proposals=data.get("proposals",[])
    p={"id":len(proposals)+1,"title":title,"desc":desc,"yes":0,"no":0,"deadline":time.strftime("%Y-%m-%d"),"status":"active"}
    proposals.append(p)
    save({"proposals":proposals},GOVERN_FILE)
    print("Proposal created! ID: "+str(p["id"]))
def vote():
    data=load(GOVERN_FILE)
    proposals=data.get("proposals",[])
    if not proposals: print("No proposals"); return
    for p in proposals:
        print(str(p["id"])+". "+p["title"])
    pid=int(input("Proposal ID: "))
    v=input("Vote yes or no: ")
    wallet=json.load(open("my_wallet.json")) if os.path.exists("my_wallet.json") else {}
    chain=load(CHAIN)
    balance=chain.get("balances",{}).get(wallet.get("name",""),0)
    for p in proposals:
        if p["id"]==pid:
            if v=="yes": p["yes"]+=int(balance)
            else: p["no"]+=int(balance)
            print("Vote cast! Weight: "+str(int(balance))+" FREE")
            print("Yes: "+str(p["yes"])+" No: "+str(p["no"]))
    save({"proposals":proposals},GOVERN_FILE)
print("1.Create Proposal 2.Vote 3.Exit")
c=input("Choice: ")
if c=="1": create_proposal()
elif c=="2": vote()
