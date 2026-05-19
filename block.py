import hashlib
import time

def create_block(data, previous_hash):
    timestamp = str(time.time())
    content = data + previous_hash + timestamp
    hash = hashlib.sha256(content.encode()).hexdigest()
    return {
        "data": data,
        "previous_hash": previous_hash,
        "timestamp": timestamp,
        "hash": hash
    }

# Create first block (genesis block)
genesis = create_block("Genesis Block", "0000")
print("Block 1:", genesis["hash"])

# Create second block using first block's hash
block2 = create_block("Send 1 BTC to Alice", genesis["hash"])
print("Block 2:", block2["hash"])

# Create third block
block3 = create_block("Send 0.5 BTC to Bob", block2["hash"])
print("Block 3:", block3["hash"])
