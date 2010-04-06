#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os

def backupAndReplace(file, path):
    os.system('/bin/mv -f ' + path + ' ' + path + '.bak')
    os.system('/bin/cp -f /usr/share/findik/conf/' + file + ' ' + path )

def recoverFromBackup(path):
    os.system('/bin/mv -f ' + path + '.bak ' + path )

def ensureDepmod():
    if not os.path.exists('/lib/' + os.uname()[2] + '/modules.dep'):
        os.system('/sbin/depmod -a')

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    ensureDepmod()

    backupAndReplace('dhcpd.conf', '/etc/dhcp/dhcpd.conf')

    os.system('/bin/service dhcp on')
    os.system('/bin/service dhcp start')

    os.system('/bin/service openssh on')
    os.system('/bin/service iptables off')

def preRemove():
    os.system('/bin/service dhcp stop')
    recoverFromBackup('/etc/dhcp/dhcpd.conf')
    os.system('/bin/service dhcp off')

