import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_error(message):
    print(f"{Fore.RED}{message}{Style.RESET_ALL}")

def print_success(message):
    print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")

def print_info(message):
    print(f"{Fore.CYAN}{message}{Style.RESET_ALL}")

def print_warning(message):
    print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")

def get_user_input(prompt):
    return input(f"{Fore.YELLOW}{prompt}{Style.RESET_ALL}")

def get_user_choice(prompt, choices):
    while True:
        choice = get_user_input(prompt)
        if choice in choices:
            return choice
        else:
            print_error("Erreur : choix invalide. Veuillez sélectionner une option valide.")

def wait_for_user():
    input(f"{Fore.YELLOW}Appuyez sur Entrée pour continuer...")

def get_current_directory():
    return os.getcwd()

def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print_error(f"Erreur : le répertoire {path} n'existe pas.")
    except PermissionError:
        print_error(f"Erreur : vous n'avez pas les autorisations nécessaires pour accéder au répertoire {path}.")
    except Exception as e:
        print_error(f"Erreur inconnue : {e}")

def get_file_list(directory):
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        print_error(f"Erreur : le répertoire {directory} n'existe pas.")
        return []
    except PermissionError:
        print_error(f"Erreur : vous n'avez pas les autorisations nécessaires pour accéder au répertoire {directory}.")
        return []
    except Exception as e:
        print_error(f"Erreur inconnue : {e}")
        return []