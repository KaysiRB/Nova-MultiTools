from colorama import Fore, Style, init
import os
from utils import common

init(autoreset=True)

def list_files(directory='.'):
    try:
        files = os.listdir(directory)
        print(f"\nContenu du répertoire {directory}:")
        for file in files:
            print(f"- {file}")
    except FileNotFoundError:
        common.print_error(f"Erreur : le répertoire {directory} n'existe pas.")
    except PermissionError:
        common.print_error(f"Erreur : vous n'avez pas les autorisations nécessaires pour accéder au répertoire {directory}.")
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")
    common.wait_for_user()

def change_directory():
    new_dir = common.get_user_input("Entrez le chemin du répertoire où aller : ")
    try:
        os.chdir(new_dir)
        print(f"Répertoire actuel : {os.getcwd()}")
    except FileNotFoundError:
        common.print_error(f"Erreur : le répertoire {new_dir} n'existe pas.")
    except PermissionError:
        common.print_error(f"Erreur : vous n'avez pas les autorisations nécessaires pour accéder au répertoire {new_dir}.")
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")
    common.wait_for_user()

def copy_file():
    source = common.get_user_input("Entrez le chemin du fichier à copier : ")
    destination = common.get_user_input("Entrez la destination du fichier (répertoire ou chemin complet) : ")
    try:
        common.shutil.copy(source, destination)
        common.print_success(f"Fichier copié de {source} à {destination}.")
    except FileNotFoundError:
        common.print_error(f"Erreur : le fichier {source} ou le répertoire {destination} n'existe pas.")
    except PermissionError:
        common.print_error(f"Erreur : vous n'avez pas les autorisations nécessaires pour copier le fichier {source} vers {destination }.")
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")
    common.wait_for_user()

def move_file():
    source = common.get_user_input("Entrez le chemin du fichier à déplacer : ")
    destination = common.get_user_input("Entrez la destination du fichier (répertoire ou chemin complet) : ")
    try:
        common.shutil.move(source, destination)
        common.print_success(f"Fichier déplacé de {source} à {destination}.")
    except FileNotFoundError:
        common.print_error(f"Erreur : le fichier {source} ou le répertoire {destination} n'existe pas.")
    except PermissionError:
        common.print_error(f"Erreur : vous n'avez pas les autorisations nécessaires pour déplacer le fichier {source} vers {destination}.")
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")
    common.wait_for_user()

def delete_file():
    path = common.get_user_input("Entrez le chemin du fichier ou dossier à supprimer : ")
    if os.path.isfile(path):
        try:
            os.remove(path)
            common.print_success(f"Fichier {path} supprimé.")
        except PermissionError:
            common.print_error(f"Erreur : vous n'avez pas les autorisations nécessaires pour supprimer le fichier {path}.")
        except Exception as e:
            common.print_error(f"Erreur inconnue : {e}")
    elif os.path.isdir(path):
        try:
            common.shutil.rmtree(path)
            common.print_success(f"Dossier {path} supprimé.")
        except PermissionError:
            common.print_error(f"Erreur : vous n'avez pas les autorisations nécessaires pour supprimer le dossier {path}.")
        except Exception as e:
            common.print_error(f"Erreur inconnue : {e}")
    else:
        common.print_error(f"Erreur : le chemin {path} est introuvable.")
    common.wait_for_user()

def create_directory():
    new_dir = common.get_user_input("Entrez le nom du répertoire à créer : ")
    try:
        os.mkdir(new_dir)
        common.print_success(f"Répertoire {new_dir} créé.")
    except FileExistsError:
        common.print_error(f"Erreur : le répertoire {new_dir} existe déjà.")
    except PermissionError:
        common.print_error(f"Erreur : vous n'avez pas les autorisations nécessaires pour créer le répertoire {new_dir}.")
    except Exception as e:
        common.print_error(f"Erreur inconnue : {e}")
    common.wait_for_user()

def manage_files():
    while True:
        common.clear_screen()
        current_dir = os.getcwd()
        print(" ")
        print(f"{Fore.CYAN}Répertoire actuel-> {current_dir}")
        print(f"\n{Fore.CYAN}                                      ╔═════════════════════════════════════════╗")
        print(f"{Fore.CYAN}                                      ║        {Fore.LIGHTGREEN_EX} Gestionnaire de fichiers {Fore.CYAN}       ║")
        print(f"{Fore.CYAN}                                      ╠═════════════════════════════════════════╣")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}1{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Lister les fichiers et dossiers     {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}2{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Changer de répertoire               {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}3{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Copier un fichier                   {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}4{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Déplacer un fichier                 {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}5{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Supprimer un fichier ou dossier     {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}6{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Créer un répertoire                 {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ╠═════════════════════════════════════════╣")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}0{Fore.CYAN} │ {Fore.LIGHTRED_EX}Retour au menu principal            {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ╚═════════════════════════════════════════╝{Style.RESET_ALL}")
        print(" ")
        print(" ")

        choice = common.get_user_input("Votre choix: ")

        if choice == '1':
            list_files()
        elif choice == '2':
            change_directory()
        elif choice == '3':
            copy_file()
        elif choice == '4':
            move_file()
        elif choice == '5':
            delete_file()
        elif choice == '6':
            create_directory()
        elif choice == '0':
            break
        else:
            common.print_error("Erreur : choix invalide. Veuillez sélectionner une option valide (0-6).")
            common.wait_for_user()
