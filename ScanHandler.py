#!/usr/bin/env python3
import os
from crontab import CronTab
import InputHandler

class Scans:

    def __init__(self, user_input):
        self.userInput = user_input


    # def default_scan(self, target):
    #     os.system("nmap -F " + target + " -oX ~/.mapdiff/default_scans/dscan.xml")

    #default scan excluding some ports
    def default_scan(self, target, excl_ports=None):
           if (excl_ports!=None):
                os.system("nmap -F " + target + " --exclude-ports " + excl_ports + " -oX ~/.mapdiff/default_scans/dscan.xml")
           else:
               os.system("nmap -F " + target + " -oX ~/.mapdiff/default_scans/dscan.xml")


    def start_routine_scan(self):
        # my_cron = CronTab(user="artur")
        my_cron = CronTab(user=True)
        job = my_cron.new(command='/usr/bin/python3 /home/artur/Desktop/studia/zit/projekt/port_monitor/CronJob.py')

        if (self.userInput.frequency[0] == 'm'):
            job.minute.every(int(self.userInput.frequency[1:len(self.userInput.frequency)]))
        elif (self.userInput.frequency[0] == 'h'):
            job.minute.every(60 * int(self.userInput.frequency[1:len(self.userInput.frequency)]))


        my_cron.write()
        print("job started")


    def stop_routine_scan(self):
        os.system("crontab -r")
