import os
import subprocess

# === clear terminal ===
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        subprocess.call('clear')