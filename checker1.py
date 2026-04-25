Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import hashlib
... 
... def check_file():
...     print("--- File Integrity Checker ---")
...     # 1. Ask for the file name
...     filename = input("Enter the file name (e.g., secret_data.txt): ")
...     
...     try:
...         # 2. Calculate the Digital Fingerprint (SHA-256)
...         sha256_hash = hashlib.sha256()
...         
...         # We open the file in 'rb' (read binary) mode
...         with open(filename, "rb") as f:
...             # Read the file in small chunks to be safe with memory
...             for byte_block in iter(lambda: f.read(4096), b""):
...                 sha256_hash.update(byte_block)
...         
...         current_fingerprint = sha256_hash.hexdigest()
...         
...         print(f"\n[+] Current Fingerprint: {current_fingerprint}")
...         
...         # 3. Verification Logic
...         # NOTE: This baseline matches "Hello World" exactly. 
...         # If your file has different text, the check will say "WARNING".
...         baseline = "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"
...         
...         if current_fingerprint == baseline:
...             print("✅ VERIFIED: The file is authentic and unchanged.")
...         else:
...             print("❌ WARNING: The file has been modified or is a different file!")
...             
...     except FileNotFoundError:
...         print("\n[!] Error: File not found. Make sure the file is in the same folder as this script.")
... 
... # This line starts the program
... check_file()
... 
# This line keeps the window from closing automatically
input("\nExecution finished. Press Enter to close this window...")
[DEBUG ON]
[DEBUG OFF]
