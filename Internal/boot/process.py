import os
import json
import time
from colorama import init, Back, Fore, Style

init(autoreset=True)

path = "./Internal/assets/"
images = [path+"ecorp.json", path+"apple-boot.json"]

def open_json(file):
    linecount = 0
    os.system("clear")
    with open(file, "r+") as file:
        data = json.load(file)
        for item in data:
            linecount += 1
            if linecount >= 50:
                pass
            else:
                print(Back.WHITE + Fore.BLACK + item)
            
        time.sleep(2)

if __name__ == "__main__":
    for ipath in images:
        open_json(ipath)