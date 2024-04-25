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

# Install Python3 venv for virtual environment support
sudo apt-get install python3-venv -y

# Create a virtual environment for Python packages
python3 -m venv ~/env

# Activate the virtual environment
source ~/env/bin/activate

# Install psutil within the virtual environment
pip install psutil

# Deactivate the virtual environment
deactivate

echo "All dependencies installed successfully!"

