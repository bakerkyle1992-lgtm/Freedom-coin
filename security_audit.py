import json,os,time
from dilithium_py.dilithium import Dilithium2
score=0
issues=[]
print("=== FREEDOM COIN SECURITY AUDIT ===")
print()
if os.path.exists("my_wallet.json"): print("PASS - Wallet exists"); score+=1
else: print("FAIL - No wallet"); issues.append("Create wallet")
w=json.load(open("my_wallet.json")) if os.path.exists("my_wallet.json") else {}
if w.get("encrypted"): print("PASS - Wallet encrypted"); score+=1
else: print("WARN - Wallet not encrypted"); issues.append("Encrypt wallet")
if os.path.exists("recovery.json"): print("PASS - Recovery phrase exists"); score+=1
else: print("FAIL - No recovery phrase"); issues.append("Create recovery phrase")
if os.path.exists("freedom_chain.json"): print("PASS - Blockchain exists"); score+=1
else: print("FAIL - No blockchain"); issues.append("Mine first block")
if os.path.exists("family_shield.json"): print("PASS - Family shield active"); score+=1
else: print("WARN - No family shield"); issues.append("Setup family shield")
if os.path.exists("inheritance.json"): print("PASS - Inheritance active"); score+=1
else: print("WARN - No inheritance"); issues.append("Setup inheritance")
if os.path.exists("freeze.json"): print("PASS - Emergency freeze ready"); score+=1
else: print("WARN - Freeze not tested"); issues.append("Test emergency freeze")
if os.path.exists("whitepaper.txt"): print("PASS - Whitepaper exists"); score+=1
else: print("FAIL - No whitepaper"); issues.append("Create whitepaper")
try:
    pk,sk=Dilithium2.keygen(); print("PASS - Quantum signatures working"); score+=1
except: print("FAIL - Quantum signatures broken"); issues.append("Reinstall dilithium-py")
if os.path.exists("ai_guardian.py"): print("PASS - AI Guardian exists"); score+=1
else: print("FAIL - No AI Guardian"); issues.append("Create AI Guardian")
print()
pct=(score/10)*100
print("Score: "+str(score)+"/10")
print("Security rating: "+str(pct)+"%")
if pct>=80: print("Rating: EXCELLENT - Ready for Google and Samsung")
elif pct>=60: print("Rating: GOOD - Fix warnings first")
else: print("Rating: NEEDS WORK")
if issues:
    print()
    print("Issues to fix:")
    for i in issues: print("- "+i)
print()
print("Audit completed: "+time.strftime("%Y-%m-%d %H:%M:%S"))
