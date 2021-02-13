#!/usr/bin/env python3
from InputHandler import UserInput
from ScanHandler import Scans
from DiffAnalyser import Analyser
from multiprocessing import Process
import subprocess
import os

try:
    result = subprocess.check_output('pip3 list | grep -F py-notifier', shell=True)
except Exception:
    os.system("pip3 install py-notifier > /dev/null")

if (~os.path.exists("~/.mapdiff")):
    os.system("mkdir -p ~/.mapdiff")
    print("Directory ~/.mapdiff has been created in home directory.")
if (~os.path.exists("~/.mapdiff/routine_scans")):
    os.system("mkdir -p ~/.mapdiff/routine_scans")
    print("Directory ~/.mapdiff/routine_scans has been created in home directory.")
if (~os.path.exists("~/.mapdiff/default_scans")):
    os.system("mkdir -p ~/.mapdiff/default_scans")
    print("Directory ~/.mapdiff/default_scans has been created in home directory.")

ui = UserInput()
sh = Scans(ui)
an = Analyser()

print("""
Welcome in ports monitor - MAPDIFF !!!
--------------------------------------
This app is created for monitoring open ports and watching new started services.
First, you need to tell us, which services are default or unimportant,
so that app won't be notifying you about changes in their state. Other ports will produce notifications.
""")


def start_new_scanning():
    while True:
        sh.start_routine_scan()
        an.print_notifications()


ui.input_unimportant_ports()
ui.input_target_address()
ui.input_frequency()

sh.start_default_scan()

p1 = Process(target=start_new_scanning)
p1.start()

while True:
    print()
    print("If you want to stop scanning and start new one type \"s\".")
    print("If you want to stop and exit, type \"d\"")
    command = input("Type command: ")
    if command != 's' and command != 'd':
        continue
    elif command == 'd':
        p1.terminate()
        exit()
    elif command == 's':
        p1.terminate()
        ui.input_unimportant_ports()
        ui.input_target_address()
        ui.input_frequency()
        sh.start_default_scan()
        p1 = Process(target=start_new_scanning)
        p1.start()
