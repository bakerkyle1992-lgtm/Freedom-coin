import hashlib
import time

def mine_block(data, previous_hash, difficulty=5):
    prefix = "0" * difficulty
    nonce = 0
    print(f"Mining block...")
    while True:
        content = data + previous_hash + str(nonce)
        hash = hashlib.sha256(content.encode()).hexdigest()
        if hash.startswith(prefix):
            print(f"Block mined! Nonce: {nonce}")
            print(f"Hash: {hash}")
            return hash, nonce
        nonce += 1

start = time.time()
hash1, nonce1 = mine_block("Alice sends 10 coins to Bob", "0000")
end = time.time()

print(f"Time taken: {round(end-start, 2)} seconds")
