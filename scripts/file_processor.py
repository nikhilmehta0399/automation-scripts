import os
from utils.file_ops import get_files, move_file
from utils.api_ops import call_api
from utils.log_ops import log_to_file

def run(input_folder, output_folder=None, api_url=None, mode="move", log_file="actions_log.txt"):
    files = get_files(input_folder)
    actions = []

    for f in files:
        file_path = os.path.join(input_folder, f)

        if mode == "move" and output_folder:
            moved = move_file(file_path, output_folder)
            actions.append(f"Moved: {f} → {moved}")

        elif mode == "api" and api_url:
            if call_api(file_path, api_url):
                actions.append(f"Uploaded: {f}")

    log_to_file(log_file, actions)
    print(f"✅ Task completed. Log saved at {log_file}")
