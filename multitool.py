import os
from colorama import Fore, Style, init
from Tools import system_info, file_manager, network_tools
from utils import common

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


def main():
    import os
    import sys

    # Détecter le répertoire du script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Changer le répertoire de travail vers celui du script
    os.chdir(script_dir)

    # Vérifier le répertoire de travail actuel
    print(f"Répertoire de travail actuel : {os.getcwd()}")
    common.check_for_updates()
    while True:
        common.clear_screen()
        print(logo)
        print(hub)
        print(common.version_tool)
        choice = common.get_user_input("Choix : ")

        if choice == '1':
            system_info.show_system_info()
        elif choice == '2':
            file_manager.manage_files()
        elif choice == '3':
            network_tools.show_network_menu()
        elif choice == '0':
            break
        else:
            common.print_error("Erreur : choix invalide. Veuillez sélectionner une option valide (0-3).")
            common.wait_for_user()

main()
