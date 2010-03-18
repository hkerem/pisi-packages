# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Squid",
                 "tr": "Squid"
                 })

MSG_ERR_CONF = _({"en": "Please check configuration file. 'squid -k parse' failed.",
                  "tr": "Lütfen ayar dosyasını kontrol edin. 'squid -k parse' başarısızlıkla sonuçlandı.",
                    })

def check_conf():
    if not run("/usr/sbin/squid", "-k", "parse"):
        fail(MSG_ERR_CONF)

def check_cachedir():
    import os
    if os.path.exists("/var/cache/squid") and not os.path.exists("/var/cache/squid/00"):
        run("/usr/sbin/squid", "-z")

@synchronized
def start():
    check_cachedir()
    check_conf()
    import os
    os.system("/usr/sbin/squid -DYC")
#    startService(command="/usr/sbin/squid",
#                 args="-DYC")

@synchronized
def stop():
    stopService(pidfile="/var/run/squid.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/squid.pid")
