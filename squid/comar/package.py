#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system('/bin/chown -R squid.squid /var/cache/squid')
    os.system('/bin/chown -R squid.squid /var/log/squid')
    os.system('/bin/service squid on')
    os.system('/bin/service squid start')

def preRemove():
    os.system('/bin/service squid stop')
