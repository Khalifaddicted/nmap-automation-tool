import os
import sys
import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# -----------------------------
# Utility Functions
# -----------------------------

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def save_output(filename, content):
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    path = os.path.join(logs_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(Fore.GREEN + f"[+] Results saved to {path}")

def run_nmap(command, target):
    print(Fore.YELLOW + f"[+] Running scan on {target}...")
    full_command = f"{command} {target}"
    result = os.popen(full_command).read()

    if not result.strip():
        print(Fore.RED + "[!] No output received. Check your target or Nmap installation.")
        return

    filename = f"scan_{timestamp()}.txt"
    save_output(filename, result)

# -----------------------------
# Scan Modes
# -----------------------------

def quick_scan(target):
    run_nmap("nmap -T4 -F", target)

def full_scan(target):
    run_nmap("nmap -sV -A -T4", target)

def stealth_scan(target):
    run_nmap("nmap -sS -T3", target)

def os_scan(target):
    run_nmap("nmap -O", target)

def vuln_scan(target):
    run_nmap("nmap --script vuln", target)

def port_range_scan(target):
    ports = input("Enter port range (e.g., 1-1000): ")
    run_nmap(f"nmap -p {ports}", target)

def multi_target_scan(file_path):
    if not os.path.exists(file_path):
        print(Fore.RED + "[!] File not found.")
        return

    with open(file_path, "r") as f:
        targets = [line.strip() for line in f.readlines()]

    for target in targets:
        if target:
            print(Fore.CYAN + f"\n[+] Scanning {target}...")
            full_scan(target)

# -----------------------------
# Menu Interface
# -----------------------------

def menu():
    print(Fore.CYAN + """
=========================================
        NMAP AUTOMATION TOOL
=========================================
[1] Quick Scan
[2] Full Scan
[3] Stealth Scan
[4] OS Detection Scan
[5] Vulnerability Scan
[6] Port Range Scan
[7] Multi-Target Scan (file)
[8] Exit
=========================================
""")

def main():
    while True:
        menu()
        choice = input("Select an option: ")

        if choice == "8":
            print(Fore.GREEN + "Exiting tool.")
            break

        target = None
        if choice != "7":
            target = input("Enter target IP/domain: ")

        if choice == "1":
            quick_scan(target)
        elif choice == "2":
            full_scan(target)
        elif choice == "3":
            stealth_scan(target)
        elif choice == "4":
            os_scan(target)
        elif choice == "5":
            vuln_scan(target)
        elif choice == "6":
            port_range_scan(target)
        elif choice == "7":
            file_path = input("Enter file path containing targets: ")
            multi_target_scan(file_path)
        else:
            print(Fore.RED + "[!] Invalid choice. Try again.")

if __name__ == "__main__":
    main()