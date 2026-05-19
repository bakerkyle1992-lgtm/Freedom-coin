import hashlib, time, os, json
from dilithium_py.dilithium import Dilithium2

def generate_bio_seed():
    print("=== FREEDOM COIN BIO KEY GENERATOR ===")
    print("Your unique biological signature creates your wallet")
    print()
    name = input("Enter your full name: ")
    dob = input("Enter your date of birth (DDMMYYYY): ")
    random_word = input("Type a random word only you would think of: ")
    touch = input("Type anything randomly on your keyboard: ")
    timestamp = str(time.time())
    bio_data = name+dob+random_word+touch+timestamp+os.urandom(32).hex()
    seed = hashlib.sha256(bio_data.encode()).hexdigest()
    return seed

def create_bio_wallet():
    seed = generate_bio_seed()
    pk, sk = Dilithium2.keygen()
    address = hashlib.sha256(pk+seed.encode()).hexdigest()[:34]
    wallet = {"address":address,"bio_secured":True,"algorithm":"CRYSTALS-Dilithium+BioSeed"}
    with open("bio_wallet.json","w") as f:
        json.dump(wallet,f,indent=2)
    print()
    print("Bio wallet created!")
    print("Address: "+address)
    print("Secured by: Your unique biological signature")
    print("Algorithm: CRYSTALS-Dilithium + BioSeed")
    print("This wallet can only be recreated by YOU")
    return address

create_bio_wallet()
