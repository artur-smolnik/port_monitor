#!/usr/bin/env python3
import crontab
import os
from datetime import datetime
import subprocess


class Analyser:

    def __init__(self):
        self.default_opened_ports = []

    def simple_ndiff_compare(self, def_scan_path, routine_scan_path):
        now = datetime.now()

        os.system(
            'ndiff ' + def_scan_path + ' ' + routine_scan_path + ' --xml > /home/artur/Desktop/studia/zit/projekt/port_monitor/scan_results/def_scan_' + str(
                now) + '.xml')

        # print('ndiff ' + def_scan + ' ' + routine_scan + ' --xml > /home/artur/Desktop/studia/zit/projekt/port_monitor/scan_results/def_scan_' + str(now) + '.xml' )

    def compare_results(self):
        grep = 'portid="\d{1,5}"'
        # routine_scan_ports = str(os.system("grep -oP '" + grep + "' /home/artur/Desktop/studia/zit/projekt/port_monitor/routine_scans/A.xml"))
        routine_scan_ports = subprocess.check_output(
            "grep -oP '" + grep + "' /home/artur/Desktop/studia/zit/projekt/port_monitor/routine_scans/A.xml",
            shell=True)

        # os.popen("grep -oP '" + grep + "' /home/artur/Desktop/studia/zit/projekt/port_monitor/routine_scans/A.xml").read()
        print((routine_scan_ports))

    def read_open_ports(self, path_to_scan_result):
        open_ports_list = str(subprocess.check_output(
            'grep -oP \'portid="(\d{1,5})"\' ' + path_to_scan_result + ' | grep -oP \'\d{1,5}\' ',
            shell=True))
        open_ports_list = open_ports_list[2:len(open_ports_list) - 1].split('\\n')[:-1]  # omit unnecessary chars, split by \n and pop last (empty) element

        return open_ports_list
