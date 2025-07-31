# Netmiko Scripts

This directory contains Python scripts demonstrating various features of the Netmiko library for SSH-based network automation.

---

### `01_simple_connection.py`

This script demonstrates the most fundamental task in network automation: connecting to a device.

**Key Concepts Demonstrated**:
* **Basic Connection**: Uses `netmiko.ConnectHandler` to establish an SSH session.
* **Robust Error Handling**: The `try/except/finally` block is used to create a reliable script that always closes the connection properly.
* **Secure Password Entry**: Uses the `getpass` module to prevent passwords from being displayed on screen or saved in shell history.
