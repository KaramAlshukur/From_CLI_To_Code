# 07_troubleshooting_netmiko.py

"""
Demonstrates advanced troubleshooting techniques in Netmiko.
1. Enables logging to a file to see raw SSH interactions.
2. Uses low-level write_channel() and read_channel() for manual control.
"""

import logging
from getpass import getpass
from netmiko import Netmiko
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
import time

# --- 1. Enable Netmiko Logging ---
# This will create a file named 'netmiko_debug.log' and write all the raw
# SSH session data to it. This is extremely useful for debugging.
logging.basicConfig(filename='netmiko_debug.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

# --- Device Information ---
R1 = {
    'host': '172.16.66.10',
    'device_type': 'cisco_ios',
    'username': 'karam',
    'password': getpass("Enter device password: "),
    'secret': getpass("Enter enable secret: "),
}

# --- Main Execution Block ---
connection = None
try:
    print(f"\n{'='*20} Connecting to {R1['host']} {'='*20}")
    print("NOTE: Detailed SSH logs are being written to 'netmiko_debug.log'")
    connection = Netmiko(**R1)
    connection.enable()
    print("Connection successful.")

    # --- 2. Using Low-Level Channel Methods ---
    # These are useful when standard send_command() fails or for unusual prompts.
    print("\n--- Manually sending 'show ip int br' via write/read_channel ---")
    
    # Manually send the command and a newline character to the SSH channel
    connection.write_channel("show ip int br\n")
    
    # Pause to allow the device to process the command and send output
    time.sleep(2)
    
    # Read all the data currently in the SSH buffer
    output = connection.read_channel()
    
    print("\n--- Command Output ---")
    print(output)
    print("--- End of Output ---")


except NetmikoTimeoutException:
    print(f"\nError: Connection to {R1['host']} timed out.")
except NetmikoAuthenticationException:
    print(f"\nError: Authentication failed for {R1['host']}.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")

finally:
    # Always ensure the connection is closed
    if connection:
        connection.disconnect()
        print(f"\n{'='*20} Disconnected from {R1['host']} {'='*20}")
