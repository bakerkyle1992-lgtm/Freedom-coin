import socket, json, os, time

NODES_FILE="known_nodes.json"
PORT=5000

def load(): return json.load(open(NODES_FILE)) if os.path.exists(NODES_FILE) else {"nodes":[]}
def save(d): json.dump(d,open(NODES_FILE,"w"),indent=2)

def get_local_ip():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip=s.getsockname()[0]
    s.close()
    return ip

def discover_nodes():
    print("=== FREEDOM NODE DISCOVERY ===")
    local_ip = get_local_ip()
    base_ip = ".".join(local_ip.split(".")[:3])
    print("Scanning network for FREEDOM coin nodes...")
    print("Local IP: "+local_ip)
    found = []
    for i in range(1,10):
        ip = base_ip+"."+str(i)
        if ip == local_ip:
            continue
        try:
            s=socket.socket()
            s.settimeout(0.5)
            s.connect((ip,PORT))
            found.append(ip)
            print("Found node: "+ip)
            s.close()
        except:
            pass
    if not found:
        print("No other nodes found on network")
        print("You are the first node - start sharing FREEDOM coin")
    else:
        print("Found "+str(len(found))+" nodes")
    data = load()
    data["nodes"] = found
    data["last_scan"] = time.strftime("%Y-%m-%d %H:%M:%S")
    save(data)
    print("Node list saved")

discover_nodes()
