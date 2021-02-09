# !/usr/bin/env python3
import os
from datetime import datetime

now = datetime.now()
current_time = str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '_' + str(now.hour) + '.' + str(now.minute) + '.' + str(now.second)

os.system('nmap localhost -oX ~/.mapdiff/routine_scans/'+current_time+'.xml')


