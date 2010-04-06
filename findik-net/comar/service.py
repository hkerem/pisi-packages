# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "FINDIK Ag Rutineler",
                 "tr": "FINDIK Network Routines"
                 })
serviceDefault = "on"

@synchronized
def start():
    os.system('/bin/echo 1 > /proc/sys/net/ipv4/tcp_syncookies')
    os.system('/bin/echo 1 > /proc/sys/net/ipv4/ip_forward')
    os.system('/sbin/iptables-restore < /etc/findik/iptables')
    os.system('/sbin/ifconfig eth1 10.11.12.1 netmask 255.255.255.0 up')
    startDependencies("dhcp")
    os.system('/sbin/ifconfig eth0 up')
    os.system('/sbin/dhcpcd -b eth0')

@synchronized
def stop():
    os.system('/bin/echo 0 > /proc/sys/net/ipv4/ip_forward')
    os.system('/sbin/dhcpcd -x eth0')
    os.system('/sbin/ifconfig eth0 down')
    os.system('/sbin/ifconfig eth1 down')

def status():
    return isServiceRunning(command="/sbin/dhcpcd")

