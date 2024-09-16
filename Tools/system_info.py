import platform
from colorama import Fore, Style, init
import psutil
import os

init(autoreset=True)

def get_os_info():
    return {
        'Système d\'exploitation': platform.system(),
        'Version': platform.version(),
        'Architecture': platform.machine(),
        'Nom du processeur': platform.processor(),
        'Nom de l\'ordinateur': platform.node(),
        'Distribution': platform.platform()
    }

def get_cpu_info():
    cpu_info = {
        'Nombre de cœurs logiques': psutil.cpu_count(logical=True),
        'Nombre de cœurs physiques': psutil.cpu_count(logical=False),
        'Fréquence max': f"{psutil.cpu_freq().max} MHz",
        'Fréquence actuelle': f"{psutil.cpu_freq().current} MHz",
        'Utilisation par cœur': psutil.cpu_percent(percpu=True)
    }
    return cpu_info

def get_memory_info():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    return {
        'Mémoire totale': f"{mem.total / (1024 ** 3):.2f} GB",
        'Mémoire utilisée': f"{mem.used / (1024 ** 3):.2f} GB",
        'Mémoire disponible': f"{mem.available / (1024 ** 3):.2f} GB",
        'Utilisation mémoire (%)': mem.percent,
        'Swap total': f"{swap.total / (1024 ** 3):.2f} GB",
        'Swap utilisé': f"{swap.used / (1024 ** 3):.2f} GB",
        'Swap libre': f"{swap.free / (1024 ** 3):.2f} GB",
        'Utilisation swap (%)': swap.percent
    }

def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.device] = {
            'Total': f"{usage.total / (1024 ** 3):.2f} GB",
            'Utilisé': f"{usage.used / (1024 ** 3):.2f} GB",
            'Libre': f"{usage.free / (1024 ** 3):.2f} GB",
            'Utilisation (%)': usage.percent
        }
    return disk_info

def show_system_info():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"\n{Fore.LIGHTMAGENTA_EX}=== Informations sur le système ==={Style.RESET_ALL}")
    os_info = get_os_info()
    for key, value in os_info.items():
        print(f"{Fore.CYAN}{key} : {Fore.GREEN}{value}{Style.RESET_ALL}")
    
    print(f"\n{Fore.LIGHTMAGENTA_EX}=== Informations CPU ==={Style.RESET_ALL}")
    cpu_info = get_cpu_info()
    for key, value in cpu_info.items():
        print(f"{Fore.CYAN}{key} : {Fore.GREEN}{value}{Style.RESET_ALL}")
    
    print(f"\n{Fore.LIGHTMAGENTA_EX}=== Informations sur la mémoire ==={Style.RESET_ALL}")
    memory_info = get_memory_info()
    for key, value in memory_info.items():
        print(f"{Fore.CYAN}{key} : {Fore.GREEN}{value}{Style.RESET_ALL}")

    print(f"\n{Fore.LIGHTMAGENTA_EX}=== Informations sur les disques ==={Style.RESET_ALL}")
    disk_info = get_disk_info()
    for device, info in disk_info.items():
        print(f"\n{Fore.CYAN}Périphérique : {Fore.GREEN}{device}{Style.RESET_ALL}")
        for key, value in info.items():
            print(f"{Fore.CYAN}{key} : {Fore.GREEN}{value}{Style.RESET_ALL}")
    
    input(f"\n{Fore.YELLOW}Appuyez sur Entrée pour revenir au menu...")

