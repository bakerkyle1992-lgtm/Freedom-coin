import json, os, time

CHAIN="freedom_chain.json"
BURN_FILE="burn_log.json"
BURN_ADDRESS="0000000000000000000000000000000000"

def load(fn): return json.load(open(fn)) if os.path.exists(fn) else {}
def save(d,fn): json.dump(d,open(fn,"w"),indent=2)

def burn_coins():
    print("=== FREEDOM COIN BURN ===")
    print("Burning coins reduces supply and increases value")
    print()
    name = input("Your wallet name: ")
    amount = float(input("Amount to burn: "))
    chain = load(CHAIN)
    balances = chain.get("balances",{})
    if balances.get(name,0) < amount:
        print("Insufficient balance")
        return
    balances[name] -= amount
    chain["balances"] = balances
    save(chain, CHAIN)
    burn_log = load(BURN_FILE)
    burns = burn_log.get("burns",[])
    burns.append({"wallet":name,"amount":amount,"time":time.strftime("%Y-%m-%d %H:%M:%S")})
    save({"burns":burns,"total_burned":sum(b["amount"] for b in burns)}, BURN_FILE)
    total = sum(b["amount"] for b in burns)
    print()
    print("COINS BURNED FOREVER")
    print("Amount burned: "+str(amount)+" FREE")
    print("Total ever burned: "+str(total)+" FREE")
    print("These coins are gone forever")
    print("Remaining supply reduced - your coins are worth more")

burn_coins()
