import requests

def call_api(file_path, api_url, param_name="file"):
    try:
        with open(file_path, "rb") as f:
            response = requests.post(api_url, files={param_name: f})
        if response.status_code == 200:
            print(f"✅ API success: {file_path}")
            return True
        else:
            print(f"⚠️ API failed: {file_path} ({response.status_code}) {response.text}")
            return False
    except Exception as e:
        print(f"❌ API error for {file_path}: {e}")
        return False
