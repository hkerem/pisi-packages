#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="findik"

def install():
    pisitools.insinto("/var/www/localhost/htdocs/findik", "*")

