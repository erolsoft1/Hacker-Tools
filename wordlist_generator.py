#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDLIST GENERATOR")

print("""

Welcome Wordlist Generator Tool

""")

minimum = input("Minimum Char Number Enter : ")

maximum = input("Maximum Char Number Enter : ")

char = input("Your Request Chars Enter : ")

storage_place = input("Storage Place Enter : ")

os.system("crunch " + minimum + " " + maximum + " " + char + " -o " + storage_place)

print("\nCompleted Successfully")
