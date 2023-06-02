from scapy.all import *
from scapy.layers.inet import IP

class Sniffer:
    def __init__(self, packet_count=10):
        self.packet_count = packet_count

    def packet_handler(self, packet):
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = packet[IP].proto

            print(f"Source IP: {src_ip}  Destination IP: {dst_ip}  Protocol: {protocol}")

    def start_sniffing(self):
        sniff(filter="ip", prn=self.packet_handler, count=self.packet_count)
