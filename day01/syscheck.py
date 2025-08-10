# syscheck.py
hostname = "server-prod-01"
uptime_days = 15
is_healthy = True

print(f"Host: {hostname}")
print(f"Uptime (days): {uptime_days}")
print(f"Healthy? {is_healthy}")

user = input("Enter your name: ")
print(f"Welcome, {user}. Starting checks...")
