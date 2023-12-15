#!/usr/bin/env python

import os
import py_compile

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet COMPILATION")

print("""

Welcome Compilation Tool

""")

compile = input("Program Name Enter : ")

py_compile.compile(compile)