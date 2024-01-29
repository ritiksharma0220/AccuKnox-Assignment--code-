import psutil

# define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# fn to check CPU usage
def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"CPU usage is high: {cpu_usage}%")

# fn to check memory usage
def check_memory():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"Memory usage is high: {memory_usage}%")

# fn to check disk space
def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        print(f"Disk usage is high: {disk_usage}%")

# fnt o check running processes
def check_processes():
    num_processes = len(psutil.pids())
    print(f"Number of running processes: {num_processes}")

# main function
def main():
    print("System Health Report:")
    check_cpu()
    check_memory()
    check_disk()
    check_processes()

if __name__ == "__main__":
    main()
