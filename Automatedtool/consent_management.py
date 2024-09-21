import os
from datetime import datetime

# Function to get consent details from the user
def get_consent():
    client_name = input("Enter the client name: ")
    target_ip = input("Enter the target IP addresses (comma-separated): ")
    scope = input("Enter the scope of testing (e.g., web app, network, etc.): ")
    
    # Verify consent
    consent = input("Do you have written consent from the client for this test? (yes/no): ")
    if consent.lower() != "yes":
        print("Testing cannot proceed without proper consent.")
        exit()
    
    return client_name, target_ip, scope

# Function to save consent details
def save_consent(client_name, target_ip, scope):
    # Create consent_forms directory if it doesn't exist
    if not os.path.exists("consent_forms"):
        os.makedirs("consent_forms")
    
    # Save consent details in a text file with a timestamp
    filename = f"consent_forms/{client_name}_consent_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as file:
        file.write(f"Client Name: {client_name}\n")
        file.write(f"Target IPs: {target_ip}\n")
        file.write(f"Scope of Testing: {scope}\n")
        file.write(f"Consent Verified: Yes\n")
        file.write(f"Date: {datetime.now()}\n")

# RBAC function to check user permissions
def check_user_permissions(user_role, action):
    # Define permissions for different roles
    permissions = {
        "admin": ["run_scan", "run_exploit", "view_results"],
        "tester": ["run_scan", "view_results"],
        "viewer": ["view_results"]
    }
    
    if action in permissions.get(user_role, []):
        return True
    else:
        print(f"User role '{user_role}' does not have permission to perform '{action}'")
        return False
