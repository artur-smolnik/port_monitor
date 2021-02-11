#!/usr/bin/env python3
import crontab
import os
from datetime import datetime
import subprocess
from pynotifier import Notification
import getpass

class Analyser:

    def __init__(self):
        self.path_to_routine_scan_result = ''
        self.list_of_previous_routine_scans = os.listdir('/home/artur/.mapdiff/routine_scans/')
        self.routine_scans_folder_path = "/home/" + getpass.getuser() + "/.mapdiff/routine_scans"
        self.default_scans_folder_path = "/home/" + getpass.getuser() + "/.mapdiff/default_scans"

    def find_routine_scan_path(self):
        latest_list_of_scans = os.listdir('/home/artur/.mapdiff/routine_scans')
        res = list(set(latest_list_of_scans) ^ set(
            self.list_of_previous_routine_scans))  # remove common elem's from above lists
        self.list_of_previous_routine_scans = os.listdir('/home/artur/.mapdiff/routine_scans')
        if len(res) == 0:
            return "null"
        else:
            return "~/.mapdiff/routine_scans/" + res[0]

    def print_analysis_report(self):
        def_ports, routine_ports = self.check_new_ports(self.find_routine_scan_path())
        notification_text = ''

        if len(def_ports) != 0 and len(routine_ports) != 0:
            notification_text = "Closed ports: "
            for port in def_ports:
                notification_text += port
                if def_ports.index(port) != len(def_ports) - 1:
                    notification_text += ', '

            notification_text += ", opened ports: "
            for port in routine_ports:
                notification_text += port
                if routine_ports.index(port) != len(routine_ports) - 1:
                    notification_text += ', '

            Notification(
                title='MapDiff Port Scanner',
                description=notification_text,
                icon_path='path/to/image/file/icon.png',  # On Windows .ico is required, on Linux - .png
                duration=3,  # Duration in seconds
                urgency=Notification.URGENCY_CRITICAL
            ).send()
        elif len(def_ports) != 0 and len(routine_ports) == 0:
            for port in def_ports:
                notification_text += port
                if def_ports.index(port) != len(def_ports) - 1:
                    notification_text += ', '

            Notification(
                title='MapDiff Port Scanner',
                description='Some ports are closed: ' + notification_text,
                icon_path='path/to/image/file/icon.png',  # On Windows .ico is required, on Linux - .png
                duration=3,  # Duration in seconds
                urgency=Notification.URGENCY_CRITICAL
            ).send()
        elif len(routine_ports) != 0 and len(def_ports) == 0:
            for port in routine_ports:
                notification_text += port
                if routine_ports.index(port) != len(routine_ports) - 1:
                    notification_text += ', '

            Notification(
                title='MapDiff Port Scanner',
                description='New ports are opened: ' + notification_text,
                icon_path='path/to/image/file/icon.png',  # On Windows .ico is required, on Linux - .png
                duration=3,  # Duration in seconds
                urgency=Notification.URGENCY_CRITICAL
            ).send()

    def check_new_ports(self, path_to_routine_scan_result):

        def_ports = self.read_open_ports("~/.mapdiff/default_scans/dscan.xml")
        routine_ports = self.read_open_ports(path_to_routine_scan_result)

        common_ports = []

        for port in def_ports:  # find common ports in discussed lists
            if port in routine_ports:
                common_ports.append(port)

        for port in common_ports:  # delete found ports to leave only different
            def_ports.remove(port)
            routine_ports.remove(port)
        print(routine_ports)

        return def_ports, routine_ports

    def read_open_ports(self, path_to_scan_result):
        open_ports_list = str(subprocess.check_output(
            'grep -oP \'portid="(\d{1,5})"\' ' + path_to_scan_result + ' | grep -oP \'\d{1,5}\' ',
            shell=True))                                    # read portids from scan results
        open_ports_list = open_ports_list[2:len(open_ports_list) - 1].split('\\n')[
                          :-1]                              # omit unnecessary chars, split by \n and pop last (empty) element

        return open_ports_list

    def simple_ndiff_compare(self, def_scan_path, routine_scan_path):
        now = datetime.now()
        os.system(
            'ndiff ' + def_scan_path + ' ' + routine_scan_path + ' --xml > /home/artur/Desktop/studia/zit/projekt/port_monitor/scan_results/def_scan_' + str(
                now) + '.xml')

    def check_if_scan_ended(self):
        latest_list_of_scans = os.listdir('/home/artur/.mapdiff/routine_scans')

        if len(list(set(latest_list_of_scans) ^ set(self.list_of_previous_routine_scans))) != 0:
            return True
        else:
            return False
