import platform
import socket
from github import Github
import random
import os
import time
import psutil

class SysInfo:
    def __init__(self, packet_count=10):
        self.teller = 0
        self.dir = "memorylogs"
        self.packet_count = packet_count
        self.access_token = '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'
        self.g = Github(self.access_token)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo('python_development')

    def get_info(self):
        system_name = platform.platform()
        processor = platform.processor()
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        print(f"Computer name: {hostname}\nSystem name: {system_name}\nProcessor: {processor}\nIP-Address: {ip_addr}")

    def get_usage(self, cpu_usage, mem_usage, bars=50):
        cpu_percent = cpu_usage / 100
        cpu_bar = "|" * int(cpu_percent * bars) + "-" * (bars - int(cpu_percent * bars))

        mem_percent = mem_usage / 100
        mem_bar = "|" * int(mem_percent * bars) + "-" * (bars - int(mem_percent * bars))

        print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  MEM usage: |{mem_bar}| {mem_usage:.2f}%", end="")
        content = f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  MEM usage: |{mem_bar}| {mem_usage:.2f}%"
        self.teller = random.randint(0,10000000)
        x = range(5)
        for n in x:
            self.write_to_log(content)
            time.sleep(1)
        self.send_github()
        exit()
    
    def write_to_log(self, content):
        file_name = f"memoryLog-{self.teller}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "a") as log_file:
            log_file.write(content + "\n")

    def send_github(self):        
        file_name = f"memoryLog-{self.teller}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "rb") as file:
            self.repo.create_file(f"{self.dir}/{file_name}", "Added memory log", file.read())



s = SysInfo()
s.get_usage(psutil.cpu_percent(), psutil.virtual_memory().percent,30)