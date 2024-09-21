import subprocess

def run_nmap_scan(target_ip):
    print(f"Scanning {target_ip} with Nmap...")
    result = subprocess.run(['nmap', '-sV', target_ip], stdout=subprocess.PIPE, text=True)
    return result.stdout
