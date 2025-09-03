import os

def run(folder, keyword, case_sensitive=False):
    """
    Search for a keyword in all text files in a folder
    :param folder: Folder path
    :param keyword: Keyword to search
    :param case_sensitive: Boolean
    """
    if not case_sensitive:
        keyword = keyword.lower()

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f, start=1):
                        check_line = line if case_sensitive else line.lower()
                        if keyword in check_line:
                            print(f"🔎 {file} (line {i}): {line.strip()}")
            except:
                continue
