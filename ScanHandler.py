#!/usr/bin/env python3
import os
import time
from datetime import datetime
import getpass


class Scans:

    def __init__(self, user_input):
        self.userInput = user_input
        self.routine_scans_folder_path = "/home/" + getpass.getuser() + "/.mapdiff/routine_scans/"
        self.default_scans_folder_path = "/home/" + getpass.getuser() + "/.mapdiff/default_scans/"

    def start_default_scan(self):

        if (self.userInput.unimportant_ports != -1):
            os.system(
                "nmap " + self.userInput.target_address + " --exclude-ports " + self.userInput.unimportant_ports + " -oX " + self.default_scans_folder_path + "dscan.xml > /dev/null")
        else:
            os.system(
                "nmap " + self.userInput.target_address + " -oX " + self.default_scans_folder_path + "dscan.xml > /dev/null")

    def start_routine_scan(self):
        now = datetime.now()
        current_time = str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '_' + str(now.hour) + '.' + str(
            now.minute) + '.' + str(now.second)


        if (self.userInput.frequency[0] == 'm'):
            time.sleep(60*int(self.userInput.frequency[1:len(self.userInput.frequency)]))
        elif (self.userInput.frequency[0] == 'h'):
            time.sleep(60 * 60 * int(self.userInput.frequency[1:len(self.userInput.frequency)]))

        if self.userInput.unimportant_ports != 'n':
            os.system('nmap ' + self.userInput.target_address + ' --exclude-ports ' + self.userInput.unimportant_ports +' -oX ' + self.routine_scans_folder_path + current_time + '.xml > /dev/null')
        else:
            os.system('nmap ' + self.userInput.target_address + ' -oX ' + self.routine_scans_folder_path + current_time + '.xml > /dev/null')
