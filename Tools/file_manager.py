from colorama import Fore, Style, init
import os
import shutil

init(autoreset=True)

def list_files(directory='.'):
    """Lister les fichiers et dossiers dans un répertoire."""
    try:
        files = os.listdir(directory)
        print(f"\nContenu du répertoire {directory}:")
        for file in files:
            print(f"- {file}")
    except FileNotFoundError:
        print("Répertoire introuvable.")
    input("\nAppuyez sur Entrée pour continuer...")

def change_directory():
    """Changer de répertoire."""
    new_dir = input("Entrez le chemin du répertoire où aller : ")
    try:
        os.chdir(new_dir)
        print(f"Répertoire actuel : {os.getcwd()}")
    except FileNotFoundError:
        print("Répertoire introuvable.")
    input("\nAppuyez sur Entrée pour continuer...")

def copy_file():
    """Copier un fichier d'une destination à une autre."""
    source = input("Entrez le chemin du fichier à copier : ")
    destination = input("Entrez la destination du fichier (répertoire ou chemin complet) : ")
    try:
        shutil.copy(source, destination)
        print(f"Fichier copié de {source} à {destination}.")
    except FileNotFoundError:
        print("Fichier ou répertoire introuvable.")
    except Exception as e:
        print(f"Erreur lors de la copie : {e}")
    input("\nAppuyez sur Entrée pour continuer...")

def move_file():
    """Déplacer un fichier d'une destination à une autre."""
    source = input("Entrez le chemin du fichier à déplacer : ")
    destination = input("Entrez la destination du fichier (répertoire ou chemin complet) : ")
    try:
        shutil.move(source, destination)
        print(f"Fichier déplacé de {source} à {destination}.")
    except FileNotFoundError:
        print("Fichier ou répertoire introuvable.")
    except Exception as e:
        print(f"Erreur lors du déplacement : {e}")
    input("\nAppuyez sur Entrée pour continuer...")

def delete_file():
    """Supprimer un fichier ou un dossier."""
    path = input("Entrez le chemin du fichier ou dossier à supprimer : ")
    if os.path.isfile(path):
        try:
            os.remove(path)
            print(f"Fichier {path} supprimé.")
        except Exception as e:
            print(f"Erreur lors de la suppression : {e}")
    elif os.path.isdir(path):
        try:
            shutil.rmtree(path)
            print(f"Dossier {path} supprimé.")
        except Exception as e:
            print(f"Erreur lors de la suppression du dossier : {e}")
    else:
        print("Chemin introuvable.")
    input("\nAppuyez sur Entrée pour continuer...")

def create_directory():
    """Créer un nouveau répertoire."""
    new_dir = input("Entrez le nom du répertoire à créer : ")
    try:
        os.mkdir(new_dir)
        print(f"Répertoire {new_dir} créé.")
    except FileExistsError:
        print("Le répertoire existe déjà.")
    except Exception as e:
        print(f"Erreur lors de la création du répertoire : {e}")
    input("\nAppuyez sur Entrée pour continuer...")

def manage_files():
    """Menu principal du gestionnaire de fichiers."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{Fore.CYAN}                                      ╔═════════════════════════════════════╗")
        print(f"{Fore.CYAN}                                      ║      {Fore.LIGHTGREEN_EX} Gestionnaire de fichiers {Fore.CYAN}     ║")
        print(f"{Fore.CYAN}                                      ╠═════════════════════════════════════╣")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}1{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Lister les fichiers et dossiers {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}2{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Changer de répertoire           {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}3{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Copier un fichier               {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}4{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Déplacer un fichier             {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}5{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Supprimer un fichier ou dossier {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}6{Fore.CYAN} │ {Fore.LIGHTWHITE_EX}Créer un répertoire             {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ╠═════════════════════════════════════╣")
        print(f"{Fore.CYAN}                                      ║ {Fore.YELLOW}0{Fore.CYAN} │ {Fore.LIGHTRED_EX}Retour au menu principal        {Fore.CYAN}║")
        print(f"{Fore.CYAN}                                      ╚═════════════════════════════════════╝{Style.RESET_ALL}")
        print(" ")
        print(" ")

        choice = input(f"{Fore.YELLOW}Votre choix: ")

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
            print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
            input(f"{Fore.YELLOW}Appuyez sur Entrée pour continuer...")
