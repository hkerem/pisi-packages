# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "FINDIK Content Filter",
                 "tr": "FINDIK Icerik Filtresi"
                 })

#def check_config():
#    import os
#    if not os.path.exists("/etc/ssh/sshd_config"):
#        fail(MSG_ERR_NEEDCONF)
#    if not os.path.exists("/etc/ssh/ssh_host_key"):
#        run("/usr/bin/ssh-keygen", "-t", "rsa1", "-b", "1024",
#            "-f", "/etc/ssh/ssh_host_key", "-N", "")

@synchronized
def start():
#    check_config()
    startService(command="/usr/bin/findik",
                 args="-d",
                 pidfile="/var/run/findik.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/findik.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/findik.pid")
