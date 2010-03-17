#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os

def backupAndReplace(path):
    os.system('/bin/mv -f /etc/apache2/' + path + ' /etc/apache2/' + path + '.bak')
    os.system('/bin/cp -f /usr/share/findik-web/apache2/' + path + ' /etc/apache2/' + path )
    
def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system('/bin/mkdir -p /etc/apache2/certs')

    backupAndReplace('httpd.conf')
    backupAndReplace('vhosts.d/01_ssl_vhost.conf')
    backupAndReplace('modules.d/40_mod_ssl.conf')
    backupAndReplace('certs/apache.pem')

    os.system('/bin/service apache on')
    os.system('/bin/service apache start')


