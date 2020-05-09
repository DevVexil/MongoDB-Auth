from pymongo import MongoClient
import os
import socket
import random
import time
import dns.name
import ctypes
from requests import get
import colorama
from colorama import Fore, Back, Style
colorama.init()

#Panels
apanel = """
╔══════════════════════════════════════════════════╗
║                  Admin Panel V.1                 ║
║==================================================║
║           [1] Add User || [5] Testing            ║
║           [2] Add Auth || [6] Testing            ║
║           [3] Testing  || [7] Testing            ║
║           [4] Testing  || [8] Testing            ║
╚══════════════════════════════════════════════════╝
"""

#globals   
ip = get('https://api.ipify.org').text
hwid = "dfhsdfsdf" # CHange and add this




def LoginMenu():
    print("[!] Type 1 to Login || Type 2 to Signup")
    home = input("[>] ")
    if home == "1":
        login(ip)    
    elif home == "2":
        regi(ip)

def login(ip):
    #Login
    print("Enter your username")
    userName = input()
    print("Enter Your Password")
    passWord = input()


    #Login Check
    Client = MongoClient('')
    db = Client["Login"]
    collection = db["Accounts"]
    login = {}
    login ['Public-IP'] = ip
    login ['Username'] = userName
    login ["Passowrd"] = passWord

    if collection.find_one({"Public-IP": ip}):
        print(Fore.GREEN + "Access Granted" + Fore.RESET)
        time.sleep(1)
        os.system("cls")
        
    else:
        print(Fore.RED + "Please make an account." + Fore.RESET)


def regi(ip):
    #Auth
    print("[!] Please enter your Authkey.")
    reg = input("[>] ")

    #Mongo Auth
    Client = MongoClient('')
    db = Client["Login"]
    collection = db["AuthKeys"]
    login = {}
    login ['AUTHKEY'] = reg

    #Check
    if collection.find_one({"AUTHKEY": reg}):
        print(Fore.GREEN + "Valid Auth Key" + Fore.RESET)
        username(ip)
    else:
        print("Not a Valid Auth")

def username(ip):
    #Register User - Pass - Auth
    print("[!] Please enter a username")
    UserName = input("[>] ")
    print("[!] Please enter a password")
    PassWord = input("[>] ")   
    print("[!] Please re-enter your auth token")
    authtok = input("[>] ")

    #Mongo Register
    Client = MongoClient('')
    db = Client["Login"]
    collection = db["Accounts"]
    login = {}
    login ['Public-IP'] = ip
    login ['Username'] = UserName
    login ["Passowrd"] = PassWord
    login ['Auth-Token'] = authtok

    if collection.find_one({"Username": UserName}):
        print("[" + Fore.RED + "!" + Fore.RESET + "] Username Invalid")
        os.system("cls")
        regi(ip)
    elif collection.find_one({"Auth-Token": authtok}):
        print(Fore.LIGHTRED_EX + "Auth key already used" + Fore.RESET)
        time.sleep(1)
        os.system("cls")
        LoginMenu()
    else:
        print("[" + Fore.GREEN + "!" + Fore.RESET + "] Username Valid")
        collection.insert_one(login)
        LoginMenu()


LoginMenu()


