# !/usr/bin/env python3
import os

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")



os.system('nmap localhost -oX ~/.mapdiff/routine_scans/'+current_time+'.xml')
