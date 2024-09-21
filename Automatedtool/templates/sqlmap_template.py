import subprocess
import logging

def run_sqlmap_scan(target_url, level=1, risk=1, flags=None):
    """
    Run customizable SQLMap scan with user-defined options.
    Args:
        target_url (str): Target URL for SQL injection testing.
        level (int): SQLMap level of tests (1-5, default: 1).
        risk (int): SQLMap risk level (1-3, default: 1).
        flags (str): Additional SQLMap flags (e.g., '--dbs' to enumerate databases).
    """
    command = ['sqlmap', '-u', target_url, '--level', str(level), '--risk', str(risk)]
    
    if flags:
        command += flags.split()

    print(f"Running SQLMap scan on {target_url} with options: {command}")
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=600)
        print(result.stdout)
        logging.info(f"SQLMap scan results: {result.stdout}")
    except subprocess.TimeoutExpired:
        print(f"SQLMap scan on {target_url} timed out.")
        logging.error("SQLMap scan timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.error(f"SQLMap scan failed with error: {e}")

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    level = input("Enter SQLMap level (default 1): ") or 1
    risk = input("Enter SQLMap risk level (default 1): ") or 1
    flags = input("Enter additional flags (optional): ")

    run_sqlmap_scan(target_url, level, risk, flags)
