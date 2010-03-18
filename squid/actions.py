#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir="squid-3.0.STABLE24"
WorkDir="squid-2.7.STABLE8"

def setup():
#    autotools.autoreconf()
#                --enable-underscores \
    autotools.rawConfigure("--prefix=/usr \
                --sysconfdir=/etc/squid \
                --localstatedir=/var \
                --enable-removal-policies=lru,heap \
                --enable-delay-pools \
                --enable-cache-digests \
                --enable-follow-x-forwarded-for \
                --with-large-files \
                --with-maxfd=65536")

def build():
#    pisitools.dosed("libtool", '\$echo', '$ECHO')
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/var/cache/squid")
    pisitools.dodir("/var/log/squid")

