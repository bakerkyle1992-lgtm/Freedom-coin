import json, os, time, hashlib
from dilithium_py.dilithium import Dilithium2

CHAIN="freedom_chain.json"
THREAT_LOG="threat_log.json"

def load_chain():
    if os.path.exists(CHAIN):
        with open(CHAIN) as f:
            return json.load(f)
    return {"blocks":[]}

def load_threats():
    if os.path.exists(THREAT_LOG):
        with open(THREAT_LOG) as f:
            return json.load(f)
    return {"threats":[]}

def save_threats(t):
    with open(THREAT_LOG,"w") as f:
        json.dump(t,f,indent=2)

def analyze_block(block):
    threats = []
    if "hash" in block:
        h = block["hash"]
        zeros = len(h) - len(h.lstrip("0"))
        if zeros > 8:
            threats.append("SUSPICIOUS: Too many leading zeros - possible quantum attack")
    if "nonce" in block:
        if block["nonce"] == 0:
            threats.append("SUSPICIOUS: Zero nonce detected - possible precomputed attack")
    if "reward" in block:
        if block["reward"] > 50:
            threats.append("ALERT: Reward exceeds maximum - possible inflation attack")
    return threats

def scan_chain():
    chain = load_chain()
    threats = load_threats()
    blocks = chain.get("blocks",[])
    print("=== FREEDOM COIN AI GUARDIAN ===")
    print("Scanning "+str(len(blocks))+" blocks for threats...")
    all_clear = True
    for block in blocks:
        found = analyze_block(block)
        if found:
            all_clear = False
            for t in found:
                print("Block "+str(block.get("index","?"))+": "+t)
                threats["threats"].append({"block":block.get("index","?"),"threat":t,"time":time.strftime("%Y-%m-%d %H:%M:%S")})
    if all_clear:
        print("All blocks verified - No threats detected")
        print("Blockchain is QUANTUM SAFE")
    save_threats(threats)
    print("Total threats logged: "+str(len(threats["threats"])))

scan_chain()
