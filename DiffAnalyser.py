#!/usr/bin/env python3
import os
import subprocess
from pynotifier import Notification
import getpass


class Analyser:

    def __init__(self):
        self.list_of_previous_routine_scans = os.listdir('/home/artur/.mapdiff/routine_scans/')
        self.routine_scans_folder_path = "/home/" + getpass.getuser() + "/.mapdiff/routine_scans/"
        self.default_scans_folder_path = "/home/" + getpass.getuser() + "/.mapdiff/default_scans/"
        self.previous_scan_path = self.default_scans_folder_path + "dscan.xml"

    def get_last_routine_scan_path(self):
        latest_list_of_scans = os.listdir(self.routine_scans_folder_path)
        res = list(set(latest_list_of_scans) ^ set(
            self.list_of_previous_routine_scans))  # remove common elem's from above lists
        self.list_of_previous_routine_scans = os.listdir(self.routine_scans_folder_path)
        if len(res) == 0:
            return "null"
        else:
            return self.routine_scans_folder_path + res[0]

    def print_notifications(self):
        def_ports, routine_ports, def_ports_names, routine_ports_names = self.extract_changed_ports()
        notification_text = ''

        if len(def_ports) != 0 and len(routine_ports) != 0:
            notification_text = "Closed ports: "
            for port in def_ports:
                notification_text += port
                if def_ports.index(port) != len(def_ports) - 1:
                    notification_text += ', '

            notification_text += " | Opened ports: "
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

    def extract_changed_ports(self):
        def_ports = self.read_ports_from_xml(self.previous_scan_path)

        def_ports_names = str(
            subprocess.check_output('grep -oP \'<service name="(.*?)"\' ' + self.previous_scan_path, shell=True))
        def_ports_names = def_ports_names.replace("<service name=", "").replace('"', '')
        def_ports_names = def_ports_names[2:len(def_ports_names) - 1].split('\\n')[:-1]

        self.previous_scan_path = self.get_last_routine_scan_path()
        routine_ports = self.read_ports_from_xml(self.previous_scan_path)

        routine_ports_names = str(
            subprocess.check_output('grep -oP \'<service name="(.*?)"\' ' + self.previous_scan_path, shell=True))
        routine_ports_names = routine_ports_names.replace("<service name=", "").replace('"', '')
        routine_ports_names = routine_ports_names[2:len(routine_ports_names) - 1].split('\\n')[:-1]

        common_ports = []

        for port in def_ports:  # find common ports in discussed lists
            if port in routine_ports:
                common_ports.append(port)

        for port in common_ports:  # delete found ports to leave only different
            def_ports.remove(port)
            routine_ports.remove(port)

        common_ports.clear()

        for name in def_ports_names:
            if name in routine_ports_names:
                common_ports.append(name)

        for name in common_ports:
            def_ports_names.remove(name)
            routine_ports_names.remove(name)

        for i in range(len(def_ports)):
            def_ports[i] += '(' + def_ports_names[i] + ')'

        for i in range(len(routine_ports)):
            routine_ports_names[i] += '(' + routine_ports_names[i] + ')'

        return def_ports, routine_ports, def_ports_names, routine_ports_names

    def read_ports_from_xml(self, path_to_xml):
        open_ports_list = str(subprocess.check_output(
            'grep -oP \'portid="(\d{1,5})"\' ' + path_to_xml + ' | grep -oP \'\d{1,5}\' ',
            shell=True))  # read portids from scan results
        open_ports_list = open_ports_list[2:len(open_ports_list) - 1].split('\\n')[
                          :-1]  # omit unnecessary chars, split by \n and pop last (empty) element

        return open_ports_list
