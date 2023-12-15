#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC SWITCHER")

print("""

Welcome Mac Switcher Tool

1) Random Mac Adress Determination
2) Manuel Mac Adress Determination
3) Change Mac Adress to Original

""")

process_number = input("Process Number Enter : ")

if process_number == "1":
    os.system("ifconfig eth0 down")
    os.system("macchanger -r eht0")
    os.system("ifconfig eth0 up")
    print("\033[92mNew Mac Adress Random Determination")

elif process_number == "2":
    mac_adress = input("New Mac Adress Enter : ")
    os.system("ifconfig eth0 down")
    os.system("macchanger --mac " + mac_adress + " eth0")
    os.system("ifconfig eth0 up")
    print("\033[92mNew Mac Adress Manuel Determination")

elif process_number == "3":
    os.system("ifconfig eth0 down")
    os.system("macchanger -p eth0")
    os.system("ifconfig eth0 up")
    print("\033[92mNew Mac Adress Original Determination")

else:
    print("Wrong Choice")
    os.system("python mac_switcher.py")