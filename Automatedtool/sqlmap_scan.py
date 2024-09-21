import subprocess

def run_sqlmap_scan(target_url):
    print(f"Scanning {target_url} with SQLMap...")
    
    # Add extra SQLMap options for a more comprehensive scan
    sqlmap_command = [
        'sqlmap', '-u', target_url, '--batch', '--level', '5', '--risk', '3',
        '--dump-all', '--dbs', '--random-agent'
    ]
    
    try:
        # Running the SQLMap command with extended options
        result = subprocess.run(sqlmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=600)
        
        # Check for errors during SQLMap execution
        if result.stderr:
            print(f"Error occurred during SQLMap scan: {result.stderr}")
            return None
        
        # Output the results
        return result.stdout
    
    except subprocess.TimeoutExpired:
        print(f"SQLMap scan timed out after 600 seconds.")
        return None

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    scan_results = run_sqlmap_scan(target_url)
    
    if scan_results:
        # Save the scan results to a file
        with open('sqlmap_results.txt', 'w') as f:
            f.write(scan_results)
        print("Scan completed and results saved to sqlmap_results.txt")
    else:
        print("SQLMap scan did not complete successfully.")
