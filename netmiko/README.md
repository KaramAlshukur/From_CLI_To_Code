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
