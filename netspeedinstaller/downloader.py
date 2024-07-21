import os
import requests
from colorama import Fore, Style

def download_app(url, app_name):
    local_filename = os.path.join(os.getcwd(), app_name)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"{Fore.GREEN}{app_name} has been downloaded.{Style.RESET_ALL}")
