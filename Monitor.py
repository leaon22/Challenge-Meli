import json
import platform
import psutil
import requests
import socket
import csv
from datetime import datetime


# Hostname and IP Address
hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)
print("hostname is", hostname)
print("hostip is", hostip)
# Processor type
print(f"Processor type: {platform.processor()}")
# Platform type
print(f"Platform type: {platform.platform()}")
# Operating system
print(f"Operating system: {platform.system()}")
# Operating system release
print(f"Operating system release: {platform.release()}")
# Operating system version
print(f"Operating system version: {platform.version()}")
# Physical cores
print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
# Logical cores
print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")
# Current frequency
print(f"Current CPU frequency: {psutil.cpu_freq().current}")
# System-wide CPU utilization
print(f"Current CPU utilization: {psutil.cpu_percent(interval=1)}")
# Number of Users
print(f"Number of Users: {psutil.users()}")
# Number of Process
print(f"Number of Process: {psutil.Process()}")

data = {
    "processorType": platform.processor(),
    "platformType": platform.platform(),
    "operatingSystem": platform.system(),
    "operatingSystemRelease": platform.release(),
    "operatingSystemVersion": platform.version(),
    "numberOfPhysicalCores": psutil.cpu_count(logical=False),
    "numberOfLogicalCores": psutil.cpu_count(logical=True),
    "currentCpuFrequency": psutil.cpu_freq().current,
    "numberOfUsers": psutil.users(),
    "numberOfProcess": psutil.Process(),
    "hostname": socket.gethostname(),
    "hostip": socket.gethostbyname(hostname),
}

r = requests.post(
    "http://localhost:4333/monitor",
    json=data,
    headers={"Content-Type": "application/json"},
)
print(r.json())
