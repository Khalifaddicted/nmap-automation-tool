🚀 Nmap Automation Tool — Advanced Version

https://img.shields.io/badge/License-MIT-yellow.svg


A powerful, user‑friendly automation tool built on top of Nmap, designed for penetration testers, SOC analysts, and cybersecurity students.
This tool provides multiple scan modes, logging, colored output, error handling, and multi‑target scanning.

---

## 🔥 Features

### ✔ Multiple Scan Modes
- Quick Scan  
- Full Scan  
- Stealth Scan  
- OS Detection  
- Vulnerability Scan  
- Custom Port Range Scan  

### ✔ Multi-Target Scanning
Provide a file containing multiple IPs/domains and scan them automatically.

### ✔ Automatic Logging
All scan results are saved in the `logs/` folder with timestamped filenames.

### ✔ Colored Output
Improved readability using **colorama**.

### ✔ Error Handling
Detects:
- Missing files  
- Invalid targets  
- Empty output  
- Nmap installation issues  

### ✔ Clean Menu Interface
Easy to use, even for beginners.

---

## 📦 Requirements

Install Nmap:
sudo apt install nmap


Install Python dependencies:
pip install colorama


---

🛠 Installation
- Clone the repository:
git clone https://github.com/Khalifaddicted/nmap-automation-tool.git

- Navigate into the folder:
cd nmap-automation-tool

- Install dependencies:
pip install colorama

## ▶️ Usage

Run the tool:
python3 nmap_auto.py


Menu:
[1] Quick Scan [2] Full Scan [3] Stealth Scan [4] OS Detection [5] Vulnerability Scan [6] Port Range Scan [7] Multi-Target Scan (file) [8] Exi


---

## 📸 Screenshots

### 🔹 Main Menu


### 🔹 Example Scan Output


### 🔹 Logs Folder
<img width="1920" height="962" alt="Screenshot 2026-04-27 141455" src="https://github.com/user-attachments/assets/807658ab-7e92-4c99-bcf8-336876cf8cde" />
<img width="1402" height="288" alt="Screenshot 2026-04-27 141405" src="https://github.com/user-attachments/assets/70396dc4-cde4-43a8-915f-57393f8aba80" />
<img width="876" height="618" alt="Screenshot 2026-04-27 140121" src="https://github.com/user-attachments/assets/29430947-bfe2-4fbe-9067-bc04b2066e15" />






⚙️ How It Works
The tool is built around a modular and organized structure to make scanning simple, reliable, and automated.
🔹 1. Menu System
A clean text-based interface guides the user through different scan options.
Each menu choice triggers a specific scan function.
🔹 2. Scan Functions
Each scan mode is handled by its own function:
- Quick Scan → Fast scan of common ports
- Full Scan → Service detection, OS detection, aggressive scan
- Stealth Scan → SYN scan for quieter probing
- OS Detection Scan → Attempts to identify the target OS
- Vulnerability Scan → Uses Nmap NSE vulnerability scripts
- Port Range Scan → User-defined port range
This modular design keeps the code clean and easy to expand.

🔹 3. Logging System
Every scan result is automatically saved in the logs/ folder with a timestamped filename:

logs/scan_YYYY-MM-DD_HH-MM-SS.txt

This ensures no scan results are lost and makes it easy to track historical scans.

🔹 4. Multi-Target Engine
The tool can read a file containing multiple IPs/domains and scan them one by one.
This is useful for:
- Reconnaissance
- Network-wide scanning
- Bulk testing

🔹 5. Error Handling
The tool checks for:
- Missing files
- Invalid targets
- Empty Nmap output
- Missing Nmap installation
This prevents crashes and improves reliability.

---

🚀 Future Improvements
Planned enhancements for upcoming versions of the tool:
- Add multi-threading for faster parallel scanning
- Add HTML or JSON report output
- Add a GUI version using Tkinter or PyQt
- Add automatic OS detection for Windows/Linux environments
- Add Shodan API integration for external intelligence
- Add PDF export for scan reports
- Add scan scheduling (cron-like automation)
- Add a configuration file for custom defaults
- Add real-time progress indicators
- Add error logging to a separate file
These improvements will make the tool more powerful, scalable, and user-friendly.

---

🧩 Version
Current Version: v1.0.0

---

📄 License
This project is licensed under the MIT License.
See the LICENSE file for details

---

## 👨‍💻 Author

**Khalifa Zaid Alyafei**  
Cybersecurity Student — Qatar

---

🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.


