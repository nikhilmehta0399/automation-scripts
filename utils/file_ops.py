import os
import shutil

def get_files(folder):
    return os.listdir(folder) if os.path.exists(folder) else []

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"🗑 Deleted: {file_path}")
        return True
    except Exception as e:
        print(f"❌ Error deleting {file_path}: {e}")
        return False

def move_file(src, dst_folder):
    os.makedirs(dst_folder, exist_ok=True)
    dst = os.path.join(dst_folder, os.path.basename(src))
    shutil.move(src, dst)
    print(f"📂 Moved: {src} → {dst}")
    return dst
