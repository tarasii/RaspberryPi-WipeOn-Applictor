#! /usr/bin/python
#
import sys
import tty, termios
import shutil
import setbarcode
from datetime import datetime

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


while True:
    ch = getch()
    if ch == 'q':
        break;

    #print ch
    setbarcode.barcodefromconfig()
    shutil.copy('/home/pi/barcode.bas', '/dev/lp0')
	str = "print " + datetime.utcnow().strftime("%a %b %d %H:%M:%S EEST %Y ")
    with open('/home/pi/prn.log','wb') as fl:
        fl.write(str)
