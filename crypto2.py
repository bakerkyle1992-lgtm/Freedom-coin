import hashlib

messages = [
    "Hello Quantum World",
    "Hello Quantum World!",
    "hello Quantum World",
]

for m in messages:
    h = hashlib.sha256(m.encode()).hexdigest()
    print(f"Message: {m}")
    print(f"Hash:    {h}")
    print()
