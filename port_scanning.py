#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT SCANNING")

print("""

WELCOME PORT SCANNING TOOL 

1) FAST SCANNER
2) SERVICE AND VERSION INFORMATION
3) OPERATING SYSTEM INFORMATION

""")

process_number = input("Process Number Enter : ")

if(process_number == "1"):
	target_ip = input("Target Ip Enter : ")
	os.system("nmap " + target_ip)

elif(process_number == "2"):
	target_ip = input("Target Ip Enter : ")
	os.system("nmap -sV " + target_ip)

elif(process_number == "3"):
	target_ip = input("Target Ip Enter : ")
	os.system("nmap -o " + target_ip)
	
else:
	print("\nWrong Choice")
