import platform
import psutil


def get_os_info():
    OS_NAMES = {
        'Darwin': 'macOS',
        'Linux': 'Linux',
        'Windows': 'Windows',
    }

    system_info = {
        'OS': OS_NAMES[platform.system()],
        'System': platform.system(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Architecture': platform.architecture(),
    }
    return system_info


def get_computer_specifications():
    cpu_info = {
        'CPU': platform.processor(),
        'Physical Cores': psutil.cpu_count(logical=False),
        'Total Cores': psutil.cpu_count(logical=True),
    }

    memory_info = {
        'Total Memory': round(psutil.virtual_memory().total / (1024**3), 2),
        'Available Memory': round(psutil.virtual_memory().available / (1024**3), 2),
    }

    return cpu_info, memory_info


def display_system_info():
    os_info = get_os_info()
    cpu_info, memory_info = get_computer_specifications()

    print("Operating System Information:")
    print(f"===============================")
    for key, value in os_info.items():
        print(f"{key}: {value}")

    print("\nComputer Specifications:")
    print(f"===============================")
    for info_dict in [cpu_info, memory_info]:
        for key, value in info_dict.items():
            print(f"{key}: {value}")


def get_storage_details_info():
    partitions = psutil.disk_partitions()

    storage_info = []

    for partition in partitions:
        partition_info = {
            'Device': partition.device,
            'Mount Point': partition.mountpoint,
            'File System': partition.fstype,
            'Total Size': psutil.disk_usage(partition.mountpoint).total,
            'Used': psutil.disk_usage(partition.mountpoint).used,
            'Free': psutil.disk_usage(partition.mountpoint).free,
            'Percentage Used': psutil.disk_usage(partition.mountpoint).percent,
        }
        storage_info.append(partition_info)

    return storage_info


def display_storage_details_info():
    storage_info = get_storage_details_info()

    for info in storage_info:
        print("Storage Information for {}: {}".format(
            info['Device'], info['Mount Point']))
        print("File System: {}".format(info['File System']))
        print("Total Size: {} GB".format(
            round(info['Total Size'] / (1024**3), 2)))
        print("Used: {} GB".format(round(info['Used'] / (1024**3), 2)))
        print("Free: {} GB".format(round(info['Free'] / (1024**3), 2)))
        print("Percentage Used: {}%".format(info['Percentage Used']))


def get_storage_info():
    partitions = psutil.disk_partitions()

    total_size = 0
    used = 0

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        total_size += usage.total
        used += usage.used

    return total_size, used


def display_storage_info():
    total_size, used = get_storage_info()

    print("\nStorage:")
    print(f"===============================")
    print("Total Storage Size: {} GB".format(round(total_size / (1024**3), 2)))
    print("Used Storage: {} GB".format(round(used / (1024**3), 2)))
    print("Percentage Used: {}%".format(round((used / total_size) * 100, 2)))

if __name__ == "__main__":
    display_system_info()
    display_storage_info()
