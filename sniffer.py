from scapy.all import *
from scapy.layers.inet import IP
from github import Github
import time
from datetime import datetime
class Sniffer:
    def __init__(self, packet_count=10):
        self.teller = 0
        self.dir = "snifferlogs"
        self.packet_count = packet_count
        self.access_token = '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'
        self.g = Github(self.access_token)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo('pythonDevelopment2')

    def packet_handler(self, packet):
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto

            content = f"Source IP: {src_ip}  Destination IP: {dst_ip}  Protocol: {protocol}"
            current_time = datetime.now()
            self.timeStamp = current_time.strftime("%d-%m-%Y-%Hu%Mm%Ss")
            x = range(5)
            for n in x:
                self.write_to_log(content)
                time.sleep(1)
            self.send_github()

    def write_to_log(self, content):
        file_name = f"snifferLog-{self.timeStamp}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "a") as log_file:
            log_file.write(content + "\n")

    def send_github(self):        
        file_name = f"snifferLog-{self.timeStamp}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "rb") as file:
            self.repo.create_file(f"{self.dir}/{file_name}", "Added sniffer log", file.read())
    def start_sniffing(self):
        print("Het programma begint met sniffen.")
        sniff(filter="ip", prn=self.packet_handler, count=self.packet_count)

