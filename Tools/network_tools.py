import socket
from colorama import Fore, Style, init
import requests
import os
from utils import common

init(autoreset=True)

def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except socket.gaierror as e:
        common.print_error(f"Erreur : impossible de résoudre le nom d'hôte. Vérifiez votre configuration réseau. Erreur : {e}")
        return None
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")
        return None

def get_public_ip():
    try:
        public_ip = requests.get('https://api.ipify.org').text
        return public_ip
    except requests.ConnectionError as e:
        common.print_error(f"Erreur : impossible de se connecter au service externe. Vérifiez votre connexion internet. Erreur : {e}")
        return None
    except requests.Timeout as e:
        common.print_error(f"Erreur : le service externe n'a pas répondu dans les temps. Vérifiez votre connexion internet. Erreur : {e}")
        return None
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")
        return None

def list_network_interfaces():
    try:
        interfaces = socket.getaddrinfo(socket.gethostname(), None)
        return interfaces
    except socket.gaierror as e:
        common.print_error(f"Erreur : impossible de résoudre le nom d'hôte. Vérifiez votre configuration réseau. Erreur : {e}")
        return []
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")
        return []

def ping_host(host):
    try:
        response = os.system(f"ping -c 4 {host}" if os.name != 'nt' else f"ping {host}")
        if response == 0:
            return f"{host} est accessible."
        else:
            return f"{Fore.RED}{host} n'est pas accessible.{Style.RESET_ALL}"
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")
        return None

def check_internet_connection():
    try:
        requests.get('https://www.google.com', timeout=3)
        return "Connexion internet active."
    except requests.ConnectionError as e:
        common.print_error(f"Erreur : impossible de se connecter à Internet. Vérifiez votre connexion internet. Erreur : {e}")
        return None
    except requests.Timeout as e:
        common.print_error(f"Erreur : le serveur n'a pas répondu dans les temps. Vérifiez votre connexion internet. Erreur : {e}")
        return None
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")
        return None
    
def scan_ports(host, start_port, end_port):
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()
    except socket.gaierror as e:
        common.print_error(f"Erreur : impossible de résoudre le nom d'hôte. Vérifiez votre configuration réseau. Erreur : {e}")
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")

def get_system_info(host):
    try:
        response = os.system(f"ssh {host} uname -a")
        if response == 0:
            return "Informations de système récupérées avec succès."
        else:
            return f"{Fore.RED}Erreur : impossible de récupérer les informations de système.{Style.RESET_ALL}"
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")

def send_file(host, file_path):
    try:
        response = os.system(f"scp {file_path} {host}:~/")
        if response == 0:
            return "Fichier envoyé avec succès."
        else:
            return f"{Fore.RED}Erreur : impossible d'envoyer le fichier.{Style.RESET_ALL}"
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")

def get_network_info(host):
    try:
        response = os.system(f"ssh {host} ip addr show")
        if response == 0:
            return "Informations de réseau récupérées avec succès."
        else:
            return f"{Fore.RED}Erreur : impossible de récupérer les informations de réseau.{Style.RESET_ALL}"
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")

def show_network_menu():
    while True:
        common.clear_screen()
        print(f"\n{Fore.CYAN}                                    ╔════════════════════════════════════════╗")
        print(f"{Fore.CYAN}                                    ║             {Fore.LIGHTGREEN_EX} Outils réseau {Fore.CYAN}            ║")
        print(f"{Fore.CYAN}                                    ╠════════════════════════════════════════╣")
        print(f"{Fore.CYAN}                                    ║ {Fore.YELLOW}1{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Obtenir l'adresse IP locale        {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                    ║ {Fore.YELLOW}2{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Obtenir l'adresse IP publique      {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                    ║ {Fore.YELLOW}3{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Lister les interfaces réseau       {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                    ║ {Fore.YELLOW}4{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Pinger une adresse IP ou un domaine{Fore.CYAN}║")
        print(f"{Fore.CYAN}                                    ║ {Fore.YELLOW}5{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Vérifier la connexion internet     {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                    ╠════════════════════════════════════════╣")
        print(f"{Fore.CYAN}                                    ║ {Fore.YELLOW}0{Fore.CYAN} │ {Fore.LIGHTRED_EX}Retour au menu principal           {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                    ╚════════════════════════════════════════╝{Style.RESET_ALL}")
        print(" ")
        print(" ")

        choice = common.get_user_input("Votre choix: ")

        if choice == '1':
            print(f"Adresse IP locale : {get_local_ip()}")
        elif choice == '2':
            print(f"Adresse IP publique : {get_public_ip()}")
        elif choice == '3':
            print("\nInterfaces réseau :")
            interfaces = list_network_interfaces()
            for interface in interfaces:
                print(f"- {interface[4][0]}")
        elif choice == '4':
            host = common.get_user_input("Entrez l'adresse IP ou le nom de domaine à pinger : ")
            print(ping_host(host))
        elif choice == '5':
            print(check_internet_connection())
        elif choice == '6':
            host = common.get_user_input("Entrez l'adresse IP ou le nom de domaine à scanner : ")
            start_port = int(common.get_user_input("Entrez le port de départ : "))
            end_port = int(common.get_user_input("Entrez le port de fin : "))
            scan_ports(host, start_port, end_port)
        elif choice == '0':
            break
        else:
            common.print_error("Erreur : choix invalide. Veuillez sélectionner une option valide (0-9).")
        
        common.wait_for_user()