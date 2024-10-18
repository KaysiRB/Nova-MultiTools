import os
import subprocess
from colorama import Fore, Style, init
from Tools import system_info, file_manager, network_tools, FiveM
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
{Fore.CYAN}                                      ║ {Fore.MAGENTA}{common.version_tool}        {Fore.LIGHTGREEN_EX}Menu Principal{Fore.CYAN}        ║
{Fore.CYAN}                                      ╠══════════════════════════════════════╣
{Fore.CYAN}                                      ║ {Fore.YELLOW}1{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Informations système{Fore.CYAN}             ║
{Fore.CYAN}                                      ║ {Fore.YELLOW}2{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Gestionnaire de fichiers{Fore.CYAN}         ║
{Fore.CYAN}                                      ║ {Fore.YELLOW}3{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Outils réseau{Fore.CYAN}                    ║
{Fore.CYAN}                                      ║ {Fore.YELLOW}4{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}DDoS         {Fore.CYAN}                    ║
{Fore.CYAN}                                      ║ {Fore.YELLOW}5{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}FiveM        {Fore.CYAN}                    ║
{Fore.CYAN}                                      ╠══════════════════════════════════════╣
{Fore.CYAN}                                      ║ {Fore.YELLOW}0{Fore.CYAN} │ {Fore.LIGHTRED_EX}Quitter{Fore.CYAN}                          ║
{Fore.CYAN}                                      ╚══════════════════════════════════════╝
{Fore.CYAN}
{Style.RESET_ALL}"""


def main():
    import os
    import sys


    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print(f"Répertoire de travail actuel : {os.getcwd()}")
    common.check_for_updates()
    while True:
        common.clear_screen()
        print(logo)
        print(hub)
        choice = common.get_user_input("Choix : ")

        if choice == '1':
            system_info.show_system_info()
        elif choice == '2':
            file_manager.manage_files()
        elif choice == '3':
            network_tools.show_network_menu()
        elif choice == '4':
            DDoS_gui_path = os.path.join(script_dir, 'Tools', 'DDoS.py')
            if os.path.exists(DDoS_gui_path):
                try:
                    subprocess.run(['python', DDoS_gui_path])
                except Exception as e:
                    common.print_error(f"Erreur lors de l'exécution du script : {e}")
            else:
                common.print_error("Le fichier DDoS.py est introuvable.")
        elif choice == '5':
            FiveM.ask()
        elif choice == '0':
            break
        else:
            common.print_error("Erreur : choix invalide. Veuillez sélectionner une option valide (0-5).")
            common.wait_for_user()

main()
