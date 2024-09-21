import consent_management  # Importing the consent management module
import nmap_scan
import sqlmap_scan
import exploit_module
import post_exploitation
import logging_setup as log
import getpass
import hashlib
import signal
import time

# In-memory user data
USERS_DB = {
    'admin': {
        'password': hashlib.sha256('adminpass'.encode()).hexdigest(),
        'role': 'admin'
    },
    'tester': {
        'password': hashlib.sha256('testerpass'.encode()).hexdigest(),
        'role': 'tester'
    }
}

# Timeout values in seconds
NMAP_TIMEOUT = 600
SQLMAP_TIMEOUT = 1200
EXPLOIT_TIMEOUT = 1200
POST_EXPLOITATION_TIMEOUT = 1200
OVERALL_TIMEOUT = 3600  # 1 hour overall timeout

# Function to handle timeouts
def timeout_handler(signum, frame):
    raise TimeoutError("Operation timed out")

# Set the signal for the overall timeout
signal.signal(signal.SIGALRM, timeout_handler)

# Function to authenticate the user
def authenticate(username, password):
    if username in USERS_DB:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if USERS_DB[username]['password'] == hashed_password:
            return True, USERS_DB[username]['role']
    return False, None

# RBAC check function
def check_access(role, action):
    if role == 'admin':
        return True  # Admins can perform all actions
    elif role == 'tester' and action in ['nmap_scan', 'sqlmap_scan']:
        return True  # Testers can only perform scanning actions
    return False  # Unauthorized access

# Function to execute a customizable script
def run_custom_script(script_path):
    try:
        with open(script_path, 'r') as script_file:
            script_code = script_file.read()
            exec(script_code)
            return True
    except Exception as e:
        print(f"Error executing custom script: {e}")
        return False

def main():
    # Step 1: User authentication
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Authenticate user
    is_authenticated, role = authenticate(username, password)
    if not is_authenticated:
        print("Authentication failed. Exiting.")
        return
    print(f"Authentication successful. Logged in as {username} with role: {role}")

    # Step 2: Obtain consent for penetration testing
    if not consent_management.get_consent():
        print("Consent not obtained. Exiting.")
        log.log_action(username, "Consent not obtained", "")
        return
    log.log_action(username, "Consent obtained", "")

    # Step 3: Get target details
    target_ip = input("Enter the target IP address: ")
    target_url = input("Enter the target URL: ")

    # Ask user if they want to use custom scripts
    use_custom_nmap = input("Do you want to use a custom Nmap script? (yes/no): ").lower() == 'yes'
    use_custom_sqlmap = input("Do you want to use a custom SQLMap script? (yes/no): ").lower() == 'yes'
    use_custom_exploit = input("Do you want to use a custom Exploit script? (yes/no): ").lower() == 'yes'
    use_custom_post_exploit = input("Do you want to use a custom Post-Exploitation script? (yes/no): ").lower() == 'yes'

    # Start the overall timeout
    signal.alarm(OVERALL_TIMEOUT)

    try:
        # Step 4: Start Nmap scan
        if check_access(role, 'nmap_scan'):
            print("\nStarting Nmap scan...")
            log.log_action(username, "Nmap scan started", target_ip)
            signal.alarm(NMAP_TIMEOUT)  # Set Nmap timeout
            
            if use_custom_nmap:
                nmap_script = input("Enter the path to your custom Nmap script: ")
                nmap_result = run_custom_script(nmap_script)
            else:
                nmap_result = nmap_scan.run_nmap_scan(target_ip)
                
            log.log_action(username, "Nmap scan completed", target_ip)
        else:
            nmap_result = "N/A"
            print("You do not have permission to run the Nmap scan.")

        # Step 5: Start SQLMap scan
        if check_access(role, 'sqlmap_scan'):
            print("\nStarting SQLMap scan...")
            log.log_action(username, "SQLMap scan started", target_url)
            signal.alarm(SQLMAP_TIMEOUT)  # Set SQLMap timeout
            
            if use_custom_sqlmap:
                sqlmap_script = input("Enter the path to your custom SQLMap script: ")
                sqlmap_result = run_custom_script(sqlmap_script)
            else:
                sqlmap_result = sqlmap_scan.run_sqlmap_scan(target_url)
                
            log.log_action(username, "SQLMap scan completed", target_url)
        else:
            sqlmap_result = "N/A"
            print("You do not have permission to run the SQLMap scan.")

        # Step 6: Run the exploit
        if check_access(role, 'exploit'):
            print("\nRunning exploit...")
            log.log_action(username, "Exploit started", target_ip)

            # Manually input exploit module and payload
            exploit_module_name = input("Enter the exploit module (e.g., exploit/unix/ftp/vsftpd_234_backdoor): ")
            payload_name = input("Enter the payload (e.g., payload/unix/reverse_perl): ")
            rport = input("Enter the remote port (e.g., 21): ")

            lhost = input("Enter your local IP address: ")
            lport = input("Enter your local port (e.g., 4444): ")

            signal.alarm(EXPLOIT_TIMEOUT)  # Set Exploit timeout
            
            if use_custom_exploit:
                exploit_script = input("Enter the path to your custom Exploit script: ")
                exploit_result = run_custom_script(exploit_script)
            else:
                exploit_result = exploit_module.run_exploit(
                    module=exploit_module_name,
                    payload=payload_name,
                    rhost=target_ip,
                    rport=rport,
                    lhost=lhost,
                    lport=lport
                )
            log.log_action(username, "Exploit completed", target_ip)
        else:
            exploit_result = False
            print("You do not have permission to run the exploit.")

        # Step 7: Post-exploitation
        if exploit_result:
            print("Exploit succeeded. Moving to post-exploitation...")
            session_id = input("Enter the session ID for post-exploitation: ")

            signal.alarm(POST_EXPLOITATION_TIMEOUT)  # Set Post-exploitation timeout
            
            if use_custom_post_exploit:
                post_exploit_script = input("Enter the path to your custom Post-Exploitation script: ")
                run_custom_script(post_exploit_script)
            else:
                # Post-exploitation actions
                log.log_action(username, "Post-exploitation (Privilege Escalation) started", target_ip)
                post_exploitation.run_privilege_escalation(session_id)
                log.log_action(username, "Post-exploitation (Privilege Escalation) completed", target_ip)

                log.log_action(username, "Post-exploitation (System Info) started", target_ip)
                post_exploitation.gather_system_info(session_id)
                log.log_action(username, "Post-exploitation (System Info) completed", target_ip)
        else:
            print("Exploit failed. Skipping post-exploitation.")

        # Step 8: Generate the overall report
        print("\nGenerating final report...")
        report_content = f"""Penetration Testing Report
        Target IP: {target_ip}
        Target URL: {target_url}

        Nmap Scan Results:
        {nmap_result}

        SQLMap Scan Results:
        {sqlmap_result}

        Exploit Status: {'Succeeded' if exploit_result else 'Failed'}
        """

        # Save the final report
        with open("final_report.txt", "w") as report_file:
            report_file.write(report_content)
        print("Final report saved to final_report.txt")

    except TimeoutError as e:
        print(f"Error: {str(e)}")
        log.log_action(username, f"Operation timed out: {str(e)}", target_ip)

    finally:
        signal.alarm(0)  # Disable the alarm

if __name__ == "__main__":
    main()
