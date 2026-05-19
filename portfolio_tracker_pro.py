import urllib.request, json, time

print("=== CRYPTO PORTFOLIO TRACKER PRO ===")
print("Enter your holdings (0 if you don't own it)\n")

coins = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "solana": "SOL",
    "cardano": "ADA",
    "ripple": "XRP"
}

holdings = {}
for coin, symbol in coins.items():
    amount = float(input(f"How many {symbol} do you own? "))
    holdings[coin] = amount

print("\nFetching live prices...\n")
total = 0
for coin, symbol in coins.items():
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=aud"
        req = urllib.request.urlopen(url)
        data = json.loads(req.read())
        price = data[coin]["aud"]
        value = price * holdings[coin]
        total += value
        if holdings[coin] > 0:
            print(f"{symbol}: {holdings[coin]} x ${price:,} = ${value:,.2f} AUD")
        time.sleep(1)
    except Exception as e:
        print(f"{symbol}: Price unavailable")

print(f"\nTOTAL PORTFOLIO VALUE: ${total:,.2f} AUD")
