import requests
import pandas as pd

def run(input_csv, api_url, param_name="id", method="GET", output_csv="api_results.csv"):
    """
    Call API in bulk using values from CSV
    :param input_csv: CSV with IDs/params
    :param api_url: API endpoint (use {value} placeholder if needed)
    :param param_name: Field in CSV
    :param method: GET or POST
    :param output_csv: Save results
    """
    df = pd.read_csv(input_csv)
    results = []

    for _, row in df.iterrows():
        value = row[param_name]
        try:
            if method.upper() == "GET":
                resp = requests.get(api_url.format(value=value))
            else:
                resp = requests.post(api_url, json={param_name: value})

            results.append({"value": value, "status": resp.status_code, "response": resp.text[:200]})
            print(f"📡 Called API with {value} → {resp.status_code}")

        except Exception as e:
            results.append({"value": value, "status": "error", "response": str(e)})

    pd.DataFrame(results).to_csv(output_csv, index=False)
    print(f"✅ Results saved: {output_csv}")
