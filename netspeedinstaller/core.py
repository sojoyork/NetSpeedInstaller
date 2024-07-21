import time
import sys
import os
import requests
from colorama import init, Fore, Style
from .downloader import download_app

class NetSpeedInstaller:
    def __init__(self):
        init(autoreset=True)
        self.apps = {
            "chrome.exe": "https://dl.google.com/chrome/install/latest/chrome_installer.exe",
            "firefox.exe": "https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US",
            "vscode.exe": "https://update.code.visualstudio.com/latest/win32-x64-user/stable"
        }
        self.installed_apps = []

    def boot_up(self):
        print(f"{Fore.YELLOW}booting-up[{Style.RESET_ALL}", end="")
        for _ in range(60):
            print(f"{Fore.GREEN}#{Style.RESET_ALL}", end="")
            sys.stdout.flush()
            time.sleep(0.05)
        print(f"{Fore.YELLOW}]")
        print(f"{Fore.GREEN}Boot-up successful!")
        print(f"{Fore.CYAN}")
        print("""
 _ _         _    ___                   _  _             _         _  _           
| \ | ___  _| |_ / __> ___  ___  ___  _| || |._ _  ___ _| |_  ___ | || | ___  _ _ 
|   |/ ._>  | |  \__ \\| . \\ / ._>/ ._>/ . || || ' |<_-<  | |  <_> || || |/ ._>| '_>
|_\_|\___.  |_|  <___/|  _/\\___.\\___.\\___||_||_|_|/__/  |_|  <___||_||_|\___.|_|  
                      |_|                                                         
""")
        print(f"{Fore.YELLOW}netspeedinstaller: type 'help' for information{Style.RESET_ALL}")

    def main_interface(self):
        while True:
            command = input(f"{Fore.BLUE}nsi>{Style.RESET_ALL} ")
            if command == "help":
                self.help()
            elif command == "available-apps":
                self.show_apps()
            elif command.startswith("install"):
                app_name = command.split()[1]
                self.install_app(app_name)
            elif command.startswith("add-apps"):
                app_path = command.split()[1]
                self.add_app(app_path)
            elif command == "exit":
                print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Unknown command, type 'help' for information.{Style.RESET_ALL}")

    def help(self):
        print(f"""
{Fore.YELLOW}available-apps:{Style.RESET_ALL} shows all downloadable apps
{Fore.YELLOW}add-apps:{Style.RESET_ALL} add more apps to netspeedinstaller!
{Fore.YELLOW}install <app name>:{Style.RESET_ALL} install app!
{Fore.YELLOW}exit:{Style.RESET_ALL} leave
""")

    def show_apps(self):
        for app in self.apps:
            print(f"{Fore.CYAN}{app}{Style.RESET_ALL}")

    def install_app(self, app_name):
        if app_name in self.apps:
            url = self.apps[app_name]
            print(f"{Fore.YELLOW}installing {app_name}[", end="")
            for _ in range(50):
                print(f"{Fore.GREEN}#{Style.RESET_ALL}", end="")
                sys.stdout.flush()
                time.sleep(0.05)
            print(f"{Fore.YELLOW}]")
            print(f"{Fore.CYAN}Downloading...{Style.RESET_ALL}")
            self.download_app(url, app_name)
            self.installed_apps.append(app_name)
            print(f"{Fore.GREEN}Done!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}App not found!{Style.RESET_ALL}")

    def download_app(self, url, app_name):
        local_filename = os.path.join(os.getcwd(), app_name)
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"{Fore.GREEN}{app_name} has been downloaded.{Style.RESET_ALL}")

    def add_app(self, app_path):
        app_name = app_path.split('/')[-1]
        self.apps[app_name] = app_path
        print(f"{Fore.GREEN}app added!{Style.RESET_ALL}")

if __name__ == "__main__":
    nsi = NetSpeedInstaller()
    nsi.boot_up()
    nsi.main_interface()
