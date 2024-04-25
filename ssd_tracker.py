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
        print(f"Executing command: {' '.join(cmd)}")
        
        # Start the badblocks process
        badblocks_process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, universal_newlines=True)

        # Open a CSV file to store the results
        with open('system_metrics.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp', 'Bad Blocks Output'])

            while True:
                output = badblocks_process.stdout.readline()
                if output:
                    print("Badblocks output:", output.strip())
                    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                    writer.writerow([timestamp, output.strip()])
                    file.flush()
                if badblocks_process.poll() is not None:
                    if output == '':
                        break

        # Check for any errors
        stderr_output = badblocks_process.stderr.read()
        if stderr_output:
            print("Errors encountered during badblocks test:", stderr_output)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py /dev/sdX")
        sys.exit(1)

    device_path = sys.argv[1]
    print(f"Starting badblocks on {device_path}")
    run_badblocks(device_path)
