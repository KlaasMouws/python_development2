import platform
import psutil
import socket
import time

class SysInfo:
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
    





