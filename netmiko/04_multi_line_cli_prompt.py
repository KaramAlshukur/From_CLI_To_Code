# 04_multiline_prompt.py

"""
Demonstrates handling interactive prompts using send_command_timing().
This script connects to a device and deletes a file from flash,
handling the interactive confirmation steps.
"""

from getpass import getpass
from netmiko import Netmiko
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

# --- Device and File Information ---
device_config = {
    'host': '172.16.66.10',
    'device_type': 'cisco_ios',
    'username': 'karam',
    'password': getpass("Enter device password: "),
    'secret': getpass("Enter enable secret: "),
}

filename_to_delete = input("Enter the exact filename to delete from flash: ").strip()

# Exit if no filename is provided
if not filename_to_delete:
    print("\nError: No filename entered. Script terminated.")
    exit()

# --- Main Execution Block ---
connection = None
try:
    print(f"\n{'='*20} Connecting to {device_config['host']} {'='*20}")
    connection = Netmiko(**device_config)
    connection.enable()
    print("Connection successful.")

    # 1. Check flash memory BEFORE deletion to see if the file exists
    print("\n--- Checking flash contents before deletion ---")
    flash_before = connection.send_command('dir flash:')
    print(flash_before)

    if filename_to_delete not in flash_before:
        print(f"\nResult: File '{filename_to_delete}' not found in flash. Nothing to do.")
    else:
        # 2. The file exists, so proceed with deletion
        print(f"\n--- Attempting to delete '{filename_to_delete}' ---")
        delete_command = f"delete flash:{filename_to_delete}"
        
        # Use send_command_timing() to send the initial command.
        # It will return when it receives the confirmation prompt.
        output = connection.send_command_timing(delete_command)
        
        # 3. Check if confirmation is needed and send it
        if 'confirm' or 'delete' in output.lower():
            # Send a newline to confirm the deletion.
            # send_command_timing is used again because we are not expecting a normal prompt back.
            print("Confirmation prompt detected. Sending confirmation...")
            output += connection.send_command_timing('\n')

        print("\n--- Verifying deletion ---")
        # 4. Check flash memory AFTER deletion to verify
        flash_after = connection.send_command('dir flash:')
        
        if filename_to_delete not in flash_after:
            print(f"Success! File '{filename_to_delete}' has been deleted.")
        else:
            print(f"Error: File '{filename_to_delete}' still exists in flash.")
        
        print("\nFinal flash contents:")
        print(flash_after)

except NetmikoTimeoutException:
    print(f"Error: Connection to {device_config['host']} timed out.")
except NetmikoAuthenticationException:
    print(f"Error: Authentication failed for {device_config['host']}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # Always ensure the connection is closed
    if connection:
        connection.disconnect()
        print(f"\n{'='*20} Disconnected from {device_config['host']} {'='*20}")