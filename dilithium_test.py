from dilithium_py.dilithium import Dilithium2

print("=== CRYSTALS-Dilithium Test ===")
print("NIST approved quantum resistant signatures")
print()

pk, sk = Dilithium2.keygen()
print(f"Public key size: {len(pk)} bytes")
print(f"Secret key size: {len(sk)} bytes")

msg = b"Alice sends 10 FREE to Bob"
sig = Dilithium2.sign(sk, msg)
print(f"Signature size: {len(sig)} bytes")

valid = Dilithium2.verify(pk, msg, sig)
print(f"Signature valid: {valid}")

tampered = Dilithium2.verify(pk, b"Alice sends 999 FREE to Bob", sig)
print(f"Tampered valid: {tampered}")

print()
print("FREEDOM coin now uses true quantum resistance!")
