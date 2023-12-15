#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BRUTE FORCE")

print("""

Welcome Brute Force Tool

 1) FTP
 2) SSH
 3) TELNET
 4) HTTP
 5) SMB
 6) ROP
 7) SIP
 8) REDIS
 9) VNC
10) POSTGRESQL
11) MYSQL

""")

process_number = input("Process Number Enter : ")

targer_ip = input("Target Ip Enter : ")

username = input("Username Enter : ")

password = input("Wordlist File Path Enter : ")

if process_number == "1":
	os.system("nrack -p 21 -u " + username + " -P " + password + " " + target_ip)
	
elif process_number == "2":
	os.system("nrack -p 22 -u " + username + " -P " + password + " " + target_ip)
	
else:
	print("Wrong Choice")
