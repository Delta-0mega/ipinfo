import os
import importlib
import sys

libraries = ['requests', 'fade', 'colorama']
for library in libraries:
    try:
        importlib.import_module(library)
    except ImportError:
        os.system(f"pip install {library}")
os.system('cls' if os.name == 'nt' else 'clear')

from colorama import Fore
import requests
import fade

def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix
def in_virtualenv(): 
    return get_base_prefix_compat() != sys.prefix
if in_virtualenv():
    sys.exit()
else:
    def get_ip_info(ip_address):
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    def display_banner():
        banner = """
                ▄█     ▄███████▄       ▄█  ███▄▄▄▄      ▄████████  ▄██████▄  
                ███    ███    ███      ███  ███▀▀▀██▄   ███    ███ ███    ███ 
                ███▌   ███    ███      ███▌ ███   ███   ███    █▀  ███    ███ 
                ███▌   ███    ███      ███▌ ███   ███  ▄███▄▄▄     ███    ███ 
                ███▌ ▀█████████▀       ███▌ ███   ███ ▀▀███▀▀▀     ███    ███ 
                ███    ███             ███  ███   ███   ███        ███    ███ 
                ███    ███             ███  ███   ███   ███        ███    ███ 
                █▀    ▄████▀           █▀    ▀█   █▀    ███         ▀██████▀  
                                                                            
                                    (enter exit to leave)
                                [DISCORD] dsc.gg/delta-omega                                       
        """
        
        banner2 = fade.fire(banner)
        print(banner2)
        
    def display_ip_info(ip_info):
        if ip_info is not None:
            info = ""
            if 'ip' in ip_info:
                info += f"[IP] : {ip_info.get('ip')}\n"
            if 'city' in ip_info:
                info += f"[CITY] : {ip_info.get('city')}\n"
            if 'region' in ip_info:
                info += f"[DEPARTEMENT] : {ip_info.get('region')}\n"
            if 'country' in ip_info:
                info += f"[COUNTRY] : {ip_info.get('country')}\n"
            if 'postal' in ip_info:
                info += f"[POSTAL CODE] : {ip_info.get('postal')}\n"
            if 'hostname' in ip_info:
                info += f"[HOSTNAME] : {ip_info.get('hostname')}\n"
            if 'org' in ip_info:
                info += f"[ORGANIZATION] : {ip_info.get('org')}\n"
            if 'loc' in ip_info:
                info += f"[LOCATION] : {ip_info.get('loc')}\n"
                info += f"[MAP 1] : https://api.maptiler.com/maps/satellite/?key=aCUnLN4HAjC2dzu2J0Tk#17.76/{ip_info.get('loc').replace(',', '/')}\n"
                info += f"[MAP 2] : https://api.maptiler.com/maps/basic-v2/?key=aCUnLN4HAjC2dzu2J0Tk#19/{ip_info.get('loc').replace(',', '/')}\n"
                info += f"[STREET VIEW] : https://www.instantstreetview.com/@{ip_info.get('loc')},h50,p-50,z1\n"
            if info:
                i2 = fade.fire(info)
                print(i2)
            else:
                print("[ERROR] : No information available")
        else:
            print("[ERROR] : Invalid IP")

    display_banner()
    banner_displayed = True

    while True:
        if banner_displayed:
            banner_displayed = False
        else:
            a = fade.fire("------------------------------------------------------------")
            print(a)
            dsc = fade.fire("[DISCORD] dsc.gg/delta-omega")
            print(dsc)
        it = Fore.YELLOW + "[INPUT] ADRESSE IP : "
        adresse_ip = input(it)
        
        if adresse_ip.lower() == 'exit':
            break
        ip_info = get_ip_info(adresse_ip)
        display_ip_info(ip_info)
