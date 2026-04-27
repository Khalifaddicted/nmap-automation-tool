import os
import sys

if len(sys.argv) != 2:
    print("Usage: python3 nmap_auto.py <target>")
    sys.exit(1)

target = sys.argv[1]

print(f"[+] Starting scan on: {target}")
command = f"nmap -sV -A {target} -oN scan_results.txt"

os.system(command)

print("[+] Scan complete. Results saved to scan_results.txt")