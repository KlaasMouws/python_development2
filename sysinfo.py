import platform
import socket
from github import Github
from datetime import datetime
import os

class sysInfo():
    def __init__(self):
        self.dir = "infoLogs"
        self.access_token = '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'
        self.g = Github(self.access_token)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo('pythonDevelopment2')

    def get_info(self):
        current_time = datetime.now()
        self.timeStamp = current_time.strftime("%d-%m-%Y-%Hu%Mm%Ss")
        system_name = platform.platform()
        processor = platform.processor()
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        content = f"Computer name: {hostname}\nSystem name: {system_name}\nProcessor: {processor}\nIP-Address: {ip_addr}"
        print(f"Computer name: {hostname}\nSystem name: {system_name}\nProcessor: {processor}\nIP-Address: {ip_addr}")
        self.write_to_log(content)
        self.send_github()
        
    
    def write_to_log(self, content):
        file_name = f"sysInfo-{self.timeStamp}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "a") as log_file:
            log_file.write(content + "\n")

    def send_github(self):        
        file_name = f"sysInfo-{self.timeStamp}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "rb") as file:
            self.repo.create_file(f"{self.dir}/{file_name}", "Added sysInfo log", file.read())
