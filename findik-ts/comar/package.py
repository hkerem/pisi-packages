#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system('/bin/mkdir -p /var/log/findik/ts')
    os.system('/bin/touch /var/log/findik/ts/timestamp.log')
    os.system('/bin/service findik-ts on')
    os.system('/bin/service findik-ts start')

def preRemove():
    os.system('/bin/service findik-ts stop')
