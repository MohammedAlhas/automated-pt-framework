# Automated Penetration Testing Framework

## Overview
This project is an automated penetration testing framework designed to perform various security assessments, including network scanning, SQL injection testing, exploitation, and post-exploitation. It integrates tools like Nmap, SQLMap, and Metasploit, providing a modular, customizable, and automated approach to penetration testing.

## Features
- **Nmap Scan Module**: Performs network scanning to identify open ports and services.
- **SQLMap Scan Module**: Automates SQL injection testing and data extraction.
- **Exploit Module**: Automates Metasploit exploits with dynamic payload selection.
- **Post-Exploitation Module**: Executes post-exploitation steps, such as privilege escalation and persistence.
- **Logging and Reporting**: Logs all actions and generates a final report with the results of the testing.
- **Role-Based Access Control (RBAC)**: Implements secure access with authentication and permissions based on user roles.
- **Consent Management**: Ensures legal and ethical guidelines by obtaining written consent from clients before starting tests.

## Project Structure

Automatedtool/ │ ├── consent_management.py # Manages client consent and permissions ├── exploit_module.py # Handles automated Metasploit exploitation ├── logging_setup.py # Configures logging for all actions ├── master.py # Main script that orchestrates the entire process ├── nmap_scan.py # Executes Nmap scans ├── post_exploitation.py # Handles post-exploitation tasks ├── sqlmap_scan.py # Runs SQLMap for SQL injection testing ├── consent_forms/ # Stores saved consent forms ├── pentest_framework.log # Logs activities during the test └── final_report.txt # Contains the final penetration test report


## Prerequisites
Before setting up this project, ensure that the following tools are installed on your system:

1. **Python 3.x**: The framework is written in Python.
2. **Nmap**: For network scanning.
3. **SQLMap**: For SQL injection testing.
4. **Metasploit Framework**: For exploitation and post-exploitation activities.

You can install these tools on Kali Linux with the following commands:
```bash
sudo apt update
sudo apt install nmap
sudo apt install sqlmap
sudo apt install metasploit-framework

**Installation**

## Clone the repository to your local machine:


git clone https://github.com/MohammedAlhas/automated-pt-framework.git
cd automated-pt-framework/Automatedtool

## Install Python dependencies (if any):

pip install -r requirements.txt

**Configure permissions**: Ensure that you have the necessary permissions to execute the required tasks, especially when running system-level tools like Metasploit, Nmap, and SQLMap.

**Running the Framework**
## Obtain Client Consent: Before running any tests, gather and save the client’s consent using the consent_management.py module
python3 consent_management.py

- This script will prompt you to input the client’s name, target IP addresses, and the testing scope. Consent details will be saved in a timestamped file in the consent_forms/ directory.

## Run the Master Script: To start the penetration testing process, run the master.py script
python3 master.py

**This script will:**
- Authenticate the user with a hashed password.
- Ask for the target IP or URL for scanning.
- Execute the Nmap scan, SQLMap scan, exploitation, and post-exploitation in sequence.
- Log all actions and generate a final report.

**Running Individual Modules**
You can also run individual modules if you only need to perform a specific action:

## Run Nmap scan
python3 nmap_scan.py

## Run SQLMap scan
python3 sqlmap_scan.py

## Execute Exploitation Module
python3 exploit_module.py

**View Logs and Reports** All actions are logged in pentest_framework.log. The final penetration test report is saved as final_report.txt.

**Example Workflow**
- Run the master.py script.
- The framework will gather consent, authenticate the user, and proceed with network scanning (Nmap).
- It will run SQL injection tests using SQLMap, followed by exploiting any discovered vulnerabilities with Metasploit.
- The framework will perform post-exploitation tasks like privilege escalation and persistence.
- Finally, it will generate a report and log all the activities.

**Timeouts**
- Nmap: 600 seconds
- SQLMap: 1200 seconds
- Exploitation: 1200 seconds
- Post-exploitation: 1200 seconds
These timeouts can be adjusted in the respective scripts.

**Contributing**If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. For any issues or feature requests, open an issue on the GitHub page.
