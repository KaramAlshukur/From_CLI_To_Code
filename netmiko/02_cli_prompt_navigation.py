# 02_find_prompt.py

"""
Demonstrates connecting to a device, entering different operational modes
(enable and configuration mode), and finding the prompt at each stage.
"""

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException

# Device details are stored in a dictionary for clean code.
# The 'secret' is the enable password.
net_device = {
    'device_type': 'cisco_ios',
    'host': '172.16.66.10',
    'username': 'karam',
    'password': getpass(),
    'secret': 'cisco', 
}

# Initialize the connection object to None.
# This ensures we don't try to disconnect from a failed connection.
net_connect = None
try:
    print(f"--> Attempting to connect to {net_device['host']}...")
    net_connect = ConnectHandler(**net_device)
    
    # If successful, Netmiko automatically finds the initial prompt.
    print("--> Connection successful.")
    print(f"Initial prompt: {net_connect.find_prompt()}")

    # Enter enable mode. Netmiko uses the 'secret' for this.
    print("--> Entering enable mode...")
    net_connect.enable()
    print(f"Enable mode prompt: {net_connect.find_prompt()}")

    # Enter global configuration mode.
    print("--> Entering configuration mode...")
    net_connect.config_mode()
    print(f"Config mode prompt: {net_connect.find_prompt()}")

    # Gracefully exit configuration mode before disconnecting.
    net_connect.exit_config_mode()
    print("--> Exited configuration mode.")

except NetmikoTimeoutException:
    print(f"Error: Connection to {net_device['host']} timed out. Check connectivity.")
except NetmikoAuthenticationException:
    print(f"Error: Authentication failed for {net_device['host']}. Check credentials.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # This block always runs, ensuring we close the connection if it was opened.
    if net_connect:
        print("--> Closing connection.")
        net_connect.disconnect()