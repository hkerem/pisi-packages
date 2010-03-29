# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "FINDIK Timestamping Service",
                 "tr": "FINDIK Zaman Damgasi Servisi"
                 })
serviceDefault = "on"

@synchronized
def start():
    startDependencies("findik")
    os.system('/usr/bin/python /usr/share/findik/ts/findik-pyinotify.py')

@synchronized
def stop():
    stopService(pidfile="/var/run/findik/findik-ts.pid",
                donotify=True)

def status():
    return isServiceRunning(pidfile="/var/run/findik/findik-ts.pid")
