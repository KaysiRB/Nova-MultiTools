import os
from colorama import Fore, Style, init
from Tools import system_info, file_manager, network_tools

init(autoreset=True)

logo = f"""
{Fore.RED}    ███▄    █ ▒█████  ██▒   █▓▄▄▄             ███▄ ▄███▓█    ██ ██▓ ▄▄▄█████▓██▄▄▄█████▓▒█████  ▒█████  ██▓     ██████ 
{Fore.RED}    ██ ▀█   █▒██▒  ██▓██░   █▒████▄          ▓██▒▀█▀ ██▒██  ▓██▓██▒ ▓  ██▒ ▓▓██▓  ██▒ ▓▒██▒  ██▒██▒  ██▓██▒   ▒██    ▒ 
{Fore.RED}   ▓██  ▀█ ██▒██░  ██▒▓██  █▒▒██  ▀█▄        ▓██    ▓██▓██  ▒██▒██░ ▒ ▓██░ ▒▒██▒ ▓██░ ▒▒██░  ██▒██░  ██▒██░   ░ ▓██▄   
{Fore.RED}   ▓██▒  ▐▌██▒██   ██░ ▒██ █░░██▄▄▄▄██       ▒██    ▒██▓▓█  ░██▒██░ ░ ▓██▓ ░░██░ ▓██▓ ░▒██   ██▒██   ██▒██░     ▒   ██▒
{Fore.RED}   ▒██░   ▓██░ ████▓▒░  ▒▀█░  ▓█   ▓██▒      ▒██▒   ░██▒▒█████▓░██████▒██▒ ░░██░ ▒██▒ ░░ ████▓▒░ ████▓▒░██████▒██████▒▒
{Fore.RED}   ░ ▒░   ▒ ▒░ ▒░▒░▒░   ░ ▐░  ▒▒   ▓▒█░      ░ ▒░   ░  ░▒▓▒ ▒ ▒░ ▒░▓  ▒ ░░  ░▓   ▒ ░░  ░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░▓  ▒ ▒▓▒ ▒ ░
{Fore.RED}   ░ ░░   ░ ▒░ ░ ▒ ▒░   ░ ░░   ▒   ▒▒ ░      ░  ░      ░░▒░ ░ ░░ ░ ▒  ░ ░    ▒ ░   ░     ░ ▒ ▒░  ░ ▒ ▒░░ ░ ▒  ░ ░▒  ░ ░
{Fore.RED}      ░   ░ ░░ ░ ░ ▒      ░░   ░   ▒         ░      ░   ░░░ ░ ░  ░ ░  ░      ▒ ░ ░     ░ ░ ░ ▒ ░ ░ ░ ▒   ░ ░  ░  ░  ░  
{Fore.RED}            ░    ░ ░       ░       ░  ░             ░     ░        ░  ░      ░             ░ ░     ░ ░     ░  ░     ░  
{Fore.RED}                          ░                                                                                            
{Style.RESET_ALL}"""

hub = f"""
{Fore.CYAN}                                      ╔══════════════════════════════════════╗
{Fore.CYAN}                                      ║              {Fore.LIGHTGREEN_EX}Menu Principal{Fore.CYAN}          ║
{Fore.CYAN}                                      ╠══════════════════════════════════════╣
{Fore.CYAN}                                      ║ {Fore.YELLOW}1{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Informations système{Fore.CYAN}             ║
{Fore.CYAN}                                      ║ {Fore.YELLOW}2{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Gestionnaire de fichiers{Fore.CYAN}         ║
{Fore.CYAN}                                      ║ {Fore.YELLOW}3{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Outils réseau{Fore.CYAN}                    ║
{Fore.CYAN}                                      ╠══════════════════════════════════════╣
{Fore.CYAN}                                      ║ {Fore.YELLOW}0{Fore.CYAN} │ {Fore.LIGHTRED_EX}Quitter{Fore.CYAN}                          ║
{Fore.CYAN}                                      ╚══════════════════════════════════════╝
{Fore.CYAN}
{Style.RESET_ALL}"""


def os_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        os_clear()
        print(logo)
        print(hub)
        choice = input(f"{Fore.YELLOW}Choix : ")

        if choice == '1':
            system_info.show_system_info()
        elif choice == '2':
            file_manager.manage_files()
        elif choice == '3':
            network_tools.show_network_menu()
        elif choice == '0':
            break
        else:
            print(f"{Fore.RED}Choix invalide.")
            input(f"{Fore.YELLOW}Appuyez sur Entrée pour continuer...")

main()
