# Configuration Templating with Jinja2

demonstrating how to generate network device configurations using Python, Jinja2 templates.

### File Descriptions

* **`generate_configs.py`**: The main Python script that drives the process. It reads data from `ports.csv`, uses the `switchport_template.j2` template, and generates the final configuration files.
* **`ports.csv`**: The source of truth for our variables. It contains all the specific data for each switch port (VLANs, description, etc.).
* **`switchport_template.j2`**: A Jinja2 template file. It contains the base configuration structure with placeholders for the variables defined in the CSV file.

### How to Use

1.  Ensure you have the required Python libraries installed (see the main `requirements.txt`).
2.  Modify `ports.csv` with your desired port data.
3.  Run the script from within this directory: `python3 generate_configs.py`
4.  The script will generate new `.conf` files containing the full configuration for each device.
