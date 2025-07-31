# 05_textfsm.py

"""
Demonstrates the power of TextFSM for parsing CLI output into structured data.
This script runs 'show arp' on a device and uses the 'use_textfsm=True'
argument to automatically convert the string output into a list of dictionaries.
"""

from getpass import getpass
from netmiko import Netmiko
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

# --- Device and Connection Setup ---
R1 = {
    'host': '172.16.66.10',
    'username': 'karam',
    'password': getpass("Enter device password: "),
    'device_type': 'cisco_ios',
    'secret': getpass("Enter enable secret: "),
}

# --- Main Execution Block ---
connection = None
try:
    print(f"\n{'='*20} Connecting to {R1['host']} {'='*20}")
    connection = Netmiko(**R1)
    connection.enable()
    print("Connection successful.")

    # Execute the command and parse the output using TextFSM
    print("\n--- Running 'show arp' with TextFSM parsing ---")
    arp_table = connection.send_command('show arp', use_textfsm=True)

    # Print the raw data structure returned by TextFSM
    print("\n--- Raw Parsed Output ---")
    print(arp_table)
    
    # Print the type and length to confirm it's a list
    print(f"\nType of parsed data: {type(arp_table)}")
    print(f"Number of ARP entries found: {len(arp_table)}")


except NetmikoTimeoutException:
    print(f"Error: Connection to {R1['host']} timed out.")
except NetmikoAuthenticationException:
    print(f"Error: Authentication failed for {R1['host']}.")
except Exception as e:
    # This can happen if TextFSM templates aren't found or if the command is not supported
    print(f"An unexpected error occurred: {e}")

finally:
    # Always ensure the connection is closed
    if connection:
        connection.disconnect()
        print(f"\n{'='*20} Disconnected from {R1['host']} {'='*20}")