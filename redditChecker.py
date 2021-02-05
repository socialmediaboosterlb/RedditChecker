import requests
import concurrent.futures
from termcolor import colored
import time
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

available = open('aReddit.txt', 'a+')
notAvailable = open('notAReddit.txt', 'a+')

def checker(username):
    link = "https://www.reddit.com/api/username_available.json?user="+username
    header= {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Host":"www.reddit.com"
    }
    r = requests.get(link,headers=header,verify=False).text
    if "true" in r:
        print(colored("[+] "+ username,"green"))
        available.write(username+"\n")
    else:
        print(colored("[-] "+ username,"red"))
        notAvailable.write(username+"\n")

print(colored('''
  _____          _     _ _ _      _____ _               _             
 |  __ \        | |   | (_) |    / ____| |             | |            
 | |__) |___  __| | __| |_| |_  | |    | |__   ___  ___| | _____ _ __ 
 |  _  // _ \/ _` |/ _` | | __| | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | | \ \  __/ (_| | (_| | | |_  | |____| | | |  __/ (__|   <  __/ |   
 |_|  \_\___|\__,_|\__,_|_|\__|  \_____|_| |_|\___|\___|_|\_\___|_|                                                              
CREDITS INSTAGRAM: socialmediaboosterlb TELEGRAM: socialmediaboosterlb
''','yellow'))


with open('usernames.txt', 'r') as f:
    usernames = [line.strip() for line in f]

lol = input("press Enter to start checking")
time.sleep(.5)

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(checker,usernames)
