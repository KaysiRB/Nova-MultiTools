import os
import requests
import re
import subprocess
import shutil
from colorama import Fore, Style, init
import time
import sys
import tempfile

init(autoreset=True)

version_tool = "0.2.1.0"  # La version actuelle du tool
github_repo_url = "https://github.com/KaysiRB/Nova-MultiTools.git"
url_config = "https://raw.githubusercontent.com/KaysiRB/Nova-MultiTools/main/utils/common.py"

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

def wait_for_user():
    input(f"{Fore.YELLOW}Appuyez sur Entrée pour continuer...")

def clone_repo(url, temp_dir):
    """Cloner le dépôt dans un répertoire temporaire."""
    print_info(f"Clonage du dépôt GitHub pour la mise à jour dans {temp_dir}...")
    result = subprocess.run(["git", "clone", url, temp_dir], capture_output=True, text=True)
    if result.returncode == 0:
        print_success("Clonage réussi.")
        return True
    else:
        print_error(f"Erreur lors du clonage : {result.stderr}")
        return False

def update_files(temp_dir):
    """Remplace les fichiers existants avec ceux du nouveau dépôt."""
    try:
        print_info("Mise à jour des fichiers...")

        ignore_patterns = ['.git']

        for item in os.listdir(temp_dir):
            if item not in ignore_patterns:
                s = os.path.join(temp_dir, item)
                d = os.path.join(os.getcwd(), item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
        
        print_info("Nettoyage des fichiers temporaires...")
        shutil.rmtree(temp_dir, ignore_errors=True)
        print_success("Mise à jour réussie !")
    except Exception as e:
        print_error(f"Erreur lors de la mise à jour des fichiers : {e}")

def check_for_updates():
    """Vérifie si une mise à jour est disponible et offre la possibilité de l'appliquer."""
    try:
        response = requests.get(url_config)
        response.raise_for_status()

        new_version = re.search(r'version_tool\s*=\s*"([^"]+)"', response.text).group(1)

        if new_version != version_tool:
            print_warning(f"Nouvelle version disponible : {version_tool} -> {new_version}")
            update_choice = get_user_input("Voulez-vous mettre à jour maintenant ? (o/n) : ").lower()
            
            if update_choice == 'o':
                print_info("Clonage du dépôt et mise à jour en cours...")

                with tempfile.TemporaryDirectory() as temp_dir:
                    if clone_repo(github_repo_url, temp_dir):
                        update_files(temp_dir)

                        print_info("Mise à jour terminée. Redémarrage de l'outil...")
                        time.sleep(3)

                        input(f"{Fore.YELLOW}Appuyez sur Entrée pour Redémarrer l'outil...")
                        os.execv(sys.executable, ['python'] + sys.argv)
                    else:
                        print_error("La mise à jour a échoué. Essayez manuellement.")
            else:
                print_info("Vous avez choisi de continuer avec la version actuelle.")
        else:
            print_success("Vous utilisez déjà la dernière version.")
    
    except requests.exceptions.RequestException as req_err:
        print_error(f"Erreur lors de la vérification des mises à jour : {req_err}")
    except AttributeError:
        print_error("Erreur lors de l'extraction de la version.")
    except Exception as e:
        print_error(f"Erreur inattendue : {e}")
