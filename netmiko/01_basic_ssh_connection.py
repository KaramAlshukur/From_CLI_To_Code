# 01_simple_connection.py

"""
A simple Python script to demonstrate a basic SSH connection to a network device
using the Netmiko library. This version includes robust error handling and
ensures the connection is always closed properly.
"""

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoAuthenticationException, NetmikoTimeoutException
from getpass import getpass

# Store device information in a dictionary for clarity and ease of management.
device = {
    'device_type': 'cisco_ios',
    'host': '172.16.66.30',
    'username': 'karam',
    'password': getpass(),
}

# Initialize connection object to None. This is important for the finally block.
net_conn = None
try:
    # Establish the connection to the device.
    print(f"Connecting to device: {device['host']}...")
    net_conn = ConnectHandler(**device)

    # If the connection is successful, find the device prompt.
    prompt = net_conn.find_prompt()
    print(f"✅ Success! Connected to device. Prompt is: {prompt}")

except NetmikoTimeoutException:
    print(f"❌ Error: Connection to {device['host']} timed out. Check IP or firewall.")
except NetmikoAuthenticationException:
    print(f"❌ Error: Authentication failed for {device['host']}. Check username/password.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")

finally:
    # The 'finally' block always executes, whether there was an error or not.
    # This ensures we always attempt to disconnect if a connection was made.
    if net_conn:
        print("Closing connection.")
        net_conn.disconnect()