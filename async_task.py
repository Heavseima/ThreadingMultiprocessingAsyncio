import asyncio

async def async_write_to_file(filename, data, duration):
    """Simulates an asynchronous I/O task by writing data to a file."""
    print(f"Starting async write to {filename}...")
    await asyncio.sleep(duration)  # Simulate I/O delay
    
    # Simulate writing data to the file
    with open(filename, "a") as f:  # Using "a" to append to the file
        f.write(f"{data}\n")
    
    print(f"Completed async write to {filename}.")

async def run_async_tasks():
    """Runs multiple asynchronous I/O tasks."""
    tasks = [
        async_write_to_file("async_file1.txt", "Some data", 2),
        async_write_to_file("async_file2.txt", "More data", 3),
        async_write_to_file("async_file3.txt", "Even more data", 1),
    ]
    
    await asyncio.gather(*tasks)
    print("All async I/O tasks completed.")

