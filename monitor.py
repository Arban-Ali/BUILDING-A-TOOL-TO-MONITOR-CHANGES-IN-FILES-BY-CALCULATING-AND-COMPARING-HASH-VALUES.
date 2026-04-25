import hashlib
import time
import os

# 1. Ask for the file to monitor
file_to_check = input("Enter the full path of the file to monitor: ")

def get_hash(filename):
    """This function calculates the file's unique fingerprint."""
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        # Read the file in small chunks to handle any file size
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# 2. Create the 'Baseline' (Initial fingerprint)
print("Creating baseline... please wait.")
baseline_hash = get_hash(file_to_check)
print(f"Initial Fingerprint: {baseline_hash}\nMonitoring for changes...")

# 3. Continuous Monitoring Loop
try:
    while True:
        time.sleep(2)  # Wait 2 seconds between checks
        current_hash = get_hash(file_to_check)
        
        if current_hash != baseline_hash:
            print(f"!!! ALERT: Change detected at {time.ctime()} !!!")
            print(f"New Fingerprint: {current_hash}")
            # Update the baseline so it stops alerting until the next change
            baseline_hash = current_hash
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
