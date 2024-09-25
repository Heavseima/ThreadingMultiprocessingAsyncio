import threading
import time

def simulate_io_task(file_name, duration):
    """Simulates an I/O-bound task by 'writing' to a file."""
    print(f"Starting I/O task on {file_name}...")
    time.sleep(duration)  # Simulate I/O delay
    print(f"Completed I/O task on {file_name}.")

def run_io_tasks():
    """Runs multiple I/O tasks in parallel using threading."""
    threads = []
    file_tasks = [("file1.txt", 3), ("file2.txt", 2), ("file3.txt", 4)]  # Simulate file names and durations
    
    for file_name, duration in file_tasks:
        thread = threading.Thread(target=simulate_io_task, args=(file_name, duration))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All I/O tasks completed.")
