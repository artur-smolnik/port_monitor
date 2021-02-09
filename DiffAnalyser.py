#!/usr/bin/env python3
import crontab
import os
from datetime import datetime
import subprocess


class Analyser:

    # def __init__(self):
    #     self.default_opened_ports = []


    def print_analysis_report(self, path_to_routine_scan_result):
        scan, ports = self.check_new_ports(path_to_routine_scan_result)

        if scan == -1:
            print("There are no any changes.")
            return -1
        elif scan == 0:
            print("Some ports are closed: ", end='')

            for port in ports:
                print(port, end='')

                if ports.index(port) != len(ports)-1:
                    print(', ', end='')
            return 0
        elif scan == 1:
            print("Some new ports are opened: ", end='')
            for port in ports:
                print(port, end=' ')

                if ports.index(port) != len(ports)-1:
                    print(', ', end='')
            return 0


    def check_new_ports(self, path_to_routine_scan_result):

        def_open_ports = self.read_open_ports("~/.mapdiff/default_scans/dscan.xml")
        routine_open_ports = self.read_open_ports(path_to_routine_scan_result)

        # res = list(set(def_open_ports)^set(routine_open_ports))  #remove common elem's from above lists
        common_ports = []

        for port in def_open_ports:  # find common ports in discussed lists
            if port in routine_open_ports:
                common_ports.append(port)

        for port in common_ports:  # delete found ports to leave only different
            def_open_ports.remove(port)
            routine_open_ports.remove(port)

        if len(def_open_ports) != 0:  # some ports are closed
            return 0,def_open_ports
        elif len(routine_open_ports) != 0:
            return 1,routine_open_ports  # new ports are opened
        else:
            return -1,-1



    def read_open_ports(self, path_to_scan_result):
        open_ports_list = str(subprocess.check_output(
            'grep -oP \'portid="(\d{1,5})"\' ' + path_to_scan_result + ' | grep -oP \'\d{1,5}\' ',
            shell=True))
        open_ports_list = open_ports_list[2:len(open_ports_list) - 1].split('\\n')[
                          :-1]  # omit unnecessary chars, split by \n and pop last (empty) element

        return open_ports_list


    def simple_ndiff_compare(self, def_scan_path, routine_scan_path):
        now = datetime.now()

        os.system(
            'ndiff ' + def_scan_path + ' ' + routine_scan_path + ' --xml > /home/artur/Desktop/studia/zit/projekt/port_monitor/scan_results/def_scan_' + str(
                now) + '.xml')

        # print('ndiff ' + def_scan + ' ' + routine_scan + ' --xml > /home/artur/Desktop/studia/zit/projekt/port_monitor/scan_results/def_scan_' + str(now) + '.xml' )
