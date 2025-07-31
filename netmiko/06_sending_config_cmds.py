# 06_sending_config_cmds.py

"""
Demonstrates two methods for sending configuration commands to network devices:
1. send_config_from_file(): Pushes configurations from an external file.
2. send_config_set(): Pushes a list of commands defined in the script.
It also shows how to save the configuration on the device.
"""

from getpass import getpass
from netmiko import Netmiko
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

# --- Credentials and Device List ---
password = getpass()
R1 = {
    'host': '172.16.66.10',
    'device_type': 'cisco_ios',
    'username': 'karam',
    'password': password,
    'secret': 'cisco',
}
# Add R2, SW, etc., as needed
ios_devices = [R1] 

# --- Configuration Commands to be Sent via send_config_set ---
config_set_commands = [
    'interface loopback600',
    'description Configured by send_config_set',
    'ip address 6.6.6.6 255.255.255.255',
]

# --- Main Execution Loop ---
for device in ios_devices:
    print(f"\n{'='*20} Connecting to {device['host']} {'='*20}")
    connection = None
    try:
        connection = Netmiko(**device)
        connection.enable()

        # --- Method 1: Using send_config_from_file ---
        print("\n--- Sending configuration from file 'cmds.txt' ---")
        output_from_file = connection.send_config_from_file('cmds.txt')  #Assuming these is cmds.txt file that holding the cli config
        print(output_from_file)

        # --- Method 2: Using send_config_set ---
        print("\n--- Sending configuration from a Python list ---")
        output_from_set = connection.send_config_set(config_set_commands)
        print(output_from_set)
        
        # --- Save the configuration ---
        print("\n--- Saving configuration ---")
        save_output = connection.save_config()
        print(save_output)

    except NetmikoTimeoutException:
        print(f"Error: Connection to {device['host']} timed out.")
    except NetmikoAuthenticationException:
        print(f"Error: Authentication failed for {device['host']}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if connection:
            connection.disconnect()
            print(f"\nDisconnected from {device['host']}.")
