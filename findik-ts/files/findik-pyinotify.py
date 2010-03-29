import pyinotify
import os

from os import fork, setsid, umask, dup2, getpid
from sys import stdin, stdout, stderr

if fork(): exit(0)
umask(0) 
setsid() 
if fork(): exit(0)

outfile = open('/var/run/findik/findik-ts.pid', 'w')
outfile.write('%i' % getpid())
outfile.close()

stdout.flush()
stderr.flush()
si = file('/dev/null', 'r')
so = file('/dev/null', 'a+')
se = file('/dev/null', 'a+', 0)
dup2(si.fileno(), stdin.fileno())
dup2(so.fileno(), stdout.fileno())
dup2(se.fileno(), stderr.fileno())

wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_CREATE  # watched events

class HandleEvents(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        if event.pathname.find(".gz") != -1 and event.pathname.find(".zd") == -1:
            os.system("/usr/bin/findik-generate-ts %s" % (event.pathname))

p = HandleEvents()
notifier = pyinotify.Notifier(wm, p)
wdd = wm.add_watch('/var/log/findik', mask, rec=True)

notifier.loop()
