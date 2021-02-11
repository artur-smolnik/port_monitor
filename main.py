#!/usr/bin/env python3
import InputHandler
import ScanHandler
import os
import sys
import DiffAnalyser
import getpass
import glob
import time
import threading
from pynotifier import Notification
from multiprocessing import Process

# to install:
# pip install py-notifier

if (~os.path.exists("~/.mapdiff")):
    os.system("mkdir -p ~/.mapdiff")
    print("Directory ~/.mapdiff has been created in home directory.")
if (~os.path.exists("~/.mapdiff/routine_scans")):
    os.system("mkdir -p ~/.mapdiff/routine_scans")
    print("Directory ~/.mapdiff/routine_scans has been created in home directory.")
if (~os.path.exists("~/.mapdiff/default_scans")):
    os.system("mkdir -p ~/.mapdiff/default_scans")
    print("Directory ~/.mapdiff/default_scans has been created in home directory.")

ui = InputHandler.UserInput()
sh = ScanHandler.Scans(ui)
an = DiffAnalyser.Analyser()

mapdiff_path = "/home/" + getpass.getuser() + "/.mapdiff/"
print(mapdiff_path)
print("""
Welcome in ports monitor - MAPDIFF !!!
--------------------------------------
This app is created for monitoring open ports and watching new started services.
First, you need to tell us, which services are default or unimportant,
so that app won't be notifying you about changes in their state. Other ports will produce notifications.
""")


def start_new_scanning():
    while True:
        sh.start_routine_scan2()

ui.input_unimportant_ports()
ui.input_target_address()
ui.input_frequency()
sh.start_default_scan()

p1 = Process(target=start_new_scanning)
p1.start()

while True:
    print("If you want to stop scanning and start new one type \"s\".")
    print("If you want to stop and exit, type \"d\"")
    command = input("Type command: ")
    if command != 's' and command != 'd':
        continue
    elif command == 'd':
        p1.kill()
        exit()
    elif command == 's':
        p1.kill()
        ui.input_unimportant_ports()
        ui.input_target_address()
        ui.input_frequency()
        sh.start_default_scan()
        p1.start()


