#!/bin/bash

# Function to get service name from port
get_service_name() {
    local port="$1"
    local service_name=$(sudo lsof -i :$port | awk 'NR==2{print $1}')
    echo "$service_name"
}

# Main function to summarize used ports and service names
summarize_ports() {
    echo "SUMMARY OF USED PORTS AND SERVICE NAMES ON LOCALHOST"
    echo "----------------------------------------------------"
    echo "PORT     SERVICE NAME"
    echo "-----------------------------------"
    
    # Get list of used ports and iterate through them
    used_ports=$(netstat -tuln | grep "LISTEN" | awk '{print $4}' | awk -F ":" '{print $NF}' | sort -n | uniq)
    for port in $used_ports; do
        service_name=$(get_service_name $port)
        echo "$port       $service_name"
    done
}

# Call the main function
summarize_ports
