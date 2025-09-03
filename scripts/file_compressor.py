import os
import zipfile
import tarfile

def run(input_folder, output_file, mode="zip"):
    """
    Compress files/folders into zip or tar.gz
    :param input_folder: Folder to compress
    :param output_file: Output archive file
    :param mode: 'zip' or 'tar'
    """
    if mode == "zip":
        with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(input_folder):
                for file in files:
                    path = os.path.join(root, file)
                    arcname = os.path.relpath(path, input_folder)
                    zipf.write(path, arcname)
        print(f"📦 Created ZIP archive: {output_file}")

    elif mode == "tar":
        with tarfile.open(output_file, "w:gz") as tarf:
            tarf.add(input_folder, arcname=os.path.basename(input_folder))
        print(f"📦 Created TAR.GZ archive: {output_file}")
