import platform
import psutil
import socket
import time

def getInfo():
    comp_name = platform.node()
    system_name =platform.platform()
    processor = platform.processor()

def getIP():
    hostname = socket.gethostname()
    ipAddr = socket.gethostbyname(hostname)
    print(f"\nHostname : {hostname}")
    print(f"IP-address : {ipAddr} \n")

def getUsage(cpu_usage, mem_usage, bars = 50):
    cpu_precent = (cpu_usage / 100)
    cpu_bar = '' * int(cpu_precent * bars)+ '-' * (bars - int(cpu_precent*bars)) 

    mem_precent = (mem_usage / 100)
    mem_bar = '' * int(mem_precent*bars)+'-'*(bars-int(mem_precent*bars))

    print(f"\r CPU Usage: |{cpu_bar}| {cpu_usage:.2f}%", end="")
    print (f"MEM usage: |{mem_bar}| {mem_usage: .2f}%  ", end="\r")


while True:
    getUsage(psutil.cpu_percent(), psutil.virtual_memory().percent,30)
    time.sleep(0.5)



