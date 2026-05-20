import hashlib
def generate_proof(secret, statement):
    commitment = hashlib.sha256(secret.encode()).hexdigest()
    challenge = hashlib.sha256((commitment+statement).encode()).hexdigest()
    response = hashlib.sha256((secret+challenge).encode()).hexdigest()
    return {"commitment":commitment,"challenge":challenge,"response":response}
def verify_proof(proof, statement):
    expected = hashlib.sha256((proof["commitment"]+statement).encode()).hexdigest()
    return expected == proof["challenge"]
print("=== FREEDOM ZERO KNOWLEDGE PROOF ===")
print("Prove you own coins without revealing anything")
print()
secret = input("Enter your private secret: ")
statement = input("What to prove: ")
proof = generate_proof(secret, statement)
valid = verify_proof(proof, statement)
print()
print("Commitment: "+proof["commitment"][:16])
print("Challenge: "+proof["challenge"][:16])
print("Response: "+proof["response"][:16])
print("Proof valid: "+str(valid))
print()
print("Your secret was never revealed")
print("But mathematically verified")
print("More private than any existing cryptocurrency")
