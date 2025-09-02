import argparse
from scripts import file_processor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automation Scripts CLI")
    parser.add_argument("--script", choices=["file_processor"], required=True, help="Which script to run")
    parser.add_argument("--input", required=True, help="Input folder")
    parser.add_argument("--output", help="Output folder (for move mode)")
    parser.add_argument("--api", help="API URL (for api mode)")
    parser.add_argument("--mode", choices=["move", "api"], default="move", help="Operation mode")
    parser.add_argument("--log", default="actions_log.txt", help="Log file path")
    args = parser.parse_args()

    if args.script == "file_processor":
        file_processor.run(
            input_folder=args.input,
            output_folder=args.output,
            api_url=args.api,
            mode=args.mode,
            log_file=args.log
        )
