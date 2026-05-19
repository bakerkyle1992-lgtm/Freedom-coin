import urllib.request, json

coins = {
    "bitcoin": "BTC",
    "ethereum": "ETH",
    "solana": "SOL"
}

print("=== CRYPTO PORTFOLIO TRACKER ===")
for coin, symbol in coins.items():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=aud"
    req = urllib.request.urlopen(url)
    data = json.loads(req.read())
    price = data[coin]["aud"]
    print(f"{symbol}: ${price:,} AUD")
