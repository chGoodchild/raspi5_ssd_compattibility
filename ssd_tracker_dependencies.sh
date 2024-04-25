#!/bin/bash

# Update package list and upgrade existing packages
sudo apt-get update
sudo apt-get upgrade -y

# Install smartmontools for smartctl
sudo apt-get install smartmontools -y

# Install nethogs for network monitoring
sudo apt-get install nethogs -y

# Install iotop for disk I/O monitoring
sudo apt-get install iotop -y

# Install pip for Python3 if not already installed
sudo apt-get install python3-pip -y

# Install psutil, a Python library for fetching system utilization (CPU, memory, disks, network, sensors)
sudo pip3 install psutil

echo "All dependencies installed successfully!"
