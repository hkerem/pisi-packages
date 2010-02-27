#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 H. Kerem Cevahir <kerem@medratech.com>
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-magic=no \
                        --enable-clamdav=no \
                        --enable-fileext=no \
                        --enable-adkerb=no \
                        --enable-ldap=no \
                        --enable-boostmt=yes")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodir("/var/log/findik")
    shelltools.copy("packaging/pardus/findik-postinst",
            "%s/usr/share/findik/scripts/" % get.installDIR())

