import argparse

def list_directory(path, recure=False, files_only=False, search_name=None, extension=None):
    pass

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["L", "Q"])
    parser.add_argument("initial_path")
    parser.add_argument("-r", "--recure", action="store_true")
    parser.add_argument("-f", "--files", action="store_true")
    parser.add_argument("-s", "--search")
    parser.add_argument("-e", "--extension")
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        print(f"Error: {e}")
        sys.exit(1)

    if args.command == "Q":
        sys.exit(0)
    elif args.command == "L":
        list_directory(args.initial_path, args.recure, args.files, args.search, args.extension)

def main():
    create_parser()

if __name__ == "__main__":
    main()