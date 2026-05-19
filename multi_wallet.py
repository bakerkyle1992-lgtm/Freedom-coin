import json, os
from dilithium_py.dilithium import Dilithium2
import hashlib
WALLETS_FILE = 'all_wallets.json'
CHAIN_FILE = 'freedom_chain.json'
wallets = json.load(open(WALLETS_FILE)) if os.path.exists(WALLETS_FILE) else {}
data = json.load(open(CHAIN_FILE)) if os.path.exists(CHAIN_FILE) else {'blocks':[],'balances':{},'total_mined':0}
balances = data['balances']
while True:
    print('=== FREEDOM WALLETS ===')
    print('1.New 2.Balance 3.Send 4.All 5.Exit')
    c = input('Choice: ')
    if c == '5':
        break
    elif c == '4':
        [print(k,':',v,'FREE') for k,v in balances.items()]
    elif c == '2':
        n = input('Name: ')
        print(n,':',balances.get(n,0),'FREE')
    elif c == '3':
        s = input('From: ')
        r = input('To: ')
        a = int(input('Amount: '))
        if balances.get(s,0) < a:
            print('Insufficient funds!')
        else:
            balances[s] -= a
            balances[r] = balances.get(r,0) + a
            data['balances'] = balances
            json.dump(data,open(CHAIN_FILE,'w'),indent=2)
            print('Sent!')
