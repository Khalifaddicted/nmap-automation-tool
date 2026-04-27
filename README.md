Nmap Automation Tool — Advanced Version

A powerful, user‑friendly automation tool built on top of Nmap, designed for penetration testers, SOC analysts, and cybersecurity students.
This tool provides multiple scan modes, logging, colored output, error handling, and multi‑target scanning.

Features
Multiple Scan Modes
• 	Quick Scan
• 	Full Scan
• 	Stealth Scan
• 	OS Detection
• 	Vulnerability Scan
• 	Custom Port Range Scan

Multi‑Target Scanning
Provide a file containing multiple IPs/domains and scan them automatically.

Automatic Logging
All scan results are saved in the  folder with timestamped filenames.

Colored Output
Improved readability using colorama.

Error Handling
Detects:
• 	Missing files
• 	Invalid targets
• 	Empty output
• 	Nmap installation issues

Clean Menu Interface
Easy to use, even for beginners.

Requirements
Install Nmap:

sudo apt install nmap

Install Python dependencies:

pip install colorama

Usage
Run the tool:

python3 nmap_auto.py

You will see a menu:

[1] Quick Scan
[2] Full Scan
[3] Stealth Scan
[4] OS Detection
[5] Vulnerability Scan
[6] Port Range Scan
[7] Multi-Target Scan (file)
[8] Exit


Logs
All scan results are saved automatically in:

logs/scan_YYYY-MM-DD_HH-MM-SS.txt


Multi‑Target File Example
Create a file named :

192.168.1.1
scanme.nmap.org
10.0.0.5

Then choose option 7 in the menu.

Author
Khalifa Zaid Alyafei
Cybersecurity Student
Qatar