#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN CONTROL")

print("""

Welcome Vpn Control Tool

""")

target_ip = input("Target Ip Enter : ")

os.system("ike-scan " + target_ip)