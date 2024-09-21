import subprocess
import logging

def run_nmap_scan(target_ip, scan_type='-sV', ports=None, flags=None):
    """ 
    Run customizable Nmap scan with user-defined options. 
    Args:
        target_ip (str): Target IP address.
        scan_type (str): Nmap scan type (e.g., -sV, -sS, -A, etc.).
        ports (str): Port range (e.g., '80,443' or '1-65535').
        flags (str): Additional Nmap flags (e.g., '-T4' for faster scan).
    """
    command = ['nmap', scan_type]

    if ports:
        command += ['-p', ports]
    
    if flags:
        command += flags.split()

    command.append(target_ip)

    print(f"Running Nmap scan on {target_ip} with options: {command}")
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=600)
        print(result.stdout)
        logging.info(f"Nmap scan results: {result.stdout}")
    except subprocess.TimeoutExpired:
        print(f"Nmap scan on {target_ip} timed out.")
        logging.error("Nmap scan timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"Nmap scan failed with error: {e}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    scan_type = input("Enter Nmap scan type (default -sV): ") or '-sV'
    ports = input("Enter port range (optional): ")
    flags = input("Enter additional flags (optional): ")

    run_nmap_scan(target_ip, scan_type, ports, flags)
