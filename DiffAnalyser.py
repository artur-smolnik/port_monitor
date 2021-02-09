#!/usr/bin/env python3
import crontab
import os
from datetime import datetime
import subprocess

class Analyser:
    def simple_ndiff_compare(self, def_scan, routine_scan):
        now = datetime.now()

        print(def_scan)
        print(routine_scan)

        os.system('ndiff ' + def_scan + ' ' + routine_scan + ' --xml > /home/artur/Desktop/studia/zit/projekt/port_monitor/scan_results/def_scan_' + str(now) + '.xml' )

        # print('ndiff ' + def_scan + ' ' + routine_scan + ' --xml > /home/artur/Desktop/studia/zit/projekt/port_monitor/scan_results/def_scan_' + str(now) + '.xml' )

    def port_compare(self):
        grep = 'portid="\d{1,5}"'
        # routine_scan_ports = str(os.system("grep -oP '" + grep + "' /home/artur/Desktop/studia/zit/projekt/port_monitor/routine_scans/A.xml"))
        routine_scan_ports = subprocess.check_output("grep -oP '" + grep + "' /home/artur/Desktop/studia/zit/projekt/port_monitor/routine_scans/A.xml", shell=True)


        # os.popen("grep -oP '" + grep + "' /home/artur/Desktop/studia/zit/projekt/port_monitor/routine_scans/A.xml").read()
        print((routine_scan_ports))
