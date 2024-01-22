import argparse

def create_parser():
    parser = argparse.ArgumentParser
    parser.add_argument("command", choices=["L", "Q"])
    parser.add_argument("initial_path")
    parser.add_argument("-r", "--recure")
    parser.add_argument("-f", "--files")
    parser.add_argument("-s", "--search")
    parser.add_argument("-e", "--extension")

def main():
    create_parser()

if __name__ == "__main__":
    main()