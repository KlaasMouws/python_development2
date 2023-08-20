import psutil
import os
from github import Github
from datetime import datetime
import time

class getMemory:
    def __init__(self):
        self.dir = "memorylogs"
        self.access_token = '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'
        self.g = Github(self.access_token)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo('pythonDevelopment2')

    
    def get_usage(self, cpu_usage, mem_usage, bars=50):
        cpu_percent = cpu_usage / 100
        cpu_bar = "|" * int(cpu_percent * bars) + "-" * (bars - int(cpu_percent * bars))

        mem_percent = mem_usage / 100
        mem_bar = "|" * int(mem_percent * bars) + "-" * (bars - int(mem_percent * bars))

        print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  MEM usage: |{mem_bar}| {mem_usage:.2f}%", end="")
        content = f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  MEM usage: |{mem_bar}| {mem_usage:.2f}%"
        current_time = datetime.now()
        self.timeStamp = current_time.strftime("%d-%m-%Y-%Hu%Mm%Ss")
        x = range(5)
        for n in x:
            self.write_to_log(content)
            time.sleep(1)
        self.send_github()
    
    def write_to_log(self, content):
        file_name = f"memoryLog-{self.timeStamp}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "a") as log_file:
            log_file.write(content + "\n")

    def send_github(self):        
        file_name = f"memoryLog-{self.timeStamp}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "rb") as file:
            self.repo.create_file(f"{self.dir}/{file_name}", "Added memory log", file.read())

    