# 03_sending_show_commands.py

"""
Connects to a list of network devices one by one and executes a specific
'show' command on each. This demonstrates how to scale an automation task
across multiple devices.
"""

from getpass import getpass
from netmiko import Netmiko
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

# Get the password securely at the start of the script
password = getpass()

# Define the devices. Storing them in dictionaries makes them easy to manage.
R1 = {
    'host': '172.16.66.10',
    'device_type': 'cisco_ios',
    'username': 'karam',
    'password': password,
    'secret': 'cisco',
}
R2 = {
    'host': '172.16.66.20',
    'device_type': 'cisco_ios',
    'username': 'karam',
    'password': password,
    'secret': 'cisco',
}
SW = {
    'host': '172.16.66.30',
    'device_type': 'cisco_ios',
    'username': 'karam',
    'password': password,
    'secret': 'cisco',
}

# A list of tuples, where each tuple contains the device dictionary and the command to run.
# This data structure makes it easy to loop through and execute tasks.
ios_devices = [
    (R1, 'show ip int br'),
    (R2, 'show arp'),
    (SW, 'show vlan br'),
]

# Iterate through each device and its corresponding command in the list.
for device, command in ios_devices:
    # Use a separator for clean, readable output for each device
    print(f"\n{'='*20} Connecting to {device['host']} {'='*20}")
    device_connection = None
    try:
        device_connection = Netmiko(**device)
        device_connection.enable()
        
        print(f"Executing command: '{command}'")
        output = device_connection.send_command(command)
        
        print("\n--- Command Output ---")
        print(output)
        print("--- End of Output ---\n")

    except NetmikoTimeoutException:
        print(f"Error: Connection to {device['host']} timed out.")
    except NetmikoAuthenticationException:
        print(f"Error: Authentication failed for {device['host']}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # Ensure disconnection happens for each device, if the connection was successful.
        if device_connection:
            device_connection.disconnect()
            print(f"Disconnected from {device['host']}.")