import subprocess
import time

def monitor_disk_io(duration=10):
    command = ['iostat', '-d', str(duration)]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    try:
        # Read the output continuously
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
            time.sleep(1)  # Adjust interval as needed

    except KeyboardInterrupt:
        process.terminate()
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_disk_io(duration=10)
