# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "FINDIK Content Filter",
                 "tr": "FINDIK Icerik Filtresi"
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
    startDependencies("mysql_server")
    startDependencies("squid")
    os.system('/usr/share/findik/scripts/wait_for_mysqld')
    os.system('/sbin/start-stop-daemon --start --exec /usr/bin/findik -- -d')

@synchronized
def stop():
#    stopService(pidfile="/var/run/findik.pid",
#                donotify=True)
    os.system('/sbin/start-stop-daemon --stop --exec /usr/bin/findik')

def status():
    return isServiceRunning(command="/usr/bin/findik")
