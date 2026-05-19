import json, os, time

RATE_FILE="rate_limits.json"
MAX_TX_PER_MINUTE = 10

def load(): return json.load(open(RATE_FILE)) if os.path.exists(RATE_FILE) else {"transactions":{}}
def save(d): json.dump(d,open(RATE_FILE,"w"),indent=2)

def check_rate(wallet):
    data = load()
    now = time.time()
    txs = data["transactions"].get(wallet,[])
    recent = [t for t in txs if now - t < 60]
    if len(recent) >= MAX_TX_PER_MINUTE:
        print("RATE LIMIT: Too many transactions")
        print("Max "+str(MAX_TX_PER_MINUTE)+" transactions per minute")
        print("Possible attack detected - transaction blocked")
        return False
    recent.append(now)
    data["transactions"][wallet] = recent
    save(data)
    print("Transaction approved: "+str(len(recent))+"/"+str(MAX_TX_PER_MINUTE)+" this minute")
    return True

print("=== FREEDOM RATE LIMITER ===")
wallet = input("Wallet name: ")
print("Checking rate limit...")
check_rate(wallet)
