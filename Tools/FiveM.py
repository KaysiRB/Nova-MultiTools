import os
import shutil
import subprocess
import webbrowser
from colorama import Fore, Style, init
from utils import common

init(autoreset=True)

game_folder1 = r'C:\Users\juste\AppData\Local\FiveM\FiveM.app'
game_folder2 = r'C:\Users\juste\AppData\Local\FiveM\FiveM.app\data'

folders_to_delete1 = ['crashes', 'logs']
folders_to_delete2 = ['cache', 'nui-storage', 'server-cache', 'server-cache-priv']

def delete_folders(folder_path, folders_list):
    for folder in folders_list:
        full_path = os.path.join(folder_path, folder)
        if os.path.exists(full_path):
            try:
                shutil.rmtree(full_path)
                common.print_success(f"Dossier {folder} supprimé avec succès !")
            except PermissionError:
                common.print_error(f"Erreur : vous n'avez pas les autorisations nécessaires pour supprimer {folder}.")
            except Exception as e:
                common.print_error(f"Erreur inconnue lors de la suppression de {folder}: {e}")
        else:
            common.print_error(f"Dossier {folder} n'existe pas.")

def launch_app():
    try:
        subprocess.run([r'C:\Users\juste\AppData\Local\FiveM\FiveM.exe'], check=True)
        common.print_success("Application lancée avec succès !")
    except Exception as e:
        common.print_error(f"Erreur lors du lancement de l'application : {e}")

def launch_FlashBackFA():
    url = "https://cfx.re/join/k4aqg7"
    webbrowser.open(url)
    common.print_success("FlashBackFA lancée avec succès !")

def ask():
    while True :

        common.clear_screen()
        current_dir = os.getcwd()
        print(" ")
        print(f"\n{Fore.CYAN}                                      ╔═════════════════════════════════════════╗")
        print(f"{Fore.CYAN}                                      ║                {Fore.LIGHTGREEN_EX} FiveM          {Fore.CYAN}         ║")
        print(f"{Fore.CYAN}                                      ╠═════════════════════════════════════════╣")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}1{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Supprimer les dossiers caches       {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}2{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Lancer FlashBack FA                 {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}3{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Lancer FiveM                        {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ╠═════════════════════════════════════════╣")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}0{Fore.CYAN} │ {Fore.LIGHTRED_EX}Retour au menu principal            {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ╚═════════════════════════════════════════╝{Style.RESET_ALL}")
        print(" ")
        print(" ")

        choice = common.get_user_input("Entrez votre choix (0/3) : ")

        if choice == '1':
            print("Suppression des dossiers dans FiveM.app :")
            delete_folders(game_folder1, folders_to_delete1)
        
            print("\nSuppression des dossiers dans FiveM.app\\data :")
            delete_folders(game_folder2, folders_to_delete2)
        elif choice == '2':
            launch_FlashBackFA()
        elif choice == '3':
            launch_app()
        elif choice == '0':
            break
        else:
            common.print_error("Erreur : choix invalide. Veuillez sélectionner une option valide (0-3).")
            common.wait_for_user()