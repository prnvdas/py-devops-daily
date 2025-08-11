load = float(input("Enter the load: "))

if load > 1.0:
    print("Load is high, checking system status...")
elif  load > 0.5:
    print("Load is normal, proceeding with checks...")
else:
    print("Load is low, system is idle.")