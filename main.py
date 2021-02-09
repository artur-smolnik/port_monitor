#!/usr/bin/env python3
import InputHandler
import ScanHandler
import os
import DiffAnalyser
import glob


if(~os.path.exists("~/.mapdiff")):
    os.system("mkdir -p ~/.mapdiff")
    print("Directory ~/.mapdiff has been created in home directory.")
if(~os.path.exists("~/.mapdiff/routine_scans")):
    os.system("mkdir -p ~/.mapdiff/routine_scans")
    print("Directory ~/.mapdiff/routine_scans has been created in home directory.")
if(~os.path.exists("~/.mapdiff/default_scans")):
    os.system("mkdir -p ~/.mapdiff/default_scans")
    print("Directory ~/.mapdiff/default_scans has been created in home directory.")


print("""
Welcome in ports monitor - MAPDIFF !!!
--------------------------------------
This app is created for monitoring open ports and watching new started services.
First, you need to tell us, which services are default or unimportant,
so that app won't be notifying you about changes in their state. Other ports will produce notifications.

""")

ui = InputHandler.UserInput()
sh = ScanHandler.Scans(ui)
an = DiffAnalyser.Analyser()

# ui.input_unimportant_ports()
# ui.input_frequency()
# sh.default_scan('localhost')
# sh.start_routine_scan()

# sh.start_routine_scan()
# an.simple_ndiff_compare('/home/artur/Desktop/studia/zit/projekt/port_monitor/routine_scans/1.xml', '/home/artur/Desktop/studia/zit/projekt/port_monitor/routine_scans/2.xml')
# an.port_compare()

######### main function loop

# os.listdir('~/.mapdiff/routine_scans/')
# print(glob.glob('~/.mapdiff/routine_scans/'))



# lista = os.listdir('/home/artur/.mapdiff/routine_scans')

# for file in  lista:
#     an.check_new_ports('~/.mapdiff/routine_scans/' + file)
#     break

an.print_analysis_report('~/.mapdiff/routine_scans/00:16:01.xml')



# os.system("nmap localhost -oX test0.xml")
# os.system("nmap scanme.nmap.org -oX test1.xml")
# os.system("ndiff -v test0.xml test1.xml")
