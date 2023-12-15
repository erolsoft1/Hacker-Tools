#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet FIREWALL DETECTION")

print("""

Welcome Firewall Detection Tool

""")

site = input("Site Adress Enter : ")

os.system("wafw00f " + site)
