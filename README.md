# 🚀 Nmap Automation Tool — Advanced Version

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful, user-friendly automation tool built on top of **Nmap**, designed for penetration testers, SOC analysts, and cybersecurity students.  
This tool provides multiple scan modes, live output streaming, automatic logging, colored output, input validation, and multi-target scanning.

---

## 🔥 Features

**✔ Multiple Scan Modes**
- Quick Scan
- Full Scan
- Stealth Scan
- OS Detection
- Vulnerability Scan
- Custom Port Range Scan

**✔ Multi-Target Scanning**  
Provide a file containing multiple IPs/domains and scan them automatically.

**✔ Automatic Logging**  
All scan results are saved in the `logs/` folder with timestamped filenames.

**✔ Live Output Streaming**  
Scan results are displayed in real-time as Nmap runs — no waiting for the scan to finish.

**✔ Input Validation**  
Validates IP addresses, CIDR ranges, and domain names before scanning.

**✔ Colored Output**  
Improved readability using **colorama**.

**✔ Error Handling**  
Detects:
- Missing files
- Invalid targets
- Empty output
- Nmap not installed

**✔ Clean Menu Interface**  
Easy to use, even for beginners.

---

## 📦 Requirements

- Python 3.x
- Nmap installed on your system

Install Nmap:
```bash
sudo apt install nmap
```

Install Python dependencies:
```bash
pip install colorama
```

---

## 🛠 Installation

1. Clone the repository:
```bash
git clone https://github.com/Khalifaddicted/nmap-automation-tool.git
```

2. Navigate into the folder:
```bash
cd nmap-automation-tool
```

3. Install dependencies:
```bash
pip install colorama
```

---

## ▶️ Usage

Run the tool:
```bash
python3 nmap_auto.py
```

Menu:
```
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
```

---

## 📸 Screenshots

### 🔹 Main Menu

### 🔹 Example Scan Output

### 🔹 Logs Folder
<img width="876" height="618" alt="Screenshot 2026-04-27 140121" src="https://github.com/user-attachments/assets/19c18b9b-d8b7-4fa7-bd11-4ec92da6eb34" />
<img width="1402" height="288" alt="Screenshot 2026-04-27 141405" src="https://github.com/user-attachments/assets/ae5835c7-fddd-469a-b720-b5b65b581e28" />
<img width="1920" height="962" alt="Screenshot 2026-04-27 141455" src="https://github.com/user-attachments/assets/d0546bf9-ab95-48f9-8dbd-f5f4d5d45d1c" />

---

## ⚙️ How It Works

**🔹 1. Menu System**  
A clean text-based interface guides the user through different scan options. Each menu choice triggers a specific scan function.

**🔹 2. Scan Functions**  
Each scan mode is handled by its own function:
- Quick Scan → Fast scan of common ports
- Full Scan → Service detection, OS detection, aggressive scan
- Stealth Scan → SYN scan for quieter probing
- OS Detection Scan → Attempts to identify the target OS
- Vulnerability Scan → Uses Nmap NSE vulnerability scripts
- Port Range Scan → User-defined port range

**🔹 3. Logging System**  
Every scan result is automatically saved in the `logs/` folder with a timestamped filename. No scan results are lost.

**🔹 4. Multi-Target Engine**  
The tool reads a file of IPs/domains and scans them one by one. Useful for reconnaissance, network-wide scanning, and bulk testing.

**🔹 5. Error Handling**  
Checks for missing files, invalid targets, empty Nmap output, and missing Nmap installation — preventing crashes and improving reliability.

---

## 🚀 Future Improvements

- [ ] Multi-threading for faster parallel scanning
- [ ] HTML and JSON report output
- [ ] GUI version using Tkinter or PyQt
- [ ] Shodan API integration for external intelligence
- [ ] PDF export for scan reports
- [ ] Scan scheduling (cron-like automation)
- [ ] Configuration file for custom defaults
- [ ] Error logging to a separate file

---

## 🧩 Version

Current Version: **v1.0.0**

---

## 👨‍💻 Author

**Khalifa Zaid Alyafei**  
Cybersecurity Student — Qatar

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
