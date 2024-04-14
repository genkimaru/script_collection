#!/bin/bash

# Define the output file
output_file="startup_services.txt"

# Check if the output file already exists and remove it if it does
if [ -e "$output_file" ]; then
    rm "$output_file"
fi

# Get the list of services loaded at startup
startup_services=$(systemctl list-unit-files --type=service | grep enabled | awk '{print $1}')

# Output the list of services to the output file
echo "Services loaded at startup:" >> "$output_file"
echo "$startup_services" >> "$output_file"

echo "The list of startup services has been saved to $output_file."
