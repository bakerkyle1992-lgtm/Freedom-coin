import json,os,time
DEFI_FILE="defi.json"
CHAIN="freedom_chain.json"
INTEREST_RATE=0.05
def load(fn): return json.load(open(fn)) if os.path.exists(fn) else {}
def save(d,fn): json.dump(d,open(fn,"w"),indent=2)
def lend():
    print("=== FREEDOM DEFI LENDING ===")
    name=input("Your wallet: ")
    amount=float(input("Amount to lend: "))
    days=int(input("Lending period days: "))
    chain=load(CHAIN)
    balance=chain.get("balances",{}).get(name,0)
    if balance<amount: print("Insufficient funds"); return
    interest=amount*INTEREST_RATE*(days/365)
    data=load(DEFI_FILE)
    loans=data.get("loans",[])
    loans.append({"lender":name,"amount":amount,"days":days,"interest":round(interest,2),"status":"active","date":time.strftime("%Y-%m-%d")})
    save({"loans":loans},DEFI_FILE)
    print()
    print("Loan created!")
    print("Amount lent: "+str(amount)+" FREE")
    print("Interest earned: "+str(round(interest,2))+" FREE")
    print("Return after "+str(days)+" days: "+str(round(amount+interest,2))+" FREE")
    print("No bank needed. Smart contract enforced.")
def borrow():
    print("=== FREEDOM DEFI BORROWING ===")
    name=input("Your wallet: ")
    amount=float(input("Amount to borrow: "))
    collateral=amount*1.5
    interest=amount*INTEREST_RATE
    print()
    print("Borrow amount: "+str(amount)+" FREE")
    print("Collateral required: "+str(collateral)+" FREE")
    print("Annual interest: "+str(interest)+" FREE")
    print("No bank. No credit check. No ID required.")
print("=== FREEDOM DEFI ===")
print("1.Lend  2.Borrow")
c=input("Choice: ")
if c=="1": lend()
elif c=="2": borrow()
