#!/usr/bin/env python3
import InputHandler
import ScanHandler
import os
import DiffAnalyser
import CronJob
import glob
from pynotifier import Notification
#to install:
#pip install py-notifier

if(~os.path.exists("~/.mapdiff")):
    os.system("mkdir -p ~/.mapdiff")
    print("Directory ~/.mapdiff has been created in home directory.")
if(~os.path.exists("~/.mapdiff/routine_scans")):
    os.system("mkdir -p ~/.mapdiff/routine_scans")
    print("Directory ~/.mapdiff/routine_scans has been created in home directory.")
if(~os.path.exists("~/.mapdiff/default_scans")):
    os.system("mkdir -p ~/.mapdiff/default_scans")
    print("Directory ~/.mapdiff/default_scans has been created in home directory.")



ui = InputHandler.UserInput()
sh = ScanHandler.Scans(ui)
an = DiffAnalyser.Analyser()
cr = CronJob.Cron(an)
print("""
Welcome in ports monitor - MAPDIFF !!!
--------------------------------------
This app is created for monitoring open ports and watching new started services.
First, you need to tell us, which services are default or unimportant,
so that app won't be notifying you about changes in their state. Other ports will produce notifications.
""")
ui.input_unimportant_ports()
ui.input_target_address()
ui.input_frequency()




sh.start_default_scan()
sh.start_routine_scan()

# sh.start_routine_scan()
# an.simple_ndiff_compare('/home/artur/Desktop/studia/zit/projekt/port_monitor/routine_scans/1.xml', '/home/artur/Desktop/studia/zit/projekt/port_monitor/routine_scans/2.xml')
# an.port_compare()




# lista = os.listdir('/home/artur/.mapdiff/routine_scans')

# for file in  lista:
#     an.check_new_ports('~/.mapdiff/routine_scans/' + file)
#     break

# an.print_analysis_report('~/.mapdiff/routine_scans/00:16:01.xml')


