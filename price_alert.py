
import urllib.request, json, time

def get_price(coin):
    url = "https://api.coingecko.com/api/v3/simple/price?ids="+coin+"&vs_currencies=aud"
    try:
        req = urllib.request.urlopen(url)
        data = json.loads(req.read())
        return data[coin]["aud"]
    except:
        return None

print("=== CRYPTO PRICE ALERT BOT ===")
coin = input("Coin (bitcoin/ethereum/solana): ")
target = float(input("Alert above: "))
low = float(input("Alert below: "))
print("Monitoring... Press Ctrl+C to stop")

while True:
    price = get_price(coin)
    if price:
        print("Price: "+str(price)+" AUD")
        if price >= target:
            print("ALERT - Price above target of "+str(target))
        elif price <= low:
            print("ALERT - Price below "+str(low))
    time.sleep(30)
