import psutil
import json
import datetime

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage
    
def get_ram_info():
    ram_info = psutil.virtual_memory()
    return ram_info.percent

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return disk_usage.percent

def main():
    cpu = get_cpu_usage()
    ram = get_ram_info()
    disk = get_disk_usage()
    
    metrics_data = {
        'cpu_usage_percent': cpu,
        'ram_usage_percent': ram,
        'disk_usage_percent': disk
    }
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"health_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(metrics_data, f, indent=4)
    
    print(f"Successfully saved metrics to {filename}")
    
if __name__ == "__main__":
    main()