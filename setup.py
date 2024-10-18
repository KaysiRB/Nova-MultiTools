try:
    import sys
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    print("Installing the python modules required for the Tool:")

    if sys.platform.startswith("win"):
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        os.system("python multitool.py")

    elif sys.platform.startswith("linux"):
        os.system("python3 -m pip3 install --upgrade pip")
        os.system("python3 -m pip3 install -r requirements.txt")
        os.system("python3 multitool.py")

except Exception as e:
    print(f"An error occurred: {e}")

input("Press Enter to exit...")  # Keeps the window open until Enter is pressed