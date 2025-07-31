# Netmiko Scripts

This directory contains Python scripts demonstrating various features of the Netmiko library for SSH-based network automation.

---

### `01_simple_connection.py`

This script demonstrates the most fundamental task in network automation: connecting to a device.

**Key Concepts Demonstrated**:
* **Basic Connection**: Uses `netmiko.ConnectHandler` to establish an SSH session.
* **Robust Error Handling**: The `try/except/finally` block is used to create a reliable script that always closes the connection properly.
* **Secure Password Entry**: Uses the `getpass` module to prevent passwords from being displayed on screen or saved in shell history.

---

### `02_cli_prompt_navigation.py`

This script builds on the first by demonstrating how to move between different operational modes on a Cisco IOS device.

**Key Concepts Demonstrated**:
* **Changing Modes**: Uses `.enable()` to enter privileged exec mode and `.config_mode()` to enter global configuration mode.
* **Finding the Prompt**: Shows how `.find_prompt()` can be used to identify the device's current prompt, which changes with each mode.
* **Enable Secret**: The `secret` parameter in the device dictionary is used as the enable password.
