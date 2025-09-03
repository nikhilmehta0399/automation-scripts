import os
import shutil
from datetime import datetime

def run(source_folder, backup_folder):
    """
    Create a timestamped backup of a folder
    :param source_folder: Folder to backup
    :param backup_folder: Destination backup directory
    """
    os.makedirs(backup_folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(backup_folder, f"backup_{timestamp}")
    shutil.copytree(source_folder, dest)
    print(f"🗄 Backup created: {dest}")
