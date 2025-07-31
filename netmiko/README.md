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

---

### `04_multi_line_cli_prompt.py`

This script tackles a common challenge in automation: handling commands that require interactive confirmation. It demonstrates how to delete a file from a device's flash, which requires pressing Enter to confirm the action.

**Key Concepts Demonstrated**:
* **`send_command_timing()`**: This is the core of the script. Unlike `send_command()`, which waits for a standard device prompt (`#` or `>`), `send_command_timing()` waits for a short period of inactivity. This is perfect for capturing intermediate prompts like `[confirm]`.
* **Interactive Workflow**: The script sends the `delete` command, checks the output for the word "confirm" or "delete", and then sends a newline character (`\n`) to simulate pressing the Enter key.
* **Pre and Post Checks**: It verifies the file exists before attempting deletion and confirms it's gone afterward, a crucial practice for reliable automation.

---

### `05_textfsm.py`

This script highlights one of Netmiko's most powerful capabilities: parsing unstructured command-line output into structured data using TextFSM.

**Key Concepts Demonstrated**:
* **`use_textfsm=True`**: This simple argument tells Netmiko to find a matching TextFSM template for the command being run (`show arp`) and use it to parse the output.
* **Structured vs. Unstructured Data**: Instead of returning one large string, the command now returns a list of dictionaries (`[{'address': '...', 'mac': '...'}, ...]`).
* **Using Parsed Data**: The script demonstrates how to take unstructured data from the output of show commands like "show arp" and transform this into structured data like lists in python which makes further processing much easier.

---

### `06_sending_config_cmds.py`

This script demonstrates how to make configuration changes to devices. It shows two different methods for sending commands and how to save the running configuration to make it persistent.

**Key Concepts Demonstrated**:
* **`send_config_from_file()`**: This method is used to send a set of commands stored in an external text file (`cmds.txt`). This is very useful for applying large or standardized configurations.
* **`send_config_set()`**: This method is used to send a list of commands that are defined directly within the Python script. It's ideal for smaller, dynamic, or more targeted changes.
* **`save_config()`**: After making changes, this command is used to save the running configuration to the startup configuration (the equivalent of `copy running-config startup-config` or `write memory`). This ensures the changes persist after a reboot.

---

### `07_troubleshooting_netmiko.py`

This script covers essential techniques for debugging and handling advanced use-cases where standard Netmiko methods might not be sufficient.

**Key Concepts Demonstrated**:
* **Enabling Logging**: The script configures Python's `logging` module to capture all underlying SSH communications from Netmiko and save them to a file (`netmiko_debug.log`). Reviewing this log is the single most effective way to diagnose connection and command issues.
* **Low-Level Channel Access**: It demonstrates the use of `write_channel()` and `read_channel()`. These methods provide direct, raw access to the SSH channel, allowing you to send commands and read output manually. This is an "escape hatch" for dealing with non-standard prompts, banner screens, or situations where you need fine-grained control over the interaction timing.
