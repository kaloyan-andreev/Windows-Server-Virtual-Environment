from datetime import timedelta
from time import time
import platform
import psutil
import socket

# Server name
def ID():
    return platform.node()

# Get ip of the machine
def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

# Server OS
def OS():
    return platform.system()

# Total CPU cores
def cpu_cores():
    return psutil.cpu_count()

# CPU usage
def cpu_usage():
    while True:
        return (f"{psutil.cpu_percent(interval=1)} %")

# Total Ram installed
def total_memory():
    return int(round(psutil.virtual_memory().total/1000000000, 2))

# Merory usage
def memory_usage():
    while True:
        return f"{psutil.virtual_memory().percent} %"




"""ADDITIONAL FUNCTIONS"""

# # Boot time
# def boot_time():
#     while True:
#         return str(timedelta(seconds=time()-psutil.boot_time()))

# # CPU cores - phisical
# def phis_CPU():
#     return psutil.cpu_count(logical=False)

# # CPU cores - logical
# def log_CPU():
#     return psutil.cpu_count(logical=True)