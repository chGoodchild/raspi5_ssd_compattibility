import subprocess
import sys
import time
import csv
import psutil

def fetch_ssd_temperature(device):
    """Fetch SSD temperature using smartctl."""
    try:
        result = subprocess.run(['sudo', 'smartctl', '-A', device], capture_output=True, text=True, check=True)
        for line in result.stdout.splitlines():
            if "Temperature" in line:
                return line.split()[-1]
    except subprocess.CalledProcessError:
        return "Error retrieving temperature"
    return "N/A"

def write_metrics_to_csv(data):
    """Write metrics to the CSV file."""
    with open('system_metrics.csv', 'a', newline='') as file:  # Open in append mode
        writer = csv.writer(file)
        writer.writerow(data)
        file.flush()  # Ensure data is written to disk

def monitor_system_metrics(device):
    """Monitor system metrics over time."""
    # Write CSV header if file is new
    with open('system_metrics.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'CPU Usage', 'Memory Usage', 'Disk IO', 'System Voltage',
                         'Network Activity', 'SSD Temperature'])

    while True:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        ssd_temperature = fetch_ssd_temperature(device)

        # Prepare data row
        data = [timestamp, cpu_usage, memory_usage, "Disk IO Placeholder", "System Voltage Placeholder",
                "Network Activity Placeholder", ssd_temperature]

        # Write to CSV
        write_metrics_to_csv(data)

        print(f"Logged at {timestamp}: CPU {cpu_usage}%, Memory {memory_usage}%, SSD Temp {ssd_temperature}")
        time.sleep(10)  # Adjust as necessary

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python monitor.py /dev/sdX")
        sys.exit(1)

    device_path = sys.argv[1]
    print(f"Monitoring system metrics for {device_path}")
    monitor_system_metrics(device_path)
