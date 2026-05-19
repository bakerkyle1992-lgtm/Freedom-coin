import json,os,time
NOTIF="notifications.json"
def load(): return json.load(open(NOTIF)) if os.path.exists(NOTIF) else {"notifications":[]}
def save(d): json.dump(d,open(NOTIF,"w"),indent=2)
def add(t,m):
    d=load()
    d["notifications"].append({"type":t,"msg":m,"time":time.strftime("%H:%M:%S"),"read":False})
    save(d)
def check():
    d=load()
    un=[n for n in d["notifications"] if not n["read"]]
    if not un: print("No new notifications"); return
    print(str(len(un))+" new notifications")
    for n in un:
        print("["+n["type"]+"] "+n["msg"]+" at "+n["time"])
        n["read"]=True
    save(d)
print("1.Check 2.Test")
c=input("Choice: ")
if c=="2":
    add("RECEIVED","You received 50 FREE")
    add("MINING","Block mined reward 50 FREE")
    add("SECURITY","New node connected")
    print("Test notifications sent")
elif c=="1": check()
