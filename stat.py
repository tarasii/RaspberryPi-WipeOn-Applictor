#! /usr/bin/python
#
from datetime import datetime
import os
from collections import Counter

daycnt = Counter()
hwrcnt = Counter()

if os.path.exists(flog):
    with open('/home/pi/prnt.log','r') as fl:
        for line in fl.readlines():
            line = line.replace("\0","")
            str = line[6:]
            date_object = datetime.strptime(str, '%a %b %d %H:%M:%S %Z %Y ')
            daykey = "%s%02d%02d" % (date_object.year, date_object.month, date_obje$
            hwrkey = "%s%02d%02d %02d:00" % (date_object.year, date_object.month, d$
            daycnt[daykey] +=1
            hwrcnt[hwrkey] +=1


#print daycnt
#print hwrcnt

print "Content-Type: text/html\n\n"
print "<hmtl>"
print '<head><meta content="text/html; charset=UTF-8" />'
print "<title>RPi WipeOn Stat</title>"
print "<body>"

print "<h1>Statistics:</h1>"

hwrlst =  list(hwrcnt)
hwrlst.sort()

bufkey = ""
for key in hwrlst:
    daykey = key[:8]
    if bufkey != daykey:
        print "<p>",daykey, "     ", daycnt[daykey],"</p>"
        bufkey = daykey

    print "<a>",key, hwrcnt[key],"</a><br>"

if (bufkey == ""):
    print "<a>empty</a><br>"

print "</body>"
print "</html>"
