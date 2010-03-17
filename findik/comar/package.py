#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system('/bin/chown -R daemon.daemon /var/log/findik')
    os.system('/usr/share/findik/scripts/findik-postinst')
