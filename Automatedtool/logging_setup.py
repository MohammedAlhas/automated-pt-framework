import logging
from datetime import datetime

logging.basicConfig(
    filename='pentest_framework.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def log_action(username, action, target_ip=None):
    if target_ip:
        logging.info(f"User {username} performed {action} on {target_ip}")
    else:
        logging.info(f"User {username} performed {action}")

import configparser

config = configparser.ConfigParser()
config.read('config/logging.conf')

# Setup logging based on the config
import logging

# Define logging format and log file location
logging.basicConfig(
    filename='pentest_framework.log',  # Log file location
    level=logging.INFO,                # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

# Function to log actions
def log_action(client_name, action, target_ip=None):
    if target_ip:
        logging.info(f"Client: {client_name}, Action: {action}, Target IP: {target_ip}")
    else:
        logging.info(f"Client: {client_name}, Action: {action}")

# Example usage: logging an action when consent is saved
if __name__ == "__main__":
    log_action("ExampleClient", "Consent saved", "192.168.0.10")

import logging

def setup_logging():
    """
    Set up logging configuration for the framework.
    """
    logging.basicConfig(filename='pentest_framework.log', 
                        level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger()
