import argparse
from .installer import NetSpeedInstaller

def main():
    parser = argparse.ArgumentParser(description='NetSpeedInstaller - A command-line tool to download and install applications from the internet.')
    parser.add_argument('-run', action='store_true', help='Run the NetSpeedInstaller')
    
    args = parser.parse_args()
    
    if args.run:
        nsi = NetSpeedInstaller()
        nsi.boot_up()
        nsi.main_interface()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
