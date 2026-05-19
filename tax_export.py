import json, os, time

CHAIN="freedom_chain.json"

def load(): return json.load(open(CHAIN)) if os.path.exists(CHAIN) else {"blocks":[],"balances":{}}

def export_tax():
    print("=== FREEDOM COIN TAX EXPORT ===")
    name = input("Your wallet name: ")
    year = input("Tax year (e.g. 2026): ")
    data = load()
    blocks = data.get("blocks",[])
    balance = data.get("balances",{}).get(name,0)
    report = {
        "wallet": name,
        "tax_year": year,
        "total_blocks_mined": len([b for b in blocks if b.get("miner")==name]),
        "current_balance": balance,
        "total_rewards": len([b for b in blocks if b.get("miner")==name])*50,
        "generated": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    filename = "tax_report_"+year+".json"
    with open(filename,"w") as f:
        json.dump(report,f,indent=2)
    print()
    print("TAX REPORT GENERATED")
    print("Wallet: "+name)
    print("Tax year: "+year)
    print("Blocks mined: "+str(report["total_blocks_mined"]))
    print("Total rewards earned: "+str(report["total_rewards"])+" FREE")
    print("Current balance: "+str(balance)+" FREE")
    print("Saved to: "+filename)
    print()
    print("Share this report with your accountant or tax office")

export_tax()
