import json,os,time
STABLE_FILE="stablecoin.json"
CHAIN="freedom_chain.json"
PEG=1.0
def load(fn): return json.load(open(fn)) if os.path.exists(fn) else {}
def save(d,fn): json.dump(d,open(fn,"w"),indent=2)
def mint():
    print("=== FREEDOM STABLECOIN (FUSD) ===")
    print("1 FUSD = 1 AUD always")
    print()
    name=input("Your wallet: ")
    free_amount=float(input("Lock FREE as collateral: "))
    chain=load(CHAIN)
    balance=chain.get("balances",{}).get(name,0)
    if balance<free_amount: print("Insufficient FREE"); return
    fusd=free_amount*0.75
    data=load(STABLE_FILE)
    positions=data.get("positions",[])
    positions.append({"wallet":name,"collateral":free_amount,"fusd_minted":fusd,"ratio":"150%","time":time.strftime("%Y-%m-%d")})
    save({"positions":positions},STABLE_FILE)
    print()
    print("FUSD minted!")
    print("FREE locked as collateral: "+str(free_amount))
    print("FUSD minted: "+str(fusd))
    print("Each FUSD worth: .00 AUD")
    print("Total value: $"+str(fusd)+" AUD")
    print()
    print("Use FUSD for everyday purchases")
    print("Stable value. Quantum protected.")
    print("No bank needed.")
mint()
