#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS SCAN")

print("""

Welcome Wordpress Scan Tool

1) Quick Scan
2) Plugin Scan
3) Theme Scan
4) Executive Username Scan

""")

process_number = input("Process Number Enter : ")

if process_number == "1":
    site =  input("Site Adress Enter : ")
    os.system("wpscan --url " + site)

elif process_number == "2":
    site =  input("Site Adress Enter : ")
    os.system("wpscan --url " + site + " --enumerate p")

elif process_number == "3":
    site =  input("Site Adress Enter : ")
    os.system("wpscan --url " + site + " --enumerate t")

elif process_number == "4":
    site =  input("Site Adress Enter : ")
    os.system("wpscan --url " + site + " --enumerate u")

else:
    print("Wrong Choice")