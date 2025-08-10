import os
import subprocess

# Get hostname (like `hostname` in bash)
hostname = subprocess.run(["hostname"], capture_output=True, text=True).stdout.strip()

# Get uptime output (like `uptime -p`)
uptime_output = subprocess.run(["uptime", "-p"], capture_output=True, text=True).stdout.strip()

# Get load average from /proc/loadavg
with open("/proc/loadavg", "r") as f:
    load_avg = f.read().split()[0]  # first number = 1-min load

print(f"Server: {hostname}")
print(f"Uptime: {uptime_output}")
print(f"Load Average (1 min): {load_avg}")
