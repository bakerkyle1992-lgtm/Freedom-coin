import hashlib, json, os, random

WORDS = ["apple","bridge","crystal","dragon","eagle","forest","golden","harbor","island","jungle","knight","lemon","mountain","noble","ocean","purple","quantum","river","silver","tiger","umbrella","valley","winter","yellow","zebra","anchor","breeze","castle","desert","ember","falcon","garden","horizon","ivory","jasper","kingdom","lantern","marble","nectar","onyx","phoenix","quartz","rainbow","sapphire","thunder","ultra","violet","warrior","xenon","yarrow","zenith"]

RECOVERY_FILE="recovery.json"

def generate_phrase():
    return " ".join(random.choices(WORDS, k=12))

def create_recovery():
    print("=== FREEDOM COIN RECOVERY PHRASE ===")
    print("Your 12 word recovery phrase is the master key to your wallet")
    print("Write it down and keep it safe offline")
    print()
    phrase = generate_phrase()
    phrase_hash = hashlib.sha256(phrase.encode()).hexdigest()
    recovery = {"phrase_hash": phrase_hash, "created": "2026"}
    with open(RECOVERY_FILE,"w") as f:
        json.dump(recovery,f,indent=2)
    print("YOUR 12 WORD RECOVERY PHRASE:")
    print()
    words = phrase.split()
    for i,w in enumerate(words):
        print(str(i+1)+". "+w)
    print()
    print("WRITE THESE DOWN NOW")
    print("Anyone with these words can access your wallet")
    print("Never share them with anyone")
    print("Store them offline in a safe place")

def verify_recovery():
    if not os.path.exists(RECOVERY_FILE):
        print("No recovery phrase found")
        return
    phrase = input("Enter your 12 word recovery phrase: ")
    stored = json.load(open(RECOVERY_FILE))
    if hashlib.sha256(phrase.encode()).hexdigest() == stored["phrase_hash"]:
        print("Recovery phrase VERIFIED - Wallet access granted")
    else:
        print("Invalid recovery phrase")

print("=== FREEDOM RECOVERY ===")
print("1.Generate Phrase  2.Verify Phrase")
c = input("Choice: ")
if c=="1": create_recovery()
elif c=="2": verify_recovery()
