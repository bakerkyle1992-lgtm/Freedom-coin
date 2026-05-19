import qrcode, json, os

WALLET_FILE="my_wallet.json"

def generate_qr():
    print("=== FREEDOM COIN QR GENERATOR ===")
    if os.path.exists(WALLET_FILE):
        wallet = json.load(open(WALLET_FILE))
        address = wallet.get("address","no address found")
    else:
        address = input("Enter wallet address: ")
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(address)
    qr.make(fit=True)
    qr.print_ascii()
    print()
    print("Address: "+address)
    print("Scan QR code to send FREE coins to this wallet")

generate_qr()
