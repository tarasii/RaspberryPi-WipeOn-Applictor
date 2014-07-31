#! /usr/bin/python
#
import sys
import tty, termios
import shutil
import os
import setbarcode
from datetime import datetime

fdev = '/dev/usb/lp0'
flog = '/home/pi/prn.log'
fbar = '/home/pi/barcode.bas'

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
    
    
def printlabel():
    setbarcode.barcodefromconfig()
    if os.path.exists(fdev):
        shutil.copy(fbar, fdev)
        str = "print "
            
    else:
	    str = "error "
        
	str = str + datetime.utcnow().strftime("%a %b %d %H:%M:%S EEST %Y ") + "\n"
    with open(flog,'a') as fl:
        fl.write(str)
        
    return

printlabel()

while True:
    ch = getch()
    if ch == 'q':
        break;

    #print ch
    printlabel()        
