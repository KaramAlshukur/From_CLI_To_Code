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

---

### `03_sending_show_commands.py`

This script demonstrates how to scale a simple task across multiple devices. It reads from a list of devices, connects to each one sequentially, and runs a unique command on each.

**Key Concepts Demonstrated**:
* **Iteration**: Uses a `for` loop to perform the same set of actions on a list of different devices. This is a foundational concept for scaling automation.
* **Data Structures**: Organizes devices and commands into a list of tuples `[(device_dict, command_str)]`, a clean way to manage targets and tasks.
* **Per-Device Error Handling**: The `try/except` block is inside the loop, so if one device fails, the script reports the error and continues to the next device.
