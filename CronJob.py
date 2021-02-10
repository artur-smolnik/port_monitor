# !/usr/bin/env python3
import os
from datetime import datetime
import DiffAnalyser


class Cron:

    def __init__(self, analyser):
        self.analyser = analyser


    def do_job(self):
        now = datetime.now()
        current_time = str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '_' + str(now.hour) + '.' + str(
            now.minute) + '.' + str(now.second)

        os.system('nmap localhost -oX ~/.mapdiff/routine_scans/' + current_time + '.xml')
        self.analyser.print_analysis_report()


cron = Cron()
cron.do_job()
