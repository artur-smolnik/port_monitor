# !/usr/bin/env python3
import os
from datetime import datetime
import DiffAnalyser
from pynotifier import Notification

analyser = DiffAnalyser.Analyser()

now = datetime.now()
current_time = str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '_' + str(now.hour) + '.' + str(
    now.minute) + '.' + str(now.second)

os.system('nmap localhost -oX ~/.mapdiff/routine_scans/' + current_time + '.xml')

# analyser.print_analysis_report()

Notification(
    title='MapDiff Port Scanner',
    description='New ports are opened: ',
    icon_path='path/to/image/file/icon.png',  # On Windows .ico is required, on Linux - .png
    duration=3,  # Duration in seconds
    urgency=Notification.URGENCY_CRITICAL
).send()
