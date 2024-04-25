import subprocess
import sys
import time
import csv
import psutil

def run_badblocks(device):
    """Run badblocks on the specified device and monitor system metrics."""
    try:
        # Command to start badblocks in non-destructive read-write mode
        cmd = ['sudo', 'badblocks', '-nsv', device]
        badblocks_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Open a CSV file to store the results
        with open('system_metrics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # Write CSV header
            writer.writerow(['Timestamp', 'CPU Usage', 'Memory Usage', 'Disk IO', 'System Voltage',
                             'Network Activity', 'SSD Temperature', 'Bad Blocks'])

            # Monitor metrics while badblocks is running
            while True:
                if badblocks_process.poll() is not None:
                    break

                # Get current time
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

                # Use psutil to fetch CPU and memory usage
                cpu_usage = psutil.cpu_percent(interval=1)
                memory_usage = psutil.virtual_memory().percent

                # These metrics would be fetched using appropriate commands or APIs
                disk_io = "Fetch with iotop or similar"
                system_voltage = "Use external hardware or specialized HAT"
                network_activity = "Fetch with nethogs or similar"

                # Correctly execute smartctl within a subprocess
                try:
                    ssd_temperature = subprocess.run(['sudo', 'smartctl', '-A', device], capture_output=True, text=True, check=True)
                    temperature_line = [line for line in ssd_temperature.stdout.split('\n') if "Temperature" in line]
                    ssd_temperature = temperature_line[0].split()[-1] if temperature_line else "N/A"
                except subprocess.CalledProcessError as e:
                    ssd_temperature = "Error retrieving temperature"

                # Read badblocks output to get the current count of bad blocks
                output = badblocks_process.stdout.readline()
                bad_blocks = "Parse output for bad block count"

                # Write metrics to CSV
                writer.writerow([timestamp, cpu_usage, memory_usage, disk_io, system_voltage, network_activity,
                                 ssd_temperature, bad_blocks])

                # Sleep before next measurement
                time.sleep(10)

        # Check for any errors
        errors = badblocks_process.stderr.read()
        if errors:
            print("Errors encountered during badblocks test:", errors)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py /dev/sdX")
        sys.exit(1)

    device_path = sys.argv[1]
    run_badblocks(device_path)


