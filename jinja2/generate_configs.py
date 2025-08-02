import csv
import jinja2

# Load the Jinja2 template from the file
with open('switchport_template.j2') as f:
    template_content = f.read()
    template = jinja2.Template(template_content)

# This dictionary will hold the final configuration for each switch
switch_configs = {}

# Open and read the CSV file
with open('ports.csv') as f:
    csv_reader = csv.DictReader(f)

    # Loop through each row in the CSV
    for row in csv_reader:
        # Render the template with the data from the current row
        interface_config = template.render(row)

        # Get the hostname for the current row to use as a filename
        hostname = row['switch_hostname']
        filename = f"{hostname}.conf"

        # Append the generated config to the correct switch's entry
        if filename in switch_configs:
            switch_configs[filename] += interface_config
        else:
            switch_configs[filename] = interface_config

# Loop through the completed configurations and write each one to a file
for filename, config_data in switch_configs.items():
    with open(filename, 'w') as f:
        f.write(config_data)
    print(f"Configuration file '{filename}' created.")