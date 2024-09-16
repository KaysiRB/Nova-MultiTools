import socket
from colorama import Fore, Style, init
import requests
import os

init(autoreset=True)

def get_local_ip():
    """Obtenir l'adresse IP locale."""
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_public_ip():
    """Obtenir l'adresse IP publique en utilisant un service externe."""
    try:
        public_ip = requests.get('https://api.ipify.org').text
        return public_ip
    except requests.ConnectionError:
        return f"{Fore.RED}Impossible de récupérer l'adresse IP publique.{Style.RESET_ALL}"

def list_network_interfaces():
    """Lister les interfaces réseau et leurs adresses IP."""
    interfaces = socket.getaddrinfo(socket.gethostname(), None)
    return interfaces

def ping_host(host):
    """Pinger une adresse IP ou un nom de domaine."""
    response = os.system(f"ping -c 4 {host}" if os.name != 'nt' else f"ping {host}")
    if response == 0:
        return f"{host} est accessible."
    else:
        return f"{Fore.RED}{host} n'est pas accessible.{Style.RESET_ALL}"

def check_internet_connection():
    """Vérifier la connexion internet."""
    try:
        requests.get('https://www.google.com', timeout=3)
        return "Connexion internet active."
    except requests.ConnectionError:
        return f"{Fore.RED}Pas de connexion internet.{Style.RESET_ALL}"

def show_network_menu():
    """Menu principal des outils réseau."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
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

        choice = input(f"{Fore.YELLOW}Votre choix: ")

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
            host = input("Entrez l'adresse IP ou le nom de domaine à pinger : ")
            print(ping_host(host))
        elif choice == '5':
            print(check_internet_connection())
        elif choice == '0':
            break
        else:
            print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}Appuyez sur Entrée pour continuer...")

