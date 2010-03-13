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

#def check_config():
#    import os
#    if not os.path.exists("/etc/ssh/sshd_config"):
#        fail(MSG_ERR_NEEDCONF)
#    if not os.path.exists("/etc/ssh/ssh_host_key"):
#        run("/usr/bin/ssh-keygen", "-t", "rsa1", "-b", "1024",
#            "-f", "/etc/ssh/ssh_host_key", "-N", "")

@synchronized
def start():
#    startService(command="/usr/bin/findik",
#                 args="-d",
#                 pidfile="/var/run/findik.pid",
#                 donotify=True)
    startDependencies("findik")
    os.system('/usr/bin/python /usr/share/findik/ts/findik-pyinotify.py')

@synchronized
def stop():
#    stopService(pidfile="/var/run/findik.pid",
#                donotify=True)
    os.system("/usr/bin/kill -9 $(ps aux |grep findik-pyinotify.py|awk '{ print $2 }')")

def status():
    return isServiceRunning(command="/usr/bin/python /usr/share/findik/ts/findik-pyinotify.py")
