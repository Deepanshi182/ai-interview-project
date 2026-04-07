import subprocess
import sys
import os

def install_heavy():
    # flag file to avoid reinstall every restart
    flag_file = "/tmp/heavy_installed"

    if os.path.exists(flag_file):
        print("Heavy libs already installed ✅")
        return

    print("Installing heavy libraries... ⏳")

    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-r", "heavy.txt"
    ])

    # create flag
    with open(flag_file, "w") as f:
        f.write("done")

    print("Heavy libraries installed ✅")