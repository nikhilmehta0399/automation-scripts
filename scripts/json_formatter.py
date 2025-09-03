import json

def run(input_file, output_file=None):
    """
    Format & validate JSON
    :param input_file: Input JSON file
    :param output_file: Optional, write formatted JSON to file
    """
    try:
        with open(input_file, "r") as f:
            data = json.load(f)

        formatted = json.dumps(data, indent=4, sort_keys=True)

        if output_file:
            with open(output_file, "w") as f:
                f.write(formatted)
            print(f"✅ JSON formatted and saved: {output_file}")
        else:
            print(formatted)

    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
