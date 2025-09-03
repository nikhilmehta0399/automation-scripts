import requests
import os

def run(url_list, output_folder):
    """
    Download files from a list of URLs
    :param url_list: List of URLs (txt file or Python list)
    :param output_folder: Folder to save files
    """
    os.makedirs(output_folder, exist_ok=True)

    if isinstance(url_list, str) and url_list.endswith(".txt"):
        with open(url_list, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        urls = url_list

    for url in urls:
        try:
            filename = os.path.join(output_folder, os.path.basename(url))
            resp = requests.get(url, stream=True)
            with open(filename, "wb") as f:
                for chunk in resp.iter_content(1024):
                    f.write(chunk)
            print(f"⬇️ Downloaded: {filename}")
        except Exception as e:
            print(f"❌ Failed to download {url}: {e}")
