import os
import requests
import webbrowser
import re
from colorama import Fore, Style, init

init(autoreset=True)

version_tool = "0.0.0"  # La version actuelle du tool
github_tool = "https://github.com/KaysiRB/Nova-MultiTools"
url_config = "https://github.com/KaysiRB/Nova-MultiTools/blob/main/utils/common.py"

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
    
def check_for_updates():
    try:
        # Récupérer la version du fichier distant sur GitHub
        response = requests.get(url_config)
        response.raise_for_status()  # Assure qu'il n'y a pas d'erreurs HTTP

        # Extraire la version du tool avec une expression régulière
        new_version = re.search(r'version_tool\s*=\s*"([^"]+)"', response.text).group(1)

        # Comparer avec la version actuelle
        if new_version != version_tool:
            print(f"Nouvelle version disponible : {version_tool} -> {new_version}")
            update_choice = input("Voulez-vous mettre à jour maintenant ? (o/n) : ").lower()
            
            if update_choice == 'o':
                print("Mise à jour en cours...")
                webbrowser.open(github_tool)  # Ouvre le lien GitHub pour télécharger la nouvelle version
                
                # Possibilité de télécharger et remplacer automatiquement
                os.system(f"git clone {github_tool} temp_update")
                os.system("cp -r temp_update/* ./")  # Remplace les fichiers avec la nouvelle version
                os.system("rm -rf temp_update")  # Supprime le répertoire temporaire
                print("Mise à jour réussie ! Redémarrez l'outil.")
                exit()
            else:
                print("Vous continuez avec la version actuelle.")
        else:
            print("Vous utilisez déjà la dernière version.")
    
    except requests.exceptions.RequestException as req_err:
        print(f"Erreur lors de la vérification des mises à jour : {req_err}")
    except AttributeError:
        print("Erreur lors de l'extraction de la version.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
