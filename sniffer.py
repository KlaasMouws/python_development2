from scapy.all import *
from scapy.layers.inet import IP
from github import Github
import time
import random
class Sniffer:
    def __init__(self, packet_count=10):
        self.teller = 0
        self.dir = "snifferlogs"
        self.packet_count = packet_count
        self.access_token = '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'
        self.g = Github(self.access_token)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo('python_development')

    def packet_handler(self, packet):
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto

            content = f"Source IP: {src_ip}  Destination IP: {dst_ip}  Protocol: {protocol}"
            self.teller = random.randint(0,10000000)
            x = range(20)
            for n in x:
                self.write_to_log(content)
                time.sleep(1)
            self.send_github()
            exit()

    def write_to_log(self, content):
        file_name = f"snifferLog-{self.teller}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "a") as log_file:
            log_file.write(content + "\n")

    def send_github(self):        
        file_name = f"snifferLog-{self.teller}"
        log_path = os.path.join(self.dir, file_name)
        with open(log_path, "rb") as file:
            self.repo.create_file(f"{self.dir}/{file_name}", "Added sniffer log", file.read())
    def start_sniffing(self):
        sniff(filter="ip", prn=self.packet_handler, count=self.packet_count)


s = Sniffer()
s.start_sniffing()