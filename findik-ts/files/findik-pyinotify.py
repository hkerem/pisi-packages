import pyinotify
import os

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
