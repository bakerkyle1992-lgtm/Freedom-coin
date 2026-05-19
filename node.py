import socket,json,os,threading
CHAIN="freedom_chain.json"
PORT=5000
def load(): return json.load(open(CHAIN)) if os.path.exists(CHAIN) else {"blocks":[],"balances":{},"total_mined":0}
def handle(conn):
    data=load()
    conn.send(json.dumps(data).encode())
    conn.close()
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("0.0.0.0",PORT))
s.listen(5)
print("FREEDOM coin node running on 192.168.1.6:"+str(PORT))
print("Other devices can connect to sync the blockchain")
print("Press Ctrl+C to stop")
while True:
    conn,addr=s.accept()
    print("Device connected: "+str(addr))
    t=threading.Thread(target=handle,args=(conn,))
    t.start()
