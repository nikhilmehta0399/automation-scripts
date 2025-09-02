import os
import shutil
import requests

# --- Configuration ---
INPUT_FOLDER = "input_files"
PROCESSED_FOLDER = "processed_files"
API_URL = "http://example.com/upload"  # replace with your API endpoint
API_PARAM_NAME = "file"  # change this if your API expects a different field name

def process_files():
    # Ensure processed folder exists
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)

    # List files in input folder
    files = [f for f in os.listdir(INPUT_FOLDER) if os.path.isfile(os.path.join(INPUT_FOLDER, f))]

    for filename in files:
        file_path = os.path.join(INPUT_FOLDER, filename)

        try:
            # Send file to API
            with open(file_path, "rb") as f:
                response = requests.post(API_URL, files={API_PARAM_NAME: f})

            if response.status_code == 200:
                print(f"✅ Successfully processed {filename}")
                # Move file to processed folder
                shutil.move(file_path, os.path.join(PROCESSED_FOLDER, filename))
            else:
                print(f"❌ Failed to process {filename}, Status: {response.status_code}, Response: {response.text}")

        except Exception as e:
            print(f"⚠️ Error processing {filename}: {e}")

if __name__ == "__main__":
    process_files()