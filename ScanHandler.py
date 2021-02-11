#!/usr/bin/env python3
import os
from crontab import CronTab
import InputHandler
import time
from datetime import datetime


class Scans:

    def __init__(self, user_input):
        self.userInput = user_input

    def start_default_scan(self):

        if (self.userInput.unimportant_ports != -1):
            os.system(
                "nmap -F " + self.userInput.target_address + " --exclude-ports " + self.userInput.unimportant_ports + " -oX ~/.mapdiff/default_scans/dscan.xml > /dev/null")
            print("nmap -F " + self.userInput.target_address + " -oX ~/.mapdiff/default_scans/dscan.xml > /dev/null")
        else:
            os.system(
                "nmap -F " + self.userInput.target_address + " -oX ~/.mapdiff/default_scans/dscan.xml > /dev/null")

    def start_routine_scan2(self):
        now = datetime.now()
        current_time = str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '_' + str(now.hour) + '.' + str(
            now.minute) + '.' + str(now.second)

        os.system('nmap localhost -oX ~/.mapdiff/routine_scans/' + current_time + '.xml > /dev/null')

        if (self.userInput.frequency[0] == 'm'):
            time.sleep(int(self.userInput.frequency[1:len(self.userInput.frequency)]))
        elif (self.userInput.frequency[0] == 'h'):
            time.sleep(60 * 60 * int(self.userInput.frequency[1:len(self.userInput.frequency)]))

    def start_routine_scan(self):
        # my_cron = CronTab(user="artur")
        my_cron = CronTab(user=True)
        job = my_cron.new(command='/usr/bin/python3 /home/artur/Desktop/studia/zit/projekt/port_monitor/CronJob.py')

        if (self.userInput.frequency[0] == 'm'):
            job.minute.every(60 * int(self.userInput.frequency[1:len(self.userInput.frequency)]))
        elif (self.userInput.frequency[0] == 'h'):
            job.minute.every(60 * int(self.userInput.frequency[1:len(self.userInput.frequency)]))

        my_cron.write()
        # print("job started")

    def stop_routine_scan(self):
        os.system("crontab -r")

    # def default_scan(self, target):
    #     os.system("nmap -F " + target + " -oX ~/.mapdiff/default_scans/dscan.xml")

    # default scan excluding some ports
    # def default_scan(self, target, excl_ports=None):
    #     if (excl_ports != None):
    #         os.system(
    #             "nmap -F " + target + " --exclude-ports " + excl_ports + " -oX ~/.mapdiff/default_scans/dscan.xml")
    #     else:
    #         os.system("nmap -F " + target + " -oX ~/.mapdiff/default_scans/dscan.xml")
