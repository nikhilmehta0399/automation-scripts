import argparse
from scripts import (
    file_processor,
    file_compressor,
    json_formatter,
    text_search,
    bulk_api_caller,
    file_downloader,
    backup_utility,
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automation Scripts CLI")
    parser.add_argument("--script", choices=[
        "file_processor",
        "file_compressor",
        "json_formatter",
        "text_search",
        "bulk_api_caller",
        "file_downloader",
        "backup_utility"
    ], required=True, help="Which script to run")

    # Common args
    parser.add_argument("--input", help="Input folder or file")
    parser.add_argument("--output", help="Output folder or file")
    parser.add_argument("--api", help="API URL")
    parser.add_argument("--mode", help="Mode (move, api, zip, tar, etc.)")
    parser.add_argument("--param", help="Parameter name for API/CSV (default: id)", default="id")
    parser.add_argument("--method", help="HTTP method (GET/POST)", default="GET")
    parser.add_argument("--keyword", help="Keyword for text search")
    parser.add_argument("--urls", help="URL list file (.txt) for downloader")
    parser.add_argument("--log", default="actions_log.txt", help="Log file path")

    args = parser.parse_args()

    # Dispatch
    if args.script == "file_processor":
        file_processor.run(
            input_folder=args.input,
            output_folder=args.output,
            api_url=args.api,
            mode=args.mode or "move",
            log_file=args.log
        )

    elif args.script == "file_compressor":
        file_compressor.run(
            input_folder=args.input,
            output_file=args.output,
            mode=args.mode or "zip"
        )

    elif args.script == "json_formatter":
        json_formatter.run(
            input_file=args.input,
            output_file=args.output
        )

    elif args.script == "text_search":
        text_search.run(
            folder=args.input,
            keyword=args.keyword,
            case_sensitive=(args.mode == "case")
        )

    elif args.script == "bulk_api_caller":
        bulk_api_caller.run(
            input_csv=args.input,
            api_url=args.api,
            param_name=args.param,
            method=args.method,
            output_csv=args.output or "api_results.csv"
        )

    elif args.script == "file_downloader":
        file_downloader.run(
            url_list=args.urls or args.input,
            output_folder=args.output
        )

    elif args.script == "backup_utility":
        backup_utility.run(
            source_folder=args.input,
            backup_folder=args.output
        )
