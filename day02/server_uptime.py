import os
import subprocess

hostname= subprocess.run(["hostname"], capture_output=True, text=True).stdout.strip()
uptime_server = subprocess.run(["uptime" , "-p"], capture_output=True, text=True).stdout.strip()

with open("/proc/loadavg","r") as f:
    load_avg = f.read().split()[0]

print(f"Hostname is {hostname}")
print(f"Server is up from {uptime_server}")
print(f"Load average is {load_avg}")

