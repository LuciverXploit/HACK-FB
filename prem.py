import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess, base64
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from requests.exceptions import ConnectionError
ses = requests.Session()
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r\x1b[1;91mSedang Memukul Planet...\x1b[1;92m" + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
def luciverxploit(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
os.system('clear')
loading()
luciverxploit(f'\n\x1b[1;97m[\x1b[1;92m➢\x1b[1;97m] Maaf Script Sedang Di Update Terimakasih\n')
time.sleep(3)
