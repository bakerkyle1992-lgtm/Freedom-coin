import json, os, time

STAKE_FILE="staking.json"
CHAIN="freedom_chain.json"
STAKE_REWARD = 0.05

def load(fn): return json.load(open(fn)) if os.path.exists(fn) else {}
def save(d,fn): json.dump(d,open(fn,"w"),indent=2)

def stake_coins():
    print("=== FREEDOM COIN STAKING ===")
    print("Earn 5% annual rewards by staking your FREE coins")
    print()
    name = input("Your wallet name: ")
    amount = float(input("Amount to stake: "))
    chain = load(CHAIN)
    balance = chain.get("balances",{}).get(name,0)
    if balance < amount:
        print("Insufficient balance")
        return
    annual_reward = amount * STAKE_REWARD
    monthly_reward = annual_reward / 12
    stake = {
        "wallet": name,
        "amount": amount,
        "annual_reward": annual_reward,
        "monthly_reward": monthly_reward,
        "started": time.strftime("%Y-%m-%d"),
        "status": "active"
    }
    save(stake, STAKE_FILE)
    print()
    print("Staking activated!")
    print("Wallet: "+name)
    print("Staked amount: "+str(amount)+" FREE")
    print("Annual reward: "+str(annual_reward)+" FREE")
    print("Monthly reward: "+str(round(monthly_reward,2))+" FREE")
    print()
    print("Your coins are working for you while you sleep")

stake_coins()
