# cli.py
import argparse
from .core import main_function

def main():
    parser = argparse.ArgumentParser(description="NetSpeedInstaller CLI")
    parser.add_argument('--run', action='store_true', help="Run the main function")
    args = parser.parse_args()

    if args.run:
        main_function()

if __name__ == "__main__":
    main()
